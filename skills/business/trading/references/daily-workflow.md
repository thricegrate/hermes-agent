# Daily workflow

Jeff's full day-in-the-life. Sources:
- 2025 Substack Ch. 3–5, 7 — https://jfsrev.substack.com/p/my-trading-tools-process-routine
- 2023 summary — https://qullamaggie.net/jeff-suns-method-and-flow/

The flow: **Screening → Watchlist Management → Focus List → Pre-Market Situational Awareness → Execution → Post-Execution Management → Journal**. Terminal Stage 2b implements the middle three; Stage 3 implements the journal; Stages 5–6 expand screening and situational awareness.

## Post-market (after US close)

1. **Run screeners.** 14 Finviz + TradingView scans. The top 5 by priority:
   - 1-week mover >20% (target <60 results)
   - 1-month mover >30% (fallback to >50% when saturated)
   - 3-month mover >50%
   - 6-month mover >100%
   - CANSLIM-calibrated scan (high RS + high ADR% + liquidity)
2. **Watchlist management.** Move new screener results to the Global Watchlist (~142 stocks at Jeff's scale). Remove names whose setup is broken. Segment into 3 rotating sub-watchlists if the full set is unmanageable.
3. **Focus list promotion.** Upgrade watchlist names to today's Focus List when they show:
   - Strong catalytic move with high volume (breakout confirmation).
   - High ADR% (momentum in place).
   - Strong relative strength (VARS or IBD RS rank).
   - Volume dry-up during contraction.
   - Price above 10-MA and 20-MA.
4. **Stalk list disqualification checks** (2023 summary):
   - Earnings within 5 days → exclude.
   - 10-MA / 20-MA hasn't caught up to price → wait.
   - Running into declining 200-MA → exclude (unless 3× ADR% away).
   - Below 10-MA / 20-MA → wait.

## Pre-market (before open)

1. **Price alerts** on TradingView — one alert per Focus List name at the pivot level.
2. **Situational awareness**:
   - Breadth panel: $MMTW (% above 20-MA), NH/NL (52-week new highs minus new lows).
   - Top-down: RSP/SPY ratio (equal-weight vs cap-weight), sector RS, industry group RS.
   - Economic calendar: no entry before pre-market economic data or earnings (rule #6).
   - Index ATR% extension: check if SPY/QQQ is itself >4× ATR from 50-MA — if so, cut new-position appetite.
   - Macro overlay check: review [macroeconomic-thesis.md](macroeconomic-thesis.md) TL;DR; scan [thesis-catalysts.md](thesis-catalysts.md) for catalysts within 7 days; verify no kill switch tripped per [sizing-overlay.md](sizing-overlay.md). If any Tier 1 catalyst within 30 days, hold conviction names through Jeff Sun exit signals per Tier 1 stop override rules.
3. **Pre-market Gapper scan** on TradingView: surface high-RVOL gap-ups outside the Focus List.
4. **Fitness** (Jeff's explicit recommendation): exercise before open for mental clarity.

## Market hours

1. **First 30 minutes: wait** (rule #5). Exceptions: extreme pre-market RVOL on a Focus List name, or an M30 Re-ORH reclaim.
2. **30-min +**: enter Focus List names that trigger their pivot, respecting hard gates.
3. **Max 3 new positions per session** (rule #9). Roll risk into existing winners beyond T+3 before opening a 4th.
4. **No entry into pre/post-market economic data or earnings** (rule #6).

## Post-execution management

See [three-stop-strategy.md](three-stop-strategy.md) for stop and profit-taking mechanics. Key behaviors:
- "Sell some into strength, or death by a thousand cuts." But also "don't sell too aggressively into strength."
- Never lose two weeks' gains in a day.
- When to add: only after position is ≥1R above breakeven stop and still leading.

## Post-close routine

1. **Journal every trade** — win and loss. See [six-conviction-graphics.md](six-conviction-graphics.md) for what to track.
2. **Annotate the index chart** with every entry/exit — tests situational awareness over time.
3. **Update the Focus List for tomorrow** — this is the start of the next day's cycle.

## Terminal Stage mapping

| Stage | Implements |
|-------|------------|
| 2a | Watchlist CRUD + provider schema |
| 2b | Focus List scorer (THIS skill) — hard gates, soft signals, session gates |
| 2c | Richer brief using focus list (movers, earnings, calendars, filings) |
| 2d | Gmail + newsletter ingestion feeds into watchlist |
| 3 | Journal — R-multiple, win rate, holding period, drawdown, six conviction graphics |
| 5 | Weekly prep — situational-awareness top-down, breadth panel |
| 6 | Scanners — the 14-screener Finviz/TradingView workflow wired to the watchlist |
