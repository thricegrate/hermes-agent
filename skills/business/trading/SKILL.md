---
name: jeff-sun-method
description: |
  Swing-trading setup scorer + Stockbee stage classifier encoding Jeff Sun's
  15 hard execution rules, 3-stop strategy, scoring rubric, and daily workflow.
  Includes the 7-bucket stage system (White Up / Optimum / Secondary / Yellow /
  Blue / Red / White Down) for single-ticker classification.
  Use when: scoring whether a ticker is actionable today; "score X", "stage of X",
  "is X actionable", "what stage is X in"; generating a daily brief with
  setup_matches; evaluating VCP/RS/RVOL/ADR%/ATR-from-50-MA; designing the
  3-stop execution plan; sizing a position with -0.67R average-loss cap;
  reviewing journal stats against the six conviction graphics; running the
  post-market → watchlist → focus list → pre-market → execution flow.
  Also triggers on: "setup matcher", "setup score", "hard gate", "VCP", "RVOL",
  "ADR%", "ATR from 50-MA", "focus list", "3-stop strategy", "Jeff Sun",
  "qullamaggie", "Stockbee stage", "Pradeep stage", "swing trading rules".
---

# Jeff Sun Method — Swing-Trading Setup Scorer + Playbook

Jeff Sun is a 15-year discretionary swing trader whose methodology has been publicly documented in a long-form Substack (2025) and a 2023 summary at qullamaggie.net. This skill encodes his rule set, scoring rubric, and daily workflow so the Trading Terminal's setup matcher (Stage 2b), brief generator, and journal enforce it consistently.

**Sources (attribution required in any derivative text):**
- Primary: https://jfsrev.substack.com/p/my-trading-tools-process-routine (2025)
- Secondary: https://qullamaggie.net/jeff-suns-method-and-flow/ (2023 summary)

## When to load this skill

- Before editing the setup matcher (`api/brief/setup_matcher.py`) or validator.
- Before generating a daily brief that includes `setup_matches`.
- When the user asks whether a specific ticker is a quality setup today.
- When tuning scoring weights, thresholds, or hard-gate behavior.
- When building or reviewing the journal (R-multiple histogram, average-R tracking, drawdown simulator).
- When selecting or tuning a screener (the 14-screener Finviz + TradingView workflow).

## Live data sources

Two complementary data layers:

1. **TVRemix MCP** (preferred for live single-ticker data) — wraps TradingView server-side. 37 tools as `mcp__tvremix__*`. Use for live quotes, technicals, SMC structure, multi-timeframe ratings, news, options, calendars, and pulling the user's own TV watchlists/alerts. Full catalog: [`skills/market_pulse/references/tvremix-mcp.md`](../market_pulse/references/tvremix-mcp.md).

2. **Local Alpaca provider** (preferred for backtests and historical bars) — `skills/trading/scripts/data/providers/alpaca.py`. Use for OHLCV bar fetches at scale, the `backtest_v9.py`-style strategy validation, and any workflow that needs deterministic offline data.

**Single-ticker scoring workflow with TVRemix:**
```
mcp__tvremix__get_full_technicals(symbol)     → multi-timeframe indicator stack
mcp__tvremix__get_financials(symbol)          → fundamentals (P/E, EPS, etc.)
mcp__tvremix__get_technicals_rating(symbol)   → TV's aggregated rating (sanity check vs Jeff Sun)
mcp__tvremix__analyze_swing_tool(symbol)      → pivots, channels, range zones
mcp__tvremix__analyze_smc_tool(symbol)        → BOS/CHoCH, order blocks, FVGs, liquidity
# Then pass into Jeff Sun scorer (scripts/scorer.py) for the 15 hard-rule gate.
```

**Symbol format requirement**: TVRemix needs `EXCHANGE:TICKER` (e.g., `NASDAQ:NVDA`, not `NVDA`). If unsure, call `mcp__tvremix__search_symbols` first.

## Core deliverable

A **scorer** that takes OHLCV + a snapshot dict and returns a `SetupScore`:

1. **Hard gates** — any fail drops the ticker. The LLM never sees dropped tickers.
2. **Soft signals** — weighted sum to a 0–100 score. `score >= 70` passes.
3. **Session gates** — brief-wide rules (max 3 new positions/session, 30-min post-open delay).

Reference implementation: [`scripts/scorer.py`](scripts/scorer.py). Rule catalog: [`rules.yaml`](rules.yaml).

## Hard gates (violation → ticker dropped)

| Rule | Threshold | Rationale |
|------|-----------|-----------|
| `lod_atr_60pct` | LoD distance > 60% ATR | Entry is chasing; the spring is uncoiled |
| `atr_50ma_4x` | ATR% multiple from 50-MA > 4× | Extension is exhausted; wait for compression |
| `biotech_exclusion` | Ticker is IBB/XBI component | Gap risk; only trade biotech via LABU/LABD |
| `declining_200ma` | Price against a declining 200-MA (slope<0 AND close<200-MA) | Fighting primary trend |
| `gap_resistance_zone` | Prior gap within 1×ATR above entry | Overhead supply kills the move |
| `vcp_missing` | Fewer than 2 measurable tightening contractions in last 60 sessions | "Never enter with loose price action" |
| `earnings_within_5d` | Earnings reports in ≤5 trading sessions | Gap risk; wait for post-earnings drift setup |

## Soft signals (weighted 0–100)

| Signal | Weight | Input |
|--------|--------|-------|
| `relative_strength` | 25 | VARS or IBD-style RS rank |
| `rvol_at_trigger` | 20 | RVOL vs 50-day avg at proposed entry |
| `vcp_quality` | 15 | Count + tightness of contractions |
| `industry_group_rs` | 15 | Group in top 5 by 1-month RS |
| `base_and_pocket_pivot` | 10 | 1–3 month base + pocket-pivot volume |
| `adr_fit` | 10 | ADR% ≥ 5% |
| `positional_penalty` | −5 | Per consecutive market up-day; gap-up open |

Pass gate: `score >= 70`.

## Session gates (enforced brief-wide)

- **Max 3 new positions per session** (rule #9). The brief generator must cap `setup_matches` at 3 after scoring + sorting.
- **30-minute post-open delay** (rule #5). Emit `execution_window: "09:30-10:00 WAIT; 10:00+ OK unless extreme RVOL"`.

## How to use from code

```python
# api/brief/setup_matcher.py (Stage 2b)
from skills.jeff_sun_method.scripts.scorer import score_setup, SetupScore

score: SetupScore = score_setup(
    ticker="NVDA",
    daily_bars=bars_200,      # ≥200 bars for 200-MA
    intraday_bars=today_5m,   # None if pre-open
    snapshot={
        "float": 2_400_000_000,
        "sector": "Technology",
        "short_float": 0.02,
        "industry_group": "Semiconductors",
        "earnings_date": date(2026, 5, 22),
        "is_ibb_xbi_member": False,
    },
    as_of=datetime.now(UTC),
)

if score.hard_gate_pass and score.score >= 70:
    # surface to LLM as a setup_match
    ...
else:
    # drop silently; log to validation_warnings
    ...
```

## Standalone CLI

```bash
# score a single ticker from a CSV of daily bars
python skills/jeff-sun-method/scripts/scorer.py \
    --ticker NVDA \
    --bars-csv sample/nvda_1y.csv \
    --snapshot-json sample/nvda_snapshot.json

# backtest the rubric over a CSV of past trades
python skills/jeff-sun-method/scripts/backtest_rubric.py \
    --trades-csv sample/jeff_public_examples.csv \
    --bars-dir sample/bars/
```

## Directory

- [`rules.yaml`](rules.yaml) — machine-readable rule catalog; source of truth for the scorer.
- [`playbooks/`](playbooks/) — setup archetypes: VCP breakout, pocket pivot, post-earnings drift, inverse-ETF short.
- [`scripts/`](scripts/) — standalone Python (scorer, indicators, backtest). Zero framework dependencies.
- [`references/`](references/) — glossary, daily workflow, 3-stop strategy, six conviction graphics, screeners.

## Future layers (reserved path)

- **Layer 2 — workflow orchestrator** (post-Stage 3): chain screening → watchlist → focus list → situational awareness → brief.
- **Layer 3 — conviction + journal mirror** (post-Stage 4): the six conviction graphics as programmatic views (drawdown simulator, R-multiple histogram, tighter-entry projection).

## Attribution rules

- Reference sources by URL in code comments and brief citations.
- Do not paste Jeff Sun's rule text verbatim into user-facing output; paraphrase or link.
- Every rule in [`rules.yaml`](rules.yaml) carries `source_quote` and `source_url` for traceability.

## Macro Overlay — Aschenbrenner "Situational Awareness" thesis

A "full macro overlay" layered on top of the Jeff Sun method. Affects theme prioritization,
position sizing on thesis-aligned names (up to 3x base size), and allows stop overrides on
Tier 1 conviction names when a catalyst is within 30 days. Sourced from Leopold Aschenbrenner's
"Situational Awareness: The Decade Ahead" (June 2024, https://situational-awareness.ai/).

Entry point: [`references/macroeconomic-thesis.md`](references/macroeconomic-thesis.md)

Companion files:
- [`references/aschenbrenner-watchlist.md`](references/aschenbrenner-watchlist.md) — Tier 1/2/3 tickers + ETFs
- [`references/thesis-catalysts.md`](references/thesis-catalysts.md) — Forward catalyst calendar
- [`references/sizing-overlay.md`](references/sizing-overlay.md) — Tier multipliers, stop override rules, kill switches
- [`references/reality-check.md`](references/reality-check.md) — Prediction-vs-event tracking (monthly refresh)

The overlay does NOT replace Jeff Sun gates. VCP/RS/RVOL/ADR%/ATR-from-50-MA hard gates still apply
for every entry. The overlay modifies which themes get Focus List priority, applies tier-based
sizing multipliers, and provides kill switches that force exit regardless of price action.

## Live data layer (cyber-corsairs integration)

When scoring or staging a ticker live from chat (vs. against pre-supplied
OHLCV), use the shared data layer at `skills/trading/scripts/data/`:

```python
from skills.trading.scripts.data.providers.composite import build_default_chain
from skills.trading.scripts.data.stage import classify
from skills.trading.scripts.data.rs import get_rs

chain = build_default_chain()
bars = chain.get_bars(symbol, limit=250)
rs = get_rs(symbol)
stage_result = classify(bars, rs_percentile=rs)
print(f"{symbol}: {stage_result.stage} / {stage_result.bucket} (RS {rs})")
# Then feed bars + snapshot into scorer.score_setup() for full scoring
```

CLI shortcut for stage only:
```bash
python skills/trading/scripts/data/stage.py SYMBOL
```

The data layer wraps yfinance (primary OHLCV), Finnhub (news/earnings/profile),
Alpha Vantage (fallback bars), and FRED (macro). See
[`references/stage-classification.md`](references/stage-classification.md)
for the 7-bucket rules.
