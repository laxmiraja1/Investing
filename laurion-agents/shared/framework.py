"""Point-in-time view of an investor's framework.md, plus a leak guard.

framework.md holds rules backed by dated quotes (see verify_quotes.py):

  - **Rule title.** *note written with hindsight*
    > the exact words
    > — `archive-id` · YYYY-MM-DD · `private/path.txt`

`filter_framework(...)` rebuilds the framework as of a cutoff date. It keeps
only quotes from documents published on or before the cutoff (dates come
from archive/manifest.csv, not from the markdown), keeps a rule only if at
least one of its quotes survives, and drops everything written with
hindsight: italic notes, tables, prose, and bullets that aren't rules.

`LeakGuard` checks every prompt before it is sent. It raises LeakageError if
the text cites an archive document published after the cutoff, or contains a
framework quote dated after the cutoff that wasn't already public in an
earlier document.
"""

import csv
import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional

QUOTE = re.compile(r"^(?P<indent>[ \t]*)> (?!— )(?P<text>.+)$")
CITE = re.compile(r"^[ \t]*> — `(?P<id>[^`]+)` · (?P<date>\d{4}-\d\d-\d\d)")
RULE = re.compile(r"^- \*\*(?P<title>.+?)\*\*")


class LeakageError(RuntimeError):
    """Text dated after the run's cutoff was about to reach the model."""


@dataclass
class Quote:
    text: str
    doc_id: str
    published: date


@dataclass
class Rule:
    title: Optional[str]  # None: quotes listed directly under a section heading
    quotes: List[Quote] = field(default_factory=list)


@dataclass
class Section:
    heading: str
    rules: List[Rule] = field(default_factory=list)


def _norm(s: str) -> str:
    return " ".join(s.split())


def load_manifest(investor_dir: Path) -> Dict[str, dict]:
    with (Path(investor_dir) / "archive" / "manifest.csv").open(newline="", encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def parse(framework_md: str, manifest: Dict[str, dict]) -> List[Section]:
    sections: List[Section] = []
    rule: Optional[Rule] = None
    in_other_bullet = False  # quotes under a non-rule bullet are illustrations; drop them
    lines = framework_md.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("## "):
            sections.append(Section(line[3:].strip()))
            rule, in_other_bullet = None, False
            continue
        if not sections:
            continue  # preamble: written for people, not the model
        m = RULE.match(line)
        if m:
            rule = Rule(m["title"].strip())
            sections[-1].rules.append(rule)
            in_other_bullet = False
            continue
        if line.startswith("- "):
            rule, in_other_bullet = None, True
            continue
        q = QUOTE.match(line)
        if q and i + 1 < len(lines):
            c = CITE.match(lines[i + 1])
            if not c:
                continue
            row = manifest.get(c["id"])
            if row is None:
                raise ValueError(f"framework.md cites {c['id']}, which is not in manifest.csv")
            quote = Quote(q["text"].strip(), c["id"], date.fromisoformat(row["date_published"]))
            if q["indent"]:
                if rule is not None:
                    rule.quotes.append(quote)
                # else: under a non-rule bullet, dropped
            else:
                if not (sections[-1].rules and sections[-1].rules[-1].title is None):
                    sections[-1].rules.append(Rule(None))
                sections[-1].rules[-1].quotes.append(quote)
                rule, in_other_bullet = None, False
    return sections


@dataclass
class Filtered:
    text: str
    cutoff: date
    kept: List[Quote]
    dropped: List[Quote]


def filter_framework(investor_dir: Path, investor: str, cutoff: date) -> Filtered:
    investor_dir = Path(investor_dir)
    manifest = load_manifest(investor_dir)
    sections = parse((investor_dir / "framework.md").read_text(encoding="utf-8"), manifest)
    kept: List[Quote] = []
    dropped: List[Quote] = []
    out = [
        f"# {investor}: investment framework as of {cutoff.isoformat()}",
        "",
        f"Each rule is supported by the investor's own words, quoted verbatim from documents "
        f"public on or before {cutoff.isoformat()}. Rules with no evidence by that date are omitted.",
    ]
    for s in sections:
        body = []
        for r in s.rules:
            ok = [q for q in r.quotes if q.published <= cutoff]
            dropped += [q for q in r.quotes if q.published > cutoff]
            if not ok:
                continue
            kept += ok
            if r.title:
                body.append(f"- **{r.title}**")
            indent = "  " if r.title else ""
            for q in ok:
                body += [f"{indent}> {q.text}", f"{indent}> — `{q.doc_id}` · {q.published.isoformat()}", ""]
        if body:
            out += ["", f"## {s.heading}", ""] + body
    if not kept:
        raise LeakageError(
            f"{investor_dir / 'framework.md'} has no quotes dated on or before {cutoff}. "
            "Source the framework (see verify_quotes.py) before running this cutoff.")
    return Filtered("\n".join(out).rstrip() + "\n", cutoff, kept, dropped)


class LeakGuard:
    """Raise LeakageError if text dated after `cutoff` is about to be sent."""

    def __init__(self, investor_dir: Path, cutoff: date, manifest: Optional[Dict[str, dict]] = None,
                 framework_quotes: Optional[List[Quote]] = None):
        investor_dir = Path(investor_dir)
        self.cutoff = cutoff
        manifest = manifest if manifest is not None else load_manifest(investor_dir)
        if framework_quotes is None:
            secs = parse((investor_dir / "framework.md").read_text(encoding="utf-8"), manifest)
            framework_quotes = [q for s in secs for r in s.rules for q in r.quotes]
        self.later_ids = {i: r["date_published"] for i, r in manifest.items()
                          if date.fromisoformat(r["date_published"]) > cutoff}
        self._id_re = re.compile(
            r"(?<![\w-])(" + "|".join(sorted(map(re.escape, self.later_ids), key=len, reverse=True)) + r")(?![\w-])"
        ) if self.later_ids else None
        later = {_norm(q.text): q for q in framework_quotes if q.published > cutoff}
        if later:
            # A later quote that already appeared in an earlier document is not a leak.
            earlier = []
            for r in manifest.values():
                p = investor_dir / "archive" / r["path"]
                if date.fromisoformat(r["date_published"]) <= cutoff and p.exists():
                    earlier.append(_norm(p.read_text(encoding="utf-8", errors="ignore")))
            later = {t: q for t, q in later.items() if not any(t in e for e in earlier)}
        self.later_quotes = later

    def check(self, text: str, where: str = "prompt") -> None:
        if self._id_re:
            m = self._id_re.search(text)
            if m:
                raise LeakageError(
                    f"{where} cites {m.group(1)} (published {self.later_ids[m.group(1)]}), "
                    f"after the run's cutoff {self.cutoff}.")
        flat = _norm(text)
        for t, q in self.later_quotes.items():
            if t in flat:
                raise LeakageError(
                    f"{where} contains a quote from {q.doc_id} (published {q.published}), "
                    f"after the run's cutoff {self.cutoff}: \"{t[:80]}\"")
