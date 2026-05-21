"""ElevenLabs Text-to-Speech via Python SDK.

Usage:
    python skills/elevenlabs/scripts/text_to_speech.py --text "Hello world" [options]
    python skills/elevenlabs/scripts/text_to_speech.py --file input.txt [options]

Options:
    --voice       Voice name or ID (default: "Adam" - English male)
    --model       Model ID (default: eleven_multilingual_v2)
    --output      Output file path (default: .tmp/tts_output.mp3)
    --stability   Voice stability 0.0-1.0 (default: 0.5)
    --similarity  Similarity boost 0.0-1.0 (default: 0.75)
    --speed       Speaking speed 0.5-2.0 (default: 1.0)
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Text-to-Speech")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Text to convert to speech")
    group.add_argument("--file", help="Path to text file to convert")
    parser.add_argument("--voice", default="Adam", help="Voice name or ID")
    parser.add_argument("--model", default="eleven_multilingual_v2", help="Model ID")
    parser.add_argument("--output", default=".tmp/tts_output.mp3", help="Output file path")
    parser.add_argument("--stability", type=float, default=0.5, help="Voice stability (0.0-1.0)")
    parser.add_argument("--similarity", type=float, default=0.75, help="Similarity boost (0.0-1.0)")
    parser.add_argument("--speed", type=float, default=1.0, help="Speaking speed (0.5-2.0)")
    args = parser.parse_args()

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not found in environment")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)

    text = args.text
    if args.file:
        text = Path(args.file).read_text(encoding="utf-8")

    if not text.strip():
        print("ERROR: No text provided")
        sys.exit(1)

    # Resolve voice name to ID if needed
    voice_id = args.voice
    if len(voice_id) < 20:
        voices = client.voices.get_all()
        search = voice_id.lower()
        # Match by exact name or by first word of name (e.g. "Adam" matches "Adam - Dominant, Firm")
        match = next(
            (v for v in voices.voices
             if v.name.lower() == search or v.name.lower().split(" - ")[0].strip() == search),
            None,
        )
        if match:
            voice_id = match.voice_id
            print(f"Resolved voice '{args.voice}' -> {match.name} ({voice_id})")
        else:
            print(f"ERROR: Voice '{args.voice}' not found. Available voices:")
            for v in voices.voices:
                print(f"  {v.voice_id}  {v.name}")
            sys.exit(1)

    print(f"Generating speech ({len(text)} chars, voice={args.voice}, model={args.model})...")

    audio_gen = client.text_to_speech.convert(
        text=text,
        voice_id=voice_id,
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
