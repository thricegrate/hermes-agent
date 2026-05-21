#!/usr/bin/env python3
"""Detect speech segments using Silero neural VAD.

Alternative to refine_edl.py's ffmpeg silencedetect approach. More accurate for
speech detection but requires torch. Outputs the same EDL JSON format used by
the rest of the video-editor pipeline.

Usage:
    python3 detect_speech_silero.py input.mp4 -o edl.json

Requires: pip install torch
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time


def extract_audio(input_path: str, output_path: str, sample_rate: int = 16000):
    """Extract audio from video as WAV for VAD processing."""
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-vn", "-ar", str(sample_rate), "-ac", "1",
        "-acodec", "pcm_s16le",
        "-loglevel", "error", output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error extracting audio: {result.stderr}", file=sys.stderr)
        sys.exit(1)


def get_duration(input_path: str) -> float:
    """Get video duration in seconds."""
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", input_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())


def get_speech_timestamps_silero(
    audio_path: str,
    min_speech_duration: float = 0.25,
    min_silence_duration: float = 0.5,
    speech_pad_ms: int = 100,
) -> list[tuple[float, float]]:
    """Use Silero VAD to detect speech segments.

    Returns list of (start_sec, end_sec) tuples.
    """
    import torch

    model, utils = torch.hub.load(
        repo_or_dir='snakers4/silero-vad',
        model='silero_vad',
        force_reload=False,
        trust_repo=True
    )

    (get_speech_timestamps, save_audio, read_audio, VADIterator, collect_chunks) = utils

    SAMPLE_RATE = 16000
    wav = read_audio(audio_path, sampling_rate=SAMPLE_RATE)

    speech_timestamps = get_speech_timestamps(
        wav,
        model,
        sampling_rate=SAMPLE_RATE,
        threshold=0.5,
        min_speech_duration_ms=int(min_speech_duration * 1000),
        min_silence_duration_ms=int(min_silence_duration * 1000),
        speech_pad_ms=speech_pad_ms,
    )

    segments = []
    for ts in speech_timestamps:
        start_sec = ts['start'] / SAMPLE_RATE
        end_sec = ts['end'] / SAMPLE_RATE
        segments.append((start_sec, end_sec))

    return segments


def merge_close_segments(segments: list, max_gap: float) -> list:
    """Merge segments that are very close together."""
    if not segments:
        return []

    merged = [segments[0]]
    for start, end in segments[1:]:
        prev_start, prev_end = merged[-1]
        if start - prev_end <= max_gap:
            merged[-1] = (prev_start, end)
        else:
            merged.append((start, end))

    return merged


def add_padding(segments: list, padding_s: float, duration: float) -> list:
    """Add padding around segments and merge overlaps."""
    if not segments:
        return []

    padded = []
    for start, end in segments:
        new_start = max(0, start - padding_s)
        new_end = min(duration, end + padding_s)
        padded.append((new_start, new_end))

    merged = [padded[0]]
    for start, end in padded[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))

    return merged


def segments_to_edl(segments: list[tuple[float, float]]) -> dict:
    """Convert (start_sec, end_sec) tuples to EDL JSON format."""
    return {
        "segments": [
            {"start_ms": int(start * 1000), "end_ms": int(end * 1000)}
            for start, end in segments
        ]
    }


def main():
    parser = argparse.ArgumentParser(
        description="Detect speech segments using Silero neural VAD"
    )
    parser.add_argument("input", help="Input video file")
    parser.add_argument("-o", "--output", help="Output EDL JSON (default: <basename>_vad_edl.json)")
    parser.add_argument("--min-silence", type=float, default=0.5,
                        help="Minimum silence duration to cut (default: 0.5s)")
    parser.add_argument("--min-speech", type=float, default=0.25,
                        help="Minimum speech duration to keep (default: 0.25s)")
    parser.add_argument("--padding", type=int, default=100,
                        help="Padding around speech in ms (default: 100)")
    parser.add_argument("--merge-gap", type=float, default=0.3,
                        help="Merge segments closer than this (default: 0.3s)")
    parser.add_argument("--keep-start", action="store_true", default=True,
                        help="Always start from 0:00 (default: True)")
    parser.add_argument("--no-keep-start", action="store_false", dest="keep_start")

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output or os.path.splitext(input_path)[0] + "_vad_edl.json"

    print(f"Silero VAD Speech Detection")
    print(f"  Input: {input_path}")
    print(f"  Output: {output_path}")
    print()

    overall_start = time.time()

    duration = get_duration(input_path)
    print(f"Video duration: {duration:.2f}s ({duration/60:.1f} min)")

    # Extract audio for VAD
    print(f"Extracting audio...")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        audio_path = tmp.name

    speech_segments = []
    try:
        extract_audio(input_path, audio_path)

        print(f"Running Silero VAD...")
        speech_segments = get_speech_timestamps_silero(
            audio_path,
            min_speech_duration=args.min_speech,
            min_silence_duration=args.min_silence,
            speech_pad_ms=args.padding,
        )
        print(f"  Found {len(speech_segments)} speech segments")

        for i, (start, end) in enumerate(speech_segments[:5]):
            print(f"    {i+1}. {start:.2f}s - {end:.2f}s ({end-start:.2f}s)")
        if len(speech_segments) > 5:
            print(f"    ... and {len(speech_segments) - 5} more")

    finally:
        if os.path.exists(audio_path):
            os.remove(audio_path)

    if not speech_segments:
        print("No speech detected!")
        sys.exit(1)

    # Merge close segments (Silero already applies speech_pad_ms padding,
    # so we only merge close segments here -- no additional padding needed)
    speech_segments = merge_close_segments(speech_segments, args.merge_gap)
    print(f"After merging: {len(speech_segments)} segments")

    # Keep start
    if args.keep_start and speech_segments and speech_segments[0][0] > 0:
        first_start, first_end = speech_segments[0]
        speech_segments[0] = (0.0, first_end)
        print(f"Extended first segment to start at 0:00")

    # Calculate expected output duration
    total_speech = sum(end - start for start, end in speech_segments)
    removed = duration - total_speech
    print(f"Expected output: {total_speech:.1f}s ({total_speech/60:.1f} min)")
    print(f"Removing: {removed:.1f}s ({100*removed/duration:.1f}%)")

    # Write EDL JSON
    edl = segments_to_edl(speech_segments)
    with open(output_path, "w") as f:
        json.dump(edl, f, indent=2)

    overall_time = time.time() - overall_start
    print(f"\nEDL written to: {output_path}")
    print(f"  {len(edl['segments'])} segments")
    print(f"  Total time: {overall_time:.1f}s")


if __name__ == "__main__":
    main()
