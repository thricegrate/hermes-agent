"""Universal status checker for any Jogg AI async job (video, avatar, motion)."""

import argparse
import sys
import os
import time
sys.path.insert(0, os.path.dirname(__file__))
from _api import api_get, download_file

ENDPOINTS = {
    "avatar-video": "/avatar_video/{id}",
    "product-video": "/product_video/{id}",
    "photo-avatar": "/photo_avatar/photo",
    "motion": "/photo_avatar",
}

QUERY_PARAMS = {
    "photo-avatar": "photo_id",
    "motion": "motion_id",
}

TERMINAL_STATUSES = {"completed", "success", "failed"}


def check_once(job_type, job_id):
    """Check status once and return the response data dict."""
    if job_type in QUERY_PARAMS:
        endpoint = ENDPOINTS[job_type]
        params = {QUERY_PARAMS[job_type]: job_id}
        result = api_get(endpoint, params=params)
    else:
        endpoint = ENDPOINTS[job_type].replace("{id}", job_id)
        result = api_get(endpoint)
    return result.get("data", {})


def get_status(data):
    """Extract status from response data, handling both string and int statuses."""
    status = data.get("status", "unknown")
    if isinstance(status, int):
        return {0: "processing", 1: "completed", 2: "failed"}.get(status, f"unknown({status})")
    return status


def main():
    parser = argparse.ArgumentParser(description="Check status of any Jogg AI async job")
    parser.add_argument("--type", required=True, choices=list(ENDPOINTS.keys()), help="Job type")
    parser.add_argument("--id", required=True, help="Job ID")
    parser.add_argument("--poll", action="store_true", help="Poll until completion")
    parser.add_argument("--poll-interval", type=int, default=10, help="Seconds between polls (default: 10)")
    parser.add_argument("--download", action="store_true", help="Download video on completion")
    parser.add_argument("--output", help="Output path for download (default: .tmp/jogg_ai_{id}.mp4)")
    args = parser.parse_args()

    if not args.output:
        args.output = f".tmp/jogg_ai_{args.id}.mp4"

    data = check_once(args.type, args.id)
    status = get_status(data)
    print(f"Status: {status}")

    if args.poll and status not in TERMINAL_STATUSES:
        print(f"Polling every {args.poll_interval}s...")
        while status not in TERMINAL_STATUSES:
            time.sleep(args.poll_interval)
            data = check_once(args.type, args.id)
            status = get_status(data)
            print(f"  Status: {status}")

    if status in ("completed", "success"):
        video_url = data.get("video_url")
        cover_url = data.get("cover_url")
        if video_url:
            print(f"Video URL: {video_url}")
        if cover_url:
            print(f"Cover URL: {cover_url}")

        # Print any other useful fields
        for key in ("duration", "motion_preview_url", "image_url", "image_url_list"):
            if key in data:
                print(f"{key}: {data[key]}")

        if args.download and video_url:
            download_file(video_url, args.output)
    elif status == "failed":
        fail_msg = data.get("fail_msg", data.get("err_msg", "No details available"))
        print(f"FAILED: {fail_msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
