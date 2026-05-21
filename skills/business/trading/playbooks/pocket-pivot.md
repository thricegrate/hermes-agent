# Playbook — Pocket Pivot

**Archetype.** A single-bar volume signature inside a base: an up-day whose volume exceeds the maximum down-day volume of the prior 10 sessions. Signals institutional accumulation before the breakout pivot is reached. Jeff uses the `finallynitin` Pine script to flag these on charts.

## What qualifies

- **Location:** within a constructive base (not in a downtrend, not after a parabolic run).
- **Bar type:** green close (close > open).
- **Volume rule:** today's volume > max of the down-day volumes in the prior 10 sessions.
- **Supporting context:**
  - Price holds above 10-MA and 20-MA.
  - 50-MA is flat or rising.
  - Base has had ≥1 contraction already (does not need to be fully formed).

## Entry trigger

Take a starter position (typically 1/3 of intended full size) at or near the pocket-pivot close, with:
- LoD < 60% ATR from the pocket-pivot low (hard gate `lod_atr_60pct`).
- Price < 4× ATR from 50-MA (hard gate `atr_50ma_4x`).
- Biotech excluded (hard gate `biotech_exclusion`).

Pocket pivots let you build position **before** the official VCP breakout pivot — if the thesis plays out, the official breakout is an add, not the entry.

## Stop design

- **Stop 1 (1/3 of position):** low of the pocket-pivot bar.
- **Stop 2 (1/3 of position):** 10-MA on closing basis.
- **Stop 3 (1/3 of position):** 20-MA on closing basis.

Looser than a VCP breakout because the entry is earlier in the base. Combined with smaller size, total R risk matches a full-size VCP entry.

## Add rules

- If price forms a subsequent VCP breakout above the base pivot → add remaining 2/3 size at the breakout.
- If price has an additional pocket pivot with tighter price action → add 1/3 at that new pivot.
- Do not add against existing position unless price has moved ≥1R above breakeven stop.

## Profit-taking

Same as VCP breakout (see [`vcp-breakout.md`](vcp-breakout.md#profit-taking)): partials at 2–3× and 4–5× ATR% from 50-MA, runner trails by 10-MA daily close.

## What kills the setup

- Pocket pivot fails to hold — close below 10-MA within 3 sessions exits the starter.
- Gap-resistance zone within 1× ATR above entry — hard gate `gap_resistance_zone`.
- Loose base (no contraction yet) — hard gate `vcp_missing`.

## Scorer mapping

This playbook is scored primarily through `base_and_pocket_pivot` (10 weight) + `rvol_at_trigger` (20 weight) + `relative_strength` (25 weight). A clean pocket-pivot entry in a leading industry group typically scores 75–90.
