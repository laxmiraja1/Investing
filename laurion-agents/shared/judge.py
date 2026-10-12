"""Score calibration runs against what the investor actually did.

  python -m shared.judge --investor investors/klarman \\
      --trade investors/klarman/calibration/2003-xyz

Reads <trade>/truth.yaml and every <trade>/runs/*/ folder, writes
<trade>/runs/<run>/score.json and <trade>/scores.csv.

The LLM judge is a second opinion, not the grade: hand-score a sample of
runs with rubric.md and report how often you and the judge agree.
"""

import argparse
import csv
import json
from pathlib import Path

import anthropic
import yaml

from .schema import CalibrationScore

SHARED = Path(__file__).parent


def judge_run(client, rubric: str, truth: dict, run_dir: Path, model: str) -> dict:
    decision = (run_dir / "decision.json").read_text() if (run_dir / "decision.json").exists() else "{}"
    memo = (run_dir / "memo.md").read_text() if (run_dir / "memo.md").exists() else ""
    prompt = (
        "<what_the_investor_did>\n" + yaml.safe_dump(truth, sort_keys=False) + "</what_the_investor_did>\n\n"
        f"<agent_decision>\n{decision}\n</agent_decision>\n\n<agent_memo>\n{memo}\n</agent_memo>\n\n"
        "Score the agent's run against what the investor did, following the rubric."
    )
    resp = client.messages.parse(
        model=model,
        max_tokens=8000,
        system=rubric,
        messages=[{"role": "user", "content": prompt}],
        output_format=CalibrationScore,
        output_config={"effort": "high"},
    )
    if resp.stop_reason == "refusal":
        raise RuntimeError(f"Judge refused on {run_dir}")
    return resp.parsed_output.model_dump()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trade", required=True, type=Path)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--rescore", action="store_true")
    args = ap.parse_args()

    client = anthropic.Anthropic()
    rubric = (SHARED / "rubric.md").read_text()
    truth = yaml.safe_load((args.trade / "truth.yaml").read_text())
    rows = []
    for run_dir in sorted(p for p in (args.trade / "runs").iterdir() if p.is_dir()):
        score_file = run_dir / "score.json"
        if score_file.exists() and not args.rescore:
            score = json.loads(score_file.read_text())
        else:
            score = judge_run(client, rubric, truth, run_dir, args.model)
            score_file.write_text(json.dumps(score, indent=2))
        meta = json.loads((run_dir / "meta.json").read_text())
        matched = sum(r["match"] == "matched" for r in score["reason_scores"])
        rows.append({
            "run": run_dir.name,
            "anonymized": meta["anonymized"],
            "decision": json.loads((run_dir / "decision.json").read_text()).get("decision")
            if (run_dir / "decision.json").exists() else "",
            "decision_match": score["decision_match"],
            "sizing_match": score["sizing_match"],
            "reasons_matched": f"{matched}/{len(score['reason_scores'])}",
            "spurious": len(score["spurious_reasons"]),
            "reasoning_fidelity": score["reasoning_fidelity"],
            "leakage_suspected": score["leakage_suspected"],
        })
        print(rows[-1])
    if rows:
        with (args.trade / "scores.csv").open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=rows[0].keys())
            w.writeheader()
            w.writerows(rows)


if __name__ == "__main__":
    main()
