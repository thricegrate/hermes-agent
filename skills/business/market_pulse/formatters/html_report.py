"""Compose a self-contained HTML report from multiple Plotly figures + markdown sections.

Output is written to .tmp/trading-viz/<view>-<timestamp>.html (gitignored).
Each report is single-file (Plotly bundled inline) so it works offline.
"""
from __future__ import annotations

import html as _html
from datetime import datetime
from pathlib import Path

import plotly.graph_objects as go
import plotly.io as pio


def _esc(value) -> str:
    """HTML-escape a value, allowing safe display of API responses + user input."""
    return _html.escape(str(value), quote=False)


_ROOT = Path(__file__).resolve().parents[3]


HTML_HEAD = """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<title>{title}</title>
<style>
body {{ font-family: 'Menlo', 'Consolas', monospace; background: #0d1117; color: #e6edf3; margin: 0; padding: 20px; max-width: 1200px; margin: 0 auto; }}
h1, h2, h3 {{ color: #58a6ff; border-bottom: 1px solid #30363d; padding-bottom: 4px; }}
h1 {{ font-size: 28px; }}
table {{ border-collapse: collapse; margin: 12px 0; width: 100%; }}
th, td {{ padding: 6px 12px; border: 1px solid #30363d; text-align: left; }}
th {{ background: #161b22; }}
.section {{ margin: 24px 0; }}
.fig {{ margin: 16px 0; }}
.kv {{ background: #161b22; padding: 12px; border-radius: 6px; margin: 12px 0; }}
.kv li {{ margin: 4px 0; }}
.up {{ color: #26a641; }}
.down {{ color: #f85149; }}
.neutral {{ color: #d29922; }}
footer {{ margin-top: 40px; padding-top: 12px; border-top: 1px solid #30363d; color: #8b949e; font-size: 12px; }}
pre {{ background: #161b22; padding: 12px; border-radius: 6px; overflow-x: auto; }}
</style>
</head><body>
<h1>{title}</h1>
"""

HTML_FOOT = """
<footer>
Generated {ts} — Cyber Corsairs trading research — Data: yfinance (Yahoo) / Finnhub / FRED / Alpha Vantage
</footer>
</body></html>
"""


def write_report(title: str, sections: list[dict], view_name: str) -> Path:
    """Write HTML report; return Path.

    sections: list of dicts, each with optional keys:
      - heading (str): section header
      - html (str): raw HTML body content (rendered as-is)
      - fig (go.Figure): Plotly figure to embed
    """
    out_dir = _ROOT / ".tmp" / "trading-viz"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    path = out_dir / f"{view_name}-{ts}.html"

    parts: list[str] = [HTML_HEAD.format(title=title)]
    first_fig = True
    for s in sections:
        parts.append('<div class="section">')
        if s.get("heading"):
            parts.append(f"<h2>{s['heading']}</h2>")
        if s.get("html"):
            parts.append(s["html"])
        fig = s.get("fig")
        if fig is not None:
            parts.append('<div class="fig">')
            # Embed Plotly inline once on the first figure; subsequent figures reuse the bundle
            parts.append(pio.to_html(
                fig,
                include_plotlyjs="inline" if first_fig else False,
                full_html=False,
                config={"displaylogo": False},
            ))
            parts.append("</div>")
            first_fig = False
        parts.append("</div>")
    parts.append(HTML_FOOT.format(ts=datetime.now().strftime("%Y-%m-%d %H:%M")))

    path.write_text("".join(parts), encoding="utf-8")
    return path


def md_table_to_html(headers: list[str], rows: list[list]) -> str:
    """Render a markdown-style table as HTML. Values escaped to prevent XSS
    from upstream API responses or user-supplied tickers."""
    head = "".join(f"<th>{_esc(h)}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{_esc(c)}</td>" for c in r) + "</tr>"
        for r in rows
    )
    return f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"


def kv_to_html(items: list[tuple[str, str]]) -> str:
    """Render a kv list as a styled HTML list. Keys may contain controlled HTML
    (e.g. `&gt;` for >); values are always escaped."""
    lis = "".join(f"<li><strong>{k}:</strong> {_esc(v)}</li>" for k, v in items)
    return f'<ul class="kv">{lis}</ul>'


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(_ROOT))
    from skills.market_pulse.formatters.charts import candlestick, gauge
    from skills.trading.scripts.data.providers.composite import build_default_chain

    bars = build_default_chain().get_bars("SPY", limit=120)
    sections = [
        {"heading": "SPY Score", "html": kv_to_html([("Score", "72"), ("Stage", "2")]),
         "fig": gauge(72, title="Score")},
        {"heading": "SPY Candles + SMA", "html": "", "fig": candlestick(bars, "SPY")},
    ]
    p = write_report("SPY Setup", sections, "spy_test")
    print(f"Wrote {p}")
