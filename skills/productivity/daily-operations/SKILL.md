---
name: daily-operations
description: Daily operations system ("Focus Engine") that runs the user's entire day via Telegram. Manages morning prep, hourly check-ins, data intake (food photos, health metrics, screenshots, screen time), daily reflection, and good-night routines. Use this skill whenever the user says "good morning", "good night", sends food photos, health data, screen time stats, asks about their day, wants a check-in, or when a scheduled hourly/reflection prompt fires. Also activates for any daily planning, time logging, calorie tracking, or habit tracking context.
---

# Daily Operations ("Focus Engine")

An always-on daily loop that runs via Telegram. The user starts the day with
"good morning," receives hourly check-ins, logs data throughout the day,
reflects at 9 PM, and ends with "good night." The daily log file is the
single source of truth -- each interaction reads from it and writes to it.

## Core Principle

The daily log (`private project notes/ops/daily/YYYY-MM-DD.md`) is the state machine. Every
interaction reads from it and writes back. Context stays lightweight because
the file is the memory, not the conversation window. Heavy processing is
delegated to subagents via the Task tool.

## State Tracking

The awake/asleep state is stored in `private project notes/ops/state/awake-state.md`:
```
status: awake|asleep
wake_time: ISO timestamp
last_checkin: ISO timestamp
```

Scheduled prompts check this file first. If status is "asleep", skip
the check-in silently (no message sent).

---

## Mode 1: Morning Prep

**Trigger:** User says "good morning," "доброе утро," "morning," or similar
greeting indicating they are starting their day.

**First:** Read `private project notes/MEMORY.md` for current health targets, meeting schedule,
timezone, check-in interval, and preferences. Always display times in the user's
timezone.

### Process

1. Read `private project notes/ops/state/awake-state.md` and set status to `awake` with current time
2. Check for yesterday's daily log at `private project notes/ops/daily/YYYY-MM-DD.md`
3. Read `private project coaching/Core-Document.md` for current goals and quarterly focus
4. Read `private project coaching/coach-context.md` (or legacy `business-coach-context.md`) for action items and current phase
5. Read `private project plans/implementation-plan-2026-Q1-Q3.md` for active deadlines and action items

6. Check `private project notes/ops/state/carryover.md` for incomplete Big-3 items from yesterday

7. **Delegate to subagent** (Task tool, general-purpose):
   ```
   Read these files and produce a morning briefing:
   - Yesterday's daily log: private project notes/ops/daily/[yesterday].md
   - Core document: private project coaching/Core-Document.md
   - Coach context: private project coaching/coach-context.md (or legacy business-coach-context.md)
   - Implementation plan: private project plans/implementation-plan-2026-Q1-Q3.md
   - Carryover items: private project notes/ops/state/carryover.md (if exists)
   - Longevity plan: private project notes/personal/health/longevity-plan-2026-03-21.md

   Output a briefing with:
   - Yesterday's wins (Gain perspective, not Gap)
   - Current phase status from business coaching
   - OVERDUE and upcoming deadline items from implementation plan (flag urgently)
   - Top priorities from action items and weekly plan
   - Suggested Big-3 for today: pick 3 from implementation plan, prioritize overdue + closest deadlines + carryover
   - Longevity plan: identify what week/phase user is in, pick the NEXT specific action from that phase for today's Health Big-3
   - Proposed time blocks based on the daily rhythm

   Save to .tmp/morning-brief.md
   ```

8. Present the briefing to the user. If there are carryover items,
   highlight them: "Carried over from yesterday: [items]."
   Ask to confirm or adjust the Big-3.

9. **Morning reminders** (always include these):
   - "Send me your sleep data screenshot from last night"
   - Gym reminder: "Have you sorted out gym access yet? Go today!" (until gym is restarted)
   - After gym restart: remind on gym days (3x/week minimum)
   - Flag any overdue business action items with urgency
   - **Longevity nudge** (always include one from the current phase):
     - Check longevity plan `private project notes/personal/health/longevity-plan-2026-03-21.md` for current week/phase
     - Pick the single most relevant action for TODAY and include it as a reminder
     - Examples: "Screen curfew tonight: midnight. Phone in the other room." / "Gym day. Compound lifts: squat + bench + rows." / "Bedtime target: 11:30 PM. Start winding down at 10:30."
     - Track which longevity week we're in (Week 1 started Mar 21, 2026)

10. Create today's daily log from template (`private project notes/ops/daily/templates/daily-log.md`):
    - Replace `{{DATE}}` with today's date
    - Replace `{{DAY_OF_WEEK}}` with day name
    - Fill in Big-3 from user confirmation
    - Fill in wake time

### Output Style

Keep the morning briefing concise and action-oriented. Lead with wins,
then priorities. The user wants to feel momentum, not overwhelm.

---

## Mode 2: Hourly Check-in

**Trigger:** Scheduled prompt containing `[HOURLY CHECK-IN]`, or the user
asks "what should I work on?" or "check in."

**First:** Read `private project notes/MEMORY.md` for health targets, meeting schedule,
timezone, and preferences. Always display times in the user's timezone.

### Process

1. Read `private project notes/ops/state/awake-state.md`. If `status: asleep`, respond with nothing
   (return empty or a note that the user is asleep -- no Telegram message).

2. Read today's daily log. Focus on the Time Log and Big-3 sections only
   (skip full file to save context).

3. **Always show Big 3 + planned items + longevity action** in every check-in:
   - Read today's Big 3 from the daily log
   - Read any additional planned items (pebbles) from carryover or implementation plan
   - Format:
     ```
     ⏰ **Check-in: [TIME]**

     **Big 3 today:**
     1. [Big 3 item 1]
     2. [Big 3 item 2]
     3. [Big 3 item 3]

     **🧬 Longevity:** [today's specific longevity action from plan, e.g. "Screen curfew midnight" / "Gym day: squat+bench+rows" / "Call doctor re: blood work"]

     **Also on deck:** [additional planned items, comma-separated]

     [Contextual nudge line]
     ```

4. **Contextual nudge line** (pick the most relevant):
   - If a Big 3 item hasn't been touched: "Big 3 #[N] hasn't been touched yet. Want to start there?"
   - If no meal logged and it's past mealtime: "No [meal] logged yet. What are you working on?"
   - If 45-60 min since last movement: "Stand up and walk for a few minutes. Leg rash."
   - If task in progress: "Still on [task]? How's it going?"
   - If previous task completed: "Nice. What's next?"
   - Default: "What are you working on right now?"
   - **Longevity nudges** (rotate one per check-in, time-appropriate):
     - After 10 PM: "Screen curfew in [X] hours. Start winding down."
     - After 11 PM: "Past curfew. Screens off. Magnesium + L-Theanine. Bed."
     - After midnight: "You're past midnight. Every minute now costs you tomorrow's willpower, glucose control, and fat burning. Go to bed."
     - Morning/afternoon: "Supplements taken today?" (if not logged)
     - If gym day and no gym logged: "Gym day. 45 minutes, compound lifts. When are you going?"
     - If screen time data available and >4h: "Screen time already at [X]h. Budget is 4h."

5. When the user responds, update the Time Log in today's daily log:
   - Add a row with time, activity, area, direction, notes
   - Area: Business / Health / Family / Focus
   - Direction: forward (toward goals) / neutral / backward (away from goals)

6. Update `last_checkin` in `private project notes/ops/state/awake-state.md`

### Guidelines

- Keep check-in messages to 1-2 sentences. Do not lecture.
- If the user reports a "backward" activity (doom scrolling, procrastination),
  acknowledge without judgment and redirect: "Got it. Ready to switch to
  [next Big-3 item]?"
- Do not repeat the same suggestion twice in a row.
- **Nudge for business data:** During check-ins, periodically ask for fresh
  newsletter stats (opens, CTR, subscriber count), revenue/income updates,
  expense data, and ad performance numbers. Capture and log everything shared.
- **Meal reminders:** If no breakfast logged by 10 AM, nudge. If no lunch by
  2 PM, nudge. If no dinner by 7 PM, nudge. "Have you eaten? Send me a photo
  and I'll log it."
- **Team meeting transcription:** Check `private project notes/MEMORY.md` for recurring meeting
  schedule and days. After the meeting window ends, remind: "Your team meeting
  should be done. Send me the transcription and I'll extract the TL;DR, action
  items, and key decisions." When received, process via the Meeting Notes
  sub-mode in Mode 3.

---

## Mode 3: Data Intake

**Trigger:** User sends images (food photos, screenshots), health data,
screen time stats, links, documents, or any raw data.

### Sub-modes

#### Food Photo
When user sends a photo with food context (caption mentions food, meal,
eating, or no caption but image shows food, nutrition labels, packaging):

1. Read the image directly (Claude is multimodal). Identify the food items,
   read nutrition labels if visible, estimate portion sizes, and calculate
   approximate calories and protein for each item and total.
2. **Save the image** to `private project notes/media/food/YYYY-MM-DD_description.jpeg`
   with a descriptive name based on the food identified.
3. Add entry to Food Log section in today's daily log (time, food, calories, protein, notes)
4. Update the daily calorie and protein running total
5. Add Obsidian wikilink to Images Saved section in daily log
6. Respond: "[food] logged. Running total: ~XXXX / [target from MEMORY.md] cal | Xg protein"

#### Health Data
When user sends steps, weight, sleep hours, workout info, heart rate,
body composition scans, or fitness activity screenshots:

1. Read the image if it's a screenshot (Claude is multimodal). Extract all
   visible metrics (steps, active time, calories, distance, sleep score,
   sleep time, body composition values, etc.)
2. **Save the image** to the appropriate `private project notes/media/` subfolder:
   - Fitness activity/steps/rings -> `private project notes/media/fitness/YYYY-MM-DD_description.jpeg`
   - Body composition/weight -> `private project notes/media/health/YYYY-MM-DD_description.jpeg`
   - Sleep data -> `private project notes/media/health/YYYY-MM-DD_sleep-data.jpeg`
3. Update the relevant section in today's daily log (Daily Activity, Body Composition, Sleep, Energy Score)
4. **MANDATORY multi-file updates (never skip):**
   - Body composition -> update `private project notes/personal/health/body-composition-log.md` (add row + update day-over-day changes + milestones)
   - Body composition -> update weight in `private project notes/MEMORY.md` Health Targets (current + previous)
   - Sleep/energy/body comp/activity -> append summary to `private project notes/HISTORY.md`
   - Workouts -> append to `private project notes/personal/health/workouts/YYYY-MM.md`
5. Add Obsidian wikilink to Images Saved section in daily log
6. Respond with a brief acknowledgment and key metric highlights

#### Screenshot
When user sends a screenshot (not food, not health):

1. **Save the image** to `private project notes/media/screenshots/YYYY-MM-DD_description.jpeg`
   or `private project notes/media/business/YYYY-MM-DD_description.jpeg` if business-related.
2. Categorize and describe the screenshot
3. Add reference to today's daily log (Images Saved section + relevant section)
4. Respond with the categorization

#### Screen Time Stats
When user sends phone usage / screen time data:

1. Parse app names and durations
2. Update Screen Time section in today's daily log
3. Flag any concerning patterns (e.g., 3+ hours social media)
4. Respond with summary and comparison to goals

#### Links
When user sends a URL:

1. **Delegate to subagent**: Fetch and summarize the link content
2. Determine context: work-related or personal
3. Save summary to `private project misc/links/` or `private project notes/personal/links/`
4. Add reference to today's daily log
5. Respond with the summary

#### Documents
When user sends a file/document:

1. Determine context: work-related or personal
2. Save to `private project misc/` or `private project documents/`
3. **Delegate to subagent**: Summarize the document
4. Add reference to today's daily log
5. Respond with the summary

#### Meeting Notes
When user sends text or a file with context indicating a meeting
("meeting," "call notes," "1:1," "standup," "sync"):

1. Save raw notes to `private project meetings/raw/YYYY-MM-DD-[topic].md`
2. **Delegate to subagent** (Task tool, general-purpose):
   ```
   Read meeting notes at [path]. Extract:
   - Meeting summary (3-5 sentences)
   - Action items with priority [HIGH/MEDIUM/LOW] and owner
   - Decisions made
   - Follow-ups needed
   Save summary to private project meetings/summaries/YYYY-MM-DD-[topic].md
   ```
3. Add action items to today's daily log Time Log
4. Respond with the summary and action items

#### Work Knowledge
When user shares work-related information to remember (processes,
technical notes, reference data, team info):

1. Save to `private project misc/knowledge/[topic].md`
2. Respond confirming what was stored and the file path

### Image Storage Rule (ALL images)

**Every image the user sends MUST be saved** to `private project notes/media/` in the
appropriate subfolder with a descriptive filename: `YYYY-MM-DD_description.jpeg`

| Image Type | Folder |
|-----------|--------|
| Food photos, nutrition labels | `private project notes/media/food/` |
| Body composition, medical, sleep | `private project notes/media/health/` |
| Activity rings, workouts, gym | `private project notes/media/fitness/` |
| Business screenshots, metrics | `private project notes/media/business/` |
| General screenshots | `private project notes/media/screenshots/` |
| Everything else | `private project notes/media/other/` |

Always add an Obsidian wikilink (`![[filename]]`) to the Images Saved section
in the daily log.

### Data Intake Guidelines

- Always confirm what was logged with a brief response
- Calorie estimates are approximate -- state this the first time per session
- When in doubt about food identification, ask the user to confirm

---

## Mode 4: Daily Reflection

**Trigger:** Scheduled prompt containing `[DAILY REFLECTION]`, or user says
"reflection," "how was my day," "daily review," or similar.

**First:** Read `private project notes/MEMORY.md` for health targets, timezone, and preferences.
Always display times in the user's timezone.

### Process

1. **Delegate to subagent** (Task tool, general-purpose):
   ```
   Read today's full daily log at private project notes/ops/daily/[today].md.
   Compile a reflection summary:
   - Count activities by area (Business/Health/Family/Focus)
   - Count activities by direction (forward/neutral/backward)
   - Calculate time spent in each direction
   - Calorie total vs target (from MEMORY.md)
   - Steps vs target (from MEMORY.md)
   - 70/20/10 distribution of activities
   - Top 3 wins (Gain perspective)
   Save to .tmp/daily-reflection.md
   ```

2. Present the reflection to the user:
   - Lead with wins (Gain perspective, not Gap)
   - Show forward/neutral/backward breakdown
   - Show calorie and step totals
   - Show 70/20/10 distribution
   - Note any constraints or patterns

3. **Business plan progress check:**
   - Read `private project plans/implementation-plan-2026-Q1-Q3.md`
   - Check today's Big-3 against implementation plan items
   - Report: which action items were progressed, which deadlines are approaching
   - Flag any overdue items

4. **Longevity scorecard** (mandatory, daily):
   Read `private project notes/personal/health/longevity-plan-2026-03-21.md` and score today:
   - Sleep: What time did you go to bed? How many hours? (target: <11:30 PM, 7+ hours)
   - Movement: Steps + gym session? (target: 10K+ steps, gym on gym days)
   - Nutrition: Calories, protein, carbs, sugar? (target: <1800 cal, 150g+ protein, <50g carbs, zero sugar)
   - Screen time: Total hours? (target: <4h)
   - Supplements: All taken? (Mag at 10-11 PM, L-Theanine at 10:30 PM, rest AM)
   - What longevity phase are we in? What was today's specific longevity action? Did it happen?
   - Score each area 1-5. Report total out of 30. Compare to previous days' trend.
   - **If bedtime was after midnight: call it out directly.** "You went to bed at [time]. That's [X] hours past curfew. This is the #1 thing holding back every other health goal."

5. **Tracking completeness check** (mandatory):
   - Meals logged? (breakfast, lunch, dinner) -- if missing, ask NOW
   - Fitness activity screenshot received? -- if missing, ask NOW
   - Sleep data from last night? -- if missing, note for tomorrow morning
   - Any business metrics/stats shared today?
   - Longevity action item completed? -- if missing, flag it

6. Ask: "Anything to add or correct?"

7. Ask: "What's your key intention for tomorrow?" (suggest the next longevity action if today's was missed)

7. Update the Evening Reflection section in today's daily log with:
   - Wins
   - Activity classification
   - 70/20/10 check
   - Business plan items completed
   - Tracking gaps (what was missed)
   - Tomorrow's focus and intention

8. **Update HISTORY.md** (MANDATORY):
   - Prepend a new entry to the TOP of `private project notes/HISTORY.md` (newest first)
   - Format: `## YYYY-MM-DDTHH:MM:SS-05:00 -- Daily Reflection`
   - Summarize the day: key wins, metrics, decisions, files created/updated
   - Keep it concise -- bullet points, not paragraphs

### Reflection Style

Be honest but encouraging. Use Gain perspective (measure backward from
where you started, not forward from the ideal). If the day was rough,
acknowledge it and focus on what WAS accomplished, not what wasn't.

---

## Mode 5: Good Night

**Trigger:** User says "good night," "спокойной ночи," "going to sleep,"
or similar end-of-day message.

**First:** Read `private project notes/MEMORY.md` for health targets, timezone, and preferences.
Always display times in the user's timezone.

### Process

1. If daily reflection hasn't happened, offer a quick version:
   "Want a quick reflection before bed, or just close out the day?"

2. **Final tracking check** (MANDATORY before closing the day):
   - Verify all meals logged (breakfast, lunch, dinner). If missing, ask: "What did you have for [meal]?"
   - Verify fitness activity data received (steps, activity rings). If missing: "Send me your activity screenshot!"
   - Verify sleep data was logged this morning. If not: "Don't forget to send sleep data tomorrow morning."
   - Check implementation plan: "Did you make progress on [today's Big-3 items]? What happened?"
   - **Longevity bedtime check:**
     - Note the current time. If before curfew: "Good. You're going to bed on time. That's the win."
     - If after curfew: "It's [time]. You're [X] minutes/hours past curfew. Note it. Do better tomorrow. DFQ."
     - Remind: "Magnesium at 10-11 PM. L-Theanine at 10:30 PM. Phone in the other room. No screens."
     - If gym day and no gym logged: "Gym didn't happen today. Tomorrow?"
     - Log today's longevity score (sleep timing, movement, nutrition adherence, screen time, supplements)

3. Finalize the daily log -- fill any gaps in the Evening Reflection section

4. **Auto-carryover**: Read today's Big-3 and check which items are not
   marked as "done" in the Time Log. Save incomplete items to
   `private project notes/ops/state/carryover.md` so tomorrow's Morning Prep can pre-populate them
   as candidate Big-3 items. Also carry over any incomplete implementation
   plan items that were in today's Big-3.

5. **Delegate to subagent** (Task tool, general-purpose):
   ```
   Read today's daily log at private project notes/ops/daily/[today].md.
   Write a 3-5 line daily summary capturing the essence of the day.
   Also update the YAML frontmatter with final values:
   calories, steps, forward_pct, big3_complete, sleep_hours.
   Save summary to private project notes/ops/daily/[today]-summary.md
   ```

6. Set `private project notes/ops/state/awake-state.md` to:
   ```
   status: asleep
   wake_time: [today's wake time]
   last_checkin: [current time]
   ```

7. Respond: "Day logged. Rest well. I'll be here when you say good morning."

---

## File Paths Reference

| Path | Purpose |
|------|---------|
| `private project notes/ops/daily/YYYY-MM-DD.md` | Daily log (one per day, with YAML frontmatter for Obsidian Dataview) |
| `private project notes/ops/daily/templates/daily-log.md` | Daily log template |
| `private project notes/ops/daily/templates/weekly-review.md` | Weekly review template |
| `private project notes/ops/daily/weekly/YYYY-Www.md` | Weekly reviews |
| `private project notes/personal/health/food-log/YYYY-MM-DD.md` | Detailed food entries |
| `private project notes/personal/health/weight/log.md` | Running weight log |
| `private project notes/personal/health/steps/YYYY-MM.md` | Monthly step data |
| `private project notes/personal/health/workouts/YYYY-MM.md` | Monthly workout log |
| `private project meetings/raw/` | Raw meeting notes |
| `private project meetings/summaries/` | Processed meeting summaries with action items |
| `private project misc/knowledge/` | Persistent work knowledge base (processes, reference data) |
| `private project misc/links/` | Work-related saved links |
| `private project notes/personal/links/` | Personal saved links |
| `private project documents/` | Business documents |
| `private project notes/ops/state/awake-state.md` | Awake/asleep state |
| `private project notes/ops/state/carryover.md` | Incomplete Big-3 items carried to next day |
| `private project notes/personal/health/longevity-plan-2026-03-21.md` | 90-day longevity plan (Mar 21 - Jun 19, 2026) |
| `private project notes/personal/health/lab-analysis-summary.md` | Lab report analysis with trends and critical findings |
| `.tmp/morning-brief.md` | Morning briefing (temp) |
| `.tmp/daily-reflection.md` | Reflection data (temp) |

## Frameworks Referenced

- **Gain vs Gap** (Dan Sullivan): Measure progress backward from where you
  started, not forward from the ideal. Celebrate what was accomplished.
- **70/20/10**: 70% scaling what works, 20% improving what works, 10% new things
- **Theory of Constraints**: Identify the one bottleneck limiting throughput
- **Who Not How**: Focus on finding the right person/tool, not the method
- **10x Thinking** (Dan Hardy/Sullivan): Think in terms of 10x, not 2x
