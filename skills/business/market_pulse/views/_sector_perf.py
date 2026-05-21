"""Sub-sector + thematic ETF performance pull for Daily Market Plan."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from skills.trading.scripts.data.providers.composite import build_default_chain
from skills.trading.scripts.data.themes import all_etfs


SP_SECTOR_ETFS = ["XLY", "XLK", "XLC", "XLRE", "XLI", "XLF", "XLB", "XLV", "XLU", "XLP", "XLE", "SPY"]
SP_EW_SECTOR_ETFS = ["RSPD", "RSPT", "RSPC", "RSPR", "RSPF", "RSPN", "RSPM", "RSPH", "RSPU", "RSPS", "RSPG", "RSP"]
GROWTH_VALUE_ETFS = ["IVW", "IJK", "IJT", "IVE", "IJJ", "IJS"]


def _pct(bars, lookback):
    if len(bars) <= lookback:
        return None
    start = bars[-1 - lookback]["c"]
    if start == 0:
        return None
    return (bars[-1]["c"] - start) / start * 100


def _pct_off_high(bars):
    if not bars:
        return None
    high = max(b["h"] for b in bars[-252:])
    if high == 0:
        return None
    return (bars[-1]["c"] - high) / high * 100


def _ytd(bars):
    if not bars:
        return None
    year = bars[-1]["t"][:4]
    first_of_year = next((b for b in bars if b["t"][:4] == year), bars[0])
    if first_of_year["c"] == 0:
        return None
    return (bars[-1]["c"] - first_of_year["c"]) / first_of_year["c"] * 100


def compute_sector_performance() -> dict[str, list[dict]]:
    chain = build_default_chain()
    all_symbols = list(set(SP_SECTOR_ETFS + SP_EW_SECTOR_ETFS + GROWTH_VALUE_ETFS + all_etfs()))
    raw = chain.get_multi_bars(all_symbols, timeframe="1Day", limit=260)

    def _row(sym):
        bars = raw.get(sym, [])
        return {
            "symbol": sym,
            "daily": _pct(bars, 1),
            "p5d": _pct(bars, 5),
            "off_52w_high": _pct_off_high(bars),
            "ytd": _ytd(bars),
        }

    return {
        "sub_sector": [_row(s) for s in SP_SECTOR_ETFS],
        "ew_sector": [_row(s) for s in SP_EW_SECTOR_ETFS],
        "growth_value": [_row(s) for s in GROWTH_VALUE_ETFS],
        "thematic": sorted(
            [_row(s) for s in all_etfs()],
            key=lambda r: -(r["p5d"] or -999),
        )[:10],
    }


if __name__ == "__main__":
    import json
    out = compute_sector_performance()
    for label in ["sub_sector", "thematic"]:
        print(f"=== {label} ===")
        for r in out[label]:
            print(f"  {r['symbol']:6s} daily={r['daily'] if r['daily'] is None else f'{r['daily']:+.2f}%'} "
                  f"p5d={r['p5d'] if r['p5d'] is None else f'{r['p5d']:+.2f}%'}")
