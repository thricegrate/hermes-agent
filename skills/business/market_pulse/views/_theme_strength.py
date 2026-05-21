"""Theme strength computation. Used by theme_flow_map view."""
from __future__ import annotations

import sys
from pathlib import Path
from statistics import mean, stdev

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from skills.trading.scripts.data.providers.composite import build_default_chain
from skills.trading.scripts.data.themes import THEMES, all_etfs


TIMEFRAMES = ["1d", "5d", "10d", "1mo"]
LOOKBACKS = {"1d": 1, "5d": 5, "10d": 10, "1mo": 21}


def _pct_change(bars: list[dict], lookback: int) -> float | None:
    if len(bars) <= lookback:
        return None
    start = bars[-1 - lookback]["c"]
    if start == 0:
        return None
    return (bars[-1]["c"] - start) / start * 100


def compute_theme_strengths() -> dict[str, dict]:
    chain = build_default_chain()
    etfs = list(set(all_etfs() + ["SPY"]))
    bars_map = chain.get_multi_bars(etfs, timeframe="1Day", limit=30)
    spy_bars = bars_map.get("SPY", [])

    spy_returns = {tf: _pct_change(spy_bars, LOOKBACKS[tf]) for tf in TIMEFRAMES}

    themes_data: dict[str, dict] = {}
    for theme_name, t in THEMES.items():
        etf = t["etf"]
        if not etf:
            continue
        bars = bars_map.get(etf, [])
        if not bars:
            continue
        rets = {tf: _pct_change(bars, LOOKBACKS[tf]) for tf in TIMEFRAMES}
        excess = {
            tf: (rets[tf] - spy_returns[tf])
            if (rets[tf] is not None and spy_returns[tf] is not None)
            else None
            for tf in TIMEFRAMES
        }
        themes_data[theme_name] = {
            "etf": etf,
            "returns": rets,
            "excess_vs_spy": excess,
        }

    # Z-score across themes per timeframe
    for tf in TIMEFRAMES:
        vals = [t["excess_vs_spy"][tf] for t in themes_data.values() if t["excess_vs_spy"][tf] is not None]
        if len(vals) < 2:
            continue
        mu = mean(vals)
        sd = stdev(vals) or 1.0
        for t in themes_data.values():
            v = t["excess_vs_spy"].get(tf)
            t.setdefault("z", {})[tf] = (v - mu) / sd if v is not None else None

    # Strength = mean of z-scores across all timeframes; map to 0-100 percentile
    for t in themes_data.values():
        zs = [v for v in t.get("z", {}).values() if v is not None]
        t["strength"] = sum(zs) / len(zs) if zs else 0.0
        t["strength_pct"] = max(0, min(100, int((t["strength"] + 3) / 6 * 100)))

    return themes_data


if __name__ == "__main__":
    data = compute_theme_strengths()
    ranked = sorted(data.items(), key=lambda kv: -kv[1]["strength"])
    print(f"{'Theme':<35} {'ETF':<6} {'Strength':<10} {'1d':<8} {'5d':<8} {'10d':<8} {'1mo':<8}")
    for name, t in ranked[:15]:
        rets = t["returns"]
        def f(v):
            return f"{v:+.2f}%" if v is not None else "  -  "
        print(f"{name[:34]:<35} {t['etf']:<6} {t['strength']:+.2f} ({t['strength_pct']:3d}) {f(rets['1d']):<8} {f(rets['5d']):<8} {f(rets['10d']):<8} {f(rets['1mo']):<8}")
