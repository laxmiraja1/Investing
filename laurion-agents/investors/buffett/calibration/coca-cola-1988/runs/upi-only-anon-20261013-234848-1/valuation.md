# Stage 4: Valuation (Framework §5) and Catalyst / timing (§6)

## 4.1 The framework's only explicit valuation rule: buy below net working capital

The "Valuation" section has a single rule: buy below net working capital (`bpl-letter-1965`). I apply it as written, using end-1987 figures from the latest full balance sheet (`ar-1987`), $ millions.

| Item | Amount |
|---|---|
| Current assets | 4,136.2 |
| − Current liabilities | (4,118.5) |
| **Net working capital** | **17.7 (≈ $0.05/share)** |
| − Long-term debt | (803.4) |
| − Deferred income taxes | (209.9) |
| **Net-net (current assets less all liabilities)** | **≈ −996 (negative)** |

Against a price of **$46.56**, the stock fails this test completely. It is a franchise business, not a cigar butt, and it never will pass.

**This rule cannot decide the case on the as-of date.** By February 1989 the investor's own writing confines it to the "generals" bargain category and rejects it as the goal for this kind of purchase:

> "Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price… In the interim, I searched for 'bargains' — and had the misfortune to find some." (`brk-letter-1987#18`)

Declining to buy because the stock sells above net working capital would apply the 1965 rule against the 1987 one. The valuation has to rest on the method the framework's later passages actually use:

- **Value to a private owner.** "An overall valuation on the enterprise substantially below what careful analysis indicates its value to a private owner to be" (`bpl-letter-1963#5`).
- **Owner earnings** as the measure of what the owner receives (`brk-letter-1986`, §3).
- **A price that makes sense on the past, not on hope.** "Prices that will make sense, even should the future of the acquired enterprise develop much along the lines of its past… We may very well pay a fairly fancy price for a Category 1 business if we are reasonably confident of what we are getting" (`brk-letter-1981#3`).
- **Price to book is not the test for a high-return business.** Paying six times book "does not change [the company's] return on equity" (`brk-letter-1987#1`).

No margin-of-safety percentage is given anywhere in the framework. The hurdle I use is therefore the one the passages imply: **price at or below value when the future is assumed to look like the past, with no rise in the multiple, and a "comfortable margin of safety" (`bpl-letter-1962#4`) under conservative assumptions.**

---

## 4.2 Value to a private owner from owner earnings

### Step 1: Owner earnings for 1988 (base year)

The packet has no 1988 cash-flow statement, so I estimate it. Assumptions are flagged.

| Item | Conservative | Generous |
|---|---|---|
| Reported net income 1988 (`upi-1989-01-31`) | 1,040 | 1,040 |
| + Depreciation & amortization (assumed ≈ 1987 level) | +160 | +160 |
| − Capital expenditures | −330 (all capex, 3-year average) | −160 (maintenance ≈ D&A) |
| **Owner earnings** | **≈ 870** | **≈ 1,040** |
| − Equity income from affiliates (valued separately below; ~$118M in 1987, −57% in 1988 ≈ $51M) | −51 | −51 |
| **Core owner earnings** | **≈ 819** | **≈ 989** |
| Per share (≈ 365M average 1988 shares = $1,040M / $2.85) | **$2.24** | **$2.71** |

**Base: core owner earnings ≈ $2.47 per share** (midpoint). As Stage 2 showed, capital spending includes growth and corporate buildings, so the true figure probably sits above the midpoint.

### Step 2: Affiliate stakes, valued at market

The company reported that "the market value of these investments was over $2.3 billion at the end of 1987" (`ar-1987`). Spread over about 355M shares at end-1988 (372.4M − 18.9M bought back + about 1.3M from option exercises), that is **≈ $6.48 per share**. I add this at market value instead of capitalizing its low equity income. The 1988 write-downs at the entertainment affiliate may have lowered the figure, which is a downside risk.

### Step 3: Capitalize core owner earnings

Debt is not subtracted separately, because owner earnings are already after interest.

**Discount rate (missing from packet).** The packet has no Treasury yields. As proxies I use:
- 10%: the company's own long-term notes carry 9⅞–12¾% coupons (`ar-1987` note 7), so a high-grade long rate near 9–10% is a reasonable assumption.
- 12%: management's stated after-tax cost of capital (`ar-1987`).

**Growth, based on the past rather than projections (`brk-letter-1981#3`).**
- 1981–1988 EPS (continuing operations) went from $1.17 to $2.85, about **13.6% a year**. That figure was helped by a weaker dollar and by buybacks.
- 1977–1983 EPS went from $0.84 to $1.35, about **8.2% a year**, in a less favorable period.
- Unit volume grew 6–10% a year from 1985 to 1988.
- Little capital is needed to grow: Stage 2 found returns of about 50% on core capital.

I test 8%, 10% and 12% growth for 10 years, then 4% a year thereafter.

**Two-stage value (core value at $2.47 + $6.48 affiliates):**

| Discount rate | g = 8% | g = 10% | g = 12% (past continues) |
|---|---|---|---|
| 10% | **$64.5** | $74.0 | $85.1 |
| 12% | $49.1 | $55.7 | $63.3 |

Worked example, 10% discount and 8% growth:
- Present value of years 1–10: $2.47 × 9.05 = $22.4.
- Earnings in year 10 are $5.33. The terminal value is $5.33 × 1.04 / 0.06 = $92.4, which discounts to $35.6 today.
- Core value = $58.0. Adding affiliates of $6.48 gives $64.5.

**Using conservative owner earnings ($2.24) instead of $2.47:**
- 10% discount, 8% growth: about $59.
- 12% discount, 8% growth: about $45. This is the only corner of the grid below the current price.

### Step 4: Cross-check as an owner's return

| Item | Figure |
|---|---|
| Price for the core alone ($46.56 − $6.48) | $40.08 |
| Core owner-earnings yield | $2.24–2.71 / $40.08 = **5.6–6.8%** |
| Growth in owner earnings per share, little capital required | 8–12% (on the past record) |
| **Implied owner's return at an unchanged multiple** | **≈ 14–19% a year** |

That compares with an assumed 9–10% on high-grade bonds, whose coupon cannot grow, and with the company's own 12% cost of capital. Earnings that can be paid out and grow by themselves are better than a fixed coupon.

Inflation is a caution (`brk-letter-1979#2`). The packet does not give the inflation rate and says only that it has "slowed in the United States." Real returns will be several points lower than nominal, but management states that the business "is able to adjust prices to compensate for increasing costs," which is the kind of business that protects against inflation.

### Step 5: Price multiples, for reference only

| Measure | Value |
|---|---|
| P/E on 1988 reported EPS | 16.3x |
| P/E on 1987 reported EPS | 19.2x |
| Price / book (end-1988 book not in packet; estimated ≈ $3.1B / 355M ≈ $8.7 per share) | ≈ 5.3x |
| Peak 1987 multiple ($53 / $2.43) | ≈ 21.8x |
| Crash-low multiple ($29 / $2.43) | ≈ 11.9x |

---

## 4.3 Margin of safety against the hurdle

| Benchmark | Value | Price $46.56 as % of value | Margin |
|---|---|---|---|
| Future like the past (10% discount, 12% growth) | $85 | 55% | **≈ 45%** |
| Conservative central case (10% discount, 8% growth) | $64.5 | 72% | **≈ 28%** |
| Harsh case (12% discount, 8% growth) | $49 | 95% | ≈ 5% |
| Harsh case with conservative owner earnings | ≈ $45 | 103% | ≈ −3% |

**Against the framework's hurdle:**

1. **"Prices that make sense even should the future develop much along the lines of its past" (`brk-letter-1981#3`): met with a wide margin.** If the past continues, price is about 55% of value.
2. **A "comfortable margin of safety" under conservative assumptions (`bpl-letter-1962#4`): about 28% in the central conservative case.** This is not a Graham-sized margin. It is a sensible price for a Category 1 business, which is what the framework accepts for "an outstanding business at a sensible price" (`brk-letter-1987#18`).
3. **Downside.** Only an unusually high discount rate combined with low growth and the conservative owner-earnings figure puts value below the price, and even then only slightly. A lasting loss of capital (`bpl-letter-1967-oct`) would require the moat itself to fail. Stage 2 found it intact, and it survived the 1985 formula reversal.

**Point estimate for later stages: intrinsic value about $64 per share (range $49–85). The price is about 72% of the central value.**

---

## 4.4 Catalyst / timing (Framework §6)

**No catalyst is needed.**
- "The market may ignore business success for a while, but eventually will confirm it" (`brk-letter-1987`).
- "In the end, investor gains must equal business gains" (`brk-letter-1985#2`).

Value here grows with the business at an estimated 8–12% a year, so time works for the holder. The ongoing buyback adds a mild tailwind: 14.5M shares remain under the 40M-share program through 1990. At these prices that should add value per share, but it is not a catalyst in the work-out sense.

**Work-out (`bpl-letter-1957`): does not apply.** No announced sale, merger, liquidation or tender exists. The case is a long-term ownership stake, not a time-bound special situation.

**Control (`bpl-letter-1963`): does not apply.** At about $17B of market value, control is impossible. The relevant model is a large minority stake in a company with excellent franchise economics and capable management, which the investor already describes for Cap Cities, GEICO and the Washington Post (`brk-letter-1981#3`, `brk-letter-1987#18`).

**Mr. Market and temperament.**
- "Mr. Market is there to serve you, not to guide you" (`brk-letter-1987`).
- "Be fearful when others are greedy…" (`brk-letter-1986`).

The stock is near its highs: $46.56 against a 52-week range of $35.04–49.12, and up about 60% from the October 1987 low of $28.96. This is not a moment of fear like October 1987. Nor is it euphoria: the multiple is about 16x, compared with roughly 22x at the August 1987 peak. The packet has no data on how the overall market is valued. Following the rule against market forecasting (`bpl-letter-1966-mid`, `fortune-1977-inflation`), I do not hold off waiting for a pullback that may not come. The price is judged on value, and on value it is sensible.

**Practical timing constraint (missing from packet).** Building a position big enough to matter means buying hundreds of millions to billions of dollars of stock. Daily trading volume is not in the packet, so I cannot say how long that would take or how much the buying itself would move the price. Accumulating over several months is the assumption.

---

## Stage 4 summary

| Item | Result |
|---|---|
| Net working capital test (`bpl-letter-1965`) | Fails. Superseded for franchise businesses by `brk-letter-1987#18` |
| Core owner earnings per share, 1988 | ≈ $2.24–2.71 (base $2.47) |
| Intrinsic value (value to a private owner) | ≈ $64 central; $49–85 range |
| Price, 24 Feb 1989 | $46.56 |
| Margin of safety | ≈ 28% central; ≈ 45% if the past continues; about zero in the harshest case |
| Owner's return implied at today's price | ≈ 14–19% a year at an unchanged multiple |
| Catalyst | None needed; buybacks are a mild tailwind; not a work-out or control situation |

**Missing data that would sharpen this:**
1. Long Treasury yields and the inflation rate for early 1989.
2. The 1988 balance sheet and cash-flow statement: actual capex, D&A, net debt and buyback cost.
3. Current market values of the CCE, TCC and CPE stakes after the 1988 write-downs.
4. Trading volume for the stock.
5. Valuation data for the market as a whole.