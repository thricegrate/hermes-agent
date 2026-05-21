"""Upload media files to Jogg AI for use in video creation."""

import argparse
import sys
import os
from pathlib import Path
import requests
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_post

CONTENT_TYPES = {
    ".mp4": "video/mp4",
    ".mov": "video/quicktime",
    ".avi": "video/x-msvideo",
    ".webm": "video/webm",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".webp": "image/webp",
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
    ".aac": "audio/aac",
    ".ogg": "audio/ogg",
}


def main():
    parser = argparse.ArgumentParser(description="Upload media file to Jogg AI")
    parser.add_argument("--file", required=True, help="Local file path to upload")
    parser.add_argument("--content-type", help="MIME type (auto-detected from extension if not set)")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"ERROR: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    content_type = args.content_type
    if not content_type:
        ext = file_path.suffix.lower()
        content_type = CONTENT_TYPES.get(ext)
        if not content_type:
            print(f"ERROR: Unknown file type '{ext}'. Use --content-type to specify.", file=sys.stderr)
            sys.exit(1)

    file_size = file_path.stat().st_size
    filename = file_path.name

    print(f"Uploading: {filename} ({file_size / 1024:.1f} KB, {content_type})")

    # Step 1: Get signed upload URL
    result = api_post("/upload/asset", {
        "filename": filename,
        "content_type": content_type,
        "file_size": file_size,
    })

    data = result.get("data", {})
    sign_url = data.get("sign_url")
    asset_url = data.get("asset_url")

    if not sign_url:
        print("ERROR: No signed URL returned from API", file=sys.stderr)
        sys.exit(1)

    # Step 2: PUT file to signed URL (no API key needed, it's a cloud storage URL)
    with open(file_path, "rb") as f:
        resp = requests.put(sign_url, data=f, headers={"Content-Type": content_type}, timeout=120)

    if resp.status_code >= 400:
        print(f"ERROR: Upload failed with status {resp.status_code}: {resp.text[:500]}", file=sys.stderr)
        sys.exit(1)

    print(f"Upload complete!")
    print(f"Asset URL: {asset_url}")
    print(f"\nUse this URL with --image-url in generate_photo_avatar.py or --audio-url in create_avatar_video.py")


if __name__ == "__main__":
    main()
