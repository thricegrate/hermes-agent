# Playbook — Inverse ETF "Short" (long-only execution of bearish views)

**Archetype.** Jeff's hard rule #14: "I will always 'long' ideas, even my short ideas on weakness are based on available inverse long synthetic ETFs." Instead of shorting a weak underlying, go long its inverse or leveraged inverse ETF. Preserves the long-side toolkit (breakouts, VCPs, pocket pivots) and avoids short-specific risks (unlimited loss, hard-to-borrow fees, short-squeeze forced covers).

## Mapping — underlying → inverse ETF

| Bearish thesis on | Go long | Notes |
|-------------------|---------|-------|
| IBB / XBI (biotech) | LABD (−3×) | Replaces biotech exclusion on the long side |
| SPY / ES | SPXS / SPXU (−3×) | Use SPXL for bullish leveraged exposure |
| QQQ | SQQQ (−3×) | Use TQQQ for bullish |
| IWM (Russell 2000) | TZA (−3×) | Small-cap weakness |
| XLE (energy) | ERY (−2×) | Energy weakness |
| Semiconductor basket | SOXS (−3×) | Semi weakness |
| AMZN | AMZD (−1× synthetic) | Single-name inverse where available |
| GDX (gold miners) | DUST (−2×) | Miner weakness |

For **leveraged ETFs that track 24h underlyings** (GLD, SPXL, IBIT, SOLT, BOIL, FXI, UCO): Jeff flags these as having distinctive intraday gaps relative to their underlying — measure RVOL and LoD distance on the **ETF's own chart**, not the underlying's chart.

## What qualifies

Same setup archetype as a long breakout on the inverse ETF's chart:
- VCP, pocket pivot, or PEAD-like setup **on the inverse ETF itself**.
- All long-side hard gates apply (LoD < 60% ATR, ATR < 4× from 50-MA, etc.) — evaluated on the inverse ETF's bars.
- Underlying should confirm the bearish thesis (underlying forming a topping structure, breadth deteriorating, key MA breaks on the underlying).

## Entry trigger

Breakout on the inverse ETF with:
- RVOL ≥ 2× on the inverse ETF (not the underlying).
- LoD < 60% ATR on the inverse ETF.
- Underlying confirms (declining 200-MA on the underlying → bonus context, not a hard rule here).
- Not a Friday close for crypto-underlying inverse ETFs (weekend gap risk from 24h underlying).

## Stop design

Standard 3-stop strategy on the inverse ETF's bars. Stops get **tighter** than on underlyings because leveraged ETFs have decay and wider slippage:
- **Stop 1 (1/3):** breakout bar low.
- **Stop 2 (1/3):** 10-MA close on inverse ETF.
- **Stop 3 (1/3):** 20-MA close on inverse ETF.

## Profit-taking

Leveraged inverse ETFs decay — do not hold as long as long-side equities. Bias toward faster partials:
- **Partial 1:** 1.5× ATR% from 50-MA.
- **Partial 2:** 2.5–3× ATR% from 50-MA.
- **Runner:** 10-MA daily close on the ETF; full exit if underlying reclaims a declining 200-MA or breadth improves materially.

## What kills the setup

- Underlying reclaims a key MA with strength (breadth improving, VARS turning positive).
- Inverse ETF gaps into major resistance zone.
- Crypto-underlying inverse held into weekend (avoid per rule — exit Friday).

## Scorer notes

The scorer treats the inverse ETF as the ticker for all rule evaluation — hard gates and soft signals use the ETF's OHLCV, float (N/A for ETFs — skip), and ADR% (typically high on −3× ETFs, which boosts `adr_fit`). `biotech_exclusion` does **not** apply to LABD even though it tracks biotech — the rule excludes IBB/XBI components, not their inverses.

## Jeff's caveat on crypto-ETFs

> "Another caveat on executing US listed crypto ETFs on Friday session"

Weekend gap risk from 24h BTC/ETH/SOL can open Monday far from Friday's close. Scorer does not encode this directly; flag it in the brief narrative when a setup involves BITO / IBIT / ETHD / SOLT near EOW.
