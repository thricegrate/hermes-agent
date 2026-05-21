# View Catalog

Each market_pulse view, what it answers, sample CLI invocation, sample output.

## Daily Market Plan

**Triggers:** "daily market plan", "morning brief", "DMP", "what's the market doing today"
**File:** `skills/market_pulse/views/daily_market_plan.py`
**CLI:** `python skills/market_pulse/views/daily_market_plan.py`
**Answers:** What's the regime today? Which sectors lead? Which thematic ETFs are running? What's the macro context?
**Sections:** Market Trend signals, Macro context (FRED), Top thematic sectors, Sub-sector heat, EW sector heat, Top 10 thematic ETFs, Breadth snapshot, Last market review carryover.

## Theme Flow Map

**Triggers:** "theme flow", "rotation", "where is capital flowing", "sector flow", "flow map"
**File:** `skills/market_pulse/views/theme_flow_map.py`
**CLI:** `python skills/market_pulse/views/theme_flow_map.py`
**Answers:** Which themes are accumulating capital? What's the rotation across timeframes?
**Sections:** Rotation matrix (themes × 1d/5d/10d/1mo, color = z-score strength), Top-3 detail with rotation/breadth/leadership/confirmation/durability bars + verdict.

## Breadth

**Triggers:** "breadth", "advance/decline", "new highs", "internals", "5/10 day ratio"
**File:** `skills/market_pulse/views/breadth.py`
**CLI:** `python skills/market_pulse/views/breadth.py [days]`
**Answers:** How healthy is participation? Hot or cold? UPTREND/NEUTRAL/DOWNTREND?
**Sections:** Regime label + 5-day ratio, table of last N days with Up4%/Down4%/Up25%Q/Up25%M/Up50%M/Up13%34/ATR10x/>50DMA%.

## Setup Score (in skills/trading/, not market_pulse)

**Triggers:** "score X", "stage of X", "is X actionable", "setup score"
**File:** `skills/trading/scripts/data/stage.py` + `skills/trading/scorer.py`
**CLI:** `python skills/trading/scripts/data/stage.py SYMBOL`
**Answers:** Is this ticker actionable? What stage is it in? Score 0-100.
**Sections:** Stage 1-4 classification, bucket (White Up..White Down), RS percentile, key levels (sma50/200, 52w high/low), score components (hard gates + soft signals).

## Output tiers

All views return Tier 1 (markdown text) by default.

**Tier 2 (HTML report):** triggered by "show me", "visualize", "chart", "html version" — saves
self-contained Plotly HTML to `.tmp/trading-viz/<view>-<timestamp>.html` and returns the path.

**Tier 3 (infographic card):** triggered by "make me a card", "infographic", "summary card",
"share image" — bridges to `skills/infographic-gen/`, saves PNG to `.tmp/trading-viz/cards/`.

## Performance notes

- First run of any view triggers a ~30-90s universe + multi-bar fetch.
- Subsequent calls hit the SQLite cache (TTL 6h intraday, 24h daily, 7d universe).
- Force refresh: pass `--refresh` to any CLI.
