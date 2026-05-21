# Monthly Refresh Prompt — Aschenbrenner Macro Overlay

**What this is:** A copy-paste prompt for the monthly refresh of the Aschenbrenner macro overlay. Drop this into `/schedule` to set up a recurring routine, or run it manually on the first business day of each month.

**Recommended cadence:** Monthly, first business day, after US market close (so the prior month's full data is available).

---

## How to schedule

```
/schedule create "Aschenbrenner macro overlay monthly refresh" --cron "0 22 1 * *" --prompt-file skills/trading/references/monthly-refresh-prompt.md
```

(Adjust the cron expression as you prefer. The above runs at 22:00 UTC on the 1st of each month.)

Alternative: run manually by saying "run the monthly refresh from skills/trading/references/monthly-refresh-prompt.md".

---

## The Refresh Prompt (copy this verbatim)

```
Run the monthly Aschenbrenner macro overlay refresh.

CONTEXT FILES (read first):
- skills/trading/references/macroeconomic-thesis.md
- skills/trading/references/thesis-catalysts.md
- skills/trading/references/reality-check.md
- skills/trading/references/sizing-overlay.md

TASK:

1. Identify the current month and the prior month. Use today's date.

2. Web-search for major events in the prior month across these dimensions:
   - Hyperscaler capex announcements / earnings (MSFT, GOOGL, AMZN, META quarterly capex updates if applicable to the month)
   - NVDA earnings (if the month included a print)
   - AMD, TSM, AVGO, ASML, MU earnings (if applicable)
   - Nuclear utility PPAs (Constellation/CEG, Vistra/VST, Talen/TLN, new utility-hyperscaler deals)
   - SMR permits (NRC decisions, OKLO/NNE updates)
   - Major frontier model releases (OpenAI, Anthropic, Google, Meta, DeepSeek, Chinese labs) with benchmark deltas
   - Policy/regulatory events (executive orders, EU AI Act enforcement, congressional hearings on AI, export control updates)
   - Datacenter buildout announcements ($10B+ capex tied to specific cluster builds)
   - Defense AI contract awards (PLTR, ITA primes, AVAV, KTOS)
   - Any cybersecurity incidents involving AI labs (Ch.4 thesis)
   - Any alignment / safety incidents (Ch.5 kill switch territory)
   - US-China relations updates relevant to Ch.6

3. For each event found:
   - Match it to an existing prediction row in reality-check.md
   - Update the status tag: [PENDING] → [IN PROGRESS], or [IN PROGRESS] → [FIRED], etc.
   - Add a one-line note with the event date, brief description, and source URL
   - If the event doesn't match an existing row but is materially relevant, add a new row

4. Re-check the 7 kill-switch tripwires in sizing-overlay.md Appendix B:
   - Tripwire 1 (NVDA datacenter rev YoY < 30% for 2 Q): check latest 2 NVDA prints
   - Tripwire 2 (Sum hyperscaler capex cut > 15%): compute sum from latest earnings
   - Tripwire 3 (Model benchmark improvement < 10%): check latest flagship vs prior
   - Tripwire 4 (MU HBM down 2+ Q): check MU last 2 prints
   - Tripwire 5 (Regulatory pause): scan for any compute-cap orders or training-cap regulations
   - Tripwire 6 (Two T1 names below 50WMA): check CEG, VST, TLN, NVDA, AMD, TSM, AVGO, ASML, PLTR weekly closes
   - Tripwire 7 (Aschenbrenner public reversal): scan for any public Aschenbrenner statements

5. Update reality-check.md with:
   - New entries in the predictions table
   - Updated Quick Score bucket counts at the top
   - "Last updated" date at the top
   - A new section at the bottom under "## Monthly Update Log" with the date and a bullet list of changes

6. Update thesis-catalysts.md with:
   - Roll forward the quarterly forward calendar (drop the now-past quarter, add a new one at the end)
   - Note any catalyst that fired and what it confirmed/refuted

7. Send a Telegram summary using the `telegram-send` tool. Format:

   ```
   <b>Aschenbrenner Refresh — {Month YYYY}</b>

   <b>Events fired this month:</b>
   - [event 1 + status change]
   - [event 2 + status change]
   - ...

   <b>Kill switch status:</b>
   - Tripwire 1: NOT TRIPPED / TRIPPED (details)
   - ...

   <b>Tier 1 health:</b>
   - Names below 50WMA: [list, or 'none']

   <b>Action items:</b>
   - [any sizing adjustments required]
   - [any positions to exit per kill switch]

   <b>Next catalyst window:</b>
   - [upcoming earnings or events worth watching this month]
   ```

8. If ANY kill switch tripped, mark the Telegram message high-priority and include explicit position-adjustment instructions per sizing-overlay.md rules.

CRITICAL RULES:
- Every prediction status change MUST have a source URL or earnings-transcript reference. No status changes without evidence.
- Do NOT speculate forward — only log events that have already happened.
- Verbatim quote rigor: if you add a new quote citation, it must be verbatim from a verified source.
- If unsure whether an event qualifies, log it but tag with status uncertainty rather than promoting.
- Do not modify macroeconomic-thesis.md, aschenbrenner-watchlist.md, or sizing-overlay.md unless a kill switch was tripped (in which case update sizing-overlay.md to record the tripwire fire with date).

Return: a short summary of what changed, plus the Telegram message text for confirmation.
```

---

## What this prompt does NOT do (manual decisions only)

The refresh is a data-gathering and bookkeeping task. These decisions require your judgment, not the agent:

- **Tier reassignments:** If a name should move from Tier 1 to Tier 2 (or vice versa) based on changed conviction
- **New ticker additions to watchlist:** If a new name emerges as a thesis-aligned trade
- **Theme additions:** If a new theme (e.g., humanoid robotics) becomes thesis-relevant
- **Major thesis revisions:** If Aschenbrenner himself releases a follow-up or revision, or the market environment fundamentally shifts

These decisions should be made manually during a quarterly review session, not automated.

---

## Verification of the refresh

After each monthly run, spot-check:
1. The Quick Score bucket counts in reality-check.md make sense (more `[FIRED]` over time, fewer `[PENDING]`)
2. The kill switch worksheet matches the latest earnings data
3. The Telegram message arrived
4. No verbatim-quote drift in any updated row (every new citation has a real source)

If the refresh ever fires a kill switch alert, IMMEDIATELY:
1. Re-check the underlying data point manually
2. Re-read the affected section of sizing-overlay.md to confirm the action
3. Adjust positions per the rules
4. Log the override (or compliance) in your trading journal
