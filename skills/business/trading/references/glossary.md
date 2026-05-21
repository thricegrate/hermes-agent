# Glossary

Terms Jeff Sun uses across his Twitter, Substack, and chart templates. Source: https://jfsrev.substack.com/p/my-trading-tools-process-routine (Ch. 1).

| Term | Definition |
|------|------------|
| **LoD** | Low of intraday price action at the current moment. Used in the "LoD distance" rule — the gap between current low and proposed entry, measured in % ATR. |
| **RVOL** | Relative volume vs the 50-day average at the same time of day. Jeff's core buying-pressure proxy; ≥2× is an actionable threshold. |
| **T+0 / T+1 / T+3** | T is the execution day. T+1 is the first trading day after, T+3 is the third. Weekends and holidays excluded. Jeff's "T+3 framework" considers a position durable once it's survived 3 sessions. |
| **VARS** | Volatility-Adjusted Relative Strength — Jeff's custom RS indicator that normalizes performance by each stock's volatility. Published as a free TradingView script. |
| **VARW** | Volatility-Adjusted Relative **Weakness** — inverse of VARS for short / inverse-ETF setups. |
| **ORH** | Opening Range High — intraday high of the first N minutes (M5 / M15 / M30 variants). |
| **M30 Re-ORH** | Post-open 30 minutes reclaim of the intraday opening range high. A re-entry signal after an initial failed push. |
| **R** | R-multiple. R = initial risk on a trade (entry − stop). Every result expressed as multiples of R. "+16R" = gained 16 times the initial risk. |
| **R:R** | Risk-to-reward ratio — projected reward / initial R. |
| **ATR** | Average True Range (14-day default). Absolute dollar move magnitude. |
| **ADR** | Average Daily Range (20-day default), typically expressed as a percentage: `avg((H − L) / ((H + L) / 2))`. |
| **ATR vs ADR** | ATR is in dollar units; ADR% is dimensionless percentage. Jeff uses ADR% for sizing and ATR for stop placement. |
| **ATR% multiple from 50-MA** | `abs(close − 50MA) / ATR` — how many ATRs price sits from the 50-day moving average. Hard gate fires at >4×. |
| **VCP** | Volatility Contraction Pattern (Mark Minervini). Series of successively tighter pullbacks that compresses volatility before a breakout. |
| **PEAD** | Post-Earnings Announcement Drift. Documented market anomaly where prices drift in the direction of an earnings surprise for days/weeks. |
| **Pocket Pivot** | Single-bar volume signature: up-day with volume exceeding max down-day volume of prior 10 sessions. Gary Morsches / finallynitin. |
| **Stalk list** | Stocks building bases but not yet actionable. Promoted to Focus list when all entry conditions align. |
| **Focus list** | Today's actionable ideas. Sized by Jeff at 6–20 names; only 3 can be executed per session (rule #9). |
| **Stage 4 base** | Jeff's shorthand for late-stage distribution bases; these are higher-probability setups than early stage-2 re-accumulations because catalysts are required to break them higher. |
| **M5 / M15 / M30 ORB** | Opening-range breakout timeframe — Jeff will use M5 intra-day for tight entries and M30 for his standard re-entry after the 30-min delay. |
| **3-stop strategy** | Jeff's position-splitting approach that caps average loss at −0.67R instead of −1R by distributing exits across three levels. See [three-stop-strategy.md](three-stop-strategy.md). |
| **+EV** | Positive expected value; a strategy whose per-trade expectancy is positive over a large sample. |
| **Fresh 1-month RS high** | Industry group or ticker making a new high in 1-month relative-strength ranking — Jeff's breadth-confirmation signal. |

Not in Jeff's glossary but used throughout the scorer:
- **Soft signal** — a weighted score input (0–25 points each).
- **Hard gate** — a pass/fail rule that drops the ticker if violated.
- **Session gate** — a brief-wide rule (max 3 positions, 30-min delay).
