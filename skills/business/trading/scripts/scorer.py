"""Jeff Sun setup scorer — standalone, framework-free.

Takes OHLCV + snapshot, returns a SetupScore (hard_gate_pass, score 0-100,
rule_hits, reasons_dropped). The LLM sees only tickers where hard_gate_pass
and score >= 70.

Contract defined in /skills/jeff-sun-method/rules.yaml. Stage 2b's setup_matcher
imports `score_setup` and maps SetupScore -> Pydantic `setup_matches` entries.

CLI:
    python scorer.py --ticker NVDA --bars-csv bars.csv --snapshot-json snap.json

Source of methodology: https://jfsrev.substack.com/p/my-trading-tools-process-routine
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from typing import Literal

from compute_indicators import (
    OHLCV,
    adr_pct,
    atr,
    atr_mult_from_ma,
    consecutive_up_days,
    detect_gap_resistance,
    detect_pocket_pivot,
    detect_vcp,
    lod_distance_pct_atr,
    rvol,
    sma,
    sma_slope,
)

PASS_THRESHOLD = 70
SOFT_WEIGHT_SUM = 100


@dataclass(frozen=True)
class RuleHit:
    rule_id: str
    kind: Literal["hard_gate", "soft_signal", "session_gate"]
    passed: bool
    value: float | None
    threshold: float | None
    weight: int
    note: str = ""


@dataclass(frozen=True)
class SetupScore:
    ticker: str
    hard_gate_pass: bool
    score: int
    rule_hits: list[RuleHit] = field(default_factory=list)
    reasons_dropped: list[str] = field(default_factory=list)
    as_of: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


def _fraction_in_range(value: float, floor: float, ceiling: float) -> float:
    """Linear scale: floor -> 0.0, ceiling -> 1.0, clamped."""
    if ceiling == floor:
        return 1.0 if value >= ceiling else 0.0
    x = (value - floor) / (ceiling - floor)
    return max(0.0, min(1.0, x))


def score_setup(
    ticker: str,
    daily_bars: list[OHLCV],
    intraday_bars: list[OHLCV] | None,
    snapshot: dict,
    as_of: datetime,
) -> SetupScore:
    """Score a ticker against Jeff Sun's rule set.

    Required snapshot keys:
      - float (int)
      - sector (str)
      - short_float (float)
      - industry_group (str)
      - earnings_date (date | None)
      - is_ibb_xbi_member (bool)

    Optional snapshot keys for soft-signal scoring:
      - relative_strength_rank (float 0-1)  # e.g. 0.95 = 95th percentile
      - industry_group_rank (int)           # 1 = top group
      - market_consecutive_up_days (int)    # SPY
      - market_gap_up_open (bool)           # True if SPY gapping up
    """
    hits: list[RuleHit] = []
    reasons_dropped: list[str] = []

    # --- Indicators ---
    last_bar = daily_bars[-1] if daily_bars else None
    last_price = last_bar.c if last_bar else 0.0
    atr14 = atr(daily_bars, 14)
    adr20 = adr_pct(daily_bars, 20)
    ma50 = sma(daily_bars, 50)
    ma200 = sma(daily_bars, 200)
    ma200_slope = sma_slope(daily_bars, 200, lookback=10)

    vcp_pass, contractions = detect_vcp(daily_bars, lookback=60, min_contractions=2)
    pocket_pivot = detect_pocket_pivot(daily_bars)

    # Intraday-dependent indicators
    lod_dist = None
    rvol_today = None
    if intraday_bars:
        low_of_day = min(b.l for b in intraday_bars)
        today_vol = sum(b.v for b in intraday_bars)
        if atr14:
            lod_dist = lod_distance_pct_atr(last_price, low_of_day, atr14)
        rvol_today = rvol(today_vol, daily_bars, n=50, exclude_today=True)

    # --- HARD GATES ---

    # 1. LoD distance > 60% ATR
    passed = lod_dist is None or lod_dist <= 0.60
    hits.append(
        RuleHit(
            rule_id="lod_atr_60pct",
            kind="hard_gate",
            passed=passed,
            value=lod_dist,
            threshold=0.60,
            weight=0,
            note="pre-open; no intraday data" if lod_dist is None else "",
        )
    )
    if not passed:
        reasons_dropped.append(f"LoD distance {lod_dist:.2f} > 0.60 ATR")

    # 2. ATR% from 50-MA > 4x
    atr_mult = atr_mult_from_ma(last_price, ma50, atr14) if ma50 and atr14 else None
    passed = atr_mult is None or atr_mult <= 4.0
    hits.append(
        RuleHit(
            rule_id="atr_50ma_4x",
            kind="hard_gate",
            passed=passed,
            value=atr_mult,
            threshold=4.0,
            weight=0,
            note="insufficient bars" if atr_mult is None else "",
        )
    )
    if not passed:
        reasons_dropped.append(f"ATR mult from 50-MA {atr_mult:.2f} > 4.0")

    # 3. Biotech exclusion
    is_biotech = bool(snapshot.get("is_ibb_xbi_member", False))
    hits.append(
        RuleHit(
            rule_id="biotech_exclusion",
            kind="hard_gate",
            passed=not is_biotech,
            value=1.0 if is_biotech else 0.0,
            threshold=None,
            weight=0,
        )
    )
    if is_biotech:
        reasons_dropped.append("Biotech (IBB/XBI member) — take exposure via LABU/LABD")

    # 4. Declining 200-MA
    declining_200 = (
        ma200 is not None
        and ma200_slope is not None
        and ma200_slope < 0
        and last_price < ma200
    )
    hits.append(
        RuleHit(
            rule_id="declining_200ma",
            kind="hard_gate",
            passed=not declining_200,
            value=ma200_slope,
            threshold=0.0,
            weight=0,
        )
    )
    if declining_200:
        reasons_dropped.append("Against declining 200-MA")

    # 5. Gap resistance zone
    gap_res = atr14 is not None and detect_gap_resistance(last_price, daily_bars, atr14)
    hits.append(
        RuleHit(
            rule_id="gap_resistance_zone",
            kind="hard_gate",
            passed=not gap_res,
            value=1.0 if gap_res else 0.0,
            threshold=1.0,
            weight=0,
        )
    )
    if gap_res:
        reasons_dropped.append("Unfilled gap within 1x ATR above entry")

    # 6. VCP missing
    hits.append(
        RuleHit(
            rule_id="vcp_missing",
            kind="hard_gate",
            passed=vcp_pass,
            value=float(contractions),
            threshold=2.0,
            weight=0,
        )
    )
    if not vcp_pass:
        reasons_dropped.append(
            f"No VCP (only {contractions} contractions; need >=2 monotonically tighter)"
        )

    # 7. Earnings within 5 trading days
    earnings_date = snapshot.get("earnings_date")
    earnings_blocked = False
    if isinstance(earnings_date, (date, datetime)):
        earn = earnings_date.date() if isinstance(earnings_date, datetime) else earnings_date
        days_to_earnings = (earn - as_of.date()).days
        # Rough trading-days estimate: calendar/1.4 approximation, or 7 cal days ~ 5 trading days
        earnings_blocked = 0 <= days_to_earnings <= 7
    hits.append(
        RuleHit(
            rule_id="earnings_within_5d",
            kind="hard_gate",
            passed=not earnings_blocked,
            value=None,
            threshold=5.0,
            weight=0,
        )
    )
    if earnings_blocked:
        reasons_dropped.append("Earnings within next 5 trading days")

    hard_gate_pass = not reasons_dropped

    # --- SOFT SIGNALS ---
    # Note: we accumulate a raw points total; the actual final score is clamped at the end.

    points = 0.0

    # relative_strength (25 pts)
    rs_rank = snapshot.get("relative_strength_rank")
    if rs_rank is not None:
        pts = 25 * _fraction_in_range(rs_rank, 0.50, 0.95)
        points += pts
        hits.append(
            RuleHit(
                rule_id="relative_strength",
                kind="soft_signal",
                passed=pts >= 12.5,
                value=rs_rank,
                threshold=0.95,
                weight=25,
                note=f"+{pts:.1f}",
            )
        )
    else:
        hits.append(
            RuleHit(
                rule_id="relative_strength",
                kind="soft_signal",
                passed=False,
                value=None,
                threshold=0.95,
                weight=25,
                note="missing",
            )
        )

    # rvol_at_trigger (20 pts)
    if rvol_today is not None:
        pts = 20 * _fraction_in_range(rvol_today, 0.5, 2.0)
        points += pts
        hits.append(
            RuleHit(
                rule_id="rvol_at_trigger",
                kind="soft_signal",
                passed=pts >= 10,
                value=rvol_today,
                threshold=2.0,
                weight=20,
                note=f"+{pts:.1f}",
            )
        )
    else:
        hits.append(
            RuleHit(
                rule_id="rvol_at_trigger",
                kind="soft_signal",
                passed=False,
                value=None,
                threshold=2.0,
                weight=20,
                note="no intraday data",
            )
        )

    # vcp_quality (15 pts) — reward contraction count beyond the minimum
    if vcp_pass:
        pts = 15 * _fraction_in_range(float(contractions), 2.0, 4.0)
        points += pts
        hits.append(
            RuleHit(
                rule_id="vcp_quality",
                kind="soft_signal",
                passed=pts >= 7.5,
                value=float(contractions),
                threshold=4.0,
                weight=15,
                note=f"+{pts:.1f}",
            )
        )
    else:
        hits.append(
            RuleHit(
                rule_id="vcp_quality",
                kind="soft_signal",
                passed=False,
                value=float(contractions),
                threshold=4.0,
                weight=15,
                note="VCP hard gate failed",
            )
        )

    # industry_group_rs (15 pts)
    ig_rank = snapshot.get("industry_group_rank")
    if isinstance(ig_rank, int) and ig_rank >= 1:
        pts = 15 if ig_rank <= 5 else max(0.0, 15 - (ig_rank - 5) * 1.5)
        points += pts
        hits.append(
            RuleHit(
                rule_id="industry_group_rs",
                kind="soft_signal",
                passed=pts >= 10,
                value=float(ig_rank),
                threshold=5.0,
                weight=15,
                note=f"+{pts:.1f}",
            )
        )
    else:
        hits.append(
            RuleHit(
                rule_id="industry_group_rs",
                kind="soft_signal",
                passed=False,
                value=None,
                threshold=5.0,
                weight=15,
                note="missing",
            )
        )

    # base_and_pocket_pivot (10 pts)
    # Composite: passing VCP + pocket pivot in last 10 bars = full pts
    base_pts = (5 if vcp_pass else 0) + (5 if pocket_pivot else 0)
    points += base_pts
    hits.append(
        RuleHit(
            rule_id="base_and_pocket_pivot",
            kind="soft_signal",
            passed=base_pts >= 5,
            value=float(base_pts),
            threshold=10.0,
            weight=10,
            note=f"+{base_pts}",
        )
    )

    # adr_fit (10 pts)
    if adr20 is not None:
        pts = 10 * _fraction_in_range(adr20, 0.03, 0.05)
        points += pts
        hits.append(
            RuleHit(
                rule_id="adr_fit",
                kind="soft_signal",
                passed=pts >= 5,
                value=adr20,
                threshold=0.05,
                weight=10,
                note=f"+{pts:.1f}",
            )
        )
    else:
        hits.append(
            RuleHit(
                rule_id="adr_fit",
                kind="soft_signal",
                passed=False,
                value=None,
                threshold=0.05,
                weight=10,
                note="insufficient bars",
            )
        )

    # positional_penalty (-5 pts)
    penalty = 0
    mkt_up_days = snapshot.get("market_consecutive_up_days", 0)
    mkt_gap_up = snapshot.get("market_gap_up_open", False)
    if isinstance(mkt_up_days, int) and mkt_up_days >= 3:
        penalty += min(3, mkt_up_days - 2)
    if mkt_gap_up:
        penalty += 2
    penalty = min(5, penalty)
    points -= penalty
    hits.append(
        RuleHit(
            rule_id="positional_penalty",
            kind="soft_signal",
            passed=penalty == 0,
            value=float(penalty),
            threshold=0.0,
            weight=-5,
            note=f"-{penalty}",
        )
    )

    # --- Clamp + return ---
    score = int(max(0, min(100, round(points))))

    return SetupScore(
        ticker=ticker,
        hard_gate_pass=hard_gate_pass,
        score=score,
        rule_hits=hits,
        reasons_dropped=reasons_dropped,
        as_of=as_of,
    )


# ----- CLI -----


def _load_bars_csv(path: str) -> list[OHLCV]:
    bars: list[OHLCV] = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            bars.append(
                OHLCV(
                    t=datetime.fromisoformat(row["t"]),
                    o=float(row["o"]),
                    h=float(row["h"]),
                    l=float(row["l"]),
                    c=float(row["c"]),
                    v=int(row["v"]),
                )
            )
    bars.sort(key=lambda b: b.t)
    return bars


def _serialize(score: SetupScore) -> dict:
    d = asdict(score)
    d["as_of"] = score.as_of.isoformat()
    return d


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Score a ticker against Jeff Sun's rule set.")
    p.add_argument("--ticker", required=True)
    p.add_argument("--bars-csv", required=True, help="CSV with columns: t,o,h,l,c,v")
    p.add_argument("--intraday-csv", help="Optional intraday CSV (same columns)")
    p.add_argument("--snapshot-json", help="JSON file with snapshot dict")
    args = p.parse_args(argv)

    daily = _load_bars_csv(args.bars_csv)
    intraday = _load_bars_csv(args.intraday_csv) if args.intraday_csv else None
    snapshot = json.load(open(args.snapshot_json)) if args.snapshot_json else {}

    # Parse earnings_date if present
    if "earnings_date" in snapshot and isinstance(snapshot["earnings_date"], str):
        snapshot["earnings_date"] = date.fromisoformat(snapshot["earnings_date"])

    result = score_setup(
        ticker=args.ticker,
        daily_bars=daily,
        intraday_bars=intraday,
        snapshot=snapshot,
        as_of=datetime.now(timezone.utc),
    )

    print(json.dumps(_serialize(result), indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
