# Stage 4: Valuation (Section 5) and Catalyst/timing (Section 6)

## 5.1 The framework's stated valuation rule: buy below net working capital

The only rule listed under Valuation is the Partnership-era test: buy for less than net working capital, "before placing any value on the plants and equipment" (`bpl-letter-1965`). Applied to the end-1987 balance sheet (`ar-1987`):

| $M | |
|---|---|
| Current assets | 4,136.2 |
| − Current liabilities | 4,118.5 |
| **Net working capital** | **17.7 (about $0.05 per share)** |
| − Long-term debt (803.4) and deferred taxes (209.9) | |
| **Net-net working capital** | **about −$996M** |

At $46.56 the stock trades at 5.4 times book value ($8.66) and at roughly 900 times net working capital. **It fails this test by any margin.**

By the as-of date the investor's own writing has moved past this test for businesses of this kind:
- "Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price… I searched for 'bargains' — and had the misfortune to find some" (`brk-letter-1987#18`).
- Paying a multiple of book does not change a business's return on equity: "If… you pay, say, six times book value, that does not change CCH's return on equity" (`brk-letter-1987#1`).
- The price test now in force is to buy "at prices that will make sense, even should the future of the acquired enterprise develop much along the lines of its past," and "we may very well pay a fairly fancy price for a Category 1 business if we are reasonably confident of what we are getting" (`brk-letter-1981#3`).
- The input is owner earnings (`brk-letter-1986`), and the measure is per-share intrinsic value (`brk-letter-1983#0`).

So I record the net-working-capital failure, and then apply the later method: capitalize owner earnings on the assumption that the future looks like the past. This is not a generic DCF. It is the specific test the framework sets for a business of this quality.

## 5.2 Owner-earnings valuation: does the price make sense if the future resembles the past?

### Inputs

| Input | Value | Source / assumption |
|---|---|---|
| Core owner earnings, 1987 | about **$700M = $1.88 per share** | Stage 2 range was $661–809M. I took a midpoint maintenance capex of about $225M (between depreciation of $152M and total capex of $300M) and removed $39M of affiliate dividends so the affiliates can be valued separately. |
| Shares | 372.4M | End-1987 count. 1988 buybacks are not in the packet, so this is conservative. |
| Affiliates (CPE, CCE, TCC, other) | about **$6.0 per share** ($2.26B) | Carrying value. The packet says the market value of public investees exceeded carrying by $44M at end-1987. February 1989 market values are not in the packet. |
| Net debt (about $581M) | already reflected | Owner earnings are measured after net interest. |
| Past growth | about **11% a year** | EPS from continuing operations rose from $0.84 (1977) to $2.43 (1987), about 11.2%. Net income rose from $310M to $916M, about 11.5%. 1981–87 EPS growth was about 13%. |
| Discount rate | **9%**, with 10% shown | **Missing from the packet.** I assume a long US Treasury yield of about 9% in early 1989. Coca-Cola's own US-dollar notes carry 9¾–12¾% coupons, and management states an after-tax cost of capital of 12%. |
| 1988 results | not available | I treat 1988 as the first year of the projection and do not invent a 1988 base. This is conservative. |

### Calculation

The model is ten years of growth at g₁ followed by perpetual growth at g₂. Base owner earnings are $1.88 per share.

| Case | g₁ (10 yrs) | g₂ | r | PV years 1–10 | PV terminal | Core value | + Affiliates | **Value per share** |
|---|---|---|---|---|---|---|---|---|
| A. Past continues | 11% | 5% | 9% | $20.81 | $59.19 | $80.0 | $6.0 | **$86** |
| A′. Past continues, lower terminal | 11% | 4% | 9% | $20.81 | $46.90 | $67.7 | $6.0 | **$74** |
| B. Conservative | 8% | 4% | 10% | $17.02 | $27.12 | $44.1 | $6.0 | **$50** |
| C. Franchise weakens | 5% | 3% | 10% | $14.69 | $17.37 | $32.1 | $6.0 | **$38** |

Case A in detail: year-10 owner earnings are 1.88 × 1.11¹⁰ = $5.34. The terminal value is 5.34 × 1.05 / 0.04 = $140.1, which discounts at 1.09¹⁰ (2.367) to $59.2.

### What the price assumes about growth

Strip out the affiliates, and the market price of $46.56 values the core business at about **$40.6 per share**. That is about 21.6 times core owner earnings, an owner-earnings yield of about 4.6%. Solving for the growth that justifies that price:
- At r = 9% and g₂ = 5%, the price implies only **about 3% growth for ten years**.
- At r = 10% and g₂ = 4%, it implies **about 7%**.

The past record is 11–13%. Stage 2 found the drivers still in place: international consumption per person is 16% of the US level, local-currency operating income is growing about 8%, US efficiency gains continue, and little capital is needed. The market is pricing a much slower future than the past.

Another way to see it: a 4.6% owner-earnings yield growing at 11% passes a 9% fixed-rate Treasury yield on cost in about 6.3 years (4.6 × 1.11ⁿ = 9, so n ≈ 6.3). After that it keeps growing while the bond does not.

### Cross-check on reported earnings

The price is 19.2 times 1987 EPS of $2.43. Excluding the affiliates (about $6 of value and about $0.31 of equity income), the core trades at about 19 times reported earnings. That is a full multiple for the average business. It is moderate for one that earns more than 50% on its core capital (Stage 2).

## 5.3 Margin of safety against the framework's hurdle

**The hurdle.** The framework sets no numeric hurdle. The Partnership standard was a price "substantially below what careful analysis indicates its value to a private owner to be," which creates "a comfortable margin of safety" (`bpl-letter-1962#4`, `bpl-letter-1963#5`). The standard in force at the as-of date for an outstanding business is a price that "make[s] sense, even should the future… develop much along the lines of its past" (`brk-letter-1981#3`).

**Against that standard:**

| Basis | Value | Price $46.56 relative to value |
|---|---|---|
| Future like the past (A / A′) | $74–86 | **37–46% below value**, which meets the hurdle |
| Conservative (B) | $50 | 7% below value, a thin margin |
| Franchise weakens (C) | $38 | 22% above value |

**Reading.** On the framework's own test, the price makes sense, with a margin of safety of roughly 40%. This margin does not come from conservative arithmetic the way a net-working-capital bargain's would. It rests on the franchise remaining durable. Stage 2 judged that durability strong:
- The moat has been widening.
- The franchise survived the 1985 formula mistake.
- About 11% growth over the decade came with low capital needs and an unlevered return near 25%.

Under case B the price is still covered. Only case C, a real erosion of the franchise, leaves an investor overpaying. Even there, the business would still produce cash at high returns, so a permanent loss of capital (`bpl-letter-1967-oct`) would be modest. The main risk is a lower return, not a loss of principal.

**Risks to the estimate:**
1. **Currency.** About 77% of soft-drink operating income is earned abroad. 1986–87 dollar results were lifted by currency gains of 27% and 16%. A stronger dollar would cut the base.
2. **No 1988 figures.** The base could be stale in either direction. Most likely it understates, given the prior trend and the 26th consecutive dividend increase to $1.20.
3. **Maintenance capex is not split from total capex.** This moves the base by ±$0.20 per share.
4. **Contingent guarantees** total about $719M, or about $1.90 per share, if all were called, which is unlikely.
5. **Discount rate.** It is an assumption, not a packet figure.

## 6. Catalyst / timing

- **No catalyst needed.** "The market may ignore business success for a while, but eventually will confirm it" (`brk-letter-1987`). This is a "general"-type holding of a great business. It is not a work-out, because there is no announced corporate action to profit from, and not a control situation, because the market value is $17B. One supportive factor already exists: management's authorization to buy back up to 40M shares by 1990, more than 10% of the company. At prices below value this adds to per-share value (`brk-letter-1984#4`).
- **Mr. Market's behavior.** "Mr. Market is there to serve you, not to guide you" (`brk-letter-1987`). The stock hit $53 in Q3 1987, fell to $29 in the crash, and then traded at $35–40 through most of 1988, about 15–16 times 1987 earnings. That was the more fearful moment (`brk-letter-1986`). The price has since risen to $46.56, near its 52-week high of $49.12. The best entry has passed, but the framework does not ask anyone to wait for a better one.
- **No forecasting.** "I am not in the business of predicting general stock market or business fluctuations" (`bpl-letter-1966-mid`). The decision turns on value against price today, not on whether the stock dips again.

## Stage 4 conclusion

The company **fails** the framework's literal valuation rule (net working capital) by a wide margin. That rule is superseded at the as-of date for outstanding businesses. On the method in force, owner earnings at a price that makes sense if the future resembles the past, intrinsic value is about **$74–86 per share** against a price of **$46.56**. That is a margin of safety of roughly **37–46%**. The price is covered even under conservative assumptions ($50) and is exposed only if the franchise erodes ($38). The market price implies only 3–7% growth against a decade-long record of about 11%. No catalyst is needed, and the ongoing buyback adds per-share value. The value case is strong, and it rests mainly on the durability of the franchise.