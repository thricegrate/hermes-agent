"""Create a product entry in Jogg AI from a URL or manual details."""

import argparse
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_post


def main():
    parser = argparse.ArgumentParser(description="Create Jogg AI product entry")

    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--url", help="Product page URL (Jogg AI will crawl it)")
    source_group.add_argument("--name", help="Product name (for manual entry)")

    parser.add_argument("--description", help="Product description and selling points")
    parser.add_argument("--target-audience", help="Target audience description")
    parser.add_argument("--media", nargs="+", help="Media URLs (images/videos) to attach")
    args = parser.parse_args()

    payload = {}
    if args.url:
        payload["url"] = args.url
    if args.name:
        payload["name"] = args.name
    if args.description:
        payload["description"] = args.description
    if args.target_audience:
        payload["target_audience"] = args.target_audience
    if args.media:
        payload["media"] = [{"type": 1, "url": url} for url in args.media]

    source = args.url or args.name
    print(f"Creating product entry: {source}")
    result = api_post("/product", payload)

    data = result.get("data", {})
    product_id = data.get("product_id")

    if not product_id:
        print("ERROR: No product_id returned", file=sys.stderr)
        print(f"Response: {result}", file=sys.stderr)
        sys.exit(1)

    print(f"Product ID: {product_id}")
    print(f"Name: {data.get('name', 'N/A')}")
    if data.get("description"):
        print(f"Description: {data['description'][:200]}")
    if data.get("media"):
        print(f"Media files: {len(data['media'])}")

    print(f"\nUse with: python skills/jogg-ai/scripts/create_product_video.py --product-id {product_id}")


if __name__ == "__main__":
    main()
