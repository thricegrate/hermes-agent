"""Replay the Jeff Sun scorer over a CSV of historical trades.

Each trade row must specify:
  ticker, entry_date (ISO), bars_csv (path to OHLCV csv for that ticker),
  snapshot_json (optional), expected_label (winner | chase | skip)

Reports:
  - Hard-gate pass/fail per trade
  - Score distribution
  - How many winners score >=70 and how many chases get hard-gated

Usage:
  python backtest_rubric.py --trades-csv trades.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path

from scorer import _load_bars_csv, score_setup


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Backtest the Jeff Sun scorer over historical trades.")
    p.add_argument("--trades-csv", required=True, help="CSV: ticker,entry_date,bars_csv,snapshot_json,expected_label")
    p.add_argument("--bars-dir", default=".", help="Directory prefix for bars_csv paths (default: cwd)")
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args(argv)

    bars_dir = Path(args.bars_dir)
    stats = Counter()
    results: list[dict] = []

    with open(args.trades_csv, newline="") as f:
        for row in csv.DictReader(f):
            ticker = row["ticker"]
            entry_date = date.fromisoformat(row["entry_date"])
            bars_path = bars_dir / row["bars_csv"]
            snapshot_path = bars_dir / row["snapshot_json"] if row.get("snapshot_json") else None
            expected = row.get("expected_label", "").strip()

            daily = _load_bars_csv(str(bars_path))
            # Trim to bars up to and including entry_date
            daily = [b for b in daily if b.t.date() <= entry_date]
            snapshot = json.load(open(snapshot_path)) if snapshot_path else {}
            if "earnings_date" in snapshot and isinstance(snapshot["earnings_date"], str):
                snapshot["earnings_date"] = date.fromisoformat(snapshot["earnings_date"])

            result = score_setup(
                ticker=ticker,
                daily_bars=daily,
                intraday_bars=None,
                snapshot=snapshot,
                as_of=datetime.combine(entry_date, datetime.min.time(), tzinfo=timezone.utc),
            )

            passed_gates = result.hard_gate_pass
            passed_score = result.score >= 70
            label = (
                "KEEP" if passed_gates and passed_score
                else "DROP_GATES" if not passed_gates
                else "DROP_SCORE"
            )
            stats[(expected, label)] += 1
            results.append({
                "ticker": ticker,
                "entry_date": entry_date.isoformat(),
                "expected": expected,
                "label": label,
                "score": result.score,
                "reasons_dropped": result.reasons_dropped,
            })
            if args.verbose:
                print(f"{ticker} {entry_date} | expected={expected} | {label} | score={result.score} | {'; '.join(result.reasons_dropped)}")

    # Report
    print("\n=== Summary ===")
    for (expected, label), n in sorted(stats.items()):
        print(f"  expected={expected:<8} -> {label:<12}  n={n}")

    winners_kept = sum(n for (exp, lab), n in stats.items() if exp == "winner" and lab == "KEEP")
    winners_total = sum(n for (exp, _), n in stats.items() if exp == "winner")
    chases_dropped = sum(n for (exp, lab), n in stats.items() if exp == "chase" and lab != "KEEP")
    chases_total = sum(n for (exp, _), n in stats.items() if exp == "chase")

    print("\n=== Targets ===")
    if winners_total:
        print(f"  winners KEEP rate: {winners_kept}/{winners_total} ({100*winners_kept/winners_total:.0f}%) — target >=75%")
    if chases_total:
        print(f"  chases DROP rate:  {chases_dropped}/{chases_total} ({100*chases_dropped/chases_total:.0f}%) — target >=80%")

    return 0


if __name__ == "__main__":
    sys.exit(main())
