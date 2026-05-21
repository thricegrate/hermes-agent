"""ElevenLabs Audio Isolation (vocal/background separation) via Python SDK.

Usage:
    python skills/elevenlabs/scripts/isolate_audio.py --input recording.mp3 [--output .tmp/clean.mp3]
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Audio Isolation")
    parser.add_argument("--input", required=True, help="Input audio file")
    parser.add_argument("--output", default=".tmp/isolated_output.mp3", help="Output file path")
    args = parser.parse_args()

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not found in environment")
        sys.exit(1)

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)

    print(f"Isolating audio from: {input_path} ({input_path.stat().st_size / 1024:.1f} KB)...")

    with open(input_path, "rb") as audio_file:
        audio_gen = client.audio_isolation.audio_isolation(audio=audio_file)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        for chunk in audio_gen:
            f.write(chunk)

    size_kb = output_path.stat().st_size / 1024
    print(f"Saved: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
