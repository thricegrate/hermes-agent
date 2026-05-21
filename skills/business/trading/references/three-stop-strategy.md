# The 3-Stop Strategy

Jeff Sun's position-splitting approach that caps **average** loss at −0.67R instead of −1R, without meaningfully changing the upside. Developed before the T+3 framework; widely adopted across discretionary and quant desks.

Source: 2025 Substack Ch. 6 — https://jfsrev.substack.com/p/my-trading-tools-process-routine

## Why it exists

If your win rate is <40%, the single biggest lever on long-term equity is **controlling losses**, not finding better setups. Splitting a position across 3 independent exit levels means partial losses get taken at tighter stops, and only the worst-case scenario pays the full intended R.

Math: if the three stops are placed so that Stop 1 triggers first most often, Stop 2 occasionally, and Stop 3 rarely:

```
avg_loss ≈ (1/3 × −1R) + (1/3 × −0.67R) + (1/3 × −0.33R) ≈ −0.67R
```

Run this over 10 consecutive losers:
- 1R-per-loss sizing → −10R
- 0.67R-per-loss sizing → −6.7R

That 33% reduction in drawdown is the trade — the upside barely changes because once the setup works, all three thirds ride to the target together.

## How to execute

Size the **total** intended position at full risk (say $500 on a $10,000 account at 0.5% equity risk = $500). Then split into three slugs:

| Slug | Position size | Stop-loss |
|------|---------------|-----------|
| Slug 1 | 1/3 of total | Tightest stop (e.g., pivot low / M5 ORL) |
| Slug 2 | 1/3 of total | Middle stop (e.g., prior-day low) |
| Slug 3 | 1/3 of total | Widest stop (e.g., 10-MA close) |

Each slug's dollar risk is set so **its** stop triggering loses 1R on **its** share. Because the slugs are equal size but have different stop distances, slug 1 has the largest share count, slug 3 the smallest.

When Stop 1 triggers, the position becomes 2/3 size. When Stop 2 triggers, 1/3 size. When Stop 3 triggers, flat.

## Key nuances (Jeff's stated rules)

1. **Do not re-add a stopped-out slug.** If Stop 1 triggers and price reverses through the pivot again, keep the remaining 2/3 — do not buy back the stopped-out third. Re-adds violate the average-loss math.
2. **Use the strategy only on A-rated setups.** The 3-stop structure is a loss-capping mechanism, not a shotgun to spray lower-quality entries.
3. **Target R is unchanged.** If your target is +3R, the full position rides to +3R. Only the loss side splits.
4. **Re-entries** after full stop-out use a fresh 3-stop plan with new levels — do not revert to a single-stop 1R structure.

## Compatible with profit-taking

The 3-stop plan is independent of partials on the way up:
- Take partials at ATR% from 50-MA multiples (2×, 4×) or at key resistance levels.
- Partials reduce position size; remaining slugs still carry their original stop assignments.

## Scorer interaction

The scorer does **not** compute the 3-stop levels — that's execution-layer logic. But it surfaces the inputs the execution layer needs:
- `atr_daily` → used to size slugs by stop distance.
- `vcp_missing` hard gate ensures the setup has a clean pivot for Stop 1.
- `lod_atr_60pct` hard gate ensures entry is tight enough that Stop 1 is within reach.

Stage 2b's brief generator should emit a `stop_plan` block with the three levels when a setup passes the scorer. Stage 3's journal should record which stop triggered (or full stop-out / scale-out) for post-trade analysis.

## Further tools referenced by Jeff

- `@traderwillhu`'s 3-Stop Strategy Execution Tool on IBKR — auto-submits three bracket orders from a single target and three stop levels.
- Tuning the strategy with a 10× ATR% from 50-MA target (by `@lowerhighpivots`) produces a profit-factor-above-2 system on historical US equities.
