# Sizing Overlay — Position Sizing & Kill Switches

**Layered on top of:** [three-stop-strategy.md](three-stop-strategy.md). Does NOT replace it.

**Companion to:** [macroeconomic-thesis.md](macroeconomic-thesis.md), [aschenbrenner-watchlist.md](aschenbrenner-watchlist.md), [thesis-catalysts.md](thesis-catalysts.md).

This file defines:
1. How Aschenbrenner thesis modifies Jeff Sun base sizing per tier
2. When (if ever) the thesis can override Jeff Sun's hard gates and stops
3. Kill switches that force exit regardless of thesis

---

## Tier × Dimension Matrix

| Dimension | Tier 1 | Tier 2 | Tier 3 |
|-----------|--------|--------|--------|
| **Hold horizon** | Multi-year (through 2027-2028) | 6-12 months | 1-3 months |
| **Sizing multiplier** | 2x-3x Jeff Sun base | 1.5x base | 1.25x base |
| **Max position size** | 12% of trading capital | 6% of trading capital | 3% of trading capital |
| **Max theme concentration** | 35% of capital across all Tier 1 names in one theme | 20% per theme | 10% per theme |
| **Stop override allowed?** | YES, if catalyst within 30 days AND no kill switch tripped | NO | NO |
| **3-stop slug structure** | Standard 1/3 + 1/3 + 1/3 (per three-stop-strategy.md) | Standard | Tighter Stop 3: 0.5x normal ATR distance |
| **Drawdown tolerance (before forced exit regardless)** | 35% from peak | 20% from peak | 12% from peak |
| **Adds allowed?** | YES, 1R above breakeven stop AND still leading (per Jeff's rule) | YES, same rule | NO |
| **Hard gate that can be relaxed by override** | `lod_atr_60pct` (entry can chase up to 80% ATR if catalyst within 7 days) | NONE | NONE |
| **Hard gates that NEVER relax** | `biotech_exclusion`, `declining_200ma`, `vcp_missing`, `earnings_within_5d`, `gap_resistance_zone`, `atr_50ma_4x` | All | All |

### Reading the multipliers

Jeff Sun's standard base sizing: position is sized at $X dollar risk total (typically 0.5-1% equity risk per trade). The 3-stop strategy splits that $X across three slugs.

**Tier 1 multiplier of 2-3x means:**
- Total dollar risk on the trade = 2-3x normal $X
- Three slugs still get 1/3 each by share count weighting
- Average loss across many losers is still -0.67R, just on a larger $R

**Sizing decision tree per setup:**
1. Does the ticker pass Jeff Sun hard gates and score ≥70? If no, no trade.
2. Is the ticker on the [aschenbrenner-watchlist.md](aschenbrenner-watchlist.md) at Tier 1/2/3? If no, standard Jeff Sun sizing.
3. If yes, apply tier multiplier to total dollar risk.
4. Check max position size cap (Tier 1: 12% of capital, etc.). Cap before multiplier if needed.
5. Check max theme concentration. If already at cap on the theme, skip the trade.
6. Execute three-stop-strategy.md slug splitting on the multiplied total.

---

## Stop Override Rules (Tier 1 Only)

Tier 1 names can hold past Jeff Sun's standard exit signals IF and ONLY IF all the following are true:

1. **Catalyst window:** A scheduled catalyst per [thesis-catalysts.md](thesis-catalysts.md) is within 30 calendar days (e.g., NVDA earnings, hyperscaler capex guide quarter, NRC permit decision, scheduled executive order window).

2. **No kill switch tripped:** None of the kill-switch tripwires below have fired in the prior 30 days.

3. **No structural break:** Price has not closed below the 50-week MA. This is the absolute floor — below 50-week, no override no matter what.

4. **Position still under max:** The position size is still within the 12% max-position cap and 35% theme cap.

If all 4 hold and Jeff Sun's stop triggers, you may **hold the remaining slugs** through the stop on the conviction that the catalyst will reaccelerate. You do NOT add through the stop (Jeff's "do not re-add a stopped-out slug" rule still applies). You simply skip the exit.

If any of the 4 fails (catalyst expires, kill switch trips, 50-week breaks, max position hit), exit per standard Jeff Sun rules immediately.

### Override accounting

When you override a stop, log it. Track:
- Date of override
- Which Jeff Sun stop was bypassed
- Catalyst justifying the override
- Outcome (catalyst confirmed thesis / catalyst disappointed / kill switch tripped before catalyst / position re-rallied past entry)

After 10 overrides, review the cumulative R-multiple performance vs. counterfactual (took the stop, re-entered on next setup). If override-take cumulative R is worse than no-override-take, stop overriding entirely.

---

## Kill Switches (Force Exit / Downgrade Tier Regardless of Setup)

These are quantitative tripwires. If any fires, take the specified action regardless of price action, conviction, or remaining catalyst window.

| # | Tripwire | Source/Data | Action |
|---|----------|-------------|--------|
| 1 | NVDA datacenter revenue YoY growth < 30% for 2 consecutive quarters | NVDA quarterly earnings 10-Q | Drop ALL Tier 1 names to Tier 2 sizing immediately. Re-evaluate at next NVDA print. |
| 2 | Sum of MSFT/GOOGL/AMZN/META capex guide cut > 15% from prior quarter (any single quarter) | Quarterly earnings — sum of FY current-year capex guidance | Exit ALL Tier 3 positions. Reduce Tier 2 by 50%. Hold Tier 1. |
| 3 | Major model release shows < 10% benchmark improvement on flagship eval (MMLU-Pro / SWE-bench Verified / GPQA / ARC-AGI) | New flagship model release from OpenAI/Anthropic/Google/Meta | Reduce ALL tiers by 1 notch (T1→T2 sizing, T2→T3 sizing, T3→exit). |
| 4 | MU guides HBM revenue down 2+ consecutive quarters | MU quarterly earnings | Exit ALL HBM-specific positions (MU, SNDK, WDC). Keep broader semi exposure. |
| 5 | Regulatory pause on frontier model training (EU AI Act enforcement action OR US executive order limiting compute above any threshold) | Federal Register, EU AI Office announcements | Cut ALL sizing to base Jeff Sun (no multipliers). Re-evaluate after 60 days. |
| 6 | Two Tier 1 names break their 50-week MA structure (close below 50WMA for 2+ consecutive weeks) | Weekly closes | Review entire thesis. Reduce Tier 1 sizing to Tier 2 multipliers across the board until thesis revalidated. |
| 7 | Aschenbrenner publicly reverses his core thesis | Author public statements, fund disclosures, essay updates | Re-evaluate everything. Reduce to base Jeff Sun sizing pending review. |

### Secondary tripwires (monitor, do not automatically act)

- DeepSeek-class efficiency breakthrough at frontier scale (would compress compute demand trajectory)
- CXMT (China memory) reaches HBM3-equivalent production capacity (would compress MU pricing power)
- Major lab security breach disclosed publicly (would either accelerate HACK/PLTR upside OR trigger sector confidence collapse — direction TBD by market reaction)
- US-China diplomatic normalization (would reduce defense / cyber urgency)
- Taiwan Strait crisis escalation (would TSM tail risk, watch defense for upside)

For secondary tripwires, log the event but do not change sizing until you can assess market reaction (1-2 trading sessions).

---

## Interaction With Jeff Sun's Hard Gates

The Aschenbrenner overlay does NOT generally relax Jeff Sun's hard gates. They are loss-prevention rules and they protect the average-loss math.

**Exception — Tier 1 only, single relaxation allowed:**

The `lod_atr_60pct` hard gate (LoD distance > 60% ATR) drops a ticker when entry is chasing. For Tier 1 names with a catalyst within **7 days** (not 30), you may relax this gate to 80% ATR — meaning you can chase the entry up to 80% of an ATR from low-of-day. This acknowledges that thesis-driven pre-catalyst runs are often parabolic and waiting for full reset can miss the move.

**All other hard gates ALWAYS apply:**
- `biotech_exclusion` (gap risk — applies to all tiers)
- `atr_50ma_4x` (extension exhaustion — applies)
- `declining_200ma` (fighting trend — applies)
- `gap_resistance_zone` (overhead supply — applies)
- `vcp_missing` (no clean pivot — applies)
- `earnings_within_5d` (gap risk — applies, INCLUDING for thesis names — earnings IS the catalyst, but enter post-print not pre-print)

---

## Profit-Taking Rules (How Tier Hold Rules Interact with Partials)

Jeff Sun's normal profit-taking: partials at 2x and 4x ATR from 50-MA, or at key resistance.

**Tier 1 modification:**
- Take partials at 2x ATR (1/4 of position out)
- Take partials at 4x ATR (1/4 of position out — now at half size)
- Hold remaining half through the catalyst window
- Beyond catalyst: revert to standard 3-stop trailing per three-stop-strategy.md

**Tier 2 modification:**
- Take partials at 2x ATR (1/3 out)
- Take partials at 4x ATR (1/3 out)
- Hold remaining 1/3 to 6x ATR or catalyst, whichever first
- Standard trailing thereafter

**Tier 3:**
- Standard Jeff Sun partials. No modification.

---

## Concentration & Diversification Rules

The "full macro overlay" allows aggressive concentration but enforces theme diversification.

**Per-name max position:** 12% (Tier 1), 6% (Tier 2), 3% (Tier 3) — as in matrix above.

**Per-theme max:** 35% in any single Tier 1 theme. The 5 Tier 1 themes:
1. Nuclear / Uranium
2. Power Grid / Generation
3. Semiconductors
4. AI Infrastructure
5. Defense AI / Primes

**Across Tier 1:** If aggregate Tier 1 exposure exceeds 80% of trading capital, do not add new Tier 1 positions even if a new setup fires. Trim winners first.

**Tier 1 floor of diversification:** Always have positions in at least 3 of the 5 Tier 1 themes. If all 3 are in one theme (e.g., all Nuclear), you are functionally a single-theme fund. Rebalance.

**Hyperscaler proxies (MSFT/GOOGL/AMZN/META) do NOT count toward Tier 1 exposure** — they are Tier 3 trades at standard sizing because the market has priced their AI exposure already.

---

## Override and Tier Adjustments (Quick Reference)

| Situation | Action |
|-----------|-------|
| Tier 1 setup, catalyst within 30 days, no kill switch | Full 2-3x sizing, stop override eligible |
| Tier 1 setup, NO catalyst within 30 days | Full 2-3x sizing, NO override (standard 3-stop) |
| Tier 1 setup, catalyst within 30 days, kill switch #2 tripped | Reduce to Tier 2 multiplier (1.5x), no override |
| Tier 2 setup, any condition | 1.5x sizing, standard stops |
| Tier 3 setup, catalyst confirmed | 1.25x sizing, tighter Stop 3 |
| Tier 3 setup, catalyst already passed without thesis confirmation | Skip the trade |
| Kill switch #5 (regulatory pause) tripped | All trades to base Jeff Sun sizing, no overlay |
| Kill switch #6 tripped (two T1 names below 50WMA) | All Tier 1 to Tier 2 multipliers, review thesis |

---

## Appendix A: Math Behind The Multipliers

### Why 2-3x for Tier 1?

Standard Jeff Sun base risks 0.5-1% of equity per trade. At 2-3x, Tier 1 trades risk 1-3% of equity per trade.

Across 10 consecutive losers (which is rare but tail-possible), worst-case drawdown:
- Tier 1 at 3x with -0.67R average loss = ~-20% from equity peak
- Tier 1 at 2x with -0.67R = ~-13.4% from equity peak

Combined with the 35% drawdown tolerance per Tier 1 position, and the 80% aggregate Tier 1 cap, max plausible portfolio drawdown from a thesis collapse:

- 10 consecutive Tier 1 losers at max sizing + thesis break before kill switch trips → ~25-30% portfolio drawdown
- Compare to single-name max-out (12% of capital × 35% drawdown) = ~4% portfolio hit per name

The 35% per-Tier-1-name drawdown tolerance is the most exposed parameter. If real losses approach this in practice, tighten to 25%.

### Why 1.5x for Tier 2?

Tier 2 covers shorter-horizon capex-cycle plays where the thesis is real but the time horizon allows multiple re-entries. 1.5x reflects elevated conviction without surrendering the ability to compound from a healthy equity base. Standard 3-stop applies, so average loss is still -0.67R on a 1.5x-larger dollar size.

### Why 1.25x for Tier 3?

Tier 3 catalysts are sharper but riskier. 1.25x gives a modest size premium without exposing capital to thesis fragility. The tighter Stop 3 (0.5x ATR multiplier on the widest slug) reflects that Tier 3 setups should not require giving back as much ATR.

### Why the 35% per-name drawdown tolerance?

Tier 1 multi-year holds need to absorb 2026-2028 volatility without panic-cutting. Historical analogs:
- AAPL 2008-2009: -55% from peak then 10x in next decade
- AMZN 2008: -64% from peak then 12x
- NVDA 2022: -68% from peak then 8x in next 2 years

A 35% tolerance is conservative relative to these but generous relative to swing-trading norms. The override allows you to ignore Jeff Sun stops up to this point. Beyond 35%, no thesis is worth the position.

---

## Appendix B: Kill Switch Tracking Worksheet

Use this format in a private journal (or future scripts/) to log kill-switch states monthly:

```
DATE: YYYY-MM-DD
TRIPWIRE 1 (NVDA DC YoY < 30% for 2 Q): _ / _  (latest 2 quarter YoY growth %)
TRIPWIRE 2 (Sum hyperscaler capex cut > 15%): _% Q/Q
TRIPWIRE 3 (Model benchmark improvement < 10%): latest model = _, prior = _
TRIPWIRE 4 (MU HBM down 2+ Q): _, _ (last 2 Q guidance direction)
TRIPWIRE 5 (Regulatory pause): YES / NO — last event _
TRIPWIRE 6 (Two T1 names below 50WMA): list any names below 50WMA
TRIPWIRE 7 (Aschenbrenner thesis reversal): YES / NO — public statement _

OVERRIDES USED THIS MONTH: _ (target: <2)
OVERRIDE PNL CUMULATIVE: _R (target: positive)
TIER 1 AGGREGATE EXPOSURE: _% of capital (cap: 80%)
LARGEST THEME CONCENTRATION: _% in _ (cap: 35%)
```

Monthly refresh agent (per [thesis-catalysts.md](thesis-catalysts.md)) will update [reality-check.md](reality-check.md) with new events and re-check this worksheet.

---

## Appendix C: Quote Support for Sizing Decisions

The aggressive sizing approach is justified by Aschenbrenner's own framing:

- **Conviction:** "Before the decade is out, we will have built superintelligence." (Ch.8) — multi-year hold framing
- **Magnitude:** "As AI revenue grows rapidly, many trillions of dollars will go into GPU, datacenter, and power buildout before the end of the decade." (Ch.3, Ch.8) — justifies max position sizing on direct beneficiaries
- **Concentration:** Aschenbrenner's own fund reportedly concentrated ~70% in semis + power per Q1 2025 public filings — confirms theme concentration is the strategic choice, not over-aggression
- **Time horizon:** "The decade after — the 2030s — will be at least as eventful." (Ch.8) — supports multi-year hold over swing exits

Kill switches operate on the principle that the thesis IS falsifiable. From Ch.5: "Moments with ambiguous evidence, when metrics will superficially look ok, but there are some warning signs that hint at looming danger." The tripwires above are the hard evidence that overrides ambiguity.
