#!/usr/bin/env python3
"""Shared platform-aware video encoder detection.

Probes ffmpeg for available hardware encoders and returns the best option
for the current platform. Primary target: NVIDIA h264_nvenc on Windows.
"""

import subprocess
import sys

# Cache so we only probe once per process
_detected_encoder = None
_detected_args = None


def detect_encoder() -> tuple[str, list[str]]:
    """Detect the best available encoder and return (encoder_name, extra_args).

    Priority:
      Windows: h264_nvenc (NVIDIA) > h264_amf (AMD) > libx264
      macOS:   h264_videotoolbox > libx264
      Linux:   h264_nvenc > libx264

    Returns:
        Tuple of (encoder_name, extra_args_list) ready to splice into an ffmpeg command.
        Example: ("h264_nvenc", ["-preset", "p4", "-cq", "18"])
    """
    global _detected_encoder, _detected_args
    if _detected_encoder is not None:
        return _detected_encoder, _detected_args

    try:
        result = subprocess.run(
            ["ffmpeg", "-hide_banner", "-encoders"],
            capture_output=True, text=True, timeout=5
        )
        encoders = result.stdout
    except Exception:
        encoders = ""

    if sys.platform == "win32":
        if "h264_nvenc" in encoders:
            _detected_encoder = "h264_nvenc"
            _detected_args = ["-preset", "p4", "-cq", "18"]
        elif "h264_amf" in encoders:
            _detected_encoder = "h264_amf"
            _detected_args = ["-quality", "quality"]
        else:
            _detected_encoder = "libx264"
            _detected_args = ["-preset", "fast", "-crf", "18"]
    elif sys.platform == "darwin":
        if "h264_videotoolbox" in encoders:
            _detected_encoder = "h264_videotoolbox"
            _detected_args = ["-b:v", "8M"]
        else:
            _detected_encoder = "libx264"
            _detected_args = ["-preset", "fast", "-crf", "18"]
    else:
        # Linux
        if "h264_nvenc" in encoders:
            _detected_encoder = "h264_nvenc"
            _detected_args = ["-preset", "p4", "-cq", "18"]
        else:
            _detected_encoder = "libx264"
            _detected_args = ["-preset", "fast", "-crf", "18"]

    return _detected_encoder, _detected_args


def get_encoder_cmd() -> list[str]:
    """Return full encoder flags for an ffmpeg command.

    Example output: ["-c:v", "h264_nvenc", "-preset", "p4", "-cq", "18"]
    """
    encoder, extra = detect_encoder()
    return ["-c:v", encoder] + extra


if __name__ == "__main__":
    encoder, args = detect_encoder()
    print(f"Detected encoder: {encoder}")
    print(f"Extra args: {args}")
    print(f"Full cmd fragment: {get_encoder_cmd()}")
