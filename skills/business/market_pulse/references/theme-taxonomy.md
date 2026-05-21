# Theme Taxonomy

The 27 themes tracked by `views/theme_flow_map.py`. Each maps to a primary
ETF and a representative-constituent sample (used for breadth + leadership
computation when we expand the view).

Source of truth: `skills/trading/scripts/data/themes.py`. To add or modify
themes, edit `themes.py` and rebuild the cache (`build_default_chain` will
refetch on next call).

## Theme strength formula

Strength = z-score of theme ETF % change vs SPY % change across each
timeframe. Computed for: 1d, 5d, 10d, 1mo. The four z-scores are averaged
into a single `strength` value, then mapped to a 0-100 percentile.

Higher strength = leading SPY by more standard deviations across multiple
timeframes consistently.

## Per-theme detail bars (top-3 themes only)

For the top-3 themes by current strength, the view renders five context bars:

- **Rotation** = delta rank vs prior session (range -5..+5, mapped to bar)
- **Breadth** = % of theme constituents above 20 EMA
- **Leadership** = theme RS vs SPY (negative = lagging)
- **Confirmation** = theme volume vs 50-day avg + advance/decline pattern
- **Durability** = inverse of top-3 holdings concentration (high = diversified)

In v1, only `Rotation` and `Leadership` are populated from real data;
the other three are placeholders showing the structure (real implementations
require holdings-level data we don't have on free tiers).

## "What To Do Next" verdict

| Strength percentile | Rotation | Verdict |
|--------------------|----------|---------|
| 85+ | improving | ACTIONABLE — focus list candidate |
| 70-85 | improving | WATCH — re-check tomorrow |
| 70-85 | flat | NEUTRAL |
| <30 | any | AVOID |
| any | declining hard | AVOID |
| else | else | NEUTRAL |
