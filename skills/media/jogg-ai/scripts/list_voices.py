"""Browse available voices from Jogg AI with optional filters."""

import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_get, print_table


def main():
    parser = argparse.ArgumentParser(description="Browse Jogg AI voices")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument("--page-size", type=int, default=20, help="Results per page (default: 20)")
    parser.add_argument("--gender", choices=["female", "male"], help="Filter by gender")
    parser.add_argument("--language", help="Filter by language (e.g. english, spanish)")
    parser.add_argument("--age", choices=["young", "middle_aged", "old"], help="Filter by age group")
    parser.add_argument("--use-case", help="Filter by use case (e.g. narrative_story)")
    args = parser.parse_args()

    params = {"page": args.page, "page_size": args.page_size}
    if args.gender:
        params["gender"] = args.gender
    if args.language:
        params["language"] = args.language
    if args.age:
        params["age"] = args.age
    if args.use_case:
        params["use_case"] = args.use_case

    result = api_get("/voices", params=params)
    voices = result.get("data", {}).get("voices", [])
    has_more = result.get("data", {}).get("has_more", False)

    print(f"Found {len(voices)} voices (page {args.page}){' - more available' if has_more else ''}\n")

    rows = []
    for v in voices:
        rows.append([
            v.get("voice_id", ""),
            v.get("name", ""),
            v.get("gender", ""),
            v.get("language", ""),
            v.get("age", ""),
            v.get("use_case", ""),
        ])

    print_table(["Voice ID", "Name", "Gender", "Language", "Age", "Use Case"], rows)


if __name__ == "__main__":
    main()
