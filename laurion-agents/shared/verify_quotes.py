"""Check that every quote in an investor's framework.md is verbatim in its source.

  python -m shared.verify_quotes investors/buffett

framework.md cites each quote as two blockquote lines:

  > the exact words
  > — `archive-id` · YYYY-MM-DD · `private/path/to/file.txt`

For every pair this checks that the archive id is in archive/manifest.csv,
that the date and path match the manifest row, and that the quote appears
verbatim in that file (whitespace differences ignored, nothing else). It also
flags blockquote lines with no citation under them. Exits 1 on any failure.

The archive files live in archive/private/ (git-ignored), so run the
download scripts first.
"""

import csv
import re
import sys
from pathlib import Path

PAIR = re.compile(
    r"^[ \t]*> (?!— )(?P<quote>.+)\n[ \t]*> — `(?P<id>[^`]+)` · (?P<date>\d{4}-\d\d-\d\d)[^·\n]*· `(?P<path>[^`]+)`",
    re.M,
)
QUOTE_LINE = re.compile(r"^[ \t]*> (?!— )(.+)$", re.M)


def _norm(s: str) -> str:
    return " ".join(s.split())


def verify(investor_dir: Path) -> list:
    archive = investor_dir / "archive"
    with (archive / "manifest.csv").open(newline="", encoding="utf-8") as f:
        manifest = {r["id"]: r for r in csv.DictReader(f)}
    framework = (investor_dir / "framework.md").read_text(encoding="utf-8")

    failures, texts, cited_lines = [], {}, set()
    for m in PAIR.finditer(framework):
        quote, doc_id, d, path = m["quote"], m["id"], m["date"], m["path"]
        cited_lines.add(m.start("quote"))
        line = framework.count("\n", 0, m.start()) + 1
        where = f"framework.md:{line} [{doc_id}]"
        row = manifest.get(doc_id)
        if row is None:
            failures.append(f"{where} id not in manifest.csv")
            continue
        if row["date_published"] != d:
            failures.append(f"{where} date {d} but manifest says {row['date_published']}")
        if row["path"] != path:
            failures.append(f"{where} path {path} but manifest says {row['path']}")
        src = archive / row["path"]
        if src not in texts:
            texts[src] = _norm(src.read_text(encoding="utf-8")) if src.exists() else None
        if texts[src] is None:
            failures.append(f"{where} source file missing: {src}")
        elif _norm(quote) not in texts[src]:
            failures.append(f"{where} quote not found verbatim in {row['path']}: \"{quote[:80]}\"")

    # Quote lines that never got a citation (skips the status note at the top).
    for m in QUOTE_LINE.finditer(framework):
        if m.start(1) not in cited_lines and not m.group(1).startswith(("**Status", "The agent at date")) \
                and m.group(1).strip():
            line = framework.count("\n", 0, m.start()) + 1
            failures.append(f"framework.md:{line} blockquote with no citation: \"{m.group(1)[:80]}\"")
    print(f"{len(cited_lines)} quotes from {len({m['id'] for m in PAIR.finditer(framework)})} documents checked")
    return failures


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    failures = verify(Path(sys.argv[1]))
    if failures:
        print(f"{len(failures)} failure(s):", *failures, sep="\n  ")
        sys.exit(1)
    print("All quotes verified.")


if __name__ == "__main__":
    main()
