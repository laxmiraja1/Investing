# laurion-agents

Shared code and templates for the Laurion investor-agent project (HBS Fall 2026 EFC). Each team member builds one investor agent on the same pipeline, scored with the same rubric, so the results can be compared side by side. See `../GUIDE.md` for the full project plan.

## Setup

```bash
cd laurion-agents
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...                        # or: ant auth login
export SEC_USER_AGENT="Your Name you@school.edu"    # SEC requires contact info
```

## Layout

```
shared/
  agent.py        staged pipeline: gatekeeper -> business -> management -> valuation -> decision -> memo
  archive.py      point-in-time archive: only docs published before the as-of date, BM25 search
  packet.py       information packets + anonymization (company/ticker/people -> neutral labels)
  edgar.py        SEC EDGAR: filings filed before a date; XBRL facts as known on a date
  schema.py       shared outputs: GateResult, Decision, CalibrationScore, LeakageProbe
  run_agent.py    CLI: run an agent on a packet N times (named / anonymized / both)
  judge.py        CLI: LLM judge scores calibration runs against truth.yaml using rubric.md
  rubric.md       calibration scoring rubric (use it for hand-grading too)
  prompts/system.md
investors/_template/   copy this for your investor
packets/example/       example information packet
```

## Workflow for each team member

1. **Start your investor folder.** Run `cp -r investors/_template investors/<name>` and set `investor:` in `agent/config.yaml`.
2. **Build the archive.** Add documents under `archive/docs/` with a row in `archive/manifest.csv`. `date_published` is the date the public could first read the document; everything point-in-time depends on it. Copyrighted material goes in `archive/private/`, which git ignores.
3. **Log trades.** Fill in `trades.csv` from 13Fs and letters.
4. **Write `framework.md`.** Write it section by section, with citations. The stage prompts in `agent/prompts/` refer to these section names, so keep them in sync. Edit the stage list and prompts in `config.yaml` to match how your investor actually works. For example, an activist needs a catalyst stage, and a macro trader needs different stages entirely.
5. **Build calibration packets.** For each trade, create `calibration/<trade>/packet/` (see `packets/example/packet.yaml`) and `calibration/<trade>/truth.yaml`. Every packet document must predate `as_of`, and loading fails if one doesn't. Fill in `aliases` so the packet can be anonymized.
6. **Run and score:**
   ```bash
   python -m shared.run_agent --investor investors/<name> \
       --packet investors/<name>/calibration/<trade>/packet --runs 5 --both --probe
   python -m shared.judge --trade investors/<name>/calibration/<trade>
   ```
   Compare named and anonymized runs. If the agent only matches when the company is named, or if the leakage probe identifies the company, it is recalling the trade rather than reasoning about it. Report those runs separately.
7. **Freeze the agent.** Run `git tag <name>-frozen` before the out-of-sample basket arrives, then run each basket name with `--runs 3`.

## Notes

- **Model.** The default is `claude-opus-5-5` at `effort: high`, set per investor in `config.yaml`. Server-side fallbacks are on: if a request is declined, the API retries on a fallback model. Set `server_side_fallbacks: false` to turn this off.
- **Run metadata.** Every run saves `meta.json` with the model, effort, as-of date, anonymized flag, git commit and token usage. This makes results reproducible and supplies the cost figures for the retrospective.
- **Retrieval.** Search is keyword-based (BM25) and has no dependencies. If recall is weak, swap in embeddings, but keep the `as_of` filter.
- **EDGAR coverage.** XBRL facts only start around 2009. For older trades, use raw 10-K text (`python -m shared.edgar filings <ticker> <as_of>`) or Compustat Point-in-Time via WRDS. Tickers resolve to *current* companies only, so pass the CIK for delisted or renamed ones.
