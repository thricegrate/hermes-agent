"""Daily market trend signals — the binary YES/NO checklist on top of every DMP."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from skills.trading.scripts.data.providers.composite import build_default_chain


def _sma(values: list[float], period: int) -> float | None:
    if len(values) < period:
        return None
    return sum(values[-period:]) / period


def _rising(values: list[float], period: int) -> bool:
    """True if value at end > value `period` days ago."""
    if len(values) <= period:
        return False
    return values[-1] > values[-1 - period]


def _regime(daily: bool, weekly: bool, above: bool) -> str:
    if daily and weekly and above:
        return "UPTREND"
    if not daily and not weekly:
        return "DOWNTREND"
    return "NEUTRAL"


def compute_signals(symbol: str = "SPY") -> dict:
    chain = build_default_chain()
    bars = chain.get_bars(symbol, timeframe="1Day", limit=60)
    closes = [b["c"] for b in bars]
    if len(closes) < 20:
        return {"error": "insufficient bars"}

    sma10 = _sma(closes, 10) or 0
    sma20 = _sma(closes, 20) or 0
    daily_buy = closes[-1] > sma10 and closes[-1] > sma20 and sma10 > sma20

    # Weekly: take Friday closes (every 5th bar from end)
    weekly = closes[-50::5]
    wma10 = _sma(weekly, 10) or 0
    wma20 = _sma(weekly, 20) or 0
    weekly_buy = (
        weekly[-1] > wma10 and weekly[-1] > wma20 and wma10 > wma20
    ) if len(weekly) >= 20 else False

    sma5 = _sma(closes, 5) or 0
    sma5_rising = _rising(closes[-7:], 5)
    above_rising_5dma = closes[-1] > sma5 and sma5_rising

    return {
        "daily_buy_signal": daily_buy,
        "weekly_buy_signal": weekly_buy,
        "above_rising_5dma": above_rising_5dma,
        "regime": _regime(daily_buy, weekly_buy, above_rising_5dma),
        "spy_close": closes[-1],
        "sma10": sma10,
        "sma20": sma20,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(compute_signals(), indent=2))
