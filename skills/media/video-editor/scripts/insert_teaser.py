#!/usr/bin/env python3
"""Insert a 3D swivel teaser into a video.

Inserts a fast-forward preview of future video content with 3D rotation effects
at a specified point. Original audio continues playing throughout.

Timeline Result:
    Video: [0-3s original] [3-8s swivel teaser] [8s+ original]
    Audio: [original audio plays continuously throughout]

Usage:
    python3 insert_teaser.py input.mp4 output.mp4
    python3 insert_teaser.py input.mp4 output.mp4 --bg-image bg.png

Requires: Node.js + Remotion (npm install in video_effects/)
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Import encoder detection from shared module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from encoder_utils import get_encoder_cmd, detect_encoder

DEFAULT_INSERT_AT = 3.0
DEFAULT_DURATION = 5.0
DEFAULT_TEASER_START = 60.0
MAX_PLAYBACK_RATE = 100.0
TARGET_FPS = 30

# Path to video_effects Remotion project
VIDEO_EFFECTS_DIR = Path(SCRIPT_DIR) / "video_effects"


def get_video_info(input_path: str) -> dict:
    """Get video information using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-select_streams", "v:0",
        "-show_entries", "stream=width,height,r_frame_rate,duration",
        "-show_entries", "format=duration",
        "-of", "json", input_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    data = json.loads(result.stdout)

    stream = data.get("streams", [{}])[0]
    format_data = data.get("format", {})

    fps_str = stream.get("r_frame_rate", "30/1")
    if "/" in fps_str:
        num, den = fps_str.split("/")
        fps = float(num) / float(den)
    else:
        fps = float(fps_str)

    duration = float(stream.get("duration") or format_data.get("duration", 0))

    return {
        "width": int(stream.get("width", 1920)),
        "height": int(stream.get("height", 1080)),
        "fps": fps,
        "duration": duration
    }


def create_transition(
    input_path: str,
    output_path: str,
    start: float,
    source_duration: float,
    output_duration: float,
    playback_rate: float,
    bg_color: str = "#2d3436",
    bg_image: str = None,
) -> None:
    """Create 3D swivel transition using Remotion.

    Extracts frames from video, renders with 3D rotation effect.
    """
    if not VIDEO_EFFECTS_DIR.exists():
        print(f"Error: Remotion project not found at {VIDEO_EFFECTS_DIR}", file=sys.stderr)
        print(f"Run: cd {VIDEO_EFFECTS_DIR} && npm install", file=sys.stderr)
        sys.exit(1)

    info = get_video_info(input_path)
    width, height = info["width"], info["height"]

    # Remotion expects 60fps
    REMOTION_FPS = 60
    frame_count = int(output_duration * REMOTION_FPS)
    print(f"  Extracting {frame_count} frames...")

    # Setup public/frames directory
    frames_dir = VIDEO_EFFECTS_DIR / "public" / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    # Clear old frames
    for f in frames_dir.glob("frame_*.jpg"):
        f.unlink()

    # Extract frames at playback_rate speed
    frame_interval = source_duration / frame_count

    cmd = [
        "ffmpeg", "-y",
        "-ss", str(start),
        "-i", input_path,
        "-vf", f"fps={1/frame_interval}",
        "-vframes", str(frame_count),
        "-q:v", "2",
        "-loglevel", "error",
        str(frames_dir / "frame_%04d.jpg")
    ]
    subprocess.run(cmd, check=True)

    # Copy background image if provided
    bg_dest = frames_dir / "bg_image.png"
    if bg_image and os.path.exists(bg_image):
        shutil.copy(bg_image, bg_dest)
    else:
        # Create solid color background
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi", "-i", f"color=c={bg_color.replace('#', '0x')}:s={width}x{height}:d=1",
            "-vframes", "1",
            "-loglevel", "error",
            str(bg_dest)
        ]
        subprocess.run(cmd, check=True)

    # Render with Remotion
    print(f"  Rendering 3D transition with Remotion...")

    # Use npx.cmd on Windows
    npx_cmd = "npx.cmd" if sys.platform == "win32" else "npx"

    cmd = [
        npx_cmd, "remotion", "render",
        "src/dynamic-index.ts", "Pan3D",
        output_path,
        "--props", json.dumps({"frameCount": frame_count, "playbackRate": playback_rate}),
        "--concurrency", "4",
        "--log", "error"
    ]
    subprocess.run(cmd, cwd=str(VIDEO_EFFECTS_DIR), check=True)

    print(f"  Rendered transition")


def composite_with_transition(
    input_path: str,
    output_path: str,
    insert_at: float = DEFAULT_INSERT_AT,
    duration: float = DEFAULT_DURATION,
    teaser_start: float = DEFAULT_TEASER_START,
    bg_color: str = "#2d3436",
    bg_image: str = None,
) -> None:
    """Insert a swivel teaser into video while preserving original audio."""
    info = get_video_info(input_path)
    total_duration = info["duration"]

    if teaser_start >= total_duration:
        print(f"Error: Teaser start ({teaser_start}s) >= video duration ({total_duration}s)",
              file=sys.stderr)
        sys.exit(1)

    available_content = total_duration - teaser_start
    uncapped_rate = available_content / duration

    if uncapped_rate > MAX_PLAYBACK_RATE:
        playback_rate = MAX_PLAYBACK_RATE
        teaser_content = duration * MAX_PLAYBACK_RATE
        print(f"  Capping speed at {MAX_PLAYBACK_RATE}x (would have been {uncapped_rate:.1f}x)")
    else:
        playback_rate = uncapped_rate
        teaser_content = available_content

    print(f"Insert Swivel Teaser")
    print(f"  Input: {input_path}")
    print(f"  Insert at: {insert_at}s")
    print(f"  Teaser duration: {duration}s")
    print(f"  Content: {teaser_start}s -> {total_duration:.1f}s ({teaser_content:.1f}s at {playback_rate:.1f}x)")
    print()

    if insert_at + duration > total_duration:
        print(f"Error: Insert + duration ({insert_at + duration}s) > video duration ({total_duration}s)",
              file=sys.stderr)
        sys.exit(1)

    encoder_cmd = get_encoder_cmd()
    encoder_name, _ = detect_encoder()
    print(f"  Encoder: {encoder_name}")

    with tempfile.TemporaryDirectory() as tmpdir:
        transition_path = os.path.join(tmpdir, "transition.mp4")
        print(f"Generating swivel teaser...")

        create_transition(
            input_path=input_path,
            output_path=transition_path,
            start=teaser_start,
            source_duration=teaser_content,
            output_duration=duration,
            playback_rate=playback_rate,
            bg_color=bg_color,
            bg_image=bg_image,
        )

        print(f"\nExtracting video segments...")

        # Segment 1: 0 to insert_at
        seg1_path = os.path.join(tmpdir, "seg1.mp4")
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-t", str(insert_at),
            "-an",
        ] + encoder_cmd + ["-loglevel", "error", seg1_path]
        subprocess.run(cmd, check=True)
        print(f"  Segment 1: 0s - {insert_at}s")

        # Segment 2: transition
        seg2_path = os.path.join(tmpdir, "seg2.mp4")
        cmd = [
            "ffmpeg", "-y", "-i", transition_path,
            "-an",
        ] + encoder_cmd + ["-loglevel", "error", seg2_path]
        subprocess.run(cmd, check=True)
        print(f"  Segment 2: transition ({duration}s)")

        # Segment 3: insert_at + duration to end
        seg3_path = os.path.join(tmpdir, "seg3.mp4")
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-ss", str(insert_at + duration),
            "-an",
        ] + encoder_cmd + ["-loglevel", "error", seg3_path]
        subprocess.run(cmd, check=True)
        remaining = total_duration - (insert_at + duration)
        print(f"  Segment 3: {insert_at + duration}s - end ({remaining:.1f}s)")

        # Concatenate video segments
        print(f"\nConcatenating video segments...")
        concat_video_path = os.path.join(tmpdir, "concat_video.mp4")

        concat_list = os.path.join(tmpdir, "concat.txt")
        with open(concat_list, "w") as f:
            for p in [seg1_path, seg2_path, seg3_path]:
                f.write(f"file '{p.replace(os.sep, '/')}'\n")

        cmd = [
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", concat_list,
            "-c", "copy",
            "-loglevel", "error",
            concat_video_path
        ]
        subprocess.run(cmd, check=True)

        # Extract original audio
        print(f"Extracting original audio...")
        audio_path = os.path.join(tmpdir, "audio.aac")
        cmd = [
            "ffmpeg", "-y", "-i", input_path,
            "-vn", "-c:a", "aac", "-b:a", "192k",
            "-loglevel", "error",
            audio_path
        ]
        subprocess.run(cmd, check=True)

        # Merge video and audio
        print(f"Merging video and audio...")
        cmd = [
            "ffmpeg", "-y",
            "-i", concat_video_path,
            "-i", audio_path,
            "-c:v", "copy",
            "-c:a", "copy",
            "-shortest",
            "-loglevel", "error",
            output_path
        ]
        subprocess.run(cmd, check=True)

    print(f"\nOutput saved to {output_path}")
    print(f"  Timeline: [0-{insert_at}s] [swivel teaser {duration}s] [{insert_at+duration}s-end]")
    print(f"  Audio: Original audio preserved throughout")


def main():
    parser = argparse.ArgumentParser(
        description="Insert 3D swivel teaser into video while preserving audio"
    )
    parser.add_argument("input", help="Input video file")
    parser.add_argument("output", help="Output video file")
    parser.add_argument("--insert-at", type=float, default=DEFAULT_INSERT_AT,
                        help=f"Insert point in seconds (default: {DEFAULT_INSERT_AT})")
    parser.add_argument("--duration", type=float, default=DEFAULT_DURATION,
                        help=f"Transition duration in seconds (default: {DEFAULT_DURATION})")
    parser.add_argument("--teaser-start", type=float, default=DEFAULT_TEASER_START,
                        help=f"Where to start sourcing teaser content (default: {DEFAULT_TEASER_START}s)")
    parser.add_argument("--bg-color", type=str, default="#2d3436",
                        help="Background color (hex, default: #2d3436)")
    parser.add_argument("--bg-image", type=str, default=None,
                        help="Background image path")

    args = parser.parse_args()

    composite_with_transition(
        input_path=args.input,
        output_path=args.output,
        insert_at=args.insert_at,
        duration=args.duration,
        teaser_start=args.teaser_start,
        bg_color=args.bg_color,
        bg_image=args.bg_image,
    )


if __name__ == "__main__":
    main()
