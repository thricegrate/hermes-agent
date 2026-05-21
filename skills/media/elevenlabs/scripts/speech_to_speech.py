"""ElevenLabs Speech-to-Speech voice conversion via Python SDK.

Usage:
    python skills/elevenlabs/scripts/speech_to_speech.py --input source.mp3 --voice "Brian" [options]

Options:
    --input       Source audio file (required)
    --voice       Target voice name or ID (required)
    --model       Model ID (default: eleven_english_sts_v2)
    --output      Output file path (default: .tmp/sts_output.mp3)
    --stability   Voice stability 0.0-1.0 (default: 0.5)
    --similarity  Similarity boost 0.0-1.0 (default: 0.75)
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def resolve_voice(client, name_or_id):
    if len(name_or_id) >= 20:
        return name_or_id
    voices = client.voices.get_all()
    search = name_or_id.lower()
    match = next(
        (v for v in voices.voices
         if v.name.lower() == search or v.name.lower().split(" - ")[0].strip() == search),
        None,
    )
    if match:
        print(f"Resolved voice '{name_or_id}' -> {match.name} ({match.voice_id})")
        return match.voice_id
    print(f"ERROR: Voice '{name_or_id}' not found.")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Speech-to-Speech")
    parser.add_argument("--input", required=True, help="Source audio file")
    parser.add_argument("--voice", required=True, help="Target voice name or ID")
    parser.add_argument("--model", default="eleven_english_sts_v2", help="Model ID")
    parser.add_argument("--output", default=".tmp/sts_output.mp3", help="Output file path")
    parser.add_argument("--stability", type=float, default=0.5, help="Voice stability (0.0-1.0)")
    parser.add_argument("--similarity", type=float, default=0.75, help="Similarity boost (0.0-1.0)")
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
    voice_id = resolve_voice(client, args.voice)

    print(f"Converting voice: {input_path} -> {args.voice} (model={args.model})...")

    with open(input_path, "rb") as audio_file:
        audio_gen = client.speech_to_speech.convert(
            voice_id=voice_id,
            audio=audio_file,
            model_id=args.model,
            voice_settings={
                "stability": args.stability,
                "similarity_boost": args.similarity,
            },
        )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "wb") as f:
        for chunk in audio_gen:
            f.write(chunk)

    size_kb = output_path.stat().st_size / 1024
    print(f"Saved: {output_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
