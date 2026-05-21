---
name: market-pulse
description: |
  Market-wide views for swing-trading research. Renders four canonical
  dashboards in chat: Daily Market Plan (Trade-Brigade morning brief),
  Theme Flow Map (sector rotation matrix), Breadth Indicators (4%+ movers,
  ratios, >50DMA%), and links the single-ticker Setup Scorer / Stage
  classifier from skills/trading/.
  Use when: "daily market plan", "morning brief", "DMP", "what's the market
  doing today"; "theme flow", "rotation", "where is capital flowing", "sector
  flow", "flow map"; "breadth", "advance/decline", "new highs", "internals",
  "5/10 day ratio"; any market-wide research request that doesn't fit
  single-ticker scoring.
  Default output: markdown text. On request: interactive Plotly HTML report
  (saved to .tmp/trading-viz/) or stylized infographic-gen PNG card.
---

# Market Pulse

Cyber Corsairs trading-research views, callable from chat by natural-language
triggers. Wraps the data layer at `skills/trading/scripts/data/` and the
Jeff Sun scoring framework.

## Views

| View | CLI | Doc |
|------|-----|-----|
| Daily Market Plan | `python skills/market_pulse/views/daily_market_plan.py` | references/view-catalog.md |
| Theme Flow Map | `python skills/market_pulse/views/theme_flow_map.py` | references/theme-taxonomy.md |
| Breadth | `python skills/market_pulse/views/breadth.py [days]` | references/breadth-thresholds.md |
| Setup Score (single ticker) | `python skills/trading/scripts/data/stage.py SYMBOL` | skills/trading/SKILL.md |

## Live data via TVRemix MCP (preferred for ad-hoc requests)

For any chat-level market-pulse request that does NOT need a saved view (live quote, sector scan, SMC analysis, screener, watchlist refresh, multi-timeframe ratings), prefer the **TVRemix MCP** over the local data layer. 37 tools surface as `mcp__tvremix__*` once the MCP server is connected.

**Reference:** [`references/tvremix-mcp.md`](references/tvremix-mcp.md) — full tool catalog, decision tree, workflow recipes, caveats.

**Quick triggers:**
- "quote for X" / "what's X doing now" → `mcp__tvremix__get_quote`
- "scan [sector/theme]" / "rank [list]" → `mcp__tvremix__analyze_sector_tool` or `rank_symbol_setups`
- "SMC on X" / "order blocks for X" / "FVGs on X" → `mcp__tvremix__analyze_smc_tool`
- "multi-timeframe on X" → `mcp__tvremix__analyze_multi_timeframe`
- "my watchlist" / "pull my TV alerts" → `mcp__tvremix__my_watchlists` (requires Chrome extension)
- "screener for X" → `mcp__tvremix__run_screener`

**When to stick with local views**: Daily Market Plan, Theme Flow Map, Breadth (these have curated layouts saved as Python views). For raw TradingView-equivalent data, TVRemix is faster and matches what the user sees on their charts.

## Output tiers

1. **Markdown text (default)** — fast, copy-pasteable. All views return this
   by default.
2. **HTML report (opt-in)** — when user says "show me", "visualize",
   "chart", "open in browser". Saves to `.tmp/trading-viz/<view>-<ts>.html`
   and returns clickable file:// link. Self-contained ~5MB files with
   Plotly bundled inline (works offline, on planes). Each view has its
   own chart layout — see render_html() in each views/*.py.
3. **Infographic card (opt-in)** — when user says "make me a card",
   "infographic", "summary card". Bridges to `skills/infographic-gen/`.
   Saves PNG to `.tmp/trading-viz/cards/`.

## Triggers → Routing

When the user message matches any of these, invoke the listed view:

- "daily market plan", "morning brief", "DMP", "what's the market doing today"
  → `views.daily_market_plan.render()`
- "theme flow", "rotation", "sector flow", "flow map", "where is capital flowing"
  → `views.theme_flow_map.render()`
- "breadth", "advance/decline", "new highs", "internals", "5/10 day ratio"
  → `views.breadth.render(days=N)` (parse N if user says "last 30 days")

Single-ticker requests ("score X", "stage of X", "is X actionable") route
to `skills/trading/` instead — see skills/trading/SKILL.md.

**HTML routing:** when the user phrasing implies visual output, append
`--html` to the CLI invocation (or call `render_html()` directly):

- "show me daily market plan" / "visualize the DMP" → `daily_market_plan.py --html`
- "chart breadth" / "html version of breadth" → `breadth.py --html`
- "show me theme flow" / "open theme flow in browser" → `theme_flow_map.py --html`
- "show me STRL setup" / "chart STRL stage" → `stage.py STRL --html`

The CLI prints a `file:///...` clickable link. Reply pattern: 1-3 line
summary in chat + the link. The HTML file lives in `.tmp/trading-viz/`
(gitignored) and isn't auto-deleted; the user can clean periodically with
`rm .tmp/trading-viz/*.html`.

**Infographic card routing:** when the user wants a shareable PNG card
(Telegram, social, screenshot bait):

- "make me a daily market plan card" / "DMP card" / "infographic of today's market"
  → `python skills/market_pulse/formatters/infographic.py dmp`
- "make me a STRL card" / "score card for X" / "STRL infographic"
  → `python skills/market_pulse/formatters/infographic.py setup STRL`
- "theme flow card" / "make me a rotation card"
  → `python skills/market_pulse/formatters/infographic.py theme`

The CLI prints a path to the PNG. Reply pattern: brief summary + markdown
image embed `![Card](file:///<path>)`. Cards are 1080-wide (Telegram-ready).

Note: the renderer is named `infographic.py` to match the plan but does NOT
bridge to `skills/infographic-gen/` (which generates Gemini hand-drawn art
that's wrong-shaped for structured trading data). Uses Pillow for direct
PNG composition. If the user wants a hand-drawn conceptual illustration of
a trading idea, they should invoke `skills/infographic-gen/` directly.

## When NOT to use this skill

- Single-ticker setup scoring → use `skills/trading/` instead
- Trade execution / paper trading → out of scope; redirect to user
- Backtest / Monte Carlo → out of scope; defer to v2

## Architecture

```
skills/market_pulse/
├── SKILL.md (this file)
├── views/                     # one .py per view, all expose render() -> str
│   ├── daily_market_plan.py
│   ├── theme_flow_map.py
│   ├── breadth.py
│   ├── _market_trend.py       # helper for DMP
│   ├── _sector_perf.py        # helper for DMP
│   └── _theme_strength.py     # helper for theme flow + DMP
├── formatters/
│   ├── markdown.py            # tables, kv lists, fmt_pct/money/int
│   └── bars.py                # Unicode block bars + traffic lights
└── references/
    ├── view-catalog.md
    ├── theme-taxonomy.md
    └── breadth-thresholds.md

skills/trading/scripts/data/   # shared data layer, imported by all views
├── providers/                 # yfinance, finnhub, alpha_vantage, fred
│                              # + alpaca/fmp deferred stubs + composite
├── cache.py                   # SQLite TTL cache
├── universe.py                # 1500-ticker universe builder
├── themes.py                  # 27 thematic ETFs
├── stage.py                   # Stockbee stage classifier
└── rs.py                      # universe RS percentile rank
```

## Performance notes

- First run of any view triggers a ~30-90s universe + multi-bar fetch
- Subsequent calls hit SQLite cache (TTL 6h intraday, 24h daily, 7d universe)
- Force refresh: pass `--refresh` to any CLI

## Data freshness

- Daily bars: refreshed once per session, valid for 24h
- yfinance is primary; on rate-limit failure, composite falls through to
  Alpha Vantage (limited to 25 calls/day)
- News: refreshed every 1h via Finnhub
- FRED macro: refreshed every 24h (most series only update weekly anyway)

## Calling pattern from chat

When the user asks "show me today's daily market plan", the assistant runs:

```bash
PY=/c/Users/thric/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe
export FINNHUB_API_KEY=$(grep '^FINNHUB_API_KEY=' .env | cut -d= -f2)
export ALPHA_VANTAGE_API_KEY=$(grep '^ALPHA_VANTAGE_API_KEY=' .env | cut -d= -f2)
export FRED_API_KEY=$(grep '^FRED_API_KEY=' .env | cut -d= -f2)
PYTHONIOENCODING=utf-8 "$PY" skills/market_pulse/views/daily_market_plan.py
```

Then pastes the markdown output back into the chat (the output is already
formatted for chat consumption).
