## Stage 4: Valuation

I recognize the company. As before, I'm reasoning only from the packet as of 1989‑02‑27.

---

### 5. The framework's Valuation section: "buy below net working capital" (`bpl-letter-1965`)

This is the only valuation rule the framework records, so I apply it first and literally. The latest balance sheet is year-end 1987 (`ar-1987`).

| ($M) | YE 1987 |
|---|---|
| Current assets | 4,136.2 |
| – Current liabilities | (4,118.5) |
| **Net working capital** | **17.7**, about **$0.05/share** on 372.4M shares |
| – Long-term debt | (803.4) |
| – Deferred income taxes | (209.9) |
| **Current assets less all liabilities** | **–$995.6M (negative)** |

The price is $46.56 against net working capital of $0.05 per share. It is also 5.4× book value ($8.66 at year-end 1987). **Coca-Cola fails the rule completely.** No plausible price would pass, because the company's value is in an earning power that doesn't appear on the balance sheet.

**Why the analysis doesn't stop here.** The framework's own evidence from this date shows this rule describes the earlier "bargain" method, and that method had been superseded for businesses of this kind:
- *"Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price… I searched for 'bargains' – and had the misfortune to find some"* (`brk-letter-1987#18`).
- *"We may very well pay a fairly fancy price for a Category 1 business if we are reasonably confident of what we are getting"*, at prices *"that will make sense, even should the future of the acquired enterprise develop much along the lines of its past"* (`brk-letter-1981#3`).
- The owner-earnings rule in Business analysis (`brk-letter-1986`) supplies the earnings figure such a valuation needs.

So for an outstanding business I value **owner earnings**, and I test whether the price makes sense **if the future resembles the past**. This is a judgment on my part. The Valuation section as written doesn't contain this method. I've assembled it from rules in sections 3, 6 and 8 and from the cited passages, and I'm not using an open-ended DCF.

---

### Inputs

**A. Owner earnings base (1988).** The packet gives 1988 net income but no 1988 cash-flow statement, so parts of this are assumptions, marked [A].

| ($M) | Conservative | Upper |
|---|---|---|
| 1988 net income (`upi-1989-01-31`) | 1,040 | 1,040 |
| + Depreciation & amortization [A: 1987's $153.5M +~5%] | 160 | 160 |
| – Undistributed equity income [A: equity income ~$51M after the 57% fall; dividends received ~$39M as in 1987] | (12) | (12) |
| – Capex [conservative: 1985–87 average, all capex treated as necessary; upper: maintenance ≈ depreciation] | (353) | (160) |
| **Owner earnings** | **≈ 835** | **≈ 1,028** |
| Per share (~365M average 1988 shares) | **≈ $2.30** | **≈ $2.82** |

This is a little above Stage 2's rough $1.90–2.60. The reason is that the CPE write-downs cut equity income, so less of reported earnings is uncollected affiliate income. I value on the **conservative $2.30**. Because it deducts *all* capex, growth is already paid for out of that figure.

**B. Share count.** 372.4M at year-end 1987, minus 18.9M bought back in 1988, plus about 1.3M from option exercises, gives about **355M** shares. Market value is about **$16.5B**. The packet's $17.34B uses the stale 372M count.

**C. Discount rate.** The packet has no government bond yield, which is the missing benchmark. I anchor on figures in the packet: the company's 8% pension discount rate and expected return (`ar-1987` note 8), the roughly 10% weighted rate on its other long-term debt and its 9⅞–12¼% notes, and management's 12% after-tax cost of capital. I use **9% and 10%** as the main cases and show **12%** as a stress test.

Two features support rates at the lower end. Reinvestment needs are low (soft-drink capex was $170M against $1.43B of operating income), and management says it can raise prices to cover costs. Under the Fortune analysis, these are what protect owners from inflation (`fortune-1977-inflation`, `brk-letter-1979#2`).

---

### Test 1: What does the price assume?

If owner earnings grow at a steady rate *g* forever, then $46.56 = $2.30 × (1+g) / (r – g):

| Discount rate | Growth the price implies |
|---|---|
| 9% | **≈ 3.9%** |
| 10% | **≈ 4.8%** |
| 12% | ≈ 6.7% |

Here is what the business has actually done:
- Net income grew **11.6% a year from 1976 to 1988** ($278M to $1,040M).
- EPS grew **13.6% a year from 1981 to 1988** ($1.17 continuing to $2.85).
- 1988 international operating income rose 21% and US operating income 9%.
- International per-capita consumption is **16% of the US level**.
- Management guides to EPS growth "well into the mid-teens" for 1989.

At 9–10%, the market is pricing owner earnings to grow at about 4–5% forever. That is less than half the historical rate for a business that hasn't yet saturated its markets.

### Test 2: Value if the future looks like the past (`brk-letter-1981#3`)

Owner earnings start at $2.30. Growth runs at *g₁* for ten years, then *g₂* forever.

| Scenario | g₁ (10 yrs) | g₂ | Value @ 9% | Value @ 10% | Value @ 12% |
|---|---|---|---|---|---|
| A. No growth | 0% | 0% | $25.6 | $23.0 | $19.2 |
| B. Pessimistic | 7% | 4% | $60.6 | $50.1 | n/c |
| C. History cut by about a fifth | 10% | 5% | **$90.3** | **$71.3** | $49.7 |
| D. History continues | 12% | 5% | $106.0 | $83.3 | n/c |

Worked example, C at 10%. Years 1–10 grow at the same rate as the discount, so the PV is $2.30 × 10 = $23.0. Year‑11 owner earnings are $2.30 × 1.10¹⁰ × 1.05 = $6.26. Capitalized at 5% that gives $125.3, which discounts by 1.10¹⁰ (2.594) to $48.3. The total is **$71.3**.

### Items deliberately left out
- **Affiliate stakes.** After the January 1988 CPE spin-off, CPE is about $654M ($989M less the $335M in-kind dividend payable), plus CCE $749M, TCC $84.5M and other $435M. That totals roughly **$1.9B, or about $5.40/share** at carrying value. At year-end 1987 their market value exceeded carrying value by only about $44M. Only their cash dividends are in owner earnings.
- **Contingent offsets.** Guarantees total about $394M, and recourse on CPE receivables is about $325M (CPE indemnifies the company). That's roughly $1–2/share if all of it went bad.
- **Net effect.** About **$3–5/share of value is left uncounted**. Net debt is already reflected through interest expense in owner earnings.

### Cross-checks
- **Earnings multiple over time.** 9.8× EPS at year-end 1980, about 11.6× when the company was buying back stock in 1984, and **16.3× today**. The stock isn't cheap against its own past. The business is better, though: ROE was about 20% then and is about 33% now.
- **Owner-earnings yield against a bond.** $2.30 / $46.56 = **4.9%** today. At 10% growth, the yield on today's price reaches about 9.6% in seven years and about 12.7% in ten. A bond paying 9–10% never rises.
- **Market mood.** The stock is near the top of its 52-week range ($35.04–$49.12) and about 33% above the February 1988 low. Fifteen months ago it touched $28.96 in October 1987. The market isn't fearful today, and it isn't euphoric either: the multiple is about 16× earnings and about 20× owner earnings. `brk-letter-1986` asks for greed only when others are fearful, and that condition isn't met. The no-forecasting rule forbids waiting for a lower price on a guess.

---

### Margin of safety against the hurdle

**The hurdle.** The framework sets no number for franchise businesses. Its documented standard is a "substantial excess of value" that "creates a comfortable margin of safety" (`bpl-letter-1961#3`, `bpl-letter-1962#4`), and for buybacks "well below… intrinsic value" (`brk-letter-1984`). I make this operational with two conditions:
1. The price is **at least one-third below value** in the "history, discounted" case, at the main discount rates.
2. The price is **no higher than value** in the pessimistic case.

| Test | Value | Price / value | Discount to value | Meets hurdle? |
|---|---|---|---|---|
| Literal Valuation rule (net working capital) | $0.05 | — | — | **No** |
| C (history cut by a fifth) @ 9% | $90.3 | 0.52 | **48%** | Yes |
| C @ 10% | $71.3 | 0.65 | **35%** | Yes |
| B (pessimistic) @ 9% / 10% | $60.6 / $50.1 | 0.77 / 0.93 | 23% / 7% | Yes, no loss of value |
| A (no growth) @ 10% | $23.0 | 2.02 | –102% | No. The buyer pays for growth |
| C @ 12% (management's own WACC) | $49.7 | 0.94 | 6% | Thin |
| C @ 10% using $1.90 base (Stage 2 low end) | $58.9 | 0.79 | 21% | Short of one-third |

**Reading the table.** Under the framework's method for outstanding businesses, the price is about **35–48% below** value when history is discounted by a fifth. Even the pessimistic case leaves value at or above the price. The margin depends on three things:
1. **Growth actually continuing.** The no-growth value is half the price, so the moat (Stage 2) is the real margin of safety.
2. **A discount rate near 9–10%.** At 12%, the margin nearly disappears.
3. **The owner-earnings base.** With the low $1.90 figure, the margin shrinks to about 21%.

This is not a "princes at toad-like prices" situation in the sense of `brk-letter-1981#3`. It is a good margin, not an extreme one. It rests mainly on how certain the franchise's growth is, not on asset value.

---

### 6. Catalyst / timing

- **No catalyst needed** (`brk-letter-1987`: *"The market may ignore business success for a while, but eventually will confirm it"*). This fits. The gap between the roughly 4–5% growth the price implies and the 11–13% historical record should close as reported results come in. Mr. Market *"is there to serve you, not to guide you."* The 1987 crash shows the market can offer this stock at very different prices within months.
- **Work-out** (`bpl-letter-1957`): not applicable. No sale, merger, liquidation or tender is pending. The 40M-share buyback, of which 25.5M is done, is a continuing support to per-share value. It is not a timed corporate event.
- **Control** (`bpl-letter-1963`): not applicable. At about $16.5B of market value, control can't be bought. The relevant model is the *"substantial junior partner"* or *"non-voting partnership"* in `brk-letter-1981#3`: a large, passive minority stake in a company managed by others. That suits the Stage 3 finding that operating ability is excellent but capital allocation outside the core business is weak.
- **Timing.** The framework forbids market forecasting (`bpl-letter-1966-mid`, `fortune-1977-inflation`). The price is near the 52-week high, but that isn't a reason to wait. The question is only whether price is sensibly below value, and it is.

---

### Facts the valuation needs that the packet lacks

1. **Long-term government bond yield**, the benchmark for the discount rate. I used 8–12% anchored on packet figures.
2. **The 1988 annual report**: capex, depreciation, deferred taxes, working capital, the year-end balance sheet, and the exact share count.
3. **Split of capex into maintenance and growth**, which accounts for the gap between the $2.30 and $2.82 owner-earnings figures.
4. **Constant-currency growth.** A weaker dollar helped by 27%, 16% and 10% in 1986–88. A stronger dollar would cut reported international earnings.
5. **Market value of CPE and the other affiliates after the spin-off**, and CCE's 1988 results.
6. **Inflation rate**, to check whether a 5% long-run growth rate is real or mostly nominal.
7. **Tax outlook**: the Puerto Rico exemption expiring in 1995 and the effect of the 34% US rate.

---

### Stage 4 conclusion

Coca-Cola fails the framework's literal Valuation rule. It is nowhere near net working capital, and it never would be. By 1989, though, the framework's own evidence has replaced that rule with "an outstanding business at a sensible price" for franchises. On that standard the stock clears the bar. At $46.56, the price assumes owner earnings grow about 4–5% a year forever. Assuming growth well below the company's record still puts value at **$71–90/share, 35–48% above the price**, and the pessimistic case still exceeds the price. The margin rests on how durable the franchise is, not on assets, and it narrows sharply at a 12% discount rate. No catalyst is required. Position sizing is the next stage, where this dependence on growth and the discount rate should limit how large a holding the "concentrate when the facts are clear" rule can justify.