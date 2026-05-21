"""Plotly figure factories. All return go.Figure ready for to_html().

Color palette derived from the founder's screenshot dashboards: dark
background, neon-green for up, neon-red for down, yellow for neutral,
cyan for highlights.
"""
from __future__ import annotations

import plotly.graph_objects as go


PALETTE = {
    "bg": "#0d1117",
    "fg": "#e6edf3",
    "grid": "#30363d",
    "up": "#26a641",
    "down": "#f85149",
    "neutral": "#d29922",
    "highlight": "#58a6ff",
    "subtle": "#8b949e",
}

LAYOUT_DARK = {
    "paper_bgcolor": PALETTE["bg"],
    "plot_bgcolor": PALETTE["bg"],
    "font": {"color": PALETTE["fg"], "family": "Menlo, Consolas, monospace"},
    "xaxis": {"gridcolor": PALETTE["grid"], "zerolinecolor": PALETTE["grid"]},
    "yaxis": {"gridcolor": PALETTE["grid"], "zerolinecolor": PALETTE["grid"]},
    "margin": {"l": 50, "r": 30, "t": 50, "b": 40},
}


def candlestick(bars: list[dict], symbol: str, sma_periods: list[int] | None = None) -> go.Figure:
    """Candlestick + optional SMA overlays."""
    sma_periods = sma_periods or [50, 200]
    if not bars:
        fig = go.Figure()
        fig.update_layout(title=f"{symbol} — no data", **LAYOUT_DARK)
        return fig
    closes = [b["c"] for b in bars]
    dates = [b["t"][:10] for b in bars]
    fig = go.Figure(data=[
        go.Candlestick(
            x=dates,
            open=[b["o"] for b in bars],
            high=[b["h"] for b in bars],
            low=[b["l"] for b in bars],
            close=closes,
            increasing_line_color=PALETTE["up"],
            decreasing_line_color=PALETTE["down"],
            name=symbol,
        )
    ])
    for p in sma_periods:
        if len(closes) >= p:
            sma = [
                sum(closes[max(0, i - p + 1): i + 1]) / min(p, i + 1)
                for i in range(len(closes))
            ]
            fig.add_trace(go.Scatter(
                x=dates, y=sma, mode="lines",
                name=f"SMA{p}", line={"width": 1, "color": PALETTE["highlight"] if p == 50 else PALETTE["subtle"]},
            ))
    fig.update_layout(title=f"{symbol} — daily ({len(bars)} bars)", xaxis_rangeslider_visible=False, **LAYOUT_DARK)
    return fig


def heatmap(matrix: list[list[float]], rows: list[str], cols: list[str], title: str = "", zmid: float = 0) -> go.Figure:
    """Diverging heatmap (red→bg→green) centered at `zmid`."""
    fig = go.Figure(data=go.Heatmap(
        z=matrix, x=cols, y=rows,
        colorscale=[[0, PALETTE["down"]], [0.5, PALETTE["bg"]], [1, PALETTE["up"]]],
        zmid=zmid,
    ))
    fig.update_layout(title=title, **LAYOUT_DARK)
    return fig


def gauge(value: float, low: float = 0, high: float = 100, title: str = "") -> go.Figure:
    """0-100 score gauge with red/yellow/green bands."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        gauge={
            "axis": {"range": [low, high]},
            "bar": {"color": PALETTE["highlight"]},
            "steps": [
                {"range": [low, high * 0.4], "color": PALETTE["down"]},
                {"range": [high * 0.4, high * 0.7], "color": PALETTE["neutral"]},
                {"range": [high * 0.7, high], "color": PALETTE["up"]},
            ],
        },
        title={"text": title},
    ))
    fig.update_layout(**LAYOUT_DARK)
    return fig


def hbar_chart(labels: list[str], values: list[float], title: str = "") -> go.Figure:
    """Horizontal bar chart, color by sign."""
    colors = [PALETTE["up"] if v >= 0 else PALETTE["down"] for v in values]
    fig = go.Figure(go.Bar(x=values, y=labels, orientation="h", marker_color=colors))
    fig.update_layout(title=title, **LAYOUT_DARK)
    return fig


def vbar_chart(labels: list[str], values: list[float], title: str = "") -> go.Figure:
    """Vertical bar chart, color by sign."""
    colors = [PALETTE["up"] if v >= 0 else PALETTE["down"] for v in values]
    fig = go.Figure(go.Bar(x=labels, y=values, marker_color=colors))
    fig.update_layout(title=title, **LAYOUT_DARK)
    return fig


def area_chart(dates: list[str], values: list[float], title: str = "", fill_color: str | None = None) -> go.Figure:
    """Area chart over a date series."""
    fig = go.Figure(go.Scatter(
        x=dates, y=values, mode="lines",
        fill="tozeroy",
        line={"color": fill_color or PALETTE["highlight"]},
    ))
    fig.update_layout(title=title, **LAYOUT_DARK)
    return fig


if __name__ == "__main__":
    import sys
    sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[3]))
    from skills.trading.scripts.data.providers.composite import build_default_chain
    bars = build_default_chain().get_bars("SPY", limit=120)
    fig = candlestick(bars, "SPY")
    out = "/tmp/spy_candles.html"
    fig.write_html(out, include_plotlyjs="inline")
    print(f"Wrote {out}")
