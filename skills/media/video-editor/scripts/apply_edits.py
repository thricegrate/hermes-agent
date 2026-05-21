#!/usr/bin/env python3
"""Apply an edit decision list (EDL) to a video using ffmpeg.

Reads an EDL JSON (list of keep-segments with start_ms/end_ms) and uses ffmpeg
to cut the original MP4 into segments, then concatenate them into the final edit.

Supports two modes:
  - Single-pass (default): Uses ffmpeg trim+concat filter. Faster for many segments.
  - Legacy (--legacy): Cuts each segment individually then concat-copies. Safer fallback.

Also supports:
  - Hardware encoding via encoder_utils (NVIDIA h264_nvenc on Windows)
  - Audio normalization (--normalize): highpass 80Hz + loudnorm
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time

# Import encoder detection from shared module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from encoder_utils import get_encoder_cmd, detect_encoder


def build_trim_concat_filter(segments: list, normalize: bool = False) -> str:
    """Build ffmpeg trim+concat filter for single-pass processing.

    Each segment is trimmed independently, then all are concatenated.
    """
    n = len(segments)
    filter_parts = []

    for i, seg in enumerate(segments):
        start = seg["start_ms"] / 1000.0
        end = seg["end_ms"] / 1000.0
        filter_parts.append(
            f"[0:v]trim=start={start:.6f}:end={end:.6f},setpts=PTS-STARTPTS[v{i}]"
        )

    for i, seg in enumerate(segments):
        start = seg["start_ms"] / 1000.0
        end = seg["end_ms"] / 1000.0
        if normalize:
            filter_parts.append(
                f"[0:a]atrim=start={start:.6f}:end={end:.6f},asetpts=PTS-STARTPTS,"
                f"highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11[a{i}]"
            )
        else:
            filter_parts.append(
                f"[0:a]atrim=start={start:.6f}:end={end:.6f},asetpts=PTS-STARTPTS[a{i}]"
            )

    concat_inputs = "".join(f"[v{i}][a{i}]" for i in range(n))
    filter_parts.append(f"{concat_inputs}concat=n={n}:v=1:a=1[outv][outa]")

    return ";".join(filter_parts)


def apply_edits_singlepass(
    mp4_path: str, edl: dict, output_path: str, normalize: bool = False
) -> None:
    """Single-pass trim+concat. Reads input once, faster for many segments."""
    segments = edl["segments"]
    print(f"Single-pass processing {len(segments)} segments...")
    start_time = time.time()

    filter_complex = build_trim_concat_filter(segments, normalize=normalize)

    # Write filter to temp file (can be very long for many segments)
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(filter_complex)
        filter_script_path = f.name

    try:
        encoder_cmd = get_encoder_cmd()
        encoder_name, _ = detect_encoder()
        print(f"  Encoder: {encoder_name}")

        cmd = [
            "ffmpeg", "-y",
            "-i", mp4_path,
            "-filter_complex_script", filter_script_path,
            "-map", "[outv]", "-map", "[outa]",
        ]
        cmd.extend(encoder_cmd)
        cmd.extend([
            "-c:a", "aac", "-b:a", "192k",
            "-movflags", "+faststart",
            "-loglevel", "error",
            output_path
        ])

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"  ffmpeg error: {result.stderr[:1000]}", file=sys.stderr)
            sys.exit(1)

        elapsed = time.time() - start_time
        print(f"  Done in {elapsed:.1f}s")
    finally:
        if os.path.exists(filter_script_path):
            os.remove(filter_script_path)


def apply_edits_legacy(
    mp4_path: str, edl: dict, output_path: str, temp_dir: str = None
) -> None:
    """Legacy segment-by-segment mode. Cuts each segment then concat-copies."""
    segments = edl["segments"]
    print(f"Legacy mode: cutting {len(segments)} segments individually...")

    encoder_cmd = get_encoder_cmd()
    encoder_name, _ = detect_encoder()
    print(f"  Encoder: {encoder_name}")

    workdir = temp_dir or tempfile.mkdtemp(prefix="video_edit_")
    segment_files = []

    for i, seg in enumerate(segments):
        start_s = seg["start_ms"] / 1000.0
        end_s = seg["end_ms"] / 1000.0
        duration_s = end_s - start_s

        seg_path = os.path.join(workdir, f"seg_{i:04d}.mp4")
        segment_files.append(seg_path)

        cmd = [
            "ffmpeg", "-y",
            "-ss", f"{start_s:.3f}",
            "-i", mp4_path,
            "-t", f"{duration_s:.3f}",
        ]
        cmd.extend(encoder_cmd)
        cmd.extend([
            "-c:a", "aac",
            "-b:a", "192k",
            "-avoid_negative_ts", "make_zero",
            "-movflags", "+faststart",
            seg_path,
        ])

        print(f"  Segment {i + 1}/{len(segments)}: {start_s:.2f}s - {end_s:.2f}s ({duration_s:.2f}s)")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  ffmpeg error on segment {i}: {result.stderr[-500:]}", file=sys.stderr)
            sys.exit(1)

    # Write concat file (use forward slashes for ffmpeg compatibility on Windows)
    concat_path = os.path.join(workdir, "concat.txt")
    with open(concat_path, "w") as f:
        for seg_path in segment_files:
            safe_path = seg_path.replace(os.sep, "/")
            f.write(f"file '{safe_path}'\n")

    # Concatenate all segments
    print(f"\nConcatenating {len(segment_files)} segments...")
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_path,
        "-c", "copy",
        "-movflags", "+faststart",
        output_path,
    ]
    result = subprocess.run(concat_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Concat error: {result.stderr[-500:]}", file=sys.stderr)
        sys.exit(1)

    # Cleanup temp segment files
    if not temp_dir:
        for f_path in segment_files:
            os.remove(f_path)
        os.remove(concat_path)
        os.rmdir(workdir)
        print("Temp files cleaned up.")


def apply_edits(
    mp4_path: str,
    edl_path: str,
    output_path: str,
    legacy: bool = False,
    normalize: bool = False,
    temp_dir: str = None,
) -> None:
    """Cut video per EDL and concatenate."""
    with open(edl_path) as f:
        edl = json.load(f)

    segments = edl["segments"]
    if not segments:
        print("No segments to keep -- nothing to output.", file=sys.stderr)
        sys.exit(1)

    print(f"Applying {len(segments)} segments to {mp4_path}")
    print(f"Output: {output_path}")

    if legacy:
        apply_edits_legacy(mp4_path, edl, output_path, temp_dir)
    else:
        apply_edits_singlepass(mp4_path, edl, output_path, normalize=normalize)

    # Show output info
    probe_cmd = [
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration,size",
        "-of", "json", output_path
    ]
    probe = subprocess.run(probe_cmd, capture_output=True, text=True)
    if probe.returncode == 0:
        info = json.loads(probe.stdout)
        duration = float(info["format"]["duration"])
        size_mb = int(info["format"]["size"]) / (1024 * 1024)
        print(f"\nOutput: {output_path}")
        print(f"Duration: {duration:.1f}s ({duration / 60:.1f}min)")
        print(f"Size: {size_mb:.1f}MB")


def main():
    parser = argparse.ArgumentParser(description="Apply EDL cuts to a video")
    parser.add_argument("mp4", help="Path to original MP4 file")
    parser.add_argument("edl", help="Path to EDL JSON file")
    parser.add_argument("-o", "--output", help="Path for output MP4 (default: <basename>_edited.mp4)")
    parser.add_argument("--legacy", action="store_true",
                        help="Use legacy segment-by-segment mode instead of single-pass")
    parser.add_argument("--normalize", action="store_true",
                        help="Apply audio normalization (highpass 80Hz + loudnorm)")
    parser.add_argument("--temp-dir", help="Directory for temp segment files (legacy mode only)")
    args = parser.parse_args()

    output_path = args.output or os.path.splitext(args.mp4)[0] + "_edited.mp4"
    apply_edits(
        args.mp4, args.edl, output_path,
        legacy=args.legacy,
        normalize=args.normalize,
        temp_dir=args.temp_dir,
    )


if __name__ == "__main__":
    main()
