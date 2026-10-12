# Buffett archive: what to collect and where

Everything listed is already a row in `manifest.csv`; put the text file at that row's `path` (under `private/`, which git ignores). Fix each placeholder `date_published` as you collect the document.

| Source | Coverage | Where | Notes |
|---|---|---|---|
| Berkshire shareholder letters | 1977-2024 | berkshirehathaway.com/letters | `python investors/buffett/archive/fetch_brk_letters.py` downloads them. Core of the archive. |
| Buffett Partnership letters | 1957-1969 | Compiled online; Miller, *Ground Rules* | Graham-era framework: generals, workouts, controls. Essential for any pre-1970 trade. |
| Annual meeting Q&A | 1994-2024 | CNBC Warren Buffett Archive (buffett.cnbc.com) | Full transcripts and video. Best source for *why he sold* (e.g. airlines 2020, IBM 2017-18). |
| Owner's Manual | 1983, rev. 1996 | Berkshire annual reports | His own statement of operating principles. |
| Superinvestors of Graham-and-Doddsville | 1984 | Columbia Business School | Value investing defended against efficient-market theory. |
| Fortune / Forbes / NYT pieces | 1974-2008 | Magazine archives (Factiva/ProQuest via Baker Library) | Market-level views: inflation 1977, 1999 bubble, 2008 "Buy American". |
| UF talk | 1998 | Video/transcripts online | Clear, compact statement of the framework. |
| Berkshire 13F-HR filings | ~1999 onward | EDGAR, CIK 1067983 | `python -m shared.edgar filings 1067983 <date> 13F-HR` |
| Berkshire 10-K / annual reports | | EDGAR, berkshirehathaway.com | Size of Berkshire on each date (for the size filter) and cost bases of holdings. |
| Secondary: Lowenstein (1995), Schroeder (2008), Cunningham's *Essays* | | Books | Leads only: cite the primary document they quote. Marked primary=false. |

## Rules for this archive

- **Date = when Buffett wrote or said it.** For the partnership letters (private at the time), use the date written, since what matters is what he thought then.
- **Watch for later explanations.** The 1989 letter explains the 1988 Coca-Cola purchase, and the archive's date filter keeps it out of a 1988 run. Don't paste later explanations into packets either.
- **After 2010, not every 13F position is Buffett's.** Todd Combs and Ted Weschler manage part of the portfolio. Only use trades Buffett publicly attributed to himself.
