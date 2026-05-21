"""Theme Flow Map — sector rotation matrix with strength + per-theme detail."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[3]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from skills.market_pulse.views._theme_strength import compute_theme_strengths
from skills.market_pulse.formatters import markdown as md
from skills.market_pulse.formatters.bars import hbar


def _verdict(strength_pct: int) -> str:
    if strength_pct >= 85:
        return "ACTIONABLE"
    if strength_pct >= 70:
        return "WATCH"
    if strength_pct < 30:
        return "AVOID"
    return "NEUTRAL"


def _fmt_pct(v: float | None) -> str:
    return f"{v:+.2f}%" if v is not None else "-"


def render() -> str:
    data = compute_theme_strengths()
    if not data:
        return "_Theme Flow Map: no data._"

    ranked = sorted(data.items(), key=lambda kv: -kv[1]["strength"])

    out: list[str] = []
    out.append(md.section("Theme Flow Map"))
    out.append(md.section("Rotation Matrix", level=3))

    headers = ["#", "Theme", "ETF", "Strength", "1d", "5d", "10d", "1mo"]
    rows = []
    for i, (name, t) in enumerate(ranked, 1):
        rets = t["returns"]
        rows.append([
            i,
            name,
            t["etf"],
            f"{t['strength_pct']:3d} {hbar(t['strength_pct'], 100, width=8)}",
            _fmt_pct(rets["1d"]),
            _fmt_pct(rets["5d"]),
            _fmt_pct(rets["10d"]),
            _fmt_pct(rets["1mo"]),
        ])
    out.append(md.table(headers, rows))

    out.append(md.section("Top 3 detail", level=3))
    for i, (name, t) in enumerate(ranked[:3], 1):
        out.append(f"\n#### {i}. {name} ({t['etf']}) — strength {t['strength_pct']}/100\n")
        out.append(md.kv([
            ("Verdict", _verdict(t["strength_pct"])),
            ("5d return", _fmt_pct(t["returns"]["5d"])),
            ("1mo return", _fmt_pct(t["returns"]["1mo"])),
            ("Strength bar", hbar(t["strength_pct"], 100, width=20)),
        ]))
        out.append("\n")

    return "".join(out)


def render_html() -> str:
    """Render theme flow map as interactive HTML. Returns file path."""
    from skills.market_pulse.formatters.html_report import write_report, md_table_to_html, kv_to_html
    from skills.market_pulse.formatters.charts import heatmap, hbar_chart

    data = compute_theme_strengths()
    if not data:
        return ""

    ranked = sorted(data.items(), key=lambda kv: -kv[1]["strength"])
    timeframes = ["1d", "5d", "10d", "1mo"]

    # Build heatmap matrix: themes × timeframes
    matrix = []
    theme_names = []
    for name, t in ranked:
        z = t.get("z", {})
        matrix.append([z.get(tf) or 0 for tf in timeframes])
        theme_names.append(name)
    fig_hm = heatmap(matrix, rows=theme_names, cols=timeframes,
                     title="Excess return vs SPY (z-score)", zmid=0)

    # Top-3 strength bar
    top3 = ranked[:3]
    fig_top = hbar_chart(
        [n for n, _ in top3],
        [t["strength_pct"] for _, t in top3],
        title="Top 3 themes — strength percentile",
    )

    # Rotation table HTML
    rows_html = md_table_to_html(
        ["#", "Theme", "ETF", "Strength", "1d", "5d", "10d", "1mo"],
        [[
            i,
            name,
            t["etf"],
            f"{t['strength_pct']}/100",
            _fmt_pct(t["returns"]["1d"]),
            _fmt_pct(t["returns"]["5d"]),
            _fmt_pct(t["returns"]["10d"]),
            _fmt_pct(t["returns"]["1mo"]),
        ] for i, (name, t) in enumerate(ranked, 1)],
    )

    summary = kv_to_html([
        ("Top theme", f"{ranked[0][0]} ({ranked[0][1]['etf']})"),
        ("Top strength", f"{ranked[0][1]['strength_pct']}/100"),
        ("Top 5d return", _fmt_pct(ranked[0][1]['returns']['5d'])),
    ])

    sections = [
        {"heading": "Summary", "html": summary, "fig": None},
        {"heading": "Theme z-score heatmap (themes × timeframes)", "html": "", "fig": fig_hm},
        {"heading": "Top 3 strength", "html": "", "fig": fig_top},
        {"heading": "Full rotation table", "html": rows_html, "fig": None},
    ]
    p = write_report("Theme Flow Map", sections, "theme_flow_map")
    return str(p)


if __name__ == "__main__":
    if "--html" in sys.argv:
        path = render_html()
        print(f"HTML report: file:///{path.replace(chr(92), '/')}")
    else:
        print(render())
