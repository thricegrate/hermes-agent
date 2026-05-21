"""Unicode block-bar rendering for chat-friendly visualizations."""
from __future__ import annotations

# Block characters: blank, then 8 levels of fill height
BLOCKS = " ▁▂▃▄▅▆▇█"
SOLID = "█"
EMPTY = "░"


def hbar(value: float, max_val: float = 1.0, width: int = 20) -> str:
    """Render a horizontal solid/empty bar. value/max -> filled fraction."""
    if max_val == 0:
        return EMPTY * width
    frac = max(0.0, min(1.0, value / max_val))
    filled = round(frac * width)
    return SOLID * filled + EMPTY * (width - filled)


def diverging_hbar(value: float, max_abs: float = 1.0, width: int = 20) -> str:
    """Bar centered at zero. Negative renders left, positive right."""
    half = width // 2
    if max_abs == 0:
        return " " * half + "│" + " " * half
    frac = max(-1.0, min(1.0, value / max_abs))
    if frac >= 0:
        filled = round(frac * half)
        return " " * half + "│" + SOLID * filled + EMPTY * (half - filled)
    else:
        filled = round(-frac * half)
        return EMPTY * (half - filled) + SOLID * filled + "│" + " " * half


def heatmap_cell(value: float, low: float, high: float) -> str:
    """Pick a block character intensity based on value's position in [low, high]."""
    if high == low:
        return BLOCKS[len(BLOCKS) // 2]
    frac = max(0.0, min(1.0, (value - low) / (high - low)))
    idx = round(frac * (len(BLOCKS) - 1))
    return BLOCKS[idx]


def traffic_light(value: float, neutral_band: tuple[float, float] = (-0.5, 0.5)) -> str:
    if value < neutral_band[0]:
        return "🔴"
    if value > neutral_band[1]:
        return "🟢"
    return "🟡"


if __name__ == "__main__":
    print("hbar(0.5):       ", hbar(0.5))
    print("hbar(0.9):       ", hbar(0.9))
    print("hbar(0.1):       ", hbar(0.1))
    print("diverging(0.7):  ", diverging_hbar(0.7))
    print("diverging(-0.4): ", diverging_hbar(-0.4))
    print("diverging(0.0):  ", diverging_hbar(0.0))
    print("heatmap(50,0,100):", heatmap_cell(50, 0, 100))
    print("heatmap(95,0,100):", heatmap_cell(95, 0, 100))
    print("traffic(0.7):    ", traffic_light(0.7))
    print("traffic(-0.7):   ", traffic_light(-0.7))
    print("traffic(0.1):    ", traffic_light(0.1))
