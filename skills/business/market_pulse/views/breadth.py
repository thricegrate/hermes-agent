"""Breadth indicator view. Renders a markdown table of internals over the last N days."""
from __future__ import annotations

import sys
from pathlib import Path

# Ensure project root on sys.path so absolute imports work when run as script
_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from skills.trading.scripts.data.providers.composite import build_default_chain
from skills.trading.scripts.data.universe import load_universe
from skills.trading.scripts.data.cache import Cache
from skills.market_pulse.formatters import markdown as md
from skills.market_pulse.formatters.bars import hbar


CACHE_KEY = "breadth:rolling:30d"
CACHE_TTL = 6 * 3600  # 6 hours


def _ret(bars: list[dict], idx: int, lookback: int) -> float | None:
    """Total return at bars[idx] vs bars[idx - lookback]."""
    target_idx = idx - lookback
    if target_idx < -len(bars):
        return None
    if abs(target_idx) > len(bars):
        return None
    try:
        cur = bars[idx]["c"]
        prev = bars[target_idx]["c"]
    except (IndexError, KeyError):
        return None
    if prev == 0:
        return None
    return (cur - prev) / prev


def _atr(bars: list[dict], period: int = 14) -> float | None:
    """Average True Range over `period` bars ending at last bar."""
    if len(bars) < period + 1:
        return None
    trs = []
    for i in range(-period, 0):
        h = bars[i]["h"]
        l = bars[i]["l"]
        prev_c = bars[i - 1]["c"] if i - 1 >= -len(bars) else bars[i]["c"]
        tr = max(h - l, abs(h - prev_c), abs(l - prev_c))
        trs.append(tr)
    return sum(trs) / period


def compute_breadth(days: int = 30, refresh: bool = False, universe_cap: int = 1500) -> list[dict]:
    """Returns list of breadth snapshots, most recent first."""
    cache = Cache()
    if not refresh:
        cached = cache.get(CACHE_KEY)
        if cached and len(cached) >= days:
            return cached[:days]

    chain = build_default_chain()
    universe = load_universe()
    symbols = [u["symbol"] for u in universe][:universe_cap]

    # Need enough history for quarter return (63d) + buffer
    raw = chain.get_multi_bars(symbols, timeframe="1Day", limit=90)

    out: list[dict] = []
    for offset in range(days):
        idx = -1 - offset
        up_4 = down_4 = 0
        up_25_q = up_25_m = up_50_m = up_13_34 = 0
        ext_10x_atr = 0
        above_50ma = total = 0
        date_for_row = ""

        for sym, bars in raw.items():
            if len(bars) <= abs(idx) + 1:
                continue
            if not date_for_row:
                date_for_row = bars[idx]["t"][:10]
            cur_close = bars[idx]["c"]
            prev_close = bars[idx - 1]["c"]
            if prev_close > 0:
                chg = (cur_close - prev_close) / prev_close
                if chg >= 0.04:
                    up_4 += 1
                if chg <= -0.04:
                    down_4 += 1

            # Multi-period returns
            r_q = _ret(bars, idx, 63)
            r_m = _ret(bars, idx, 21)
            r_34 = _ret(bars, idx, 34)
            if r_q is not None and r_q >= 0.25:
                up_25_q += 1
            if r_m is not None:
                if r_m >= 0.25:
                    up_25_m += 1
                if r_m >= 0.50:
                    up_50_m += 1
            if r_34 is not None and r_34 >= 0.13:
                up_13_34 += 1

            # 50-MA + 10x ATR
            if len(bars) >= 50 + abs(idx):
                window = bars[idx - 49: idx + 1] if idx + 1 != 0 else bars[idx - 49:]
                if len(window) >= 50:
                    sma50 = sum(b["c"] for b in window) / 50
                    if cur_close > sma50:
                        above_50ma += 1
                    atr14 = _atr(window[-15:], 14)
                    if atr14 and cur_close > sma50 + 10 * atr14:
                        ext_10x_atr += 1
            total += 1

        out.append({
            "date": date_for_row,
            "up_4": up_4,
            "down_4": down_4,
            "up_25_q": up_25_q,
            "up_25_m": up_25_m,
            "up_50_m": up_50_m,
            "up_13_34": up_13_34,
            "ext_10x_atr": ext_10x_atr,
            "pct_above_50ma": (above_50ma / total * 100) if total else 0,
            "universe_size": total,
        })

    out.sort(key=lambda x: x["date"], reverse=True)
    cache.set(CACHE_KEY, out, ttl=CACHE_TTL)
    return out[:days]


def _regime(rows: list[dict]) -> tuple[str, float]:
    if len(rows) < 5:
        return "🟡 NEUTRAL (insufficient history)", 0.0
    today = rows[0]
    five_day_ratio = sum(r["up_4"] for r in rows[:5]) / max(sum(r["down_4"] for r in rows[:5]), 1)
    if five_day_ratio > 1.5 and today["pct_above_50ma"] > 50 and today["up_25_q"] > 300:
        return "🟢 UPTREND", five_day_ratio
    if five_day_ratio < 0.6 and today["pct_above_50ma"] < 30:
        return "🔴 DOWNTREND", five_day_ratio
    return "🟡 NEUTRAL", five_day_ratio


def render(days: int = 30, refresh: bool = False) -> str:
    rows = compute_breadth(days=days, refresh=refresh)
    if not rows:
        return "_No breadth data available._"

    regime_label, five_day_ratio = _regime(rows)
    today = rows[0]

    out: list[str] = []
    out.append(md.section(f"Breadth — last {len(rows)} days"))
    out.append(md.kv([
        ("Regime", regime_label),
        ("5-day Ratio", f"{five_day_ratio:.2f}"),
        ("Today >50DMA%", f"{today['pct_above_50ma']:.1f}%"),
        ("Universe size", f"{today['universe_size']}"),
    ]))
    out.append("\n")

    headers = ["Date", "Up4%", "Down4%", "Up25%Q", "Up25%M", "Up50%M", "Up13%34", "ATR10x", ">50DMA%", "Univ"]
    table_rows = []
    for r in rows:
        bar = hbar(r["pct_above_50ma"], 100, width=8)
        table_rows.append([
            r["date"],
            r["up_4"], r["down_4"],
            r["up_25_q"], r["up_25_m"], r["up_50_m"], r["up_13_34"],
            r["ext_10x_atr"],
            f"{r['pct_above_50ma']:.1f}% {bar}",
            r["universe_size"],
        ])
    out.append(md.table(headers, table_rows))
    return "".join(out)


def render_html(days: int = 30, refresh: bool = False) -> str:
    """Render breadth as an interactive HTML report. Returns the file path."""
    from skills.market_pulse.formatters.html_report import write_report, kv_to_html, md_table_to_html
    from skills.market_pulse.formatters.charts import heatmap, hbar_chart, area_chart

    rows = compute_breadth(days=days, refresh=refresh)
    if not rows:
        return ""

    regime_label, five_day_ratio = _regime(rows)
    today = rows[0]

    # Heatmap of >50DMA% over time (one row, 30 days of dates as columns)
    rev_rows = list(reversed(rows))
    fig_hm = heatmap(
        [[r["pct_above_50ma"] for r in rev_rows]],
        rows=[">50DMA%"],
        cols=[r["date"] for r in rev_rows],
        title=">50DMA% over time",
        zmid=50,
    )

    # Bar of up vs down 4% on most recent date
    fig_bar = hbar_chart(
        ["Up 4%", "Down 4%"],
        [today["up_4"], -today["down_4"]],
        title=f"Today's 4% movers ({today['date']})",
    )

    # Area chart of advancing-declining differential
    diff = [r["up_4"] - r["down_4"] for r in rev_rows]
    fig_diff = area_chart(
        [r["date"] for r in rev_rows],
        diff,
        title="Advancing − Declining (4%+ moves)",
    )

    summary_html = kv_to_html([
        ("Regime", regime_label),
        ("5-day Ratio", f"{five_day_ratio:.2f}"),
        ("Today &gt;50DMA%", f"{today['pct_above_50ma']:.1f}%"),
        ("Universe size", f"{today['universe_size']}"),
    ])

    table_html = md_table_to_html(
        ["Date", "Up4%", "Down4%", "Up25%Q", "Up25%M", "Up50%M", "Up13%34", "ATR10x", ">50DMA%", "Univ"],
        [
            [r["date"], r["up_4"], r["down_4"], r["up_25_q"], r["up_25_m"], r["up_50_m"],
             r["up_13_34"], r["ext_10x_atr"], f"{r['pct_above_50ma']:.1f}%", r["universe_size"]]
            for r in rows
        ],
    )

    sections = [
        {"heading": "Summary", "html": summary_html, "fig": None},
        {"heading": ">50DMA% heatmap", "html": "", "fig": fig_hm},
        {"heading": "Advance/Decline differential", "html": "", "fig": fig_diff},
        {"heading": "Today's 4% movers", "html": "", "fig": fig_bar},
        {"heading": "Full breadth table", "html": table_html, "fig": None},
    ]
    p = write_report(f"Breadth — last {days} days", sections, "breadth")
    return str(p)


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 15
    refresh = "--refresh" in sys.argv
    if "--html" in sys.argv:
        path = render_html(days=days, refresh=refresh)
        print(f"HTML report: file:///{path.replace(chr(92), '/')}")
    else:
        print(render(days=days, refresh=refresh))
