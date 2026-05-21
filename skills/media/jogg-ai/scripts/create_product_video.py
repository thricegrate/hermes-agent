"""Create a product marketing video from a Jogg AI product entry."""

import argparse
import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_post, api_get, download_file

SCRIPT_STYLES = [
    "Storytime", "Discovery", "Don't Worry",
    "Data", "Top 3 reasons", "Light marketing",
]


def main():
    parser = argparse.ArgumentParser(description="Create Jogg AI product marketing video")
    parser.add_argument("--product-id", required=True, help="Product ID (from create_product.py)")
    parser.add_argument("--aspect-ratio", default="portrait", choices=["portrait", "landscape", "square"],
                        help="Video aspect ratio (default: portrait)")
    parser.add_argument("--length", default="30", choices=["15", "30", "60"],
                        help="Video length in seconds (default: 30)")
    parser.add_argument("--language", default="english", help="Script language (default: english)")
    parser.add_argument("--avatar-id", type=int, help="Avatar ID (from list_avatars.py)")
    parser.add_argument("--avatar-type", type=int, default=0, choices=[0, 1],
                        help="0=public, 1=custom (default: 0)")
    parser.add_argument("--voice-id", help="Voice ID (from list_voices.py)")
    parser.add_argument("--music-id", type=int, help="Background music ID (from list_music.py)")
    parser.add_argument("--script-style", choices=SCRIPT_STYLES,
                        help="AI script generation style")
    parser.add_argument("--visual-style", help="Visual style/template name (from list_styles.py)")
    parser.add_argument("--override-script", help="Custom script text (overrides AI generation)")
    parser.add_argument("--caption", action="store_true", help="Enable captions/subtitles")
    parser.add_argument("--poll", action="store_true", help="Poll until video is complete")
    parser.add_argument("--poll-interval", type=int, default=20,
                        help="Seconds between polls (default: 20)")
    parser.add_argument("--download", action="store_true", help="Download video on completion (implies --poll)")
    parser.add_argument("--output", help="Output path (default: .tmp/jogg_product_{id}.mp4)")
    args = parser.parse_args()

    if args.download:
        args.poll = True

    # Build payload
    payload = {
        "product_id": args.product_id,
        "aspect_ratio": args.aspect_ratio,
        "length": args.length,
        "language": args.language,
        "caption": args.caption,
    }

    if args.avatar_id is not None:
        payload["avatar_id"] = args.avatar_id
        payload["avatar_type"] = args.avatar_type
    if args.voice_id:
        payload["voice_id"] = args.voice_id
    if args.music_id is not None:
        payload["music_id"] = args.music_id
    if args.script_style:
        payload["script_style"] = args.script_style
    if args.visual_style:
        payload["visual_style"] = args.visual_style
    if args.override_script:
        payload["override_script"] = args.override_script

    print(f"Creating product video (product={args.product_id}, {args.length}s, {args.aspect_ratio})...")
    result = api_post("/create_video_from_product", payload)

    video_id = result.get("data", {}).get("product_video_id")
    if not video_id:
        print("ERROR: No product_video_id returned", file=sys.stderr)
        print(f"Response: {result}", file=sys.stderr)
        sys.exit(1)

    print(f"Video ID: {video_id}")

    if not args.poll:
        print(f"\nCheck status with: python skills/jogg-ai/scripts/check_status.py --type product-video --id {video_id}")
        return

    # Poll for completion
    print(f"Polling every {args.poll_interval}s (product videos typically take 5-10 min)...")
    while True:
        time.sleep(args.poll_interval)
        status_result = api_get(f"/product_video/{video_id}")
        data = status_result.get("data", {})
        status = data.get("status", "unknown")
        print(f"  Status: {status}")

        if status == "completed":
            video_url = data.get("video_url")
            cover_url = data.get("cover_url")
            duration = data.get("duration")
            print(f"\nVideo ready!")
            if video_url:
                print(f"Video URL: {video_url}")
            if cover_url:
                print(f"Cover URL: {cover_url}")
            if duration:
                print(f"Duration: {duration}s")

            if args.download and video_url:
                output = args.output or f".tmp/jogg_product_{video_id}.mp4"
                download_file(video_url, output)
            break
        elif status == "failed":
            print(f"\nVideo generation failed.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
