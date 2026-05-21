"""List all available ElevenLabs voices.

Usage:
    python skills/elevenlabs/scripts/list_voices.py [--gender male|female|neutral] [--accent american|british|...]
"""

import argparse
import os
import sys
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    parser = argparse.ArgumentParser(description="List ElevenLabs voices")
    parser.add_argument("--gender", help="Filter by gender (male, female, neutral)")
    parser.add_argument("--accent", help="Filter by accent (american, british, australian, ...)")
    args = parser.parse_args()

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not found in environment")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)
    voices = client.voices.get_all()

    results = []
    for v in voices.voices:
        labels = v.labels or {}
        gender = labels.get("gender", "unknown")
        accent = labels.get("accent", "unknown")

        if args.gender and gender.lower() != args.gender.lower():
            continue
        if args.accent and accent.lower() != args.accent.lower():
            continue

        results.append((v.voice_id, v.name, gender, accent))

    print(f"Found {len(results)} voices:")
    print(f"{'ID':24s}  {'Name':40s}  {'Gender':10s}  Accent")
    print("-" * 100)
    for vid, name, gender, accent in results:
        print(f"{vid:24s}  {name:40s}  {gender:10s}  {accent}")


if __name__ == "__main__":
    main()
