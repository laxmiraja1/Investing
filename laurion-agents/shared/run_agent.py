"""Run an investor agent on an information packet.

Examples:
  # 5 named + 5 anonymized runs of a calibration trade, plus a leakage probe
  python -m shared.run_agent --investor investors/klarman \\
      --packet investors/klarman/calibration/2003-xyz/packet \\
      --runs 5 --both --probe

  # out-of-sample basket name
  python -m shared.run_agent --investor investors/klarman --packet packets/ABC --runs 3

Outputs land in <packet>/../runs/<named|anon>-<n>/ unless --out is given.
"""

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

from .agent import InvestorAgent, save_run
from .packet import Packet


def git_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--investor", required=True, type=Path)
    ap.add_argument("--packet", required=True, type=Path)
    ap.add_argument("--runs", type=int, default=1, help="Repeat runs; report the distribution.")
    ap.add_argument("--anonymize", action="store_true")
    ap.add_argument("--both", action="store_true", help="Run named and anonymized.")
    ap.add_argument("--probe", action="store_true", help="Run the leakage probe once.")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--label", help="Batch label, prefixed to run folder names and saved in meta.json.")
    args = ap.parse_args()

    agent = InvestorAgent(args.investor)
    out_root = args.out or args.packet.parent / "runs"
    modes = [False, True] if args.both else [args.anonymize]

    if args.probe:
        probe = agent.probe_leakage(Packet.load(args.packet, anonymize=True))
        out_root.mkdir(parents=True, exist_ok=True)
        (out_root / "leakage_probe.json").write_text(json.dumps(probe, indent=2))
        print("leakage probe:", probe)

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    for anon in modes:
        packet = Packet.load(args.packet, anonymize=anon)
        for n in range(1, args.runs + 1):
            tag = f"{args.label + '-' if args.label else ''}{'anon' if anon else 'named'}-{stamp}-{n}"
            result = agent.run(packet)
            save_run(result, out_root / tag, {
                "investor": agent.cfg["investor"],
                "model": agent.model,
                "effort": agent.effort,
                "packet": str(args.packet),
                "as_of": packet.as_of.isoformat(),
                "anonymized": anon,
                "label": args.label,
                "agent_commit": git_commit(),
            })
            d = result.decision or {}
            print(f"{tag}: {d.get('decision')} conviction={d.get('conviction')} "
                  f"size={d.get('position_size_pct')}")


if __name__ == "__main__":
    main()
