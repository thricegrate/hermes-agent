"""ElevenLabs Voice Cloning via Python SDK.

Usage:
    python skills/elevenlabs/scripts/voice_clone.py --name "My Voice" --files sample1.mp3 sample2.mp3 [options]

Options:
    --name          Name for the cloned voice (required)
    --files         One or more audio files for cloning (required)
    --description   Voice description
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Voice Cloning")
    parser.add_argument("--name", required=True, help="Name for the cloned voice")
    parser.add_argument("--files", nargs="+", required=True, help="Audio sample files")
    parser.add_argument("--description", default="", help="Voice description")
    args = parser.parse_args()

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not found in environment")
        sys.exit(1)

    for f in args.files:
        if not Path(f).exists():
            print(f"ERROR: File not found: {f}")
            sys.exit(1)

    client = ElevenLabs(api_key=api_key)

    files = []
    for f in args.files:
        p = Path(f)
        files.append(open(p, "rb"))
        print(f"  Sample: {p.name} ({p.stat().st_size / 1024:.1f} KB)")

    print(f"Cloning voice '{args.name}' from {len(files)} sample(s)...")

    voice = client.clone(
        name=args.name,
        description=args.description,
        files=files,
    )

    for f in files:
        f.close()

    print(f"Voice cloned successfully!")
    print(f"  Name: {voice.name}")
    print(f"  ID:   {voice.voice_id}")
    print(f"\nUse this voice with: --voice {voice.voice_id}")


if __name__ == "__main__":
    main()
