# TVRemix MCP — Live TradingView Data + Analytics

**MCP server:** `tvremix` (HTTP transport)
**Endpoint:** `https://tvremix.xyz/api/mcp/v1`
**Auth:** `Bearer ${TRADINGVIEW_API}` (key in project `.env`, prefix `tvr_`)
**Server version (last verified):** v1.27.0 on 2026-05-14
**MCP config:** `.claude/mcp.json` (project-level, gitignored)
**Website:** https://tvremix.xyz/mcp

When loaded, all 37 tools surface as `mcp__tvremix__<name>`. Symbols use TradingView format: `EXCHANGE:TICKER` (e.g., `NASDAQ:QQQ`, `NYSE:SPY`, `BINANCE:BTCUSDT`).

This MCP is the **preferred live-data source** for any market-pulse or trading-skill workflow when up-to-the-minute prices, technicals, screeners, or smart-money-concepts structure are needed. Prefer it over WebSearch for ticker data, and prefer it over the local Alpaca provider when you need TradingView-specific outputs (their technicals rating, their screener, their SMC analysis).

## Quick decision tree

```
Need live quote / technicals for ONE ticker?       → get_quote / get_technicals / get_full_technicals
Need many tickers at once?                          → get_quotes_batch / analyze_multi_timeframe_batch
Need OHLCV bars (backtests, charting)?              → get_ohlcv
Want TV's aggregated buy/sell rating?               → get_technicals_rating
Need to scan the market for setups?                 → run_screener (TV-native) or rank_symbol_setups
Need sector / theme rotation read?                  → analyze_sector_tool
Want SMC structure (BOS/CHoCH/order blocks/FVGs)?   → analyze_smc_tool
Want classic swing structure (pivots/channels)?     → analyze_swing_tool
Want trend alignment across timeframes?             → analyze_multi_timeframe
Need news?                                          → get_news → get_news_story (for body)
Macro / earnings calendar?                          → get_economic_calendar / get_earnings_calendar
Options chain / Greeks?                             → get_option_expirations → get_option_chain
Analyst forecasts?                                  → get_forecasts
SEC filings / 10-K text?                            → get_documents → get_document_view
USER's own TV watchlists / alerts / charts?         → my_watchlists / my_alerts / my_charts
                                                       (requires TVRemix Chrome extension connected)
Need correlation between symbols?                   → calculate_correlation_tool
Filter list by indicator relationship (above EMA, near 52w high)?
                                                    → filter_by_indicator
General web search (Exa-powered)?                   → web_search
```

## Tool catalog (37 tools)

### Live quotes & technicals
| Tool | Purpose |
|---|---|
| `get_quote` | One-symbol snapshot: price, change, volume, O/H/L/C |
| `get_quotes_batch` | Many symbols in one call. Use this for watchlist sweeps. |
| `get_technicals` | RSI / MACD / SMA / EMA / Bollinger at one interval |
| `get_full_technicals` | All technicals across multiple timeframes (default 15m/1h/4h/1D/1W) |
| `get_technicals_rating` | TV's aggregated buy/sell/neutral rating |

### Fundamental & document data
| Tool | Purpose |
|---|---|
| `get_financials` | P/E, EPS, market cap, revenue growth, sector, industry |
| `get_forecasts` | WS price targets, ratings distribution, EPS estimates |
| `get_documents` | SEC filings list (10-K / 10-Q / 8-K) |
| `get_document_view` | Plain-text body of a specific filing |

### News & calendars
| Tool | Purpose |
|---|---|
| `get_news` | Latest headlines for a symbol |
| `get_news_story` | Full body of a news story (AST form) given its id |
| `get_economic_calendar` | Macro events (GDP, CPI, rates) with importance filtering |
| `get_earnings_calendar` | Upcoming / recent earnings, optionally filtered by symbols |
| `get_dividends_calendar` | Upcoming dividend payments by market |

### Search & screener
| Tool | Purpose |
|---|---|
| `search_symbols` | Fuzzy match ticker / name. Filters out indices/funds by default. |
| `run_screener` | TradingView's full screener with filter/sort/preset support |
| `get_symbol_data` | Raw scanner columns for one symbol (escape hatch) |

### Options
| Tool | Purpose |
|---|---|
| `get_option_expirations` | Available option expiration dates for a symbol |
| `get_option_chain` | Calls/puts for an expiration. Includes IV, delta, OI, volume |

### Bars (for charting / backtests)
| Tool | Purpose |
|---|---|
| `get_ohlcv` | Historical OHLCV bars at `interval`. TV format symbol. |

### Multi-symbol analysis (the heavy hitters)
| Tool | Purpose |
|---|---|
| `rank_symbol_setups` | Score a symbol list for tradable setups via scoring focus profile |
| `analyze_multi_timeframe` | Trend alignment across timeframes; returns bias profile |
| `analyze_multi_timeframe_batch` | Multi-symbol multi-timeframe ratings + indicators in one call |
| `filter_by_indicator` | Filter symbols by relationship to MA / Bollinger band / 52w level |
| `compute_levels_batch` | Pre-compute swing structure + SMC levels for many symbols at once |
| `compare_symbols_tool` | Side-by-side comparison: price, fundamentals, technicals |
| `analyze_sector_tool` | Scan a sector/industry, rank by metric (mcap, perf, RS) |
| `calculate_correlation_tool` | Pearson correlation matrix from REAL OHLCV (not synthetic) |

### Market structure analysis
| Tool | Purpose |
|---|---|
| `analyze_smc_tool` | Smart Money Concepts: BOS/CHoCH, order blocks, FVGs, liquidity, premium/discount |
| `analyze_swing_tool` | Pivots, trendlines, channels, range zones, swing bias |

### User's own TradingView state
Requires the **TVRemix Chrome extension** connected (server-side reads of user's TV). If not connected, these return `{"connected": false}` — handle gracefully.

| Tool | Purpose |
|---|---|
| `my_watchlists` | List user's TV watchlists (id, name, kind) |
| `my_watchlist_symbols` | Full symbol list for one of the user's watchlists |
| `my_alerts` | List user's saved price alerts (active + inactive) |
| `my_charts` | List user's saved chart layouts |

### Misc
| Tool | Purpose |
|---|---|
| `web_search` | General-purpose web search powered by Exa. Use for news/earnings commentary/macro context that doesn't fit get_news. |
| `report_session_intent` | Optional. Tell TVRemix what you're trying to do this session. Operator feedback. |
| `report_outcome` | Optional. After task completion, report how it went. Pairs with session_intent. |

## Common workflow recipes

### Pre-market brief (replaces WebSearch for prices)
1. `get_quotes_batch(symbols=["NASDAQ:QQQ", "AMEX:SPY", "AMEX:IWM"])` → futures-equivalent overnight snapshot
2. `get_economic_calendar(date=today, importance="high")` → catalysts
3. `get_earnings_calendar(date=today)` + `get_earnings_calendar(date=today, when="after_close")`
4. `analyze_multi_timeframe(symbol="AMEX:SPY")` → trend alignment / bias
5. `analyze_sector_tool(sector="...")` for top-of-mind sectors

### Single-ticker scoring (handoff to skills/trading/)
1. `get_full_technicals(symbol)` → multi-timeframe indicator stack
2. `get_financials(symbol)` → fundamentals
3. `get_technicals_rating(symbol)` → TV's aggregated read (sanity check vs Jeff Sun rubric)
4. `analyze_swing_tool(symbol)` → pivots and trend channels
5. Pass results into the Jeff Sun scorer at `skills/trading/scorer.py`

### Theme Flow Map (sector rotation)
1. `get_quotes_batch(sector_etfs)` → XLK/XLF/XLE/XLV/XLP/XLY/XLI/XLB/XLU/XLRE/XLC + IGV/SMH/MAG7
2. `analyze_multi_timeframe_batch(sector_etfs, timeframes=["1D","5D","1M"])` → multi-period strength
3. Compute z-scores vs SPY for "leadership" axis

### SMC scan for setups
1. `my_watchlist_symbols(watchlist_id)` OR `run_screener(preset=...)`
2. `compute_levels_batch(symbols, include=["smc", "swing"])` → batch structure
3. `analyze_smc_tool(symbol)` for the top candidates → entry/stop/target levels

### Watchlist refresh from your own TV account
1. `my_watchlists()` → find the watchlist id
2. `my_watchlist_symbols(watchlist_id)` → pull current members
3. `analyze_multi_timeframe_batch(symbols)` → rank for today's bias

## Caveats

- **Symbol format is strict**: `EXCHANGE:TICKER`. Use `search_symbols` first if unsure. `AAPL` alone may fail; `NASDAQ:AAPL` works.
- **`my_*` tools require the TVRemix Chrome extension** signed in to user's TradingView. Without it: `{"connected": false}` — fail gracefully, prompt user to connect from the extension side panel.
- **Rate limits unknown**: no documented quota, but assume reasonable per-key rate-limiting. Don't shotgun 1000-symbol batches without checking response.
- **Output is JSON**: tool responses are structured. Parse the `result` field; tool errors arrive as JSON-RPC errors with `code` + `message`.
- **TVRemix data ≠ Alpaca data**: TVRemix mirrors TradingView's data, which may differ slightly from Alpaca's IEX feed for intraday prices. For backtesting use Alpaca; for live research and matching TV charts use TVRemix.

## When to use TVRemix vs the local Alpaca provider

| Use case | Tool of choice |
|---|---|
| Backtesting 30m bars over years | `skills/trading/scripts/data/providers/alpaca.py` (already wired into `backtest_v9.py`) |
| Live pre-market quote / morning brief | TVRemix `get_quote` / `get_quotes_batch` |
| TV-style technicals rating | TVRemix `get_technicals_rating` |
| Multi-symbol watchlist refresh | TVRemix `analyze_multi_timeframe_batch` |
| Pulling YOUR TV watchlist | TVRemix `my_watchlists` (only this — Alpaca doesn't have it) |
| SMC structure analysis | TVRemix `analyze_smc_tool` (Alpaca doesn't have it) |
| TV screener | TVRemix `run_screener` (no equivalent on Alpaca) |
| News headlines | TVRemix `get_news` OR `WebSearch` if TVRemix is sparse |
| Macro / earnings calendars | TVRemix calendars first; FRED for economic time series |

## Verification (use this any session to confirm the MCP is live)

```python
# From any python session in the project
import os, json
from urllib import request
with open('.env') as f:
    for line in f:
        if '=' in line and not line.startswith('#'):
            k, v = line.strip().split('=', 1)
            os.environ[k] = v.strip('"').strip("'")
key = os.environ['TRADINGVIEW_API']
req = request.Request('https://tvremix.xyz/api/mcp/v1',
    data=json.dumps({'jsonrpc':'2.0','id':1,'method':'tools/list'}).encode(),
    method='POST',
    headers={'Authorization': f'Bearer {key}', 'Content-Type':'application/json'})
print(json.loads(request.urlopen(req).read())['result']['tools'][0])
```

If this returns a tool definition, the MCP is reachable and the key is valid.
