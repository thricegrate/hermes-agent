# Screeners

Jeff maintains 14 screeners — 12 post-market (on Finviz + TradingView) and 2 live-market (on TradingView). Together they generate the raw ticker pool that watchlist management distills into the next day's Focus List.

Source: 2025 Substack Ch. 3 + 2023 qullamaggie.net summary.

## Post-market core (5 movers)

These are the foundation. Target **<60 results** per scan by tightening filters when a scan is saturated.

| # | Scan | Filter (typical) |
|---|------|------------------|
| 1 | 1-week mover >20% | Mover filter; small-cap+; avg vol >300k; cur vol >100k |
| 2 | 1-month mover >30% | Same base; tighten to >50% when too many results |
| 3 | 1-month mover >50% | Used when (2) is saturated |
| 4 | 3-month mover >50% | Longer-base candidates |
| 5 | 6-month mover >100% | Stage-2/3 leaders |

All five: small-cap+ (or mid+), avg volume >300k, current volume >100k, volatility thresholds.

## Additional post-market scans (9)

| Scan | Purpose | Notes |
|------|---------|-------|
| CANSLIM-calibrated | Jeff's headline scan (1.9M Twitter impressions). High RS + high ADR% + institutional flow proxy on Finviz Elite | Leverage Finviz's "Institutional Transaction" filter |
| High-ADR% hottest | Filters for high-ADR% names in a strong group | Qullamaggie-style 2003–04 TASR template |
| Extended-base / Cup & Handle | Long consolidations (inspired by KC +180%) | Often produces fewer but higher-conviction setups |
| Strongest mover (1W/1M/3M/6M) | Alternative mover scan with different ranking | Use Finviz mobile when on the go |
| IPO screener | Finviz only — IPO date filter; weekly cadence | Only Finviz supports this filter |
| High short float | Weekly cadence | Only Finviz supports this filter |
| Liquid ETF | Outside-equities diversification | Include leveraged and sector ETFs |
| Screen-within-screen (watchlist) | Re-screen existing watchlist daily for tightening price action | TradingView only |
| Liquid mega-cap watchlist | Fixed list of >$1B avg-$-volume names + their synthetic leveraged ETFs | Higher ADR% via 3× leveraged ETFs |

## Live-market scans (2)

| Scan | Trigger | Purpose |
|------|---------|---------|
| Focus-list RVOL monitor | RVOL on Focus List names | Entry confirmation |
| Pre-market gapper RVOL | High pre-market RVOL across the market | Surface opportunities outside the Focus List |

## Stalk-list disqualifiers (pipeline filter)

Tickers that pass a screener but fail these checks stay on the Stalk List (not the Focus List):

- Earnings within next 5 trading days.
- Price softening — needs additional tightening.
- 10-MA / 20-MA hasn't caught up to price action.
- Running into a declining 200-MA (unless 3× ADR% distance remains).
- Price below 10-MA / 20-MA (unless trailing very closely).

## Implementation notes

- **Stage 2a** (watchlist CRUD) should store each watchlist tagged with its source screen, so the user can filter "show me only names from the 1-week mover scan".
- **Stage 6** (scanners) wires the Finviz scans via `finvizfinance` (already in REFERENCES.md) and the TradingView scans via their public screen-share URLs.
- Jeff's TradingView screener share links (Oct 2025) are the canonical configurations — reference those rather than reimplementing.
- Rate-limit Finviz aggressively (token bucket ≤1 req/sec) — scraping-based library, Finviz terms discourage aggressive use.

## Capital allocation by ADR%

Jeff publishes a capital-requirement guide by ADR% bucket. Quick reference:

| ADR% bucket | Typical sizing (relative) |
|-------------|----------------------------|
| <3% | Avoid or go to 3× leveraged ETF |
| 3–5% | Full standard size |
| 5–8% | ~0.75× standard size (tighter stops give same R) |
| 8%+ | ~0.5× standard size; use tightest entry discipline |

The scorer's `adr_fit` signal rewards ADR% ≥5% because Jeff's sizing is designed to extract more R from volatile names.
