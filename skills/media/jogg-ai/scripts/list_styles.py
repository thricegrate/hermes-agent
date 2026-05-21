"""Browse available visual styles from Jogg AI."""

import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_get, print_table


def main():
    parser = argparse.ArgumentParser(description="Browse Jogg AI visual styles for product videos")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--page-size", type=int, default=50, help="Results per page (default: 50)")
    parser.add_argument("--aspect-ratio", choices=["portrait", "landscape", "square"],
                        help="Filter by aspect ratio")
    args = parser.parse_args()

    params = {"page": args.page, "page_size": args.page_size}
    if args.aspect_ratio:
        params["aspect_ratio"] = args.aspect_ratio

    result = api_get("/visual_styles", params=params)
    styles = result.get("data", {}).get("visual_styles", [])

    print(f"Found {len(styles)} visual styles\n")

    rows = []
    for s in styles:
        rows.append([
            s.get("id", ""),
            s.get("name", ""),
        ])

    print_table(["ID", "Name"], rows)


if __name__ == "__main__":
    main()
