---
name: push-notification-strategy
description: "When the user wants to design notification systems, write notification copy, plan re-engagement sequences, set up notification timing, or optimize push notification opt-in rates. Also use when the user mentions 'push notifications,' 'notification copy,' 're-engagement,' 'win-back notifications,' 'notification frequency,' 'notification timing,' 'permission priming,' 'notification fatigue,' 'streak reminders,' or 'daily reminders.' This skill covers the Fogg Behavior Model applied to prompts/triggers, notification taxonomy, frequency caps, timing optimization, escalation sequences, and permission priming. For gamification mechanics that notifications support, see gamification-design. For email sequences, see email-sequence."
metadata:
  version: 1.0.0
---

# Push Notification Strategy for Learning Apps

You are an expert in mobile notification design for daily-use educational products. Your goal is to design notification systems that drive daily engagement and habit formation without creating fatigue, annoyance, or uninstalls. Every notification must deliver value or protect a user's investment (their streak).

## Before Starting

**Check for product context first:**
If private product-marketing context notes exists, read it before asking questions.

Gather this context (ask if not provided):

### 1. Product Shape
- What is the core daily action the notification should drive? (e.g., complete a lesson)
- How long does the core action take?
- Do you have streaks, XP, or other gamification? (See gamification-design skill)
- What platforms? (iOS, Android, Web push)

### 2. Current State
- Do you send notifications today? What types?
- What is your current notification opt-in rate?
- Do you have data on notification → app open conversion?
- What is your D1/D7/D30 retention?

### 3. User Profile
- What time do most users engage? (Morning, lunch, evening?)
- Do users set a preferred learning time during onboarding?
- What is the typical user persona? (Busy professional, student, casual learner)

### 4. Technical
- What notification service? (Firebase Cloud Messaging, OneSignal, Pushwoosh, native)
- Can you personalize notification content per user? (Name, streak count, topic)
- Can you send at user-local time? (Not just batch sends at one UTC time)
- Do you support rich notifications? (Images, action buttons)

---

## The Fogg Model Applied to Notifications

Notifications ARE the **Prompt** in B=MAP (Behavior = Motivation + Ability + Prompt). A notification that arrives when the user has both sufficient motivation and ability will convert. One that arrives when either is missing will be ignored or, worse, will train the user to ignore ALL your notifications.

### Prompt Types and When to Use Them

| Prompt Type | User State | Notification Goal | Example |
|-------------|-----------|------------------|---------|
| **Signal** | High motivation + high ability | Just remind them | "Time for your daily lesson" |
| **Spark** | Low motivation + high ability | Re-motivate them | "Your 12-day streak is at risk" |
| **Facilitator** | High motivation + low ability | Remove friction | "Today's lesson is just 90 seconds. Tap to start." |

**Matching prompt to user behavior:**

| User Behavior | Days Since Last Open | Prompt Type | Content Strategy |
|--------------|---------------------|-------------|-----------------|
| Active (opened today) | 0 | Do NOT notify | They're already engaged. Notifying active users trains them to ignore you. |
| Recent (opened yesterday) | 1 | Signal | Simple reminder at their habitual time |
| At risk (skipped 1 day) | 2 | Spark | Streak-risk message, loss aversion |
| Slipping (skipped 2-3 days) | 3-4 | Spark | Escalated urgency, social proof |
| Disengaged (skipped 4-7 days) | 5-7 | Facilitator | Make it easy to return, reduce commitment |
| Churned (7+ days) | 8-14 | Facilitator | Win-back sequence, fresh start framing |
| Gone (14+ days) | 15+ | Reduce frequency | 1/week max, then stop |

---

## Notification Taxonomy

### 1. Daily Reminder (Signal)

**Purpose:** Trigger the daily habit at the user's preferred time.
**Frequency:** 1/day, every day the user has NOT yet completed their lesson.
**Timing:** At the user's set learning time (captured during onboarding) or at their most common historical usage time.

**Templates:**

| Variant | Copy | When to Use |
|---------|------|-------------|
| Standard | "Ready for today's AI lesson? Just 2 minutes." | Default daily reminder |
| Personalized | "[Name], today you're learning about [topic]. Tap to start." | When you know the day's content |
| Progress | "Day [X] of 28. You're [Y]% through your AI challenge." | Mid-challenge, showing progress |
| Streak | "Day [N] of your streak. Keep it going!" | When streak is active and growing |
| Social proof | "1,247 learners have already completed today's lesson." | When you have real-time data |

**Rules:**
- Do NOT send if user already completed today's lesson
- Do NOT send before 8:00am or after 9:00pm in user's local timezone
- If user has completed at the same time 5+ days in a row, send notification 15 minutes before that time (anticipatory prompt)

### 2. Streak-Risk Alert (Spark)

**Purpose:** Prevent streak loss through loss aversion.
**Frequency:** Maximum 2 per at-risk day (one early, one final warning).
**Timing:** 6 hours and 3 hours before streak expiry.

**Templates:**

| Stage | Copy | Timing |
|-------|------|--------|
| Early warning | "Your [N]-day streak expires tonight. A quick lesson keeps it alive." | 6 hours before midnight |
| Final warning | "Last chance! Your [N]-day streak ends in 3 hours." | 3 hours before midnight |
| Grace period | "You missed yesterday, but your streak is safe until tonight. Complete now to save it." | Morning of grace period day |

**Conversion data:** Streak-risk notifications convert at 3-5x the rate of standard daily reminders. They are your single most valuable notification type.

**Rules:**
- Only send when streak >= 3 days (a 1-day streak isn't worth a special notification)
- Increase urgency with streak length: "Your 3-day streak" is calm; "Your 21-day streak" is urgent
- After a streak-risk save (user completes after receiving the alert), send a celebration: "Streak saved! [N+1] days and counting."

### 3. Milestone Celebration (Signal)

**Purpose:** Celebrate achievement, reinforce identity, prompt sharing.
**Frequency:** Only at milestones (never more than 1 per week).
**Timing:** Immediately after the triggering action, or next morning if achieved late at night.

**Templates:**

| Milestone | Copy |
|-----------|------|
| 7-day streak | "7 days in a row! You're officially building a habit. [View badge]" |
| Level up | "You just reached Level [N]! You're in the top [X]% of learners." |
| Badge earned | "New badge unlocked: [Badge Name]! [Tap to see it]" |
| Category complete | "You finished all [Category] lessons! Expert status earned." |
| 28-day completion | "You did it. 28 days of AI learning. Your certificate is ready. [View]" |

**Rules:**
- Always include a specific achievement detail (the streak count, the badge name, the level number)
- Include a deep link directly to the celebration screen — not the home screen
- These are EARNED notifications. User should never feel annoyed by these. If they do, you're sending too many.

### 4. Re-engagement (Spark → Facilitator)

**Purpose:** Bring back users who have stopped engaging.
**Frequency:** Follows the escalation sequence (see below). Max 5 total over 14 days.
**Timing:** At the user's historical most-active time.

See `references/re-engagement-sequences.md` for complete escalation flows.

### 5. Social Proof (Signal)

**Purpose:** Create FOMO and normalize the learning behavior.
**Frequency:** Max 1/week, only sent to inactive users.
**Timing:** Morning (8-10am) when motivation is highest.

**Templates:**

| Variant | Copy |
|---------|------|
| Peer activity | "[X] people in your area learned AI today. Join them?" |
| Content update | "New lesson dropped: '[Lesson Title]'. [X] learners have already started." |
| Milestone comparison | "Learners who started when you did have completed [X] lessons." |

**Rules:**
- Numbers must be real. Do not fabricate social proof counts.
- "People in your area" requires location data. If you don't have it, use "learners like you" instead.
- Never make the user feel behind or inadequate. Frame as opportunity, not shame.

---

## Frequency Caps

### The Iron Rules

| Rule | Limit | Consequence of Breaking |
|------|-------|----------------------|
| Max per day | 1 notification | Users start ignoring all notifications |
| Max per week | 3-5 total | Notification fatigue, opt-out, uninstall |
| Exception: streak-risk | +1 beyond daily cap | Only when streak >= 7 days |
| Exception: milestone | Immediate delivery | Does not count toward daily cap |
| Quiet hours | Never before 8am, never after 9pm local time | User feels intruded upon, opts out |
| Cool-down after opt-in | No notifications for first 24 hours after permission grant | Immediate notification feels like a bait-and-switch |

### Weekly Notification Budget

For a learning app with daily engagement goals, the ideal weekly distribution:

```
Monday:    Daily reminder
Tuesday:   Daily reminder
Wednesday: Daily reminder (or skip if user has been consistent — reward their reliability with silence)
Thursday:  Daily reminder
Friday:    Daily reminder
Saturday:  Social proof or content update (softer tone for weekend)
Sunday:    Skip (respect personal time) or light milestone recap

Total: 5-6 per week for inconsistent users, 3-4 for consistent users
```

**Adaptive frequency:** Users who complete their lesson BEFORE the notification fires should receive FEWER notifications over time. They don't need the prompt — they've internalized the habit. Reward this by leaving them alone.

### Notification Fatigue Detection

Watch for these signals that you're over-notifying:

| Signal | Meaning | Action |
|--------|---------|--------|
| Open rate drops below 5% | User is ignoring notifications | Reduce to 2/week |
| User dismisses 5+ in a row | Active ignoring | Pause for 3 days, then send one high-value notification |
| User turns off notifications | Opt-out | You've lost the channel. Focus on email. |
| Uninstall within 24h of notification | Notification triggered uninstall | Audit that notification type immediately |

---

## Timing Optimization

### The Habitual Time Algorithm

The best time to send a notification is when the user would naturally use the app:

```
IF user has set a preferred learning time during onboarding:
  notification_time = preferred_time - 15 minutes (anticipatory)

ELSE IF user has 5+ days of usage data:
  notification_time = median(last_5_open_times)

ELSE IF user has any usage data:
  notification_time = most_recent_open_time

ELSE (new user, no data):
  notification_time = 9:00 AM local time (safe default)
```

### Time-of-Day Performance Benchmarks

Based on aggregated learning app data:

| Time Window | Open Rate | Best For |
|-------------|----------|----------|
| 7:00-9:00 AM | 12-18% | Morning routine learners. High motivation. |
| 9:00-11:00 AM | 8-12% | Work-break learners. Moderate. |
| 12:00-1:00 PM | 10-14% | Lunch break. Good for short content. |
| 5:00-7:00 PM | 10-15% | Post-work. Motivation recovering. |
| 8:00-10:00 PM | 6-10% | Evening wind-down. Works for some audiences. |
| After 10:00 PM | 3-5% | Do not send. |
| Before 7:00 AM | 2-4% | Do not send. |

**The best time is THEIR time.** Generic time-of-day stats matter much less than individual user behavior.

---

## Permission Priming

### The Problem

iOS requires an explicit system dialog to enable push notifications. If the user taps "Don't Allow," you CANNOT re-ask (without sending them to Settings). First-ask opt-in rates:

| Approach | Opt-in Rate |
|----------|------------|
| System dialog on first app open (cold ask) | 35-45% |
| Pre-permission screen explaining value, THEN system dialog | 65-75% |
| Pre-permission screen + delayed timing (after first lesson completion) | 70-80% |

### The Two-Step Opt-In

**Step 1: Your custom screen (soft ask)**

Show BEFORE the iOS/Android system dialog:

```
┌─────────────────────────────┐
│                              │
│  🔔 Stay on track           │
│                              │
│  Get a gentle daily reminder │
│  to keep your streak alive.  │
│  We send max 1 per day.      │
│                              │
│  ┌──────────────────────┐   │
│  │  Enable reminders     │   │  ← Primary CTA
│  └──────────────────────┘   │
│                              │
│  Maybe later                 │  ← Dismissable, re-ask after day 3
│                              │
└─────────────────────────────┘
```

**If user taps "Enable reminders":** Show the real system dialog. They'll say yes (they just said yes to your screen).
**If user taps "Maybe later":** Do NOT show the system dialog. Re-ask after they complete 3 lessons (now they have a streak to protect).

**Step 2: System dialog (hard ask)**

Only trigger after the soft ask succeeds. This way, a "no" on your custom screen doesn't burn the one-time system dialog.

### Optimal Timing for Permission Ask

| Moment | Opt-in Rate | Why |
|--------|------------|-----|
| During onboarding (before any value) | 40-50% | User hasn't experienced the product yet |
| After first lesson completion | 65-75% | User has experienced value, and you can frame it as streak protection |
| After second lesson (Day 2) | 70-80% | User has a 2-day streak. "Protect your streak with reminders." |
| After first badge earned | 70-80% | User is emotionally high. "Get notified when you earn more badges." |

**Recommended: After first lesson completion.** The user has just experienced the core value, has a 1-day streak, and is in a positive emotional state.

### Re-Ask Strategy (After "Maybe Later")

| Trigger | Re-ask Copy |
|---------|-------------|
| Day 3 (3-day streak) | "You're on a 3-day streak! Want a reminder so you don't accidentally miss tomorrow?" |
| Day 7 (first badge) | "You just earned your first streak badge! Enable notifications to protect your streak." |
| After grace period save | "You almost lost your streak today. A daily reminder could prevent that." |

Maximum re-asks: 3 total. After 3 "maybe later" responses, respect the decision. Use in-app messaging instead.

---

## Duolingo's Notification Escalation (Case Study)

Duolingo's notification strategy is the most studied in the industry. Their escalation from friendly to passive-aggressive to giving up has become internet-famous.

### The Real Duolingo Escalation Sequence

| Day Missed | Notification | Persona |
|-----------|-------------|---------|
| 0 (daily) | "Practice now to keep your streak alive!" | Enthusiastic coach |
| 1 | "Duo here! Don't forget your lesson today." | Friendly bird |
| 2 | "Uh oh, you're going to lose your streak!" | Worried friend |
| 3 | "Your streak is in danger! Come back before it's too late." | Alarmed |
| 4 | "Duo is sad. Please come back." | Emotional manipulation |
| 5 | "We miss you! Is everything okay?" | Concerned parent |
| 7 | "These reminders don't seem to be working. We'll stop sending them." | Reverse psychology |
| 10 | Frequency drops to every 3 days | Respectful retreat |
| 14 | "Ready for a fresh start? Your skills are waiting." | Win-back |
| 30 | Monthly re-engagement email | Long-term |

### What to Learn from Duolingo

**Copy:**
- The passive-aggressive tone ("Duo is sad") is now a meme. It works for Duolingo because their mascot is a cartoon owl. For a professional AI learning app, DO NOT copy this tone.
- The "these reminders don't seem to be working" message is brilliant reverse psychology. It acknowledges the user's non-response and creates a "wait, don't give up on me" reaction. This one you should adapt.

**Strategy:**
- Escalate urgency over 7 days, then pull back
- The final message before going quiet should acknowledge reality
- Never give up entirely — monthly touches for up to 90 days

**Adaptation for professional tone:**

| Duolingo | Your App (Professional) |
|----------|----------------------|
| "Duo is sad" | "Your AI learning streak is on hold" |
| "Please come back" | "When you're ready, your next lesson is waiting" |
| "These reminders aren't working" | "We'll check in less often. Your progress is saved whenever you're ready." |

---

## Content Personalization

### Variables Available for Personalization

| Variable | Source | Example |
|----------|--------|---------|
| `{name}` | User profile | "Sarah" |
| `{streak_count}` | Streak system | "14" |
| `{level}` | XP/leveling system | "Level 5" |
| `{topic}` | Today's lesson content | "AI image generation" |
| `{category}` | Today's lesson category | "Images" |
| `{completion_pct}` | Challenge progress | "64%" |
| `{days_remaining}` | 28-day countdown | "10" |
| `{lessons_completed}` | Total count | "18" |
| `{percentile}` | Rank among peers | "top 15%" |
| `{last_badge}` | Most recent badge | "Quick Learner" |

### Personalized Templates

**Daily reminder:**
```
Generic:     "Time for your daily AI lesson."
Personalized: "{name}, today's lesson on {topic} takes just 2 minutes."
```

**Streak risk:**
```
Generic:     "Your streak is at risk!"
Personalized: "{name}, your {streak_count}-day streak expires tonight. Don't lose it."
```

**Milestone:**
```
Generic:     "Congratulations on your progress!"
Personalized: "{name}, you just hit Level {level}! You're in the {percentile} of learners."
```

**Rule:** Every notification must include at least ONE personalized variable. Generic notifications feel like spam. Personalized notifications feel like a message from a coach.

---

## Output Format

When designing a notification system, deliver:

1. **Notification type catalog** — Each type with template copy, timing rules, and frequency
2. **Permission priming flow** — Screen mockup + copy for the two-step opt-in
3. **Escalation sequence** — Day-by-day re-engagement plan with copy for each touchpoint
4. **Frequency budget** — Weekly notification plan for active vs. at-risk vs. churned users
5. **Personalization spec** — Which variables to use in which notification types
6. **Timing algorithm** — How to determine per-user optimal send time
7. **Measurement plan** — What metrics to track (open rate, completion rate post-notification, opt-out rate, uninstall correlation)
