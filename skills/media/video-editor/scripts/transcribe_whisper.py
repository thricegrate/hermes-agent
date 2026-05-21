#!/usr/bin/env python3
"""Local transcription using faster-whisper (no API key needed).

Uses the Whisper "base" model with int8 quantization for CPU-friendly performance.
Outputs the same AssemblyAI-compatible JSON format as the other transcription providers.

Usage:
    python3 transcribe_whisper.py input.mp4
    python3 transcribe_whisper.py input.mp4 -o transcript.json --model small

Requires: pip install faster-whisper
"""

import argparse
import json
import os
import sys
import time


def transcribe(
    input_path: str,
    model_name: str = "base",
    compute_type: str = "int8",
    device: str = "cpu",
) -> dict:
    """Transcribe video using faster-whisper.

    Returns AssemblyAI-compatible JSON:
        {"words": [{"text": "word", "start": 1234, "end": 5678, "confidence": 0.99}, ...]}
    Timestamps are in milliseconds.
    """
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        print("Error: faster-whisper not installed. Run: pip install faster-whisper",
              file=sys.stderr)
        sys.exit(1)

    print(f"Loading Whisper model '{model_name}' ({compute_type})...")
    start_time = time.time()

    model = WhisperModel(model_name, device=device, compute_type=compute_type)

    print(f"Transcribing {input_path}...")
    segments, info = model.transcribe(input_path, word_timestamps=True)

    words = []
    for segment in segments:
        if segment.words:
            for w in segment.words:
                words.append({
                    "text": w.word.strip(),
                    "start": int(w.start * 1000),
                    "end": int(w.end * 1000),
                    "confidence": round(w.probability, 4) if hasattr(w, 'probability') else 0.95,
                })

    elapsed = time.time() - start_time
    print(f"Transcription complete: {len(words)} words in {elapsed:.1f}s")
    print(f"Detected language: {info.language} (probability {info.language_probability:.2f})")

    return {"words": words}


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe video locally using Whisper (no API key needed)"
    )
    parser.add_argument("input", help="Input video/audio file")
    parser.add_argument("-o", "--output",
                        help="Output JSON path (default: <basename>_transcript.json)")
    parser.add_argument("--model", default="base",
                        help="Whisper model size: tiny, base, small, medium, large-v3 (default: base)")
    parser.add_argument("--compute-type", default="int8",
                        help="Compute type: int8, float16, float32 (default: int8)")
    parser.add_argument("--device", default="cpu",
                        help="Device: cpu, cuda (default: cpu)")
    args = parser.parse_args()

    output_path = args.output or os.path.splitext(args.input)[0] + "_transcript.json"

    result = transcribe(
        args.input,
        model_name=args.model,
        compute_type=args.compute_type,
        device=args.device,
    )

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"Transcript saved to: {output_path}")
    print(f"  {len(result['words'])} words")
    if result['words']:
        duration_ms = result['words'][-1]['end']
        print(f"  Duration: {duration_ms/1000:.1f}s ({duration_ms/60000:.1f}min)")


if __name__ == "__main__":
    main()
