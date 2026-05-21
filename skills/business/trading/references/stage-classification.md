# Stage Classification

The Stockbee / Pradeep stage system bins each ticker into one of seven buckets
based on relative strength vs the market and Weinstein-style trend stage.

## Buckets

| Bucket | Color | Meaning | Action |
|--------|-------|---------|--------|
| White Up | white | Stage 2 leaders, strongest + youngest trends | Top focus list |
| Optimum | green | Stage 2, in-trend, RS leader | Active swing candidates |
| Secondary | green | Stage 2, in-trend, decent RS | Watchlist |
| Yellow | yellow | Stage 1 base-building or Stage 3 distribution | Stalk only |
| Blue | blue | Stage 4 downtrend with potential reversal setup | Counter-trend only |
| Red | red | Stage 4 active downtrend | Avoid long |
| White Down | white | Confirmed Stage 4 leaders to the downside | Short candidates |

## Computation rules

For each ticker with at least 200 daily bars:

### 1. Trend stage (Weinstein)

- **Stage 1** — base-building: price within 5% of 200-MA, MA flat
  (slope of last 20 days < 0.05% / day)
- **Stage 2** — uptrend: price > rising 200-MA, 50-MA > 200-MA
- **Stage 3** — distribution: price within 10% of 200-MA, 200-MA flat,
  lower highs forming
- **Stage 4** — downtrend: price < falling 200-MA, 50-MA < 200-MA

### 2. Relative strength rank

Percentile rank of 6-month (~126 trading day) total return vs the universe.
Computed once per day in `rs.py`, cached for 24 h.

### 3. Bucket logic

- **White Up**: Stage 2 + RS rank ≥ 95 + price within 25% of 52-wk high
- **Optimum**: Stage 2 + RS rank ≥ 80 + price within 15% of 52-wk high
- **Secondary**: Stage 2 + RS rank ≥ 60
- **Yellow**: Stage 1 OR Stage 3 OR (Stage 2 with RS < 60)
- **Blue**: Stage 4 + price > 20-MA AND 20-MA > recent low (reversal forming)
- **Red**: Stage 4 + RS rank > 5 (downtrending but not crushed)
- **White Down**: Stage 4 + RS rank ≤ 5 + price near 52-wk low

## Inputs

- 200-day OHLCV bars (yfinance primary, falls back to Alpha Vantage)
- Universe RS percentile rank (computed across `universe.load_universe()`)
- 52-week high/low (computed from bars)

## Outputs

A `Stage` dataclass with:
- `stage` — "Stage 1" | "Stage 2" | "Stage 3" | "Stage 4" | "Unknown"
- `bucket` — one of the 7 buckets above, or "Unclassified"
- `rs_percentile` — 0-100
- `price`, `sma50`, `sma200`
- `pct_from_52w_high`, `pct_from_52w_low`
- `sma200_slope_pct_per_day`

## Example

```python
from skills.trading.scripts.data.providers.composite import build_default_chain
from skills.trading.scripts.data.stage import classify
from skills.trading.scripts.data.rs import get_rs

chain = build_default_chain()
bars = chain.get_bars("STRL", limit=250)
rs = get_rs("STRL")
stage = classify(bars, rs_percentile=rs)
# Stage 2 / Optimum (RS ~85)
```

## Where used

- `skills/trading/scorer.py` — stage feeds into the soft-signal weight and
  may dock score for stocks not in Stage 2.
- `skills/market_pulse/views/breadth.py` — bucket distribution drives the
  regime label.
- `skills/market_pulse/views/daily_market_plan.py` — top focus list = White
  Up + Optimum buckets.
