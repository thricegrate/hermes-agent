# The Six Conviction Graphics

Ch. 9 of Jeff's Substack identifies six graphics that, when internalized, give a swing trader the statistical conviction to hold through drawdowns and run winners. They're not setups — they're the math of why the system works. Stage 3's journal and Layer 3's conviction dashboard should render all six as live views on the user's own equity.

Source: https://jfsrev.substack.com/p/my-trading-tools-process-routine (Ch. 9)

## 1. Tight entries have a parabolic effect on R returns (Marios Stamatoudis)

Cutting entry distance in half (e.g., LoD < 30% ATR instead of LoD < 60% ATR) does not halve risk — it approximately **doubles** long-term R because:
- Stops sit tighter, so average loss drops.
- Winners still run to the same targets.
- Average R-multiple expands non-linearly.

**Journal view:** scatter plot of `LoD_distance_pct_atr_at_entry` vs `realized_r_multiple`. Fit a regression. Lower LoD should correlate with higher average R.

## 2. Monte Carlo simulation over 500 trades (tight vs loose entries)

Run 500-trade simulations with two sizing regimes (tight vs 50% tighter) and watch the equity curves diverge. Demonstrates that small changes in the **expectancy distribution** compound dramatically.

**Journal view:** monte_carlo_equity_sim widget. Sample from the user's own trade distribution and bootstrap 1000 forward paths of 500 trades. Show 10th / 50th / 90th percentile equity curves.

## 3. Know what a drawdown on your system looks like (Michael Nauss CMT)

Every +EV system has a baseline expected drawdown depth and duration. If the user doesn't know theirs, they'll abandon the system during a normal drawdown.

**Journal view:** rolling-max drawdown curve with historical 10 / 25 / 50 / 75 / 90 percentile bands overlaid. "Are you in a normal drawdown or an abnormal one?"

## 4. Fixed-% risk relative to equity — 1,000 trade effect

Always risking a fixed % of equity (e.g., 0.5% or 1%) instead of a fixed dollar amount reduces tail risk and compounds winners. Key insight: never scale risk up after wins by more than equity has grown.

**Journal view:** two equity curves from the user's actual trade history — one replayed with fixed-$ sizing, one with fixed-% sizing. Usually the fixed-% curve is both higher and smoother.

## 5. Higher average R has a disproportionate effect (Martin Luk / Kyna Kosling)

If the user raises average R from 1.2R to 1.8R by adjusting exit rules (e.g., trailing 10-MA instead of fixed +2R), the absolute increase in R compounds disproportionately because every trade benefits, not just winners.

**Journal view:** slider that lets the user simulate alternate exit rules on their historical entries. Show the counterfactual equity curve.

## 6. High ADR% securities benefit sizing

Higher-ADR% stocks need smaller capital allocation to produce the same R — you get more volatility per dollar. But they also demand tighter stops and tighter execution. Jeff maintains a capital-requirement reference guide by ADR% bucket (e.g., 8%+ ADR% stocks get 1.5× allocation discipline vs 4% ADR% stocks).

**Journal view:** table of realized R-multiple grouped by `adr_pct_at_entry` bucket. Confirms whether the user actually extracts more from high-ADR% names or just loses faster.

## Notes on implementation

- **Source data:** Stage 3's trade schema must capture every input these graphics need: `lod_distance_pct_atr_at_entry`, `atr_mult_from_50ma_at_entry`, `adr_pct_at_entry`, `stop_distance_r`, `realized_r_multiple`, `days_in_position`, `market_atr_mult_at_entry`.
- **Layer 3 timing:** these are Layer 3 deliverables (post-Stage 4). Do not block Stage 2b on them.
- **YAGNI:** do not build graphics 2, 3, or 5 until the journal has ≥50 recorded trades. With <50 trades the Monte Carlo is noise and the drawdown bands are empty.
