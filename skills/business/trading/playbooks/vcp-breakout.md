# Playbook — VCP Breakout

**Archetype.** Volatility Contraction Pattern (VCP), popularized by Mark Minervini and adopted by Jeff Sun as the default setup shape. The stock makes a price high, pulls back, tightens, pulls back less, tightens more, and eventually breaks out on volume. Every sustainable rally is preceded by contraction.

## What qualifies

- **Base:** 1 to 3 months old. Shorter bases = more immature setups; longer bases risk turning stage-4.
- **Contractions:** ≥2 measurable contractions, each shallower than the prior. Depth should decline (e.g., −25%, then −15%, then −8%).
- **Tightness:** the final contraction is the tightest — price range in the last 5–10 sessions narrows meaningfully (ATR compresses ≥30% vs 20-day avg).
- **Volume:** volume dries up during each contraction; a pocket-pivot candle (up-day volume > max down-day volume of last 10 sessions) appears late in the base.
- **Location:** price sits above 10-MA and 20-MA, and both MAs are above or catching up to the 50-MA.

## Entry trigger

Breakout above the pivot (top of the final contraction) with:
- LoD distance < 60% ATR (hard gate `lod_atr_60pct`).
- Price < 4× ATR from 50-MA (hard gate `atr_50ma_4x`).
- RVOL ≥ 2× 50-day average (soft signal `rvol_at_trigger` full weight).
- Pivot bar has a tight close (upper half of bar).

## Stop design (3-stop strategy)

See [`references/three-stop-strategy.md`](../references/three-stop-strategy.md). Total risk sized so **max average loss = −0.67R** instead of −1R.

- **Stop 1 (1/3 of position):** break of pivot low or M5/M15 opening-range low, whichever is tighter.
- **Stop 2 (1/3 of position):** break of prior-day low.
- **Stop 3 (1/3 of position):** close below 10-MA on closing basis.

If Stop 1 triggers but price reverses and reclaims M30 ORH (Re-ORH), do **not** re-add the stopped-out third — continue with the remaining 2/3 on Stop 2 and Stop 3 levels.

## Profit-taking

- **Partial 1:** take 1/3 off at the first X × ATR% from 50-MA extension, typically 2–3× multiple.
- **Partial 2:** take another 1/3 at 4–5× ATR% from 50-MA (Jeff's "favorite partial profit taking into strength" zone).
- **Runner:** remaining 1/3 trails by 10-MA daily close, or 20-MA weekly close for longer holds.

## What kills the setup

- Loose prior action (no measurable contraction phase) — hard gate `vcp_missing`.
- Pivot failure on volume — exit same day, do not wait for Stop 1.
- Against declining 200-MA — hard gate `declining_200ma`.
- Earnings within 5 trading days — hard gate `earnings_within_5d`.

## Historical examples Jeff has publicly annotated

- KC 2024 (+180% in 6 weeks from a cup-and-handle VCP, high RVOL breakout)
- COIN late Jan 2024 (+110% run after focus-listing from tight VCP)
- RGTI Sep 2025 (+40–80R via tight entry Qullamaggie-style)
- WULF early 2025 (+120% in 2 months as strongest WGMI-group leader)

Use these as scorer backtest targets: each should score ≥70 with no hard-gate fails on entry day.
