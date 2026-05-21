"""Browse available background music from Jogg AI."""

import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_get, print_table


def main():
    parser = argparse.ArgumentParser(description="Browse Jogg AI background music")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--page-size", type=int, default=20, help="Results per page (default: 20)")
    args = parser.parse_args()

    params = {"page": args.page, "page_size": args.page_size}
    result = api_get("/musics", params=params)
    data = result.get("data", {})
    tracks = data.get("music", [])
    pagination = data.get("pagination", {})
    total = pagination.get("total_items", len(tracks))

    print(f"Found {len(tracks)} music tracks (page {args.page}, {total} total)\n")

    rows = []
    for t in tracks:
        duration = t.get("duration", "")
        if isinstance(duration, (int, float)):
            duration = f"{duration}s"
        rows.append([
            t.get("id", ""),
            t.get("name", ""),
            duration,
        ])

    print_table(["ID", "Name", "Duration"], rows)


if __name__ == "__main__":
    main()
