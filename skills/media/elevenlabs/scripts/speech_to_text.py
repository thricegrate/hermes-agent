"""ElevenLabs Speech-to-Text transcription via Python SDK.

Usage:
    python skills/elevenlabs/scripts/speech_to_text.py --input audio.mp3 [options]

Options:
    --model       Model ID (default: scribe_v1)
    --output      Output text file path (default: prints to stdout)
    --diarize     Enable speaker diarization (default: false)
    --language     Language code, e.g. "en" (default: auto-detect)
"""

import argparse
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    parser = argparse.ArgumentParser(description="ElevenLabs Speech-to-Text")
    parser.add_argument("--input", required=True, help="Path to audio file")
    parser.add_argument("--model", default="scribe_v1", help="Model ID")
    parser.add_argument("--output", help="Output text file path (default: stdout)")
    parser.add_argument("--diarize", action="store_true", help="Enable speaker diarization")
    parser.add_argument("--language", help="Language code (default: auto-detect)")
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

    print(f"Transcribing: {input_path} ({input_path.stat().st_size / 1024:.1f} KB)...")

    with open(input_path, "rb") as audio_file:
        result = client.speech_to_text.convert(
            file=audio_file,
            model_id=args.model,
            tag_audio_events=True,
            diarize=args.diarize,
            **({"language_code": args.language} if args.language else {}),
        )

    text = result.text
    if args.diarize and hasattr(result, "words"):
        lines = []
        current_speaker = None
        current_line = []
        for w in result.words:
            speaker = getattr(w, "speaker_id", None)
            if speaker != current_speaker and current_line:
                prefix = f"[Speaker {current_speaker}] " if current_speaker else ""
                lines.append(prefix + " ".join(current_line))
                current_line = []
            current_speaker = speaker
            current_line.append(w.text)
        if current_line:
            prefix = f"[Speaker {current_speaker}] " if current_speaker else ""
            lines.append(prefix + " ".join(current_line))
        text = "\n".join(lines)

    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text, encoding="utf-8")
        print(f"Saved transcript: {out}")
    else:
        print("\n--- Transcript ---")
        print(text)

    lang = getattr(result, "language_code", "unknown")
    print(f"\nLanguage detected: {lang}")


if __name__ == "__main__":
    main()
