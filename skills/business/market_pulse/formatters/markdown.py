"""Markdown rendering helpers for chat-formatted view outputs."""
from __future__ import annotations


def section(title: str, level: int = 2) -> str:
    return f"\n{'#' * level} {title}\n"


def table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return ""
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    body = "\n".join("| " + " | ".join(str(c) for c in r) + " |" for r in rows)
    return f"{head}\n{sep}\n{body}\n"


def kv(items: list[tuple[str, str]]) -> str:
    return "\n".join(f"- **{k}:** {v}" for k, v in items)


def fmt_pct(value: float | None, decimals: int = 2) -> str:
    if value is None:
        return "-"
    return f"{value:+.{decimals}f}%"


def fmt_money(value: float | None) -> str:
    if value is None:
        return "-"
    if value >= 1e9:
        return f"${value / 1e9:.1f}B"
    if value >= 1e6:
        return f"${value / 1e6:.1f}M"
    return f"${value:,.2f}"


def fmt_int(value: float | int | None) -> str:
    if value is None:
        return "-"
    return f"{int(value):,}"


if __name__ == "__main__":
    print(section("Test"))
    print(table(["a", "b"], [["1", "2"], ["3", "4"]]))
    print(kv([("foo", "bar"), ("hello", "world")]))
    print("pct:", fmt_pct(1.234))
    print("money:", fmt_money(1_234_567_890))
    print("int:", fmt_int(1_234))
