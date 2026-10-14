# Stage 4: Valuation

## Which valuation rule applies on 1989-02-27

The framework's "Valuation" section has one rule, taken from the 1965 partnership letter: *buy below net working capital* (`bpl-letter-1965`). I apply it first, as written.

**Net working capital test, end-1987 balance sheet (`ar-1987`):**

| $M | |
|---|---|
| Current assets | 4,136.2 |
| − Current liabilities | (4,118.5) |
| **Net working capital** | **17.7** (about $0.05 per share) |
| − Long-term debt | (803.4) |
| − Deferred income taxes | (209.9) |
| **Net-net (current assets less all liabilities)** | **≈ −$996M** |

Against a market value of about $16.5B, the price is effectively an infinite multiple of net working capital. **Coca-Cola fails the 1965 rule completely.**

That rule no longer governs on the as-of date. The 1987 letter (`brk-letter-1987#18`) reverses it in so many words: *"Our goal is to find an outstanding business at a sensible price, not a mediocre business at a bargain price,"* and "I searched for 'bargains' - and had the misfortune to find some." The method in force in 1989 is the one the framework builds elsewhere:
- value the business on **owner earnings** (`brk-letter-1986`);
- pay a price that makes sense *"even should the future of the acquired enterprise develop much along the lines of its past"* (`brk-letter-1981#3`);
- leave a "substantial excess of value" over price, which is the margin of safety (`bpl-letter-1961#3`).

Failing the net-working-capital test therefore doesn't disqualify the company. It does mean no balance-sheet floor protects the price. The margin of safety has to come from the franchise's earning power.

---

## Inputs

| Input | Figure | Source / basis |
|---|---|---|
| Price | **$46.56** | `prices`, close on 1989-02-24 |
| Shares | **~355M** (372.4M at end-1987, less 18.9M bought back in 1988, plus ~1.3M from option exercises) | `ar-1987`, `upi-1989-01-31`. The packet's $17.34B market value uses the stale 372M count. |
| Market value | **~$16.5B** | 46.56 × 355M |
| Reported EPS, 1988 | $2.85 (P/E 16.3x, earnings yield 6.1%) | `upi-1989-01-31` |
| **Owner earnings, 1988** | **$2.45–2.75 per share; midpoint $2.60** | Stage 2 estimate. Maintenance capital spending is assumed close to depreciation, and undistributed affiliate earnings are excluded. |
| Owner-earnings yield at today's price | 5.3–5.9% | |
| Dividend | $1.20 (2.6% yield) | `prices` |
| Past growth record | Continuing EPS 1976→1988: $0.79 → $2.85, ~11%/yr. 1981→1988: ~13.6%/yr. | `ar-1986`, `ar-1987`, UPI. Includes the effect of buybacks and, in 1986–88, a weaker dollar. |
| Discount rate | **Not in the packet.** I use **10%** as the base case. | Proxy: the company's own US-dollar notes carry 9⅞–12⅛% coupons, and its other debt averages "approximately 10 percent" (`ar-1987` note 7). Management's 12% after-tax cost of capital is my stress case. |

---

## Intrinsic value: owner earnings, two stages

Method: grow owner earnings at g₁ for 10 years, then at g₂ forever, and discount at r. Base owner earnings are $2.60 per share.

| Case | g₁ (yrs 1–10) | g₂ (after) | r | PV yrs 1–10 | PV of terminal | **Value per share** |
|---|---|---|---|---|---|---|
| **Past repeats** (`brk-letter-1981#3` standard) | 13% | 5% | 10% | 30.2 | 71.5 | **~$102** |
| **Conservative base** (below the record; allows for currency effects) | 10% | 5% | 10% | 26.0 | 54.6 | **~$81** |
| Conservative, lower terminal growth | 10% | 3% | 10% | 26.0 | 38.3 | **~$64** |
| **Pessimistic** | 7% | 4% | 10% | 22.4 | 34.2 | **~$57** |
| Conservative base at management's 12% rate | 10% | 5% | 12% | 23.6 | 32.6 | **~$56** |
| Pessimistic at 12% | 7% | 4% | 12% | 20.4 | 21.4 | **~$42** |

Worked example, conservative base:
- Because g₁ equals r, each of the first ten years is worth $2.60 today, so years 1–10 are worth $26.0.
- Owner earnings in year 10 are $2.60 × 1.10¹⁰ = $6.74.
- The terminal value in year 10 is $6.74 × 1.05 / 0.05 = $141.6.
- Discounted back ten years at 10%, that is $141.6 / 2.594 = $54.6.
- Total: $26.0 + $54.6 = **$80.6**.

**Assets not captured in owner earnings:** the 49% stakes in Coca-Cola Enterprises (CCE) and Columbia Pictures Entertainment (CPE), plus the other bottler affiliates, are carried at about $2.25B (`ar-1987`). That is roughly $6 per share. They earn mid-single-digit returns, and the packet doesn't give their current market value. I add a conservative **~$3 per share** as a cushion and leave it out of the margin calculation below.

---

## Margin of safety

| Value estimate | Margin at $46.56 (1 − price/value) |
|---|---|
| Past repeats, ~$102 | ~54% |
| Conservative base, ~$81 | **~42%** |
| Conservative, lower terminal growth, ~$64 | ~27% |
| Pessimistic at 10%, ~$57 | ~18% |
| Conservative at 12%, ~$56 | ~17% |
| Pessimistic at 12%, ~$42 | **−11%** (price above value) |

**The hurdle.** The framework doesn't state a number for this period. The test it applies is (1) a "sensible price" for an outstanding business (`brk-letter-1987#18`) and (2) a price that holds up if the future merely resembles the past (`brk-letter-1981#3`).
- Test (2) passes with a wide margin: about 54% if the past repeats, and about 42% on a conservative base below the record.
- The price fails only when *both* growth well below the record *and* a 12% discount rate are assumed together.
- Cross-check: at 12% annual growth, earnings in five years would be about $5.02. That is a **~10.8% earnings yield on today's $46.56**, already above the coupon on the company's own fixed-rate notes, and it keeps rising. A fixed-coupon bond can't do that under inflation (`brk-letter-1979#2`). This business has shown it can raise prices to keep pace with inflation (Stage 2).

**Conclusion:** the price is a **sensible price for an outstanding business**. The margin is about 40% on the central estimate and about 20–25% on cautious assumptions. It is not a Graham-style bargain, and the framework, as of this date, doesn't ask for one.

**Sensitivities that could make the value lower:**
1. **Currency.** Hard currencies strengthened 27%, 16% and 10% against the dollar in 1986–88. If that reverses, reported growth slows. The 10% base case already sits below the 13–14% record partly for this reason.
2. **Owner earnings are estimated.** There is no 1988 cash-flow statement or capital-spending figure. If maintenance spending is closer to total spending than to depreciation, owner earnings fall to about $2.30, and every value above drops by about 12%.
3. **Discount rate.** No long-term government bond yield is in the packet. The 10% proxy drives the result.
4. **Low-return affiliates** could absorb more capital (Stage 3).

---

## Mr. Market check ("be fearful when others are greedy", `brk-letter-1986`)

- The stock is near its 52-week high ($35.04–49.12). It traded at $35–40 for most of 1988 and fell as low as $28.96 in October 1987.
- The multiple, however, hasn't expanded: about 15.7x at end-1987 ($38.13 / $2.43) against 16.3x now ($46.56 / $2.85). The price rose mostly because earnings did, up about 17% in 1988.
- The packet shows no sign of speculative excess in the stock. The market is serving, not guiding (`brk-letter-1987`). I make no forecast about the general market (`bpl-letter-1966-mid`).

---

## Catalyst / timing

- **No catalyst needed** (`brk-letter-1987`: "The market may ignore business success for a while, but eventually will confirm it"). Value builds through owner earnings growing at a double-digit rate and through buybacks that shrink the share count. About 14.5M shares remain in the 40M-share program, to be completed by end-1990 (`upi-1989-01-31`). That is a steady tailwind to per-share value, not an event.
- **Work-out** (`bpl-letter-1957`): no announced merger, tender offer or liquidation, so this doesn't apply.
- **Control** (`bpl-letter-1963`): with a ~$16.5B market value, control isn't feasible, and the framework rules out unfriendly takeovers (`brk-letter-1986#10`). This would be a passive, "non-voting partnership" holding (`brk-letter-1981#3`).
- **Timing:** being near the 52-week high is not a reason to wait when price is below conservatively estimated value. The approach judges valuation, not timing.

---

## Facts the method needs that the packet lacks

1. The long-term government bond yield on the as-of date, to replace my 10% proxy.
2. The 1988 cash-flow statement: capital spending, depreciation, working capital and year-end share count.
3. Volume and operating-income growth with currency effects removed.
4. Current market values of the CCE, CPE and other affiliate stakes.
5. The 1988 year-end balance sheet, to recheck net debt after the 1988 buybacks.

**Stage 4 conclusion:** the company fails the old net-working-capital rule, but that rule was abandoned by 1987. On owner earnings, valued so the price makes sense if the past merely continues, intrinsic value is about **$56–100 per share, with a central estimate of about $80**, against a price of **$46.56**. The margin of safety is roughly 40% on the central case and holds up under most cautious assumptions. No catalyst is required. How much to buy is the next stage, position sizing.