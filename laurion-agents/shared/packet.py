"""Information packets: everything the agent may see about one company on one date.

A packet is a folder:
  packet.yaml      -- metadata (see packets/example/packet.yaml)
  *.md / *.txt     -- documents listed in packet.yaml (filings, financials, news)

Anonymization replaces every alias (company name, ticker, products, people)
with a neutral label so the model has to reason instead of remember.
"""

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Dict, List

import yaml


@dataclass
class Packet:
    root: Path
    ticker: str
    company: str
    as_of: date
    question: str
    documents: List[dict]
    aliases: Dict[str, str] = field(default_factory=dict)
    anonymized: bool = False

    @classmethod
    def load(cls, path: Path, anonymize: bool = False) -> "Packet":
        path = Path(path)
        meta = yaml.safe_load((path / "packet.yaml").read_text())
        as_of = meta["as_of"]
        p = cls(
            root=path,
            ticker=meta["ticker"],
            company=meta["company"],
            as_of=as_of if isinstance(as_of, date) else date.fromisoformat(str(as_of)),
            question=meta.get("question", "Should we invest, and how much?"),
            documents=meta.get("documents", []),
            aliases=meta.get("aliases") or {},
            anonymized=anonymize,
        )
        for d in p.documents:
            published = d.get("date_published")
            if published and date.fromisoformat(str(published)) >= p.as_of:
                raise ValueError(f"{d['id']} was published {published}, on/after as_of {p.as_of}")
        return p

    def _mask(self, text: str) -> str:
        if not self.anonymized:
            return text
        # Longest aliases first so "Coca-Cola Company" wins over "Coca-Cola".
        for real in sorted(self.aliases, key=len, reverse=True):
            text = re.sub(rf"\b{re.escape(real)}\b", self.aliases[real], text, flags=re.I)
        return text

    @property
    def label(self) -> str:
        return self.aliases.get(self.ticker, "the Company") if self.anonymized else self.ticker

    def render(self) -> str:
        parts = [
            f"AS-OF DATE: {self.as_of.isoformat()} -- you know nothing that happened after this date.",
            f"COMPANY: {self._mask(self.company)} ({self.label})",
            f"QUESTION: {self._mask(self.question)}",
        ]
        for d in self.documents:
            text = (self.root / d["path"]).read_text(encoding="utf-8", errors="ignore")
            parts.append(
                f'<document id="{d["id"]}" type="{d.get("type", "")}" '
                f'published="{d.get("date_published", "")}">\n{self._mask(text)}\n</document>'
            )
        return "\n\n".join(parts)

    def mask(self, text: str) -> str:
        return self._mask(text)
