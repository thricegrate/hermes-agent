"""ElevenLabs Sound Effects Generation via Python SDK.

Usage:
    python skills/elevenlabs/scripts/sound_effects.py --prompt "rain on a tin roof" [options]

Options:
    --prompt      Description of the sound effect (required)
    --duration    Duration in seconds, 0.5-22 (default: auto)
    --output      Output file path (default: .tmp/sfx_output.mp3)
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Sound Effects")
    parser.add_argument("--prompt", required=True, help="Description of the sound effect")
    parser.add_argument("--duration", type=float, help="Duration in seconds (0.5-22)")
    parser.add_argument("--output", default=".tmp/sfx_output.mp3", help="Output file path")
    args = parser.parse_args()

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not found in environment")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)

    print(f"Generating sound effect: '{args.prompt}'...")

    kwargs = {"text": args.prompt}
    if args.duration:
        kwargs["duration_seconds"] = args.duration

    audio_gen = client.text_to_sound_effects.convert(**kwargs)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        for chunk in audio_gen:
            f.write(chunk)

    size_kb = output_path.stat().st_size / 1024
    print(f"Saved: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
