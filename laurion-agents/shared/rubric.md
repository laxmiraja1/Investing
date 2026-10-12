# Calibration Scoring Rubric

You are grading whether an AI agent reproduced a real investor's decision **and** the reasons behind it. You are given what the investor actually did (with their documented reasons and sources) and the agent's decision and memo. Grade strictly; a right answer for the wrong reasons is a failure of fidelity, not a success.

## 1. Decision match
- **exact** — same action (e.g. BUY vs BUY, PASS vs PASS).
- **directional** — same direction, different degree (BUY vs ADD, TRIM vs SELL, HOLD when the investor added modestly).
- **opposite** — different direction (BUY vs PASS/SELL, SELL vs BUY/ADD).

## 2. Sizing match
- **similar** — the agent's position size is within roughly a factor of two of the investor's actual size, or both are clearly "large/concentrated" or both "small/starter".
- **different** — otherwise.
- **not_applicable** — PASS/SELL decisions, or the investor's size is unknown.

## 3. Reasons
For each documented investor reason, mark:
- **matched** — the agent gives substantively the same reason (wording can differ).
- **partial** — the agent touches on it but misses the part that drove the decision, or gives it little weight.
- **missing** — absent.

List as **spurious** any agent reason that the investor did not give *and* that does not follow from their framework (e.g. technical analysis for a fundamental investor, a famous catchphrase applied where it doesn't fit).

## 4. Reasoning fidelity (0–4)
- **4** — Same decision; the investor's main reason is matched and most others are matched or partial; no meaningful spurious reasons.
- **3** — Same or directional decision; main reason matched; some reasons missing or a minor spurious one.
- **2** — Decision matches but reasoning is mostly generic or differs in what drove it; or decision directional with partial reasoning.
- **1** — Decision opposite but the analysis shows parts of the framework applied correctly; or decision matches for clearly wrong reasons.
- **0** — Opposite decision with little resemblance to the investor's process.

## 5. Leakage
Set **leakage_suspected** to true if the agent states or relies on anything that was not public on the as-of date: later financial results, the stock's later price path, later events, or how the investment turned out. If the agent names the real company in an anonymized run, also flag it and say so in notes.

## 6. Notes
In 2–4 sentences, explain the biggest gap between the agent and the investor and its probable cause: missing data in the packet, a framework gap, missing judgment (e.g. assessing management in person), or leakage.
