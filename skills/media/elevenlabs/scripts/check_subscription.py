"""Check ElevenLabs subscription status and credit usage.

Usage:
    python skills/elevenlabs/scripts/check_subscription.py
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

from elevenlabs import ElevenLabs


def main():
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("ERROR: ELEVENLABS_API_KEY not found in environment")
        sys.exit(1)

    client = ElevenLabs(api_key=api_key)
    sub = client.user.get_subscription()

    print("=== ElevenLabs Subscription ===")
    print(f"Tier:             {sub.tier}")
    print(f"Status:           {sub.status}")
    print(f"Characters used:  {sub.character_count:,} / {sub.character_limit:,}")
    remaining = sub.character_limit - sub.character_count
    pct = (sub.character_count / sub.character_limit * 100) if sub.character_limit > 0 else 0
    print(f"Remaining:        {remaining:,} ({100 - pct:.1f}%)")
    if hasattr(sub, "next_character_count_reset_unix"):
        from datetime import datetime
        reset = datetime.fromtimestamp(sub.next_character_count_reset_unix)
        print(f"Resets:           {reset.strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()
