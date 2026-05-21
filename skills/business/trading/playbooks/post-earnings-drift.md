# Playbook — Post-Earnings Announcement Drift (PEAD)

**Archetype.** After a strong earnings surprise, stocks drift in the direction of the surprise for days to weeks. Jeff does **not** trade into earnings (hard gate `earnings_within_5d` blocks that), but the drift afterward is a high-quality setup.

## What qualifies

- **Earnings date:** in the past. Report released ≥1 full session ago.
- **Reaction:** day-1 post-earnings close >+5% on RVOL ≥3× average, closing in the upper half of the day's range.
- **6 post-earnings outcomes to check** (Jeff's framing — evaluate at EOD of the report day):
  1. Gap up, close up (strongest)
  2. Gap up, close flat/down (failed drift setup — skip)
  3. Gap flat, close up (acceptable, weaker drift)
  4. Gap down, close up (reversal — strongest short-squeeze candidate)
  5. Gap flat, close down (skip)
  6. Gap down, close down (skip, wait for stabilization)
- **Setup shape:** outcomes 1, 3, and 4 that then form a 3–10 session micro-consolidation above the pre-earnings level.

## Entry trigger

Breakout of the micro-consolidation high with:
- LoD < 60% ATR (hard gate `lod_atr_60pct`).
- Price < 4× ATR from 50-MA (hard gate `atr_50ma_4x`) — PEAD setups often get extended fast, so this gate kills late chases.
- Next earnings date ≥5 trading days out (hard gate `earnings_within_5d` still applies).
- RVOL ≥ 2× 50-day avg on breakout (soft signal `rvol_at_trigger`).

## Stop design

Same 3-stop strategy as VCP, but with tighter stops because the consolidation is shorter:
- **Stop 1 (1/3):** consolidation low.
- **Stop 2 (1/3):** pre-earnings level (the gap up level that defined the drift).
- **Stop 3 (1/3):** 10-MA close or 50% retrace of the earnings gap, whichever is tighter.

If the earnings gap fills entirely, the thesis is broken — exit all remaining size, do not wait for Stop 3.

## Profit-taking

PEAD drifts typically exhaust faster than VCP breakouts. Bias toward earlier partials:
- **Partial 1:** 2× ATR% from 50-MA.
- **Partial 2:** 3–4× ATR% from 50-MA.
- **Runner:** trail 10-MA close; exit fully before next earnings date.

## What kills the setup

- Fills the earnings gap.
- Next earnings lands within 5 trading days of signal — hard gate.
- Industry group RS turns negative — soft signal `industry_group_rs` drops toward 0, lowering score below 70 gate.

## Scorer notes

PEAD setups rely heavily on `rvol_at_trigger` (20), `relative_strength` (25), and `industry_group_rs` (15) to reach the 70 threshold. ADR% is often elevated post-earnings (bonus on `adr_fit`), but the `positional_penalty` applies if the broader market is also in a consecutive-up-days streak.

## Historical examples

Jeff's public annotations on PEAD include breakouts after earnings in WGMI-group names (WULF) and KC's +180% run began with an earnings-driven volume expansion phase.
