"""Point-in-time access to an investor's archive.

The archive is a folder of text/markdown files plus `manifest.csv`. Every
lookup takes an `as_of` date and only returns documents whose
`date_published` is strictly before it -- this is what keeps a 1988
calibration run from reading the 1989 letter that explains the trade.
"""

import csv
import math
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import List, Optional

MANIFEST_FIELDS = [
    "id", "title", "author", "type", "date_published", "path",
    "source_url", "primary", "tickers_mentioned",
]

_WORD = re.compile(r"[a-z0-9']+")


@dataclass
class Doc:
    id: str
    title: str
    type: str
    date_published: date
    path: Path
    primary: bool


@dataclass
class Passage:
    doc_id: str
    title: str
    date_published: date
    chunk: int
    text: str

    @property
    def cite(self) -> str:
        return f"{self.doc_id}#{self.chunk}"


class Archive:
    def __init__(self, investor_dir: Path):
        self.root = Path(investor_dir) / "archive"
        self.docs: List[Doc] = []
        manifest = self.root / "manifest.csv"
        with manifest.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if not row.get("id") or row["id"].startswith("#"):
                    continue
                self.docs.append(Doc(
                    id=row["id"],
                    title=row["title"],
                    type=row["type"],
                    date_published=date.fromisoformat(row["date_published"]),
                    path=self.root / row["path"],
                    primary=row.get("primary", "true").lower() == "true",
                ))

    def available(self, as_of: date, types: Optional[List[str]] = None) -> List[Doc]:
        """Docs the public could have read before `as_of`."""
        docs = [d for d in self.docs if d.date_published < as_of and d.path.exists()]
        if types:
            docs = [d for d in docs if d.type in types]
        return sorted(docs, key=lambda d: d.date_published)

    def passages(self, as_of: date, chunk_words: int = 400) -> List[Passage]:
        out = []
        for d in self.available(as_of):
            words = d.path.read_text(encoding="utf-8", errors="ignore").split()
            for i in range(0, len(words), chunk_words):
                out.append(Passage(d.id, d.title, d.date_published, i // chunk_words,
                                   " ".join(words[i:i + chunk_words])))
        return out

    def search(self, query: str, as_of: date, k: int = 8) -> List[Passage]:
        """BM25 keyword search over point-in-time passages.

        Deliberately dependency-free. Swap in embeddings later if keyword
        recall turns out to be the bottleneck -- but keep the as_of filter.
        """
        passages = self.passages(as_of)
        if not passages:
            return []
        toks = [_WORD.findall(p.text.lower()) for p in passages]
        n = len(toks)
        avgdl = sum(map(len, toks)) / n
        df = Counter(w for t in toks for w in set(t))
        q = _WORD.findall(query.lower())
        scored = []
        for p, t in zip(passages, toks):
            tf = Counter(t)
            s = 0.0
            for w in q:
                if w not in tf:
                    continue
                idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * tf[w] * 2.2 / (tf[w] + 1.2 * (0.25 + 0.75 * len(t) / avgdl))
            scored.append((s, p))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [p for s, p in scored[:k] if s > 0]
