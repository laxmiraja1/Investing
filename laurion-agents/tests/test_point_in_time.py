"""Point-in-time framework filter and leak guard.

  python -m unittest discover -s tests

Most tests build a small synthetic investor in a temp folder, so they need
neither the (git-ignored) archive nor a model: claude_cli.call is replaced
by a fake that records every prompt. The last test checks the real Buffett
framework and is skipped when its archive hasn't been downloaded.
"""

import re
import tempfile
import textwrap
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

from shared.agent import InvestorAgent
from shared.framework import LeakageError, LeakGuard, filter_framework
from shared.packet import Packet

ROOT = Path(__file__).resolve().parent.parent

EARLY = "Buy good businesses at sensible prices and hold them."           # doc-a, 2000-01-01
CUTOFF_DAY = "Patience matters more than activity in most years."          # doc-b, 2005-06-30
LATE = "Railroads became the best way to bet on the whole economy."        # doc-c, 2010-01-01
REPEATED = "Never risk what you have for what you don't need."             # in doc-a AND quoted from doc-c

FRAMEWORK = f"""\
# Test Investor: Investment Framework

> **Status: sourced.** Preamble written for people, never sent to the model.

## 1. Rules

- **Early rule with a later example.** *Hindsight note: he repeated this in 2010.*
  > {EARLY}
  > — `doc-a` · 2000-01-01 · `private/a.txt`

  > {LATE}
  > — `doc-c` · 2010-01-01 · `private/c.txt`

- **Late-only rule.** *Stated in 2010.*
  > {LATE}
  > — `doc-c` · 2010-01-01 · `private/c.txt`

- **Repeated rule.**
  > {REPEATED}
  > — `doc-c` · 2010-01-01 · `private/c.txt`

## 2. Evidence

> {CUTOFF_DAY}
> — `doc-b` · 2005-06-30 · `private/b.txt`

## 3. Notes for builders

- A non-rule bullet written with hindsight about 2010.
  > {EARLY}
  > — `doc-a` · 2000-01-01 · `private/a.txt`
"""

MANIFEST = """\
id,title,author,type,date_published,path,source_url,primary,tickers_mentioned,notes
doc-a,Letter A,Test Investor,letter,2000-01-01,private/a.txt,,true,,
doc-b,Letter B,Test Investor,letter,2005-06-30,private/b.txt,,true,,
doc-c,Letter C,Test Investor,letter,2010-01-01,private/c.txt,,true,,
"""

CONFIG = """\
investor: "Test Investor"
model: test-model
effort: low
server_side_fallbacks: false
retrieval_queries: ["good businesses sensible prices"]
passages_per_query: 3
examples: []
stages:
  - {id: gatekeeper, prompt: prompts/01.md, output: gate}
  - {id: business, prompt: prompts/02.md, output: text}
"""


def make_investor(tmp: Path) -> Path:
    inv = tmp / "investor"
    (inv / "archive" / "private").mkdir(parents=True)
    (inv / "agent" / "prompts").mkdir(parents=True)
    (inv / "framework.md").write_text(FRAMEWORK, encoding="utf-8")
    (inv / "archive" / "manifest.csv").write_text(MANIFEST, encoding="utf-8")
    (inv / "archive" / "private" / "a.txt").write_text(f"{EARLY} Also: {REPEATED} good businesses.", encoding="utf-8")
    (inv / "archive" / "private" / "b.txt").write_text(CUTOFF_DAY, encoding="utf-8")
    (inv / "archive" / "private" / "c.txt").write_text(f"{LATE} {REPEATED}", encoding="utf-8")
    (inv / "agent" / "config.yaml").write_text(CONFIG, encoding="utf-8")
    (inv / "agent" / "prompts" / "01.md").write_text("Stage 1: apply the filters.", encoding="utf-8")
    (inv / "agent" / "prompts" / "02.md").write_text("Stage 2: analyze the business.", encoding="utf-8")
    return inv


def make_packet(tmp: Path, as_of: str) -> Path:
    pk = tmp / "packet"
    pk.mkdir()
    (pk / "packet.yaml").write_text(textwrap.dedent(f"""\
        ticker: TST
        company: Test Corp
        as_of: {as_of}
        documents:
          - {{id: fin, type: financials, date_published: 2004-01-01, path: fin.md}}
        """), encoding="utf-8")
    (pk / "fin.md").write_text("Revenue 100, net income 10.", encoding="utf-8")
    return pk


def fake_call(log):
    def call(prompt, *, system, schema=None, **kw):
        log.append((system, prompt))
        out = {"result": "ok", "usage": {}, "modelUsage": {}, "total_cost_usd": 0.0, "session_id": "s"}
        if schema is not None:
            out["structured_output"] = {"proceed": True, "filters_checked": [], "reason": "ok"}
        return out
    return call


class FilterTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.inv = make_investor(self.tmp)

    def tearDown(self):
        self._tmp.cleanup()

    def test_keeps_only_quotes_on_or_before_cutoff(self):
        fw = filter_framework(self.inv, "Test Investor", date(2005, 6, 30))
        self.assertIn(EARLY, fw.text)
        self.assertIn(CUTOFF_DAY, fw.text)          # dated exactly on the cutoff: kept
        self.assertNotIn(LATE, fw.text)
        self.assertNotIn("doc-c", fw.text)
        self.assertNotIn("Late-only rule", fw.text)  # no evidence by the cutoff
        self.assertNotIn("Repeated rule", fw.text)   # its only citation is from 2010
        self.assertIn("Early rule with a later example", fw.text)
        for hindsight in ("Hindsight note", "Preamble", "non-rule bullet", "2010"):
            self.assertNotIn(hindsight, fw.text)
        self.assertEqual({q.doc_id for q in fw.kept}, {"doc-a", "doc-b"})

    def test_day_before_cutoff_excludes_cutoff_day_document(self):
        fw = filter_framework(self.inv, "Test Investor", date(2005, 6, 29))
        self.assertNotIn(CUTOFF_DAY, fw.text)

    def test_no_evidence_before_cutoff_fails(self):
        with self.assertRaises(LeakageError):
            filter_framework(self.inv, "Test Investor", date(1999, 12, 31))

    def test_guard_flags_later_citation_and_quote(self):
        guard = LeakGuard(self.inv, date(2005, 6, 30))
        guard.check(f"{EARLY} — `doc-a` and doc-b#0")             # earlier material passes
        with self.assertRaisesRegex(LeakageError, "doc-c"):
            guard.check('<passage cite="doc-c#0">...</passage>')
        with self.assertRaisesRegex(LeakageError, "quote from doc-c"):
            guard.check(f"As he wrote: {LATE}")
        # A later quote that was already public in an earlier document is not a leak.
        guard.check(f"He said: {REPEATED}")


class RunTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.inv = make_investor(self.tmp)
        self.packet = Packet.load(make_packet(self.tmp, "2005-06-30"))

    def tearDown(self):
        self._tmp.cleanup()

    def test_run_sends_nothing_dated_after_cutoff(self):
        sent = []
        with mock.patch("shared.claude_cli.call", side_effect=fake_call(sent)):
            result = InvestorAgent(self.inv).run(self.packet)
        self.assertEqual(len(sent), 2)                         # both stages ran
        for system, prompt in sent:
            for text in (system, prompt):
                self.assertNotIn(LATE, text)
                self.assertNotIn("doc-c", text)
        self.assertIn(EARLY, sent[0][0])                       # framework reached the model
        self.assertEqual(result.framework, {"cutoff": "2005-06-30", "quotes_shown": 2, "quotes_withheld": 3})

    def test_run_fails_loudly_before_sending_a_later_quote(self):
        (self.inv / "agent" / "prompts" / "02.md").write_text(f"Stage 2. Remember: {LATE}", encoding="utf-8")
        sent = []
        with mock.patch("shared.claude_cli.call", side_effect=fake_call(sent)):
            with self.assertRaisesRegex(LeakageError, "user prompt contains a quote from doc-c"):
                InvestorAgent(self.inv).run(self.packet)
        self.assertEqual(len(sent), 1)                         # stage 1 went out; stage 2 never did

    def test_probe_is_guarded_too(self):
        sent = []
        agent = InvestorAgent(self.inv)
        with mock.patch("shared.claude_cli.call", side_effect=fake_call(sent)), \
                mock.patch.object(agent, "system_prompt", return_value=f"system {LATE}"):
            with self.assertRaises(LeakageError):
                agent.probe_leakage(self.packet)
        self.assertEqual(sent, [])


BUFFETT = ROOT / "investors" / "buffett"


@unittest.skipUnless((BUFFETT / "archive" / "private" / "letters" / "brk-1979.txt").exists(),
                     "Buffett archive not downloaded")
class RealFrameworkTest(unittest.TestCase):
    def test_buffett_framework_at_several_cutoffs(self):
        agent = InvestorAgent(BUFFETT)
        for cutoff in (date(1960, 6, 30), date(1988, 12, 31), date(2008, 10, 16), date(2015, 3, 31)):
            fw, guard = agent.point_in_time(cutoff)
            dates = [date.fromisoformat(d) for d in re.findall(r"· (\d{4}-\d\d-\d\d)", fw.text)]
            self.assertTrue(dates, cutoff)
            self.assertLessEqual(max(dates), cutoff)
            guard.check(agent.system_prompt(cutoff), where=f"system prompt {cutoff}")
        fw, _ = agent.point_in_time(date(1988, 12, 31))
        self.assertIn("The primary test of managerial economic performance", fw.text)   # 1980
        self.assertNotIn("Apple", fw.text)                                              # 1992 onward
        self.assertNotIn("favorite holding period is forever", fw.text)                 # 1989-02-28


if __name__ == "__main__":
    unittest.main()
