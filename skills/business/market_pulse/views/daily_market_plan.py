"""Daily Market Plan — Trade-Brigade-style morning brief."""
from __future__ import annotations

import glob
import sys
from datetime import datetime
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from skills.market_pulse.views._market_trend import compute_signals
from skills.market_pulse.views._sector_perf import compute_sector_performance
from skills.market_pulse.views._theme_strength import compute_theme_strengths
from skills.market_pulse.views.breadth import compute_breadth
from skills.trading.scripts.data.providers.fred import FredProvider
from skills.market_pulse.formatters import markdown as md
from skills.market_pulse.formatters.bars import hbar


def _yes_no(b: bool) -> str:
    return "✅ YES" if b else "❌ NO"


def _fmt(v):
    return f"{v:+.2f}%" if v is not None else "-"


def _last_market_review() -> str:
    """Pull the most recent market review from private project notes/personal/finance/."""
    pattern = str(_ROOT / ".memory" / "personal" / "finance" / "market-review-*.md")
    paths = sorted(glob.glob(pattern))
    if not paths:
        return "_(no recent market review found)_"
    with open(paths[-1], "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    snip: list[str] = []
    for line in lines:
        if line.startswith("## Headline") or (line.startswith("## ") and not snip):
            snip.append(line)
        elif snip and not line.startswith("## "):
            snip.append(line)
            if len([l for l in snip if l.strip()]) >= 8:
                break
    return "\n".join(snip[:12]) + f"\n\n_Source: {Path(paths[-1]).name}_"


def render() -> str:
    today = datetime.now().strftime("%d %b %Y")
    sig = compute_signals()
    sectors = compute_sector_performance()
    themes = compute_theme_strengths()
    breadth = compute_breadth(days=5)
    fred = FredProvider().get_macro_snapshot()

    out: list[str] = []
    out.append(md.section(f"Daily Market Plan — {today}"))

    # 1. Market Trend
    out.append(md.section("1. Market Trend", level=3))
    out.append(md.kv([
        ("Daily Buy Signal", _yes_no(sig.get("daily_buy_signal", False))),
        ("Weekly Buy Signal", _yes_no(sig.get("weekly_buy_signal", False))),
        ("Price > Rising 5-DMA", _yes_no(sig.get("above_rising_5dma", False))),
        ("Regime", f"**{sig.get('regime', 'UNKNOWN')}**"),
        ("SPY Close", f"${sig.get('spy_close', 0):.2f}"),
    ]))

    # 2. Macro context
    out.append(md.section("2. Macro Context (FRED)", level=3))
    macro_rows = [
        ["10Y yield", (fred.get("10y_yield") or {}).get("value", "-")],
        ["2Y yield", (fred.get("2y_yield") or {}).get("value", "-")],
        ["Fed Funds", (fred.get("fed_funds") or {}).get("value", "-")],
        ["DXY", (fred.get("dxy") or {}).get("value", "-")],
        ["VIX", (fred.get("vix") or {}).get("value", "-")],
        ["Core PCE", (fred.get("core_pce") or {}).get("value", "-")],
    ]
    out.append(md.table(["Indicator", "Latest"], macro_rows))

    # 3. Top thematic sectors
    out.append(md.section("3. Top 5 Thematic Sectors", level=3))
    ranked = sorted(themes.items(), key=lambda kv: -kv[1]["strength"])[:5]
    headers = ["Theme", "ETF", "Strength", "5d", "10d", "1mo"]
    theme_rows = [[
        n, t["etf"],
        f"{t['strength_pct']:3d} {hbar(t['strength_pct'], 100, width=10)}",
        _fmt(t["returns"]["5d"]),
        _fmt(t["returns"]["10d"]),
        _fmt(t["returns"]["1mo"]),
    ] for n, t in ranked]
    out.append(md.table(headers, theme_rows))

    # 4. Sub-sector
    out.append(md.section("4. S&P 500 Sub-Sector Performance", level=3))
    sub_rows = [[r["symbol"], _fmt(r["daily"]), _fmt(r["p5d"]), _fmt(r["off_52w_high"]), _fmt(r["ytd"])]
                for r in sectors["sub_sector"]]
    out.append(md.table(["ETF", "Daily", "5d", "Off 52w High", "YTD"], sub_rows))

    # 5. EW sub-sector
    out.append(md.section("5. EW Sub-Sector Performance", level=3))
    ew_rows = [[r["symbol"], _fmt(r["daily"]), _fmt(r["p5d"]), _fmt(r["off_52w_high"]), _fmt(r["ytd"])]
               for r in sectors["ew_sector"]]
    out.append(md.table(["ETF", "Daily", "5d", "Off 52w High", "YTD"], ew_rows))

    # 6. Top 10 thematic ETFs
    out.append(md.section("6. Top 10 Thematic ETFs (by 5d)", level=3))
    therm_rows = [[r["symbol"], _fmt(r["daily"]), _fmt(r["p5d"]), _fmt(r["off_52w_high"]), _fmt(r["ytd"])]
                  for r in sectors["thematic"]]
    out.append(md.table(["ETF", "Daily", "5d", "Off 52w High", "YTD"], therm_rows))

    # 7. Breadth snapshot
    out.append(md.section("7. Breadth Snapshot (last 5 days)", level=3))
    if breadth:
        breadth_rows = [[r["date"], r["up_4"], r["down_4"], f"{r['pct_above_50ma']:.1f}%"]
                        for r in breadth[:5]]
        out.append(md.table(["Date", "Up 4%", "Down 4%", ">50DMA%"], breadth_rows))

    # 8. Last market review carryover
    out.append(md.section("8. Last Market Review (carryover context)", level=3))
    out.append(_last_market_review())

    return "".join(out)


def render_html() -> str:
    """Render Daily Market Plan as interactive HTML. Returns file path."""
    from skills.market_pulse.formatters.html_report import write_report, kv_to_html, md_table_to_html
    from skills.market_pulse.formatters.charts import heatmap, hbar_chart, candlestick
    from skills.trading.scripts.data.providers.composite import build_default_chain

    today = datetime.now().strftime("%d %b %Y")
    sig = compute_signals()
    sectors = compute_sector_performance()
    themes = compute_theme_strengths()
    breadth = compute_breadth(days=10)
    fred = FredProvider().get_macro_snapshot()

    # SPY candlestick
    chain = build_default_chain()
    try:
        spy_bars = chain.get_bars("SPY", limit=120)
    except Exception:
        spy_bars = []
    fig_spy = candlestick(spy_bars, "SPY", sma_periods=[20, 50, 200])

    # Sub-sector heatmap (sectors × timeframes)
    sub_rows = sectors["sub_sector"]
    sub_matrix = [[r["daily"] or 0, r["p5d"] or 0, r["ytd"] or 0] for r in sub_rows]
    fig_sectors = heatmap(
        sub_matrix,
        rows=[r["symbol"] for r in sub_rows],
        cols=["Daily", "5d", "YTD"],
        title="Sub-sector performance",
        zmid=0,
    )

    # Top thematic ETFs bar
    therm = sectors["thematic"]
    fig_thematic = hbar_chart(
        [r["symbol"] for r in therm],
        [r["p5d"] or 0 for r in therm],
        title="Top 10 thematic ETFs (5-day return)",
    )

    # Build sections
    market_trend_html = kv_to_html([
        ("Daily Buy Signal", _yes_no(sig.get("daily_buy_signal", False))),
        ("Weekly Buy Signal", _yes_no(sig.get("weekly_buy_signal", False))),
        ("Price > Rising 5-DMA", _yes_no(sig.get("above_rising_5dma", False))),
        ("Regime", sig.get("regime", "UNKNOWN")),
        ("SPY Close", f"${sig.get('spy_close', 0):.2f}"),
    ])

    macro_html = md_table_to_html(
        ["Indicator", "Latest"],
        [
            ["10Y yield", (fred.get("10y_yield") or {}).get("value", "-")],
            ["2Y yield", (fred.get("2y_yield") or {}).get("value", "-")],
            ["Fed Funds", (fred.get("fed_funds") or {}).get("value", "-")],
            ["DXY", (fred.get("dxy") or {}).get("value", "-")],
            ["VIX", (fred.get("vix") or {}).get("value", "-")],
            ["Core PCE", (fred.get("core_pce") or {}).get("value", "-")],
        ],
    )

    ranked_themes = sorted(themes.items(), key=lambda kv: -kv[1]["strength"])[:5]
    themes_html = md_table_to_html(
        ["Theme", "ETF", "Strength", "5d", "1mo"],
        [[n, t["etf"], f"{t['strength_pct']}/100", _fmt(t["returns"]["5d"]), _fmt(t["returns"]["1mo"])]
         for n, t in ranked_themes],
    )

    breadth_html = md_table_to_html(
        ["Date", "Up 4%", "Down 4%", ">50DMA%"],
        [[r["date"], r["up_4"], r["down_4"], f"{r['pct_above_50ma']:.1f}%"] for r in breadth[:10]],
    )

    review_html = "<pre>" + _last_market_review() + "</pre>"

    sections = [
        {"heading": "1. Market Trend", "html": market_trend_html, "fig": None},
        {"heading": "SPY — daily candles", "html": "", "fig": fig_spy},
        {"heading": "2. Macro Context (FRED)", "html": macro_html, "fig": None},
        {"heading": "3. Top 5 Thematic Sectors", "html": themes_html, "fig": None},
        {"heading": "4. Sub-Sector Heatmap", "html": "", "fig": fig_sectors},
        {"heading": "5. Top 10 Thematic ETFs", "html": "", "fig": fig_thematic},
        {"heading": "6. Breadth Snapshot (10 days)", "html": breadth_html, "fig": None},
        {"heading": "7. Last Market Review (carryover)", "html": review_html, "fig": None},
    ]
    p = write_report(f"Daily Market Plan — {today}", sections, "daily_market_plan")
    return str(p)


if __name__ == "__main__":
    if "--html" in sys.argv:
        path = render_html()
        print(f"HTML report: file:///{path.replace(chr(92), '/')}")
    else:
        print(render())
