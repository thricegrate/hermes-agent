"""Shared Jogg AI API helper. Imported by all jogg-ai scripts."""

import os
import sys
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.jogg.ai/v2"


def get_api_key():
    """Return API key or exit with clear error."""
    api_key = os.getenv("JOGG_AI_API_KEY")
    if not api_key:
        print("ERROR: JOGG_AI_API_KEY not found in environment. Add it to .env", file=sys.stderr)
        sys.exit(1)
    return api_key


def get_headers(api_key=None):
    """Return standard headers for Jogg AI API."""
    if api_key is None:
        api_key = get_api_key()
    return {
        "x-api-key": api_key,
        "Content-Type": "application/json",
    }


def api_get(endpoint, params=None):
    """GET request to Jogg AI API. Returns parsed JSON or exits on error."""
    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.get(url, headers=get_headers(), params=params, timeout=30)
        data = resp.json()
        if data.get("code") not in (0, None):
            print(f"ERROR: API returned code {data['code']}: {data.get('msg', 'Unknown error')}", file=sys.stderr)
            sys.exit(1)
        return data
    except requests.exceptions.RequestException as e:
        print(f"ERROR: API request failed: {e}", file=sys.stderr)
        if hasattr(e, "response") and e.response is not None:
            print(f"  Response: {e.response.text[:500]}", file=sys.stderr)
        sys.exit(1)


def api_post(endpoint, payload=None):
    """POST request to Jogg AI API. Returns parsed JSON or exits on error."""
    url = f"{BASE_URL}{endpoint}"
    try:
        resp = requests.post(url, headers=get_headers(), json=payload, timeout=60)
        data = resp.json()
        if data.get("code") not in (0, None):
            print(f"ERROR: API returned code {data['code']}: {data.get('msg', 'Unknown error')}", file=sys.stderr)
            sys.exit(1)
        return data
    except requests.exceptions.RequestException as e:
        print(f"ERROR: API request failed: {e}", file=sys.stderr)
        if hasattr(e, "response") and e.response is not None:
            print(f"  Response: {e.response.text[:500]}", file=sys.stderr)
        sys.exit(1)


def print_table(headers, rows):
    """Print a formatted table to stdout."""
    if not rows:
        print("(no results)")
        return

    col_widths = []
    for i, h in enumerate(headers):
        max_w = len(str(h))
        for row in rows:
            if i < len(row):
                max_w = max(max_w, len(str(row[i])))
        col_widths.append(min(max_w, 50))

    fmt = "  ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*[str(h) for h in headers]))
    print("-" * (sum(col_widths) + 2 * (len(headers) - 1)))
    for row in rows:
        truncated = [str(v)[:w] for v, w in zip(row, col_widths)]
        while len(truncated) < len(headers):
            truncated.append("")
        print(fmt.format(*truncated))


def poll_status(endpoint, terminal_statuses=("completed", "success", "failed"),
                interval=10, status_field="status"):
    """Poll an endpoint until a terminal status is reached. Returns final response data."""
    print(f"Polling every {interval}s...")
    while True:
        data = api_get(endpoint)
        status = data.get("data", {}).get(status_field, "unknown")
        print(f"  Status: {status}")
        if status in terminal_statuses:
            return data
        time.sleep(interval)


def download_file(url, output_path):
    """Download a file from URL to local path."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, stream=True, timeout=120)
    resp.raise_for_status()
    with open(output, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)
    size_kb = output.stat().st_size / 1024
    print(f"Downloaded: {output} ({size_kb:.1f} KB)")
