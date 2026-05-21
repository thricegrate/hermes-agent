# Breadth Thresholds

Numerical definitions used by `views/breadth.py` to color-code the indicator
table and feed the regime label in Daily Market Plan.

## Universe

The breadth universe = `universe.load_universe()` filtered to common stocks.
Approximate size: 776–1500 tickers depending on yfinance availability
(some Finnhub-listed OTC/foreign tickers don't have Yahoo data). Refreshed
weekly. Always includes the 102 hand-curated seed tickers.

## Indicators

For each trading day, compute over the universe:

| Metric | Definition | Hot | Cold |
|--------|------------|-----|------|
| Stocks Up 4%+ Today | count where (close - prev_close) / prev_close ≥ 0.04 | > 200 | < 50 |
| Stocks Down 4%+ Today | same threshold but down | > 200 | < 50 |
| 5-day Ratio | sum(up 4%+ over 5 days) / sum(down 4%+ over 5 days) | > 2.0 | < 0.5 |
| 10-day Ratio | same over 10 days | > 1.5 | < 0.7 |
| Up 25%+ Quarter | count where 63-day return ≥ 25% | > 300 | < 100 |
| Up 25%+ Month | count where 21-day return ≥ 25% | > 100 | < 30 |
| Up 50%+ Month | count where 21-day return ≥ 50% | > 20 | < 5 |
| Up 13%+ 34 Days | count where 34-day return ≥ 13% | > 600 | < 200 |
| 10x ATR Ext | count where price > 50ma + 10×ATR(14) | > 8 | < 2 |
| >50DMA % | percent of universe trading above 50-day SMA | > 60 | < 30 |

## Regime

Regime is derived from a weighted blend of breadth signals:

- **🟢 UPTREND**: 5-day ratio > 1.5 AND >50DMA% > 50 AND Up 25%+ Quarter > 300
- **🔴 DOWNTREND**: 5-day ratio < 0.6 AND >50DMA% < 30 AND Up 25%+ Month < 30
- **🟡 NEUTRAL**: anything else

## Data feed notes

yfinance pulls Yahoo Finance data, which aggregates full-market US trades —
no IEX/SIP distinction concerns. Adjusted for splits/dividends by default
(`auto_adjust=True` on download). Occasional rate-limit flakiness on bulk
downloads is mitigated by the Alpha Vantage fallback in the composite chain
(though AV's 25/day quota means breadth view leans heavily on yfinance).

## Caching

- Breadth snapshot: 6h TTL (intraday refresh OK during trading hours)
- Universe: 7-day TTL
- RS percentile table: 24h TTL
