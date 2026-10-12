"""Staged investor agent.

The agent is a single conversation that walks through the investor's
process one stage at a time (gatekeeper -> business -> ... -> decision ->
memo). Each investor configures the stages in `agent/config.yaml`; the code
here is shared so every team member's agent runs the same way.

Context the model sees:
  system   = shared/prompts/system.md + the investor's framework.md
  turn 1   = the investor's own writing (archive, filtered to before as_of)
             + worked examples dated before as_of + the information packet
  turn 2.. = one stage instruction per turn
"""

import json
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import List, Optional

import anthropic
import yaml

from .archive import Archive
from .packet import Packet
from .schema import Decision, GateResult, LeakageProbe

SHARED = Path(__file__).parent
OUTPUT_TYPES = {"gate": GateResult, "decision": Decision}


class RefusalError(RuntimeError):
    pass


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


class InvestorAgent:
    def __init__(self, investor_dir: Path, client: Optional[anthropic.Anthropic] = None):
        self.dir = Path(investor_dir)
        self.cfg = yaml.safe_load((self.dir / "agent" / "config.yaml").read_text())
        self.client = client or anthropic.Anthropic()
        self.archive = Archive(self.dir)
        self.framework = (self.dir / "framework.md").read_text(encoding="utf-8")
        self.model = self.cfg.get("model", "claude-opus-5-5")
        self.effort = self.cfg.get("effort", "high")
        self.use_fallbacks = self.cfg.get("server_side_fallbacks", True)

    # ---- context ---------------------------------------------------------

    def system_prompt(self) -> list:
        base = (SHARED / "prompts" / "system.md").read_text(encoding="utf-8")
        text = base.replace("{{INVESTOR}}", self.cfg["investor"]) + \
            "\n\n<framework>\n" + self.framework + "\n</framework>"
        # Stable across every stage and run -> cache it.
        return [{"type": "text", "text": text, "cache_control": {"type": "ephemeral"}}]

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

    def _call(self, messages: list, output_type=None, max_tokens: int = 16000):
        kwargs = dict(
            model=self.model,
            max_tokens=max_tokens,
            system=self.system_prompt(),
            messages=messages,
            output_config={"effort": self.effort},
        )
        if self.use_fallbacks:
            # On a safety-classifier decline, the API retries on Anthropic's
            # recommended fallback model instead of returning the refusal.
            kwargs["extra_headers"] = {"anthropic-beta": "server-side-fallback-2026-07-01"}
            kwargs["extra_body"] = {"fallbacks": "default"}
        if output_type:
            resp = self.client.messages.parse(output_format=output_type, **kwargs)
        else:
            resp = self.client.messages.create(**kwargs)
        if resp.stop_reason == "refusal":
            raise RefusalError(str(resp.stop_details))
        if resp.stop_reason == "max_tokens":
            raise RuntimeError("Hit max_tokens; raise max_tokens for this stage.")
        return resp

    @staticmethod
    def _as_history(resp) -> dict:
        # Echo the assistant turn back unchanged (thinking blocks included).
        content = [b.model_dump(exclude_none=True, exclude={"parsed_output"}) for b in resp.content]
        return {"role": "assistant", "content": content}

    @staticmethod
    def _text(resp) -> str:
        return "".join(b.text for b in resp.content if b.type == "text")

    # ---- pipeline --------------------------------------------------------

    def run(self, packet: Packet) -> RunResult:
        result = RunResult()
        opening = "\n\n".join(filter(None, [
            self.investor_writing(packet, result),
            self.examples(packet.as_of),
            "<information_packet>\n" + packet.render() + "\n</information_packet>",
        ]))
        messages: list = []
        for i, stage in enumerate(self.cfg["stages"]):
            instruction = (self.dir / "agent" / stage["prompt"]).read_text(encoding="utf-8")
            content = f"{opening}\n\n{instruction}" if i == 0 else instruction
            messages.append({"role": "user", "content": content})

            output_type = OUTPUT_TYPES.get(stage.get("output", "text"))
            resp = self._call(messages, output_type, stage.get("max_tokens", 16000))
            messages.append(self._as_history(resp))
            result.usage.append({"stage": stage["id"], **resp.usage.model_dump(exclude_none=True)})

            parsed = resp.parsed_output.model_dump() if output_type else None
            result.stages.append(StageResult(stage["id"], self._text(resp), parsed))

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
        resp = self._call([{"role": "user", "content": prompt}], LeakageProbe, 4000)
        return resp.parsed_output.model_dump()


def save_run(result: RunResult, out_dir: Path, meta: dict) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "meta.json").write_text(json.dumps({**meta, "usage": result.usage,
                                                    "retrieved": result.retrieved}, indent=2))
    for s in result.stages:
        body = s.text if s.parsed is None else json.dumps(s.parsed, indent=2)
        (out_dir / f"{s.id}.md").write_text(body)
    if result.decision:
        (out_dir / "decision.json").write_text(json.dumps(result.decision, indent=2))
    if result.memo:
        (out_dir / "memo.md").write_text(result.memo)
