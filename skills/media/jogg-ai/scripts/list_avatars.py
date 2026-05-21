"""Browse public avatars from Jogg AI with optional filters."""

import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_get, print_table


def main():
    parser = argparse.ArgumentParser(description="Browse Jogg AI public avatars")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--page-size", type=int, default=20, help="Results per page (default: 20)")
    parser.add_argument("--aspect-ratio", choices=["portrait", "landscape", "square"], help="Filter by aspect ratio")
    parser.add_argument("--style", choices=["professional", "social"], help="Filter by style")
    parser.add_argument("--gender", choices=["female", "male"], help="Filter by gender")
    parser.add_argument("--age", choices=["adult", "senior", "young_adult"], help="Filter by age group")
    parser.add_argument("--scene", choices=["lifestyle", "outdoors", "business", "studio", "health_fitness", "education", "news"], help="Filter by scene")
    parser.add_argument("--ethnicity", choices=["european", "african", "south_asian", "east_asian", "middle_eastern", "south_american", "north_american"], help="Filter by ethnicity")
    args = parser.parse_args()

    params = {"page": args.page, "page_size": args.page_size}
    if args.aspect_ratio:
        params["aspect_ratio"] = args.aspect_ratio
    if args.style:
        params["style"] = args.style
    if args.gender:
        params["gender"] = args.gender
    if args.age:
        params["age"] = args.age
    if args.scene:
        params["scene"] = args.scene
    if args.ethnicity:
        params["ethnicity"] = args.ethnicity

    result = api_get("/avatars/public", params=params)
    avatars = result.get("data", {}).get("avatars", [])

    print(f"Found {len(avatars)} avatars (page {args.page})\n")

    rows = []
    for a in avatars:
        rows.append([
            a.get("id", ""),
            a.get("name", ""),
            a.get("gender", ""),
            a.get("style", ""),
            a.get("age", ""),
        ])

    print_table(["ID", "Name", "Gender", "Style", "Age"], rows)


if __name__ == "__main__":
    main()
