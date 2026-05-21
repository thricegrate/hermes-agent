"""Stylized trading-data cards (PNG) using Pillow.

NOTE on naming: this module is named `infographic.py` to match the plan and
the cyber-corsairs convention, but it does NOT bridge to skills/infographic-gen
(which generates hand-drawn Gemini illustrations — wrong fit for trading
data cards). Instead, it composes structured data cards directly with Pillow.

If the user later wants a Gemini illustration of a trading concept, they can
invoke skills/infographic-gen directly; the two are complementary.

Cards rendered:
- 1080x1350 portrait DMP card (regime + top-3 themes + key SPY level + macro)
- 1080x1080 square setup card (ticker + score + stage + key levels)
- 1080x1350 portrait theme-flow card (top-5 themes + RISK ON/OFF label)

Output: PNG written to .tmp/trading-viz/cards/<view>-<ts>.png (gitignored).
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


_ROOT = Path(__file__).resolve().parents[3]
CARDS_DIR = _ROOT / ".tmp" / "trading-viz" / "cards"


# Palette matches the HTML theme
PALETTE = {
    "bg": (13, 17, 23),         # #0d1117
    "fg": (230, 237, 243),      # #e6edf3
    "subtle": (139, 148, 158),  # #8b949e
    "up": (38, 166, 65),        # #26a641
    "down": (248, 81, 73),      # #f85149
    "neutral": (210, 153, 34),  # #d29922
    "highlight": (88, 166, 255),  # #58a6ff
    "panel": (22, 27, 34),      # #161b22
}


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Load a system font; fall back to default if Windows fonts unavailable."""
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)


def _color_for_regime(regime: str) -> tuple[int, int, int]:
    if "UP" in regime or "🟢" in regime:
        return PALETTE["up"]
    if "DOWN" in regime or "🔴" in regime:
        return PALETTE["down"]
    return PALETTE["neutral"]


def _draw_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, size: int, color, bold: bool = False) -> None:
    draw.text(xy, text, font=_font(size, bold=bold), fill=color)


def _ensure_dir() -> Path:
    CARDS_DIR.mkdir(parents=True, exist_ok=True)
    return CARDS_DIR


def render_dmp_card(data: dict) -> Path:
    """1080x1350 portrait DMP card.

    Expected data keys:
      regime (str), spy_close (float), top_themes (list[(name, etf, ret_5d)]),
      macro (dict like {'10y': '4.43', 'vix': '17.39', 'pce': '129.28'}),
      date (str)
    """
    W, H = 1080, 1350
    img = Image.new("RGB", (W, H), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    # Header
    _draw_text(draw, (60, 60), "DAILY MARKET PLAN", 56, PALETTE["highlight"], bold=True)
    _draw_text(draw, (60, 130), data.get("date", ""), 32, PALETTE["subtle"])

    # Regime block
    regime = data.get("regime", "UNKNOWN")
    rcolor = _color_for_regime(regime)
    draw.rounded_rectangle((60, 200, W - 60, 350), radius=16, fill=PALETTE["panel"])
    _draw_text(draw, (90, 220), "REGIME", 28, PALETTE["subtle"], bold=True)
    _draw_text(draw, (90, 260), regime.replace("🟢 ", "").replace("🔴 ", "").replace("🟡 ", ""), 80, rcolor, bold=True)

    # SPY block
    spy = data.get("spy_close", 0)
    _draw_text(draw, (W - 320, 220), "SPY CLOSE", 28, PALETTE["subtle"], bold=True)
    _draw_text(draw, (W - 320, 260), f"${spy:.2f}", 56, PALETTE["fg"], bold=True)

    # Top themes
    _draw_text(draw, (60, 410), "TOP THEMES (5d return)", 32, PALETTE["highlight"], bold=True)
    y = 470
    for i, (name, etf, ret) in enumerate(data.get("top_themes", [])[:5], 1):
        ret_color = PALETTE["up"] if ret >= 0 else PALETTE["down"]
        _draw_text(draw, (90, y), f"{i}. {name[:32]}", 32, PALETTE["fg"])
        _draw_text(draw, (W - 350, y), etf, 32, PALETTE["subtle"])
        _draw_text(draw, (W - 220, y), f"{ret:+.2f}%", 32, ret_color, bold=True)
        y += 56

    # Macro
    _draw_text(draw, (60, 870), "MACRO CONTEXT", 32, PALETTE["highlight"], bold=True)
    macro = data.get("macro", {})
    macro_y = 930
    for label, value in [
        ("10Y yield", macro.get("10y", "-")),
        ("2Y yield", macro.get("2y", "-")),
        ("DXY", macro.get("dxy", "-")),
        ("VIX", macro.get("vix", "-")),
        ("Core PCE", macro.get("pce", "-")),
    ]:
        _draw_text(draw, (90, macro_y), label, 28, PALETTE["subtle"])
        _draw_text(draw, (W - 250, macro_y), str(value), 28, PALETTE["fg"], bold=True)
        macro_y += 44

    # Footer
    _draw_text(draw, (60, H - 80), "Cyber Corsairs Trading Research", 22, PALETTE["subtle"])
    _draw_text(draw, (60, H - 50), datetime.now().strftime("%Y-%m-%d %H:%M"), 22, PALETTE["subtle"])

    out_dir = _ensure_dir()
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    out_path = out_dir / f"dmp-card-{ts}.png"
    img.save(out_path)
    return out_path


def render_setup_card(data: dict) -> Path:
    """1080x1080 square setup card.

    Expected data keys:
      symbol, score, stage, bucket, rs, price, sma200, pct_from_high,
      verdict, sma200_slope
    """
    W, H = 1080, 1080
    img = Image.new("RGB", (W, H), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    symbol = data.get("symbol", "")
    bucket = data.get("bucket", "Unclassified")
    rs = data.get("rs", 50)

    # Big ticker
    _draw_text(draw, (60, 60), symbol, 140, PALETTE["highlight"], bold=True)
    _draw_text(draw, (60, 220), f"Stage {data.get('stage', '?')[-1]}", 48, PALETTE["fg"])

    # Bucket badge
    bucket_color = {
        "White Up": (255, 255, 255), "Optimum": PALETTE["up"], "Secondary": PALETTE["up"],
        "Yellow": PALETTE["neutral"], "Blue": PALETTE["highlight"],
        "Red": PALETTE["down"], "White Down": (255, 255, 255),
    }.get(bucket, PALETTE["subtle"])
    draw.rounded_rectangle((60, 300, 60 + max(280, len(bucket) * 32), 380), radius=12, fill=PALETTE["panel"])
    _draw_text(draw, (80, 320), bucket.upper(), 36, bucket_color, bold=True)

    # RS bar visualization
    _draw_text(draw, (60, 430), f"RS PERCENTILE: {rs}", 36, PALETTE["subtle"], bold=True)
    bar_w = W - 120
    bar_h = 40
    bar_x, bar_y = 60, 480
    draw.rounded_rectangle((bar_x, bar_y, bar_x + bar_w, bar_y + bar_h), radius=8, fill=PALETTE["panel"])
    fill_w = int(bar_w * rs / 100)
    bar_color = PALETTE["up"] if rs >= 70 else PALETTE["neutral"] if rs >= 40 else PALETTE["down"]
    if fill_w > 0:
        draw.rounded_rectangle((bar_x, bar_y, bar_x + fill_w, bar_y + bar_h), radius=8, fill=bar_color)

    # Key levels
    _draw_text(draw, (60, 580), "KEY LEVELS", 32, PALETTE["highlight"], bold=True)
    levels_y = 640
    for label, value in [
        ("Price", f"${data.get('price', 0):.2f}"),
        ("SMA200", f"${data.get('sma200', 0):.2f}"),
        ("Off 52w high", f"{data.get('pct_from_high', 0):+.1f}%"),
        ("SMA200 slope", f"{data.get('sma200_slope', 0):+.3f}%/day"),
    ]:
        _draw_text(draw, (90, levels_y), label, 30, PALETTE["subtle"])
        _draw_text(draw, (W - 380, levels_y), value, 30, PALETTE["fg"], bold=True)
        levels_y += 50

    # Verdict
    verdict = data.get("verdict", "")
    if verdict:
        _draw_text(draw, (60, 900), "VERDICT", 32, PALETTE["highlight"], bold=True)
        _draw_text(draw, (60, 950), verdict, 40, PALETTE["fg"], bold=True)

    # Footer
    _draw_text(draw, (60, H - 60), f"Cyber Corsairs · {datetime.now().strftime('%Y-%m-%d')}", 20, PALETTE["subtle"])

    out_dir = _ensure_dir()
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    out_path = out_dir / f"setup-{symbol}-{ts}.png"
    img.save(out_path)
    return out_path


def render_theme_flow_card(data: dict) -> Path:
    """1080x1350 portrait theme-flow card.

    Expected data keys:
      top_themes (list[(name, etf, strength_pct, ret_5d, ret_1mo)]),
      risk_label ('RISK ON' / 'RISK OFF' / 'NEUTRAL'),
      date (str)
    """
    W, H = 1080, 1350
    img = Image.new("RGB", (W, H), PALETTE["bg"])
    draw = ImageDraw.Draw(img)

    # Header
    _draw_text(draw, (60, 60), "THEME FLOW MAP", 56, PALETTE["highlight"], bold=True)
    _draw_text(draw, (60, 130), data.get("date", ""), 32, PALETTE["subtle"])

    # Risk label badge
    risk = data.get("risk_label", "NEUTRAL")
    rcolor = _color_for_regime(risk)
    draw.rounded_rectangle((60, 200, W - 60, 320), radius=16, fill=PALETTE["panel"])
    _draw_text(draw, (90, 220), "MARKET BIAS", 28, PALETTE["subtle"], bold=True)
    _draw_text(draw, (90, 260), risk, 64, rcolor, bold=True)

    # Top 5 themes
    _draw_text(draw, (60, 380), "TOP 5 THEMES BY STRENGTH", 32, PALETTE["highlight"], bold=True)
    y = 450
    for i, (name, etf, strength, ret_5d, ret_1mo) in enumerate(data.get("top_themes", [])[:5], 1):
        # Theme name + ETF
        _draw_text(draw, (90, y), f"{i}. {name[:28]}", 30, PALETTE["fg"], bold=True)
        _draw_text(draw, (90, y + 36), etf, 24, PALETTE["subtle"])

        # Strength bar
        bar_w = 380
        bar_x = W - bar_w - 90
        bar_y = y + 18
        draw.rounded_rectangle((bar_x, bar_y, bar_x + bar_w, bar_y + 24), radius=6, fill=PALETTE["panel"])
        fill_w = int(bar_w * strength / 100)
        bar_color = PALETTE["up"] if strength >= 70 else PALETTE["neutral"] if strength >= 40 else PALETTE["down"]
        if fill_w > 0:
            draw.rounded_rectangle((bar_x, bar_y, bar_x + fill_w, bar_y + 24), radius=6, fill=bar_color)
        _draw_text(draw, (bar_x + bar_w + 16, y + 14), f"{strength}/100", 24, PALETTE["subtle"], bold=True)

        # 5d / 1mo returns
        ret_5d_color = PALETTE["up"] if ret_5d >= 0 else PALETTE["down"]
        ret_1mo_color = PALETTE["up"] if ret_1mo >= 0 else PALETTE["down"]
        _draw_text(draw, (W - 280, y + 50), f"5d {ret_5d:+.1f}%", 22, ret_5d_color)
        _draw_text(draw, (W - 140, y + 50), f"1mo {ret_1mo:+.1f}%", 22, ret_1mo_color)

        y += 130

    # Footer
    _draw_text(draw, (60, H - 80), "Cyber Corsairs Trading Research", 22, PALETTE["subtle"])
    _draw_text(draw, (60, H - 50), datetime.now().strftime("%Y-%m-%d %H:%M"), 22, PALETTE["subtle"])

    out_dir = _ensure_dir()
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    out_path = out_dir / f"theme-flow-card-{ts}.png"
    img.save(out_path)
    return out_path


# ─────────────────────────────────────────────────────────────────────
# Live-data wiring — pull from views to build the card data dicts
# ─────────────────────────────────────────────────────────────────────


def build_setup_card_live(symbol: str) -> Path:
    """Pull live data for `symbol` and render setup card."""
    import sys
    sys.path.insert(0, str(_ROOT))
    from skills.trading.scripts.data.providers.composite import build_default_chain
    from skills.trading.scripts.data.stage import classify
    from skills.trading.scripts.data.rs import get_rs

    chain = build_default_chain()
    bars = chain.get_bars(symbol, limit=250)
    rs = get_rs(symbol)
    s = classify(bars, rs_percentile=rs)

    bucket_to_verdict = {
        "White Up": "Top focus list — strongest leader",
        "Optimum": "Top focus list candidate",
        "Secondary": "Active swing watchlist",
        "Yellow": "Stalk — not actionable yet",
        "Blue": "Counter-trend reversal candidate",
        "Red": "Avoid long",
        "White Down": "Short candidate",
        "Unclassified": "Insufficient history",
    }

    return render_setup_card({
        "symbol": symbol,
        "stage": s.stage,
        "bucket": s.bucket,
        "rs": rs,
        "price": s.price,
        "sma200": s.sma200,
        "pct_from_high": s.pct_from_52w_high,
        "sma200_slope": s.sma200_slope_pct_per_day,
        "verdict": bucket_to_verdict.get(s.bucket, ""),
    })


def build_dmp_card_live() -> Path:
    """Pull live DMP data and render the card."""
    import sys
    sys.path.insert(0, str(_ROOT))
    from skills.market_pulse.views._market_trend import compute_signals
    from skills.market_pulse.views._theme_strength import compute_theme_strengths
    from skills.trading.scripts.data.providers.fred import FredProvider

    sig = compute_signals()
    themes = compute_theme_strengths()
    fred = FredProvider().get_macro_snapshot()

    ranked = sorted(themes.items(), key=lambda kv: -kv[1]["strength"])[:5]
    top_themes = [(n, t["etf"], t["returns"]["5d"] or 0) for n, t in ranked]

    return render_dmp_card({
        "date": datetime.now().strftime("%d %b %Y"),
        "regime": sig.get("regime", "UNKNOWN"),
        "spy_close": sig.get("spy_close", 0),
        "top_themes": top_themes,
        "macro": {
            "10y": (fred.get("10y_yield") or {}).get("value", "-") + "%",
            "2y": (fred.get("2y_yield") or {}).get("value", "-") + "%",
            "dxy": (fred.get("dxy") or {}).get("value", "-"),
            "vix": (fred.get("vix") or {}).get("value", "-"),
            "pce": (fred.get("core_pce") or {}).get("value", "-"),
        },
    })


def build_theme_flow_card_live() -> Path:
    """Pull live theme flow data and render the card."""
    import sys
    sys.path.insert(0, str(_ROOT))
    from skills.market_pulse.views._theme_strength import compute_theme_strengths

    themes = compute_theme_strengths()
    ranked = sorted(themes.items(), key=lambda kv: -kv[1]["strength"])[:5]

    # Risk label heuristic: top theme strength_pct > 75 -> RISK ON
    top_strength = ranked[0][1]["strength_pct"] if ranked else 50
    if top_strength > 75:
        risk = "RISK ON"
    elif top_strength < 40:
        risk = "RISK OFF"
    else:
        risk = "NEUTRAL"

    top_themes = [
        (n, t["etf"], t["strength_pct"], t["returns"]["5d"] or 0, t["returns"]["1mo"] or 0)
        for n, t in ranked
    ]

    return render_theme_flow_card({
        "date": datetime.now().strftime("%d %b %Y"),
        "risk_label": risk,
        "top_themes": top_themes,
    })


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: infographic.py <dmp|setup TICKER|theme>")
        print("  --smoke     run with synthetic data (no API calls)")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "--smoke":
        # Synthetic-data smoke test
        p = render_setup_card({
            "symbol": "STRL", "stage": "Stage 2", "bucket": "Optimum", "rs": 92,
            "price": 841.64, "sma200": 368.42, "pct_from_high": -5.3,
            "sma200_slope": 0.443, "verdict": "Top focus list candidate",
        })
        print(f"setup card: {p}")
    elif cmd == "dmp":
        p = build_dmp_card_live()
        print(f"DMP card: {p}")
    elif cmd == "setup":
        symbol = sys.argv[2] if len(sys.argv) > 2 else "SPY"
        p = build_setup_card_live(symbol)
        print(f"setup card: {p}")
    elif cmd == "theme":
        p = build_theme_flow_card_live()
        print(f"theme flow card: {p}")
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
