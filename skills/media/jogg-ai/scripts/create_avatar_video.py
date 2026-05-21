"""Create a talking avatar video from script text or custom audio."""

import argparse
import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_post, api_get, download_file


def main():
    parser = argparse.ArgumentParser(description="Create Jogg AI avatar video")
    parser.add_argument("--avatar-id", required=True, type=int, help="Avatar ID (from list_avatars.py)")
    parser.add_argument("--avatar-type", type=int, default=0, choices=[0, 1],
                        help="0=public avatar, 1=custom photo avatar (default: 0)")

    voice_group = parser.add_mutually_exclusive_group(required=True)
    voice_group.add_argument("--script", help="Text for the avatar to speak")
    voice_group.add_argument("--script-file", help="File containing script text")
    voice_group.add_argument("--audio-url", help="URL of custom audio file")

    parser.add_argument("--voice-id", help="Voice ID (required with --script/--script-file, from list_voices.py)")
    parser.add_argument("--aspect-ratio", default="portrait", choices=["portrait", "landscape", "square"],
                        help="Video aspect ratio (default: portrait)")
    parser.add_argument("--screen-style", type=int, default=1, choices=[1, 2, 3],
                        help="1=full screen, 2=split screen, 3=picture-in-picture (default: 1)")
    parser.add_argument("--caption", action="store_true", help="Enable captions/subtitles")
    parser.add_argument("--name", help="Custom name for the video project")
    parser.add_argument("--poll", action="store_true", help="Poll until video is complete")
    parser.add_argument("--poll-interval", type=int, default=15, help="Seconds between polls (default: 15)")
    parser.add_argument("--download", action="store_true", help="Download video on completion (implies --poll)")
    parser.add_argument("--output", help="Output path for download (default: .tmp/jogg_avatar_{id}.mp4)")
    args = parser.parse_args()

    # Validate voice_id is provided when using script
    if (args.script or args.script_file) and not args.voice_id:
        parser.error("--voice-id is required when using --script or --script-file")

    # Read script from file if needed
    script_text = args.script
    if args.script_file:
        try:
            with open(args.script_file, "r", encoding="utf-8") as f:
                script_text = f.read().strip()
        except FileNotFoundError:
            print(f"ERROR: Script file not found: {args.script_file}", file=sys.stderr)
            sys.exit(1)
        if not script_text:
            print("ERROR: Script file is empty", file=sys.stderr)
            sys.exit(1)

    if args.download:
        args.poll = True

    # Build payload
    payload = {
        "avatar": {
            "avatar_id": args.avatar_id,
            "avatar_type": args.avatar_type,
        },
        "aspect_ratio": args.aspect_ratio,
        "screen_style": args.screen_style,
        "caption": args.caption,
    }

    if args.audio_url:
        payload["voice"] = {
            "type": "audio",
            "audio_url": args.audio_url,
        }
    else:
        payload["voice"] = {
            "type": "script",
            "voice_id": args.voice_id,
            "script": script_text,
        }

    if args.name:
        payload["name"] = args.name

    print(f"Creating avatar video (avatar={args.avatar_id}, ratio={args.aspect_ratio})...")
    result = api_post("/create_video_from_avatar", payload)

    video_id = result.get("data", {}).get("video_id")
    if not video_id:
        print("ERROR: No video_id returned", file=sys.stderr)
        print(f"Response: {result}", file=sys.stderr)
        sys.exit(1)

    print(f"Video ID: {video_id}")

    if not args.poll:
        print(f"\nCheck status with: python skills/jogg-ai/scripts/check_status.py --type avatar-video --id {video_id}")
        return

    # Poll for completion
    print(f"Polling every {args.poll_interval}s (avatar videos typically take 2-5 min)...")
    while True:
        time.sleep(args.poll_interval)
        status_result = api_get(f"/avatar_video/{video_id}")
        data = status_result.get("data", {})
        status = data.get("status", "unknown")
        print(f"  Status: {status}")

        if status == "completed":
            video_url = data.get("video_url")
            cover_url = data.get("cover_url")
            print(f"\nVideo ready!")
            if video_url:
                print(f"Video URL: {video_url}")
            if cover_url:
                print(f"Cover URL: {cover_url}")

            if args.download and video_url:
                output = args.output or f".tmp/jogg_avatar_{video_id}.mp4"
                download_file(video_url, output)
            break
        elif status == "failed":
            print(f"\nVideo generation failed.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
