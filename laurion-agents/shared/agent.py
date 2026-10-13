"""Staged investor agent.

The agent is a single conversation that walks through the investor's
process one stage at a time (gatekeeper -> business -> ... -> decision ->
memo). Each investor configures the stages in `agent/config.yaml`; the code
here is shared so every team member's agent runs the same way.

Context the model sees:
  system   = shared/prompts/system.md + the investor's framework.md, filtered
             to quotes published on or before as_of (framework.py)
  turn 1   = the investor's own writing (archive, filtered to before as_of)
             + worked examples dated before as_of + the information packet
  turn 2.. = one stage instruction per turn

Every prompt passes a LeakGuard before it is sent: a run fails with
LeakageError if anything dated after as_of would reach the model.

Model calls go through headless Claude Code (`claude -p`); see claude_cli.py.
"""

import json
import uuid
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import List, Optional

import yaml

from . import claude_cli
from .archive import Archive
from .claude_cli import RefusalError  # noqa: F401  (re-exported)
from .framework import Filtered, LeakageError, LeakGuard, filter_framework  # noqa: F401
from .packet import Packet
from .schema import Decision, GateResult, LeakageProbe

SHARED = Path(__file__).parent
OUTPUT_TYPES = {"gate": GateResult, "decision": Decision}


@dataclass
class StageResult:
    id: str
    text: str
    parsed: Optional[dict] = None


@dataclass
class RunResult:
    stages: List[StageResult] = field(default_factory=list)
    decision: Optional[dict] = None
    memo: str = ""
    stopped_at_gate: bool = False
    usage: List[dict] = field(default_factory=list)
    retrieved: List[str] = field(default_factory=list)
    framework: dict = field(default_factory=dict)


class InvestorAgent:
    def __init__(self, investor_dir: Path):
        self.dir = Path(investor_dir)
        self.cfg = yaml.safe_load((self.dir / "agent" / "config.yaml").read_text())
        self.archive = Archive(self.dir)
        self.model = self.cfg.get("model", "claude-opus-5-5")
        self.effort = self.cfg.get("effort", "high")
        if self.cfg.get("server_side_fallbacks", False):
            raise ValueError("server_side_fallbacks is not supported with claude -p; "
                             "set it to false in agent/config.yaml.")
        self._as_of = {}  # cutoff -> (Filtered, LeakGuard)

    # ---- context ---------------------------------------------------------

    def point_in_time(self, as_of: date):
        """The framework as of `as_of` and the guard for that cutoff."""
        if as_of not in self._as_of:
            self._as_of[as_of] = (filter_framework(self.dir, self.cfg["investor"], as_of),
                                  LeakGuard(self.dir, as_of))
        return self._as_of[as_of]

    def system_prompt(self, as_of: date) -> str:
        base = (SHARED / "prompts" / "system.md").read_text(encoding="utf-8")
        framework = self.point_in_time(as_of)[0].text
        return base.replace("{{INVESTOR}}", self.cfg["investor"]) + \
            "\n\n<framework>\n" + framework + "\n</framework>"

    def investor_writing(self, packet: Packet, result: RunResult) -> str:
        queries = list(self.cfg.get("retrieval_queries", []))
        queries.append(packet.mask(packet.question))
        seen, chosen = set(), []
        per_query = self.cfg.get("passages_per_query", 3)
        for q in queries:
            for p in self.archive.search(q, packet.as_of, k=per_query):
                if p.cite not in seen:
                    seen.add(p.cite)
                    chosen.append(p)
        result.retrieved = [p.cite for p in chosen]
        blocks = [
            f'<passage cite="{p.cite}" title="{p.title}" published="{p.date_published}">\n'
            f"{p.text}\n</passage>"
            for p in chosen
        ]
        return "<investor_writing>\n" + "\n".join(blocks) + "\n</investor_writing>"

    def examples(self, as_of: date) -> str:
        out = []
        for ex in self.cfg.get("examples", []):
            if date.fromisoformat(str(ex["date_published"])) < as_of:
                text = (self.dir / "agent" / ex["path"]).read_text(encoding="utf-8")
                out.append(f'<worked_example source="{ex["source"]}">\n{text}\n</worked_example>')
        return "\n".join(out)

    # ---- model calls -----------------------------------------------------

    def _call(self, prompt: str, as_of: date, output_type=None, max_tokens: int = 16000,
              session_id: Optional[str] = None, resume: bool = False):
        """One turn via claude -p. Returns (raw result, parsed model or None).

        Raises LeakageError, before anything is sent, if the system prompt or
        this turn contains material dated after `as_of`.
        """
        system = self.system_prompt(as_of)
        guard = self.point_in_time(as_of)[1]
        guard.check(system, where="system prompt")
        guard.check(prompt, where="user prompt")
        out = claude_cli.call(
            prompt,
            system=system,
            model=self.model,
            effort=self.effort,
            schema=output_type.model_json_schema() if output_type else None,
            session_id=session_id,
            resume=resume,
            max_tokens=max_tokens,
        )
        parsed = output_type.model_validate(out["structured_output"]) if output_type else None
        return out, parsed

    # ---- pipeline --------------------------------------------------------

    def run(self, packet: Packet) -> RunResult:
        result = RunResult()
        fw = self.point_in_time(packet.as_of)[0]
        result.framework = {"cutoff": packet.as_of.isoformat(),
                            "quotes_shown": len(fw.kept), "quotes_withheld": len(fw.dropped)}
        opening = "\n\n".join(filter(None, [
            self.investor_writing(packet, result),
            self.examples(packet.as_of),
            "<information_packet>\n" + packet.render() + "\n</information_packet>",
        ]))
        # One Claude Code session per run; each stage resumes it.
        session_id = str(uuid.uuid4())
        session_cost = 0.0
        for i, stage in enumerate(self.cfg["stages"]):
            instruction = (self.dir / "agent" / stage["prompt"]).read_text(encoding="utf-8")
            content = f"{opening}\n\n{instruction}" if i == 0 else instruction

            output_type = OUTPUT_TYPES.get(stage.get("output", "text"))
            out, model = self._call(content, packet.as_of, output_type, stage.get("max_tokens", 16000),
                                    session_id=session_id, resume=i > 0)
            result.usage.append({"stage": stage["id"], **claude_cli.usage_record(out, session_cost)})
            session_cost = out.get("total_cost_usd") or session_cost

            parsed = model.model_dump() if model else None
            result.stages.append(StageResult(stage["id"], out.get("result", ""), parsed))

            if stage.get("output") == "gate" and not parsed["proceed"]:
                result.stopped_at_gate = True
                result.decision = {
                    "ticker": packet.label, "as_of": packet.as_of.isoformat(),
                    "decision": "PASS", "gate_reason": parsed["reason"],
                }
                break
            if stage.get("output") == "decision":
                result.decision = parsed
            if stage.get("output") == "memo":
                result.memo = result.stages[-1].text
        return result

    def probe_leakage(self, packet: Packet) -> dict:
        """Ask the model to identify an anonymized packet and its future.

        If it can, calibration results on this packet measure memory, not
        reasoning -- report them separately.
        """
        prompt = (
            "<information_packet>\n" + packet.render() + "\n</information_packet>\n\n"
            "Ignore the investor framework for this one question. The company above has "
            "been anonymized. Which real company do you think it is, how confident are you, "
            "and do you know what happened to it (and to its stock) after the as-of date?"
        )
        _, parsed = self._call(prompt, packet.as_of, LeakageProbe, 4000)
        return parsed.model_dump()


def save_run(result: RunResult, out_dir: Path, meta: dict) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "meta.json").write_text(json.dumps({**meta, "framework": result.framework,
                                                    "usage": result.usage,
                                                    "retrieved": result.retrieved}, indent=2))
    for s in result.stages:
        body = s.text if s.parsed is None else json.dumps(s.parsed, indent=2)
        (out_dir / f"{s.id}.md").write_text(body)
    if result.decision:
        (out_dir / "decision.json").write_text(json.dumps(result.decision, indent=2))
    if result.memo:
        (out_dir / "memo.md").write_text(result.memo)
