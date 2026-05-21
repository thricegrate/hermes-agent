#!/usr/bin/env python3
"""Generate YouTube metadata (summary + chapters) using Claude.

Reads a formatted transcript and EDL to generate a YouTube summary and
chapter timestamps adjusted for removed content.

Usage:
    python3 generate_metadata.py transcript.txt --edl edl.json --title "My Video"
    python3 generate_metadata.py transcript.txt --title "My Video" --no-chapters

Requires: pip install anthropic
          ANTHROPIC_API_KEY env var
"""

import argparse
import json
import os
import re
import sys

try:
    import anthropic
except ImportError:
    anthropic = None

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def parse_formatted_transcript(transcript_path: str) -> list[dict]:
    """Parse a formatted transcript file into timestamped chunks.

    Expected format (from format_transcript.py):
        [00:08.16 - 00:12.34] Text here...
    """
    chunks = []
    with open(transcript_path) as f:
        for line in f:
            line = line.strip()
            match = re.match(
                r'\[(\d+:\d+\.\d+)\s*-\s*(\d+:\d+\.\d+)\]\s*(.*)', line
            )
            if match:
                start_str, end_str, text = match.groups()
                start = parse_timestamp(start_str)
                end = parse_timestamp(end_str)
                chunks.append({"start": start, "end": end, "text": text})
    return chunks


def parse_timestamp(ts: str) -> float:
    """Parse MM:SS.ms or HH:MM:SS.ms to seconds."""
    parts = ts.split(":")
    if len(parts) == 2:
        return float(parts[0]) * 60 + float(parts[1])
    elif len(parts) == 3:
        return float(parts[0]) * 3600 + float(parts[1]) * 60 + float(parts[2])
    return 0.0


def load_edl_cuts(edl_path: str, original_duration: float) -> list[tuple[float, float]]:
    """Load EDL and compute the cut regions (gaps between keep-segments)."""
    with open(edl_path) as f:
        edl = json.load(f)

    segments = edl["segments"]
    if not segments:
        return []

    cuts = []
    prev_end = 0.0
    for seg in segments:
        start = seg["start_ms"] / 1000.0
        if start > prev_end:
            cuts.append((prev_end, start))
        prev_end = seg["end_ms"] / 1000.0

    if prev_end < original_duration:
        cuts.append((prev_end, original_duration))

    return cuts


def adjust_timestamp(original_time: float, cuts: list[tuple[float, float]]) -> float:
    """Adjust a timestamp by subtracting removed content before it."""
    time_removed = 0.0
    for cut_start, cut_end in cuts:
        if cut_end <= original_time:
            time_removed += cut_end - cut_start
        elif cut_start < original_time:
            time_removed += original_time - cut_start
    return max(0.0, original_time - time_removed)


def format_timestamp(seconds: float) -> str:
    """Format seconds as HH:MM:SS."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def generate_metadata(
    chunks: list[dict],
    cuts: list[tuple[float, float]],
    title: str,
    duration: float,
    model: str = "claude-sonnet-4-6",
) -> dict:
    """Generate YouTube summary and chapters using Claude."""
    if anthropic is None:
        print("Error: anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
        sys.exit(1)

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Build transcript with timestamps in ~30s chunks
    grouped = []
    current_text = []
    chunk_start = chunks[0]["start"] if chunks else 0
    for c in chunks:
        current_text.append(c["text"])
        if c["end"] - chunk_start >= 30:
            grouped.append({
                "start": chunk_start,
                "end": c["end"],
                "text": " ".join(current_text)
            })
            chunk_start = c["end"]
            current_text = []
    if current_text:
        grouped.append({
            "start": chunk_start,
            "end": chunks[-1]["end"],
            "text": " ".join(current_text)
        })

    transcript_with_times = "\n".join(
        f"[{g['start']:.0f}s - {g['end']:.0f}s]: {g['text']}"
        for g in grouped
    )

    prompt = f"""Analyze this video transcript and generate:
1. A summary for the YouTube description
2. YouTube chapters with timestamps

TRANSCRIPT (with timestamps in seconds):
{transcript_with_times}

VIDEO DURATION: {duration:.0f} seconds ({duration/60:.1f} minutes)

Respond in this exact JSON format:
{{
    "summary": "<2-4 sentence summary describing what the video covers. Write in third person ('This video covers...'). Be specific about the content.>",
    "chapters": [
        {{"time": "00:00:00", "title": "Introduction"}},
        {{"time": "00:02:30", "title": "Topic Title Here"}}
    ]
}}

Chapter guidelines:
- Generate 5-15 chapters marking major topic transitions
- First chapter MUST be at 00:00:00
- Chapters should be 1-2+ minutes apart (except intro/outro)
- Concise titles (2-6 words)

Return ONLY the JSON, no other text."""

    print("Generating metadata with Claude...")
    response = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = response.content[0].text.strip()

    # Parse JSON response
    json_match = re.search(r'\{[\s\S]*\}', response_text)
    if not json_match:
        return {"title": title, "summary": "Video content.", "chapters": "00:00:00 Introduction"}

    try:
        data = json.loads(json_match.group())
        summary = data.get("summary", "Video content.")
        chapters_list = data.get("chapters", [{"time": "00:00:00", "title": "Introduction"}])
    except json.JSONDecodeError:
        return {"title": title, "summary": "Video content.", "chapters": "00:00:00 Introduction"}

    # Adjust chapter timestamps for cuts
    adjusted_chapters = []
    for chapter in chapters_list:
        time_str = chapter.get("time", "00:00:00")
        chapter_title = chapter.get("title", "Chapter")

        # Parse timestamp
        match = re.match(r'^(\d{1,2}):(\d{2}):(\d{2})$', time_str)
        if match:
            hours, minutes, seconds = match.groups()
            original_time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        else:
            match = re.match(r'^(\d{1,2}):(\d{2})$', time_str)
            if match:
                minutes, seconds = match.groups()
                original_time = int(minutes) * 60 + int(seconds)
            else:
                adjusted_chapters.append(f"{time_str} {chapter_title}")
                continue

        adjusted_time = adjust_timestamp(original_time, cuts)
        adjusted_chapters.append(f"{format_timestamp(adjusted_time)} {chapter_title}")

    chapters_text = "\n".join(adjusted_chapters) if adjusted_chapters else "00:00:00 Introduction"

    return {
        "title": title,
        "summary": summary,
        "chapters": chapters_text
    }


def save_metadata(metadata: dict, output_path: str) -> None:
    """Save metadata to a text file."""
    content = f"""TITLE:
{metadata['title']}

SUMMARY:
{metadata['summary']}

CHAPTERS:
{metadata['chapters']}
"""
    with open(output_path, "w") as f:
        f.write(content)
    print(f"Metadata saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate YouTube metadata from transcript")
    parser.add_argument("transcript", help="Path to formatted transcript (.txt from format_transcript.py)")
    parser.add_argument("--title", required=True, help="Video title")
    parser.add_argument("--edl", help="Path to EDL JSON (for chapter time adjustment)")
    parser.add_argument("--duration", type=float, help="Original video duration in seconds (auto-detected from transcript if omitted)")
    parser.add_argument("-o", "--output", help="Output metadata path (default: <basename>_metadata.txt)")
    parser.add_argument("--model", default="claude-sonnet-4-6",
                        help="Claude model to use (default: claude-sonnet-4-6)")
    args = parser.parse_args()

    output_path = args.output or os.path.splitext(args.transcript)[0] + "_metadata.txt"

    # Parse transcript
    chunks = parse_formatted_transcript(args.transcript)
    if not chunks:
        print(f"Error: No timestamped lines found in {args.transcript}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsed {len(chunks)} transcript lines")

    # Duration from arg or transcript
    duration = args.duration or chunks[-1]["end"]

    # Load cuts from EDL if provided
    cuts = []
    if args.edl:
        cuts = load_edl_cuts(args.edl, duration)
        print(f"Loaded {len(cuts)} cut regions from EDL")

    # Generate metadata
    metadata = generate_metadata(chunks, cuts, args.title, duration, model=args.model)
    save_metadata(metadata, output_path)


if __name__ == "__main__":
    main()
