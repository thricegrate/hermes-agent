"""Generate a custom photo avatar (and optionally add motion) via Jogg AI."""

import argparse
import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_post, api_get


def main():
    parser = argparse.ArgumentParser(description="Generate custom photo avatar on Jogg AI")

    # Photo generation params
    parser.add_argument("--age", default="Adult",
                        choices=["Teenager", "Young adult", "Adult", "Elderly"],
                        help="Avatar age group (default: Adult)")
    parser.add_argument("--avatar-style", default="Professional",
                        choices=["Professional", "Social"],
                        help="Avatar style (default: Professional)")
    parser.add_argument("--gender", default="Male", choices=["Female", "Male"],
                        help="Avatar gender (default: Male)")
    parser.add_argument("--model", default="modern", choices=["classic", "modern"],
                        help="Photo generation model (default: modern)")
    parser.add_argument("--aspect-ratio", default="portrait", choices=["portrait", "landscape", "square"],
                        help="Photo aspect ratio (default: portrait)")
    parser.add_argument("--image-url", help="Reference portrait photo URL")
    parser.add_argument("--ethnicity",
                        choices=["European", "African", "South Asian", "East Asian",
                                 "Middle Eastern", "South American", "North American"],
                        help="Avatar ethnicity")
    parser.add_argument("--background", help="Background description (free text)")
    parser.add_argument("--appearance", help="Appearance description (free text)")

    # Motion params (optional second stage)
    parser.add_argument("--add-motion", action="store_true",
                        help="Add motion after photo generation (creates animated avatar)")
    parser.add_argument("--name", help="Avatar name (required with --add-motion)")
    parser.add_argument("--voice-id", help="Voice ID for motion (required with --add-motion)")
    parser.add_argument("--motion-model", default="2.0", choices=["1.0", "2.0", "3.0"],
                        help="Motion model version (default: 2.0)")
    parser.add_argument("--description", help="Avatar description for motion")

    # Polling
    parser.add_argument("--poll", action="store_true", help="Poll until completion")
    parser.add_argument("--poll-interval", type=int, default=10,
                        help="Seconds between polls (default: 10)")
    args = parser.parse_args()

    if args.add_motion:
        if not args.name:
            parser.error("--name is required when using --add-motion")
        if not args.voice_id:
            parser.error("--voice-id is required when using --add-motion")

    # Stage 1: Generate photo avatar
    photo_payload = {
        "age": args.age,
        "avatar_style": args.avatar_style,
        "gender": args.gender,
        "model": args.model,
        "aspect_ratio": args.aspect_ratio,
    }
    if args.image_url:
        photo_payload["image_url"] = args.image_url
    if args.ethnicity:
        photo_payload["ethnicity"] = args.ethnicity
    if args.background:
        photo_payload["background"] = args.background
    if args.appearance:
        photo_payload["appearance"] = args.appearance

    print(f"Generating photo avatar ({args.gender}, {args.age}, {args.avatar_style})...")
    result = api_post("/photo_avatar/photo/generate", photo_payload)

    photo_id = result.get("data", {}).get("photo_id")
    if not photo_id:
        print("ERROR: No photo_id returned", file=sys.stderr)
        print(f"Response: {result}", file=sys.stderr)
        sys.exit(1)

    print(f"Photo ID: {photo_id}")

    if not args.poll:
        print(f"\nCheck status with: python skills/jogg-ai/scripts/check_status.py --type photo-avatar --id {photo_id}")
        if args.add_motion:
            print("Note: Run with --poll to automatically proceed to motion after photo completes")
        return

    # Poll photo generation
    print(f"Polling photo generation every {args.poll_interval}s (typically 2-5 min)...")
    photo_data = None
    while True:
        time.sleep(args.poll_interval)
        status_result = api_get("/photo_avatar/photo", params={"photo_id": photo_id})
        data = status_result.get("data", {})
        status = data.get("status", "unknown")

        # Handle both string and possible status codes
        if isinstance(status, str):
            print(f"  Status: {status}")
            if status in ("success", "completed"):
                photo_data = data
                break
            elif status == "failed":
                print("Photo generation failed.", file=sys.stderr)
                sys.exit(1)
        else:
            status_name = {0: "processing", 1: "completed", 2: "failed"}.get(status, f"unknown({status})")
            print(f"  Status: {status_name}")
            if status == 1:
                photo_data = data
                break
            elif status == 2:
                print("Photo generation failed.", file=sys.stderr)
                sys.exit(1)

    image_urls = photo_data.get("image_url_list", [])
    print(f"\nPhoto avatar ready! Generated {len(image_urls)} image(s)")
    for i, url in enumerate(image_urls):
        print(f"  Image {i+1}: {url}")

    if not args.add_motion:
        print(f"\nTo add motion later:")
        print(f"  Use the image URL above with --image-url in a new run with --add-motion")
        return

    # Stage 2: Add motion
    image_url = image_urls[0] if image_urls else None
    if not image_url:
        print("ERROR: No image URL available for motion", file=sys.stderr)
        sys.exit(1)

    motion_payload = {
        "photo_id": photo_id,
        "image_url": image_url,
        "name": args.name,
        "voice_id": args.voice_id,
        "model": args.motion_model,
    }
    if args.description:
        motion_payload["description"] = args.description

    print(f"\nAdding motion to avatar '{args.name}'...")
    motion_result = api_post("/photo_avatar/add_motion", motion_payload)

    motion_data = motion_result.get("data", {})
    avatar_id = motion_data.get("avatar_id")
    motion_id = motion_data.get("motion_id")

    print(f"Avatar ID: {avatar_id}")
    print(f"Motion ID: {motion_id}")

    # Poll motion generation
    print(f"Polling motion generation every {args.poll_interval}s (typically 2-3 min)...")
    while True:
        time.sleep(args.poll_interval)
        status_result = api_get("/photo_avatar", params={"motion_id": motion_id})
        data = status_result.get("data", {})
        status = data.get("status", "unknown")
        print(f"  Status: {status}")

        if status in ("completed", "success"):
            preview_url = data.get("motion_preview_url")
            print(f"\nMotion avatar ready!")
            print(f"Avatar ID: {data.get('avatar_id', avatar_id)}")
            if preview_url:
                print(f"Preview: {preview_url}")
            print(f"\nUse in videos with: create_avatar_video.py --avatar-id {data.get('avatar_id', avatar_id)} --avatar-type 1")
            break
        elif status == "failed":
            print("Motion generation failed.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
