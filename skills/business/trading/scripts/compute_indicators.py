"""Indicator computation for the Jeff Sun setup scorer.

Zero framework dependencies: stdlib + dataclasses. Every function takes the same
`OHLCV` dataclass sequence and returns a scalar or a simple tuple. Kept separate
from scorer.py so indicators can be unit-tested in isolation.

Source of methodology: https://jfsrev.substack.com/p/my-trading-tools-process-routine
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Sequence


@dataclass(frozen=True)
class OHLCV:
    t: datetime
    o: float
    h: float
    l: float
    c: float
    v: int


def sma(bars: Sequence[OHLCV], n: int) -> float | None:
    """Simple moving average of closes over the last n bars."""
    if len(bars) < n or n <= 0:
        return None
    return sum(b.c for b in bars[-n:]) / n


def sma_slope(bars: Sequence[OHLCV], n: int, lookback: int = 10) -> float | None:
    """Slope of the n-bar SMA over the last `lookback` bars.

    Positive = rising. Negative = declining. Used for the declining-200-MA hard gate.
    """
    if len(bars) < n + lookback:
        return None
    recent = sma(bars, n)
    prior = sma(bars[:-lookback], n)
    if recent is None or prior is None:
        return None
    return recent - prior


def atr(bars: Sequence[OHLCV], n: int = 14) -> float | None:
    """Average True Range over the last n bars (Wilder's smoothing omitted; SMA of TR)."""
    if len(bars) < n + 1:
        return None
    trs: list[float] = []
    for i in range(1, len(bars)):
        prev_close = bars[i - 1].c
        b = bars[i]
        tr = max(b.h - b.l, abs(b.h - prev_close), abs(b.l - prev_close))
        trs.append(tr)
    return sum(trs[-n:]) / n


def adr_pct(bars: Sequence[OHLCV], n: int = 20) -> float | None:
    """Average Daily Range as a fraction: mean of (H - L) / ((H + L) / 2) over last n bars."""
    if len(bars) < n:
        return None
    ranges: list[float] = []
    for b in bars[-n:]:
        mid = (b.h + b.l) / 2
        if mid <= 0:
            return None
        ranges.append((b.h - b.l) / mid)
    return sum(ranges) / len(ranges)


def atr_mult_from_ma(price: float, ma: float, atr_val: float) -> float | None:
    """How many ATRs price is away from a moving average, as a positive scalar."""
    if atr_val is None or atr_val <= 0 or ma is None:
        return None
    return abs(price - ma) / atr_val


def rvol(
    today_volume: int,
    bars: Sequence[OHLCV],
    n: int = 50,
    exclude_today: bool = True,
) -> float | None:
    """Relative volume vs n-day average.

    By default excludes the most recent bar (treat it as "today" being measured).
    """
    reference = bars[:-1] if exclude_today else bars
    if len(reference) < n:
        return None
    avg = sum(b.v for b in reference[-n:]) / n
    if avg <= 0:
        return None
    return today_volume / avg


def lod_distance_pct_atr(
    proposed_entry: float,
    low_of_day: float,
    atr_val: float,
) -> float | None:
    """LoD distance as a fraction of daily ATR. Used for the 60% hard gate.

    Returns (entry - low_of_day) / atr. A value of 0.60 means entry sits 60% of ATR
    above the current low-of-day.
    """
    if atr_val is None or atr_val <= 0:
        return None
    return (proposed_entry - low_of_day) / atr_val


def detect_vcp(bars: Sequence[OHLCV], lookback: int = 60, min_contractions: int = 2) -> tuple[bool, int]:
    """Rough VCP detector.

    Scan the last `lookback` bars for swing highs + subsequent swing lows. Require
    at least `min_contractions` pullbacks, each shallower than the previous.

    Returns (qualifies, contraction_count). Simplified — the production matcher can
    use a more sophisticated swing-point algorithm.
    """
    if len(bars) < lookback:
        return False, 0

    window = bars[-lookback:]

    # Identify local swing highs/lows via 5-bar pivot rule.
    pivots: list[tuple[int, str, float]] = []  # (index, 'H'|'L', price)
    for i in range(2, len(window) - 2):
        b = window[i]
        if b.h > max(window[i - 2].h, window[i - 1].h, window[i + 1].h, window[i + 2].h):
            pivots.append((i, "H", b.h))
        if b.l < min(window[i - 2].l, window[i - 1].l, window[i + 1].l, window[i + 2].l):
            pivots.append((i, "L", b.l))

    # Compute pullback depths: each high→next low pair.
    depths: list[float] = []
    last_high: float | None = None
    for idx, kind, price in pivots:
        if kind == "H":
            last_high = price
        elif kind == "L" and last_high is not None:
            depth = (last_high - price) / last_high
            if depth > 0:
                depths.append(depth)
            last_high = None

    if len(depths) < min_contractions:
        return False, len(depths)

    # Require each contraction shallower than the previous.
    monotonic = all(depths[i] < depths[i - 1] for i in range(1, len(depths)))
    return monotonic and len(depths) >= min_contractions, len(depths)


def detect_pocket_pivot(bars: Sequence[OHLCV]) -> bool:
    """Pocket pivot: today green (close > open) AND volume > max of prior 10 down-day volumes."""
    if len(bars) < 11:
        return False
    today = bars[-1]
    if today.c <= today.o:
        return False
    prior_down_vols = [b.v for b in bars[-11:-1] if b.c < b.o]
    if not prior_down_vols:
        # No down days in prior 10 sessions — technically very strong, treat as pass.
        return True
    return today.v > max(prior_down_vols)


def detect_gap_resistance(
    proposed_entry: float,
    daily_bars: Sequence[OHLCV],
    atr_val: float,
    lookback: int = 60,
) -> bool:
    """True if an unfilled gap sits within 1x ATR above the proposed entry.

    Gap = bar's low > prior bar's high (or vice versa for down gaps).
    """
    if atr_val is None or atr_val <= 0 or len(daily_bars) < 2:
        return False
    ceiling = proposed_entry + atr_val
    recent = daily_bars[-lookback:] if len(daily_bars) >= lookback else daily_bars
    for i in range(1, len(recent)):
        prev, cur = recent[i - 1], recent[i]
        if cur.l > prev.h and proposed_entry < prev.h < ceiling:
            return True
        if cur.h < prev.l and proposed_entry < cur.h < ceiling:
            return True
    return False


def consecutive_up_days(bars: Sequence[OHLCV]) -> int:
    """Count of consecutive up-close bars ending at the last bar."""
    count = 0
    for b in reversed(bars):
        if b.c > b.o:
            count += 1
        else:
            break
    return count
