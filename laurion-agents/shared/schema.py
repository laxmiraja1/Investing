"""Output schemas shared by every investor agent.

Every agent emits the same structures so calibration scores and the
out-of-sample basket can be compared across the whole team.
"""

from typing import List, Literal

from pydantic import BaseModel, Field

Action = Literal["BUY", "ADD", "HOLD", "TRIM", "SELL", "PASS"]


class GateResult(BaseModel):
    """Stage 1: does the idea survive the investor's hard filters?"""

    proceed: bool
    filters_checked: List[str] = Field(
        description="Each gatekeeping rule from the framework that was applied."
    )
    reason: str


class Reason(BaseModel):
    reason: str
    framework_principle: str = Field(
        description="The framework.md section or principle this reason applies."
    )
    evidence: str = Field(description="The specific fact in the packet that supports it.")


class Decision(BaseModel):
    """Final structured decision. Paired with a prose memo."""

    ticker: str
    as_of: str
    decision: Action
    conviction: int = Field(description="1 (low) to 5 (highest).")
    position_size_pct: float = Field(description="Target % of portfolio; 0 for PASS/SELL.")
    intrinsic_value_estimate: str = Field(
        description="Value per share or range, with the method used."
    )
    margin_of_safety: str
    key_reasons: List[Reason]
    risks: List[str]
    what_would_change_my_mind: List[str]
    sell_triggers: List[str]
    citations: List[str] = Field(
        description="Archive doc ids or packet doc ids relied on, e.g. 'brk-1987#3'."
    )


class ReasonScore(BaseModel):
    investor_reason: str
    match: Literal["matched", "partial", "missing"]
    agent_reason_matched: str = Field(description="Empty string if missing.")


class CalibrationScore(BaseModel):
    """LLM-judge output for one calibration run (see rubric.md)."""

    decision_match: Literal["exact", "directional", "opposite"]
    sizing_match: Literal["similar", "different", "not_applicable"]
    reason_scores: List[ReasonScore]
    spurious_reasons: List[str] = Field(
        description="Agent reasons the investor never gave and that are not in their framework."
    )
    leakage_suspected: bool = Field(
        description="True if the agent cites facts that were not public on the as-of date."
    )
    reasoning_fidelity: int = Field(description="0-4 per rubric.md.")
    notes: str


class LeakageProbe(BaseModel):
    """Can the model see through the anonymization?"""

    guessed_company: str
    confidence: Literal["none", "low", "medium", "high"]
    knows_outcome: bool
    outcome_claim: str = Field(description="What the model thinks happened next; empty if unknown.")
