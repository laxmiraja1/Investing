# Investor-Agent Project: Step-by-Step Build Guide

Project: **Laurion Capital Management — Fall 2026 Public Markets Investing Seminar (HBS EFC)**

The ask, in one line: pick a real investor, build an archive of their primary sources, codify their *actual* decision process as an LLM agent, then prove (or disprove) its fidelity with **historical calibration** (3–5 real trades, point-in-time inputs) and an **out-of-sample basket** supplied by Laurion. The team then writes a retrospective on a generalizable "investor-to-agent" pipeline and which parts of an investor's edge are automatable vs. defensible.

Laurion explicitly calls the viral open-source "AI Hedge Fund" naive (persona prompts of Lynch/Graham/Munger/Buffett). Your bar is: **not a caricature of the style, but the decision framework — and evidence of whether it works.**

---

## Deliverables checklist (per the info sheet)

| # | Deliverable | Per |
|---|---|---|
| 1 | Archive of source material + outlined investment process + agent (prompts + supporting data) | each team member |
| 2 | Calibration results: 3–5 historical trades replayed with period-appropriate inputs; honest match/divergence assessment (decision **and** reasons) | each agent |
| 3 | Out-of-sample written opinions on Laurion's basket(s), in the investor's framework | each agent |
| 4 | Process retrospective: common vs. idiosyncratic, generalizable pipeline, automatable vs. defensible edge | team |

---

## Step 0 — Team setup (week 1)

1. **Agree on a shared skeleton before anyone builds.** Same repo layout, same output schema, same evaluation rubric. This is what makes the cross-agent comparison (deliverable 4) possible later.
2. **Start a build journal** (one per member, `journal.md`). Log every decision, dead end, and hour spent. The retrospective is written from this — you cannot reconstruct it at the end.
3. **Confirm data access** at Baker Library (WRDS/Compustat/CRSP point-in-time data, Capital IQ, Bloomberg, Factiva). Point-in-time data is the hardest part of the project; sort it out early.
4. **Ask Laurion early**: when will the basket arrive, how many names, what format do they want the opinions in, and do they have a preferred model/provider or data constraints.

## Step 1 — Pick your investor (week 1)

Choose someone who scores well on all four:

- **Volume of primary sources** — letters, memos, interviews, AGM transcripts, books written *by* them.
- **Documented, dated trades** — 13F history, letters naming positions, public pitches. You need 3–5 with clear entry/exit dates and stated reasons.
- **An articulable framework** — they explain *why*, not just *what*. Pure-intuition/tape-reading traders are hard to codify (which is itself a valid finding, but risky as your only agent).
- **Diversity within the team** — mix styles (deep value, quality compounder, activist, macro, special situations) so the retrospective has contrast.

Candidates with strong archives: Warren Buffett (partnership + Berkshire letters, 13F), Seth Klarman (Baupost letters, *Margin of Safety*), Howard Marks (Oaktree memos), Nick Sleep & Qais Zakaria (Nomad letters), Terry Smith (Fundsmith letters), Bill Ackman (Pershing Square letters + public presentations), Joel Greenblatt (Gotham, books, Columbia lectures), Li Lu, Mohnish Pabrai, Michael Burry (Scion letters), Stanley Druckenmiller (interviews; macro — harder), Peter Lynch (books, Magellan reports).

> If you pick Buffett/Munger/Graham/Lynch, you are directly competing with the project Laurion called naive — your rigor must visibly exceed it. Also, the LLM has memorized these investors' famous trades, which makes calibration leakage worse (see Step 5).

## Step 2 — Build the archive (weeks 1–3)

Goal: **the context an agent would need to reason like the investor**, with every item dated so you can filter by time.

**Collect:**
- Shareholder/partner letters and memos (all years available)
- Interviews, speeches, lectures, AGM/Q&A transcripts
- Books and articles they wrote
- Regulatory filings: 13F-HR (SEC EDGAR, from 1999 electronically), 13D/13G, Form 4, proxy fights
- Investment pitches / presentations (e.g., Sohn, Ira Sohn, activist decks)
- High-quality secondary sources (biographies, case studies) — tag them as secondary

**Store each document with metadata** (front-matter or a manifest CSV):

```yaml
id: brk-letter-1988
title: Berkshire Hathaway 1988 Chairman's Letter
author: Warren Buffett
type: letter        # letter | interview | filing | book | talk | secondary
date_published: 1989-02-28   # the date the PUBLIC could first see it
source_url: ...
primary: true
tickers_mentioned: [KO]
```

`date_published` is the single most important field — it drives the point-in-time filter in calibration. Use filing/publication date, never the period-end date.

**Also build a trade log** (`trades.csv`) from 13Fs and letters: ticker, action (buy/add/trim/sell), approximate date, size/% of portfolio, stated rationale + citation. You'll pick calibration trades from this.

Keep copyrighted material (books, paid transcripts) in a private repo / local storage.

## Step 3 — Outline the investment process (weeks 3–5)

Turn the archive into an explicit, cited **decision framework document** (`framework.md`). This is the intellectual core of the project. Structure it as the decision steps the investor actually goes through:

1. **Universe & idea sourcing** — where ideas come from (screens, reading, spinoffs, distress, 52-week lows, scuttlebutt).
2. **Filters / gatekeepers** — circle of competence, industries avoided, minimum quality, size, leverage limits. *What makes them stop analyzing?*
3. **Business analysis** — what they examine and how (moats, unit economics, reinvestment runway, management, capital allocation).
4. **Valuation** — the actual method (owner earnings, normalized EPS × multiple, sum-of-parts, liquidation value, FCF yield vs. bonds) and required margin of safety / hurdle rate.
5. **Catalyst / timing** — do they need one? (Activists and event-driven: yes; Buffett: mostly no.)
6. **Position sizing & portfolio construction** — concentration, max position, cash tolerance.
7. **Sell discipline** — what makes them trim/exit (valuation, thesis break, better opportunity, never).
8. **Risk & temperament** — how they treat drawdowns, macro, leverage, being early.
9. **Known evolution over time** — e.g., Buffett's shift from Graham cigar-butts to quality compounders (~1972 onward). The agent at 1975 should not reason like the agent at 2015.
10. **Anti-patterns** — what a caricature would get wrong ("Buffett only buys cheap stocks", "Lynch buys whatever he sees at the mall").

**Rules:**
- Every claim cites a dated source in the archive.
- Separate **stated** philosophy (what they say) from **revealed** behavior (what 13Fs show). Note contradictions — they're findings.
- Where possible, express rules as checkable criteria ("ROE > 15% for 10 years with low debt") *and* as judgment questions ("Would you be comfortable owning this if the market closed for 10 years?").

## Step 4 — Codify as an agent (weeks 4–7)

Keep the stack simple: Python + the Anthropic SDK (or whichever model your team chooses), prompts as version-controlled files, a runner script. Avoid heavy frameworks — clarity matters more than plumbing here.

**Recommended architecture — a staged pipeline that mirrors the framework, not one giant persona prompt:**

```
input packet (company data as of date T)
   → [1] Gatekeeper: in circle of competence? passes hard filters?  → PASS / continue
   → [2] Business quality analysis
   → [3] Management & capital allocation
   → [4] Valuation & margin of safety
   → [5] Decision + sizing + sell triggers
   → [6] Memo written in the investor's framework
```

**Components:**
- **System prompt** — the codified framework from Step 3 (not "you are Warren Buffett"; rather "apply the following decision process…"). Test both versions; the difference is a finding.
- **Retrieval over the archive** — fetch relevant passages from the investor's own writing, **filtered to `date_published < T`**. This keeps the agent grounded in what the investor believed *at that time*.
- **Few-shot examples** — 2–3 worked analyses the investor actually wrote (from letters), again only those dated before T. Never use a calibration trade as a few-shot example.
- **Tools / data inputs** — financial statements, price history, filings, news — all as of T (see data layer below).
- **Structured output** — enforce a schema so results are comparable across agents:

```json
{
  "ticker": "XYZ",
  "as_of": "1988-06-30",
  "decision": "BUY | PASS | SELL | HOLD | TRIM",
  "conviction": 1-5,
  "position_size_pct": 0-100,
  "intrinsic_value_estimate": "...",
  "key_reasons": ["..."],
  "framework_steps_applied": ["moat", "owner_earnings", "..."],
  "what_would_change_my_mind": ["..."],
  "citations": ["brk-letter-1987#p4", "10-K-1987#p12"]
}
```
plus a prose memo.

**The data layer (point-in-time):**
- Fundamentals: SEC EDGAR full-text filings and XBRL `companyfacts` API (2009+); for older periods Compustat Point-in-Time / Capital IQ via Baker Library, or raw 10-K text.
- Prices: CRSP (via WRDS) or free sources for recent periods.
- Holdings: EDGAR 13F-HR filings.
- News/context: Factiva/ProQuest historical newspapers, filtered by date.
- Rule: if a number wasn't publicly available on date T (restatements, later revisions, period-ends filed after T), it doesn't go in the packet.

## Step 5 — Calibration against history (weeks 7–10)

**5a. Pick 3–5 trades per investor.** Aim for a mix:
- at least one well-known buy,
- at least one sell or trim,
- at least one **pass** or obscure position (less likely to be memorized),
- ideally one **mistake** the investor admitted later — does the agent make the same mistake for the same reasons?

**5b. Build an information packet for each trade as of date T** (shortly before the trade): filings, financials, price, relevant news, and the archive slice dated before T. **Exclude** the investor's later letters explaining the trade.

**5c. Handle look-ahead leakage — the biggest methodological risk.** The model was trained on the internet and may simply *remember* that Buffett bought Coca-Cola in 1988. Mitigations (use several and report all):
- **Anonymize**: replace company name, ticker, product names, executives, and locations with neutral labels; scale financials by a constant.
- **Leakage probe**: ask the model, with the anonymized packet, "Which company is this? What happened next?" If it identifies it, flag the result.
- **Compare named vs. anonymized runs**: if the named run matches and the anonymized run doesn't, the agent is remembering, not reasoning.
- Prefer obscure trades and passes, which are less memorized.

**5d. Run multiple times** (e.g., 5–10 runs per trade) — LLM outputs vary; report the distribution, not the best run.

**5e. Score on two axes with a written rubric:**
- **Decision fidelity**: same action? similar sizing/conviction? similar timing?
- **Reasoning fidelity**: do the agent's key reasons match the investor's documented reasons (from contemporaneous or later letters)? Score each reason as matched / partially / missing / spurious.
Use a human grader (you) plus an LLM-as-judge with the rubric; report agreement between them.

**5f. Iterate, carefully.** If you tune the prompt on calibration trades, you're overfitting. Hold at least one or two trades out until the framework is frozen, then run them once and report as-is.

**5g. Write up honestly.** Where it matched, where it diverged, and *why* (missing data, missing judgment, framework gap, leakage). Divergences are the most valuable output.

## Step 6 — Out-of-sample basket (weeks 10–12)

1. Freeze the agent (tag the git commit) before the basket arrives — no tuning on Laurion's names.
2. Build current point-in-time packets for each name.
3. Run each agent on each name (multiple runs). "Outside my circle of competence — pass" is a legitimate, in-character answer.
4. Produce a written opinion per name in the investor's framework (the memo + structured JSON).
5. **Cross-agent matrix**: every team agent × every basket name → decision/conviction. Where agents agree, why? Where they disagree, which framework step caused it? This feeds directly into the retrospective.

## Step 7 — Process retrospective (weeks 12–13)

Answer, with evidence from your journals and calibration results:

- **Common steps** across every build (archive → dated metadata → framework extraction → staged prompts → point-in-time packets → anonymized calibration → frozen OOS test). That is your generalizable "investor-to-agent pipeline" — draw it as a diagram.
- **Idiosyncratic parts** per investor (e.g., activists need catalyst modeling; macro investors need cross-asset data; quality investors need long histories).
- **What was automatable**: screening, financial analysis, applying explicit rules, writing the memo.
- **What was defensible / failed**: judgment of people, timing, proprietary information (scuttlebutt, management access), knowing when to break one's own rules, sizing under uncertainty.
- **Effort accounting**: where the hours went (likely: data layer and archive, not prompting).
- **Evidence-based conclusion** — Laurion explicitly wants a view grounded in where agents succeeded and failed, not an opinion.

## Step 8 — Package the deliverables (week 14)

Suggested repo layout (one folder per investor, shared tooling at the top):

```
/shared
    schema.json            # common output schema
    rubric.md              # calibration scoring rubric
    run_agent.py           # runner: packet + agent → JSON + memo
    pit_data/              # point-in-time data helpers
/investors/<name>/
    archive/               # source docs (private/local if copyrighted) + manifest.csv
    trades.csv             # trade log with citations
    framework.md           # outlined process, fully cited
    agent/                 # prompts, few-shot examples, config
    calibration/<trade>/   # packet, raw runs, scores, write-up
    oos/<ticker>/          # packet, raw runs, opinion memo
    journal.md
/retrospective.md
/final_presentation
```

---

## Suggested timeline (≈14 weeks)

| Weeks | Milestone |
|---|---|
| 1 | Team setup, investor selection, data access confirmed, questions to Laurion |
| 1–3 | Archive + manifest + trade log |
| 3–5 | `framework.md` drafted and cited |
| 4–7 | Agent v1 + point-in-time data pipeline |
| 7–10 | Calibration (with leakage controls), iterate, freeze |
| 10–12 | Out-of-sample basket + cross-agent matrix |
| 12–13 | Retrospective |
| 14 | Final deliverables and presentation to Laurion |

## Common pitfalls

- **Persona prompting instead of process prompting** ("Talk like Buffett") — exactly what Laurion called naive.
- **Look-ahead bias** — later letters, restated financials, or the model's memory leaking into calibration.
- **Overfitting to calibration trades** — then claiming fidelity.
- **Cherry-picking runs** — always report the distribution.
- **Ignoring evolution** — an investor's 1970 and 2010 frameworks differ.
- **Leaving the retrospective to the end** — keep the journal from day 1.
