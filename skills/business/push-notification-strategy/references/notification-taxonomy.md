# Notification Taxonomy

Complete catalog of notification types for daily-use learning apps, with templates, timing rules, and frequency limits.

---

## Type 1: Daily Reminder

### Purpose
Trigger the core daily action (lesson completion) at the optimal moment.

### Timing Rules
- Send at user's habitual usage time minus 15 minutes (anticipatory)
- If no usage data: 9:00 AM local time
- Never before 8:00 AM or after 9:00 PM local time
- Do NOT send if user has already completed today's lesson
- Suppress if user opened the app within the last 2 hours (they're aware)

### Frequency
- 1/day maximum
- Skip days where user has been consistent for 7+ straight days (reward reliability with silence — send on day 8 if they didn't organically complete by their usual time)

### Copy Templates

**Standard:**
```
Title: Time to learn
Body:  Your daily AI lesson is ready. Just 2 minutes.
CTA:   [Start Lesson] (deep link to today's lesson)
```

**Personalized (topic-aware):**
```
Title: Today: {topic}
Body:  {name}, learn how to use {tool_name} in 2 minutes.
CTA:   [Start Lesson]
```

**Progress-aware:**
```
Title: Day {day_number} of 28
Body:  You're {completion_pct}% through your AI challenge. Keep going.
CTA:   [Continue]
```

**Streak-aware:**
```
Title: Day {streak_count + 1} awaits
Body:  Keep your {streak_count}-day streak alive with today's lesson.
CTA:   [Start Lesson]
```

**Social proof:**
```
Title: {count} learners completed today
Body:  Join the {count} people who already learned something new today.
CTA:   [Start Lesson]
```

### A/B Testing Priority
Test these variants in order:
1. Personalized (topic) vs. Standard — typically 20-40% lift in open rate
2. Streak-aware vs. Standard — 15-30% lift for users with active streaks
3. Social proof vs. Standard — 10-20% lift, but requires real-time data

---

## Type 2: Streak-Risk Alert

### Purpose
Prevent streak loss by leveraging loss aversion. This is your highest-converting notification type.

### Timing Rules
- **Early warning:** 6 hours before streak expiry (i.e., 6:00 PM if streak expires at midnight)
- **Final warning:** 3 hours before streak expiry (9:00 PM)
- **Grace period morning:** 9:00 AM on the day after a miss (if grace period is active)
- Only send when streak >= 3 days (a 1-2 day streak isn't worth the notification)

### Frequency
- Maximum 2 per at-risk day (early + final)
- 1 during grace period day
- This type is EXEMPT from the 1/day cap when streak >= 7 days (the investment justifies the extra notification)

### Copy Templates

**Early warning (6 hours):**
```
Title: Streak check
Body:  Your {streak_count}-day streak expires tonight. A quick lesson keeps it alive.
CTA:   [Save Streak]
```

**Final warning (3 hours):**
```
Title: Last chance
Body:  {name}, your {streak_count}-day streak ends at midnight. 2 minutes is all it takes.
CTA:   [Save Streak Now]
```

**Grace period:**
```
Title: Streak still safe — for now
Body:  You missed yesterday, but your {streak_count}-day streak is safe until tonight. Complete a lesson to save it.
CTA:   [Save Streak]
```

**Post-save celebration:**
```
Title: Streak saved!
Body:  {streak_count + 1} days and counting. That was close!
```

### Escalation by Streak Length

| Streak Length | Tone | Copy Style |
|--------------|------|-----------|
| 3-6 days | Casual | "Your streak is at risk. Quick lesson?" |
| 7-13 days | Warm urgency | "Your 10-day streak is worth protecting. Don't let it slip." |
| 14-20 days | Strong urgency | "14 days of learning is an achievement. Don't lose it tonight." |
| 21-27 days | High stakes | "You're days away from completing the challenge. Keep your 23-day streak!" |
| 28+ days | Maximum | "Your {streak_count}-day streak is extraordinary. Only {percentile} of users have one this long." |

---

## Type 3: Milestone Celebration

### Purpose
Celebrate achievements, reinforce identity as a learner, prompt sharing.

### Timing Rules
- Send immediately when the milestone is achieved (within 60 seconds)
- If achieved after 9:00 PM: queue for 8:00 AM next morning
- Deep link directly to the celebration/badge screen

### Frequency
- No cap (milestones are earned, not sent on a schedule)
- In practice: approximately 1 per week for active users

### Copy Templates

**Streak milestone:**
```
Title: 🔥 {streak_count}-day streak!
Body:  {name}, you've learned AI for {streak_count} days straight. Only {percentile} of learners reach this.
CTA:   [View Badge] [Share]
```

**Level up:**
```
Title: Level {level} reached!
Body:  You're making real progress. {level_fact}
CTA:   [See Your Progress]

{level_fact} examples:
- Level 3: "You've completed more than the average learner."
- Level 5: "You're in the top 30% of all learners."
- Level 7: "You know more about AI tools than 80% of people."
```

**Badge unlock:**
```
Title: Badge unlocked: {badge_name}
Body:  {badge_description}
CTA:   [View Badge]
```

**Category completion:**
```
Title: {category} Expert!
Body:  You've completed every lesson in {category}. Badge earned.
CTA:   [View Badge] [Share]
```

**28-day completion:**
```
Title: You did it! 🎓
Body:  28 days of AI learning, complete. Your certificate is ready.
CTA:   [View Certificate] [Share]
```

---

## Type 4: Re-engagement

### Purpose
Bring back users who have stopped engaging. The most delicate notification type — get it wrong and you accelerate the churn.

### Timing Rules
- Send at the user's historical most-active time
- If no data: 10:00 AM local time (mid-morning, after the rush)
- Follow the escalation sequence strictly (see re-engagement-sequences.md)

### Frequency
- Day 1 miss: 1 notification
- Day 3: 1 notification
- Day 7: 1 notification
- Day 14: 1 final notification
- Then stop. Total: 4 notifications over 14 days.

### Copy Templates

**Day 1 (light touch):**
```
Title: We missed you today
Body:  Your next lesson is waiting whenever you're ready. Just 2 minutes.
CTA:   [Continue Learning]
```

**Day 3 (value reminder):**
```
Title: 3 days since your last lesson
Body:  {name}, you've completed {lessons_completed} lessons so far. Don't let that progress fade.
CTA:   [Pick Up Where You Left Off]
```

**Day 7 (fresh start offer):**
```
Title: Fresh start?
Body:  It's been a week. We have a short, easy lesson ready for your comeback.
CTA:   [Start Fresh]
```

**Day 14 (final touch):**
```
Title: Still here when you're ready
Body:  We'll check in less often. Your progress ({lessons_completed} lessons, Level {level}) is saved.
CTA:   [Return to Learning]
```

### Rules
- NEVER use guilt or shame: not "You abandoned your streak" or "You let yourself down"
- ALWAYS acknowledge their past progress: "You've completed X lessons"
- Frame return as easy: "Just 2 minutes" or "one short lesson"
- After day 14: reduce to 1 notification per week for 4 more weeks, then stop entirely
- After 6 weeks of no engagement: move to email-only re-engagement

---

## Type 5: Social Proof

### Purpose
Create positive peer pressure by showing that others are learning.

### Timing Rules
- Morning only (8:00-10:00 AM local time)
- Only send to users who have NOT completed today's lesson
- Only send to users who are between Day 3-14 of their journey (new enough to need social validation)
- Maximum 1 per week

### Frequency
- 1/week maximum
- Do not send in the same week as a re-engagement notification (overlapping persuasion signals cancel each other out)

### Copy Templates

**Peer count:**
```
Title: Join today's learners
Body:  {daily_count} people completed their AI lesson today. Your turn?
CTA:   [Start Lesson]
```

**Peer comparison (use carefully):**
```
Title: Others are ahead — but not by much
Body:  Learners who started when you did have completed {avg_lessons} lessons. You're at {user_lessons}.
CTA:   [Catch Up]
```

**New content:**
```
Title: New lesson: {lesson_title}
Body:  Just dropped. {early_count} learners have already started.
CTA:   [Be One of the First]
```

### Rules
- All numbers MUST be real. Never fabricate counts.
- Peer comparison must never make the user feel hopelessly behind. If they're more than 50% behind the average, don't send this type.
- Test carefully: some audiences respond well to social proof, others find it annoying.

---

## Type 6: Transactional

### Purpose
Communicate system events the user needs to know about.

### Timing Rules
- Send immediately when the event occurs
- No time-of-day restrictions (these are expected)

### Frequency
- No cap (event-driven, infrequent)

### Examples

```
Account:     "Welcome to 3 Minute AI! Your journey starts now."
Streak freeze: "Your streak freeze activated. Your {streak_count}-day streak is safe."
Payment:     "Your subscription renews tomorrow. Manage it anytime in Settings."
Content:     "Your requested certificate is ready to download."
```

### Rules
- Transactional notifications should be clearly informational, not promotional
- Never combine a transactional notification with a promotional CTA
- These are trust-building communications. Keep them clean.

---

## Notification Anatomy

### Structure

```
┌─────────────────────────────────────┐
│ [App Icon]  3 Minute AI    2m ago   │  ← Header (OS-controlled)
│                                      │
│ Title: Your 12-day streak is at risk │  ← 40 chars max (truncated on some devices)
│                                      │
│ Body: Complete a 2-minute lesson     │  ← 100 chars max for reliable display
│ to save your streak. Tap to start.   │
│                                      │
│ [Save Streak]  [Later]              │  ← Action buttons (optional, iOS/Android)
└─────────────────────────────────────┘
```

### Character Limits

| Element | iOS | Android | Recommendation |
|---------|-----|---------|---------------|
| Title | 50 chars visible | 65 chars visible | Keep under 40 |
| Body | 150 chars on lock screen | 240 chars expanded | Keep under 100 for lock screen readability |
| Action buttons | 2 max | 3 max | Use 1-2 |

### Deep Linking

Every notification MUST deep link to a relevant screen:

| Notification Type | Deep Link Target |
|------------------|-----------------|
| Daily reminder | Today's lesson (pre-loaded, ready to start) |
| Streak risk | Today's lesson with streak warning banner |
| Milestone | Celebration/badge screen |
| Re-engagement | Simplified home screen with "welcome back" state |
| Social proof | Today's lesson |

**Never deep link to:** The home screen (generic), a login screen (friction), a paywall (bait and switch), or settings.

---

## Measurement Framework

### Key Metrics by Notification Type

| Metric | Definition | Good | Great |
|--------|-----------|------|-------|
| **Opt-in rate** | % of users who enable notifications | 55% | 70%+ |
| **Open rate** | % of notifications that lead to app open | 8% | 15%+ |
| **Conversion rate** | % of opens that lead to lesson completion | 40% | 60%+ |
| **Opt-out rate** | % of users who disable per month | < 5% | < 2% |
| **Uninstall correlation** | Uninstalls within 24h of notification | < 0.5% | < 0.1% |

### Per-Type Benchmarks

| Type | Expected Open Rate | Expected Conversion |
|------|-------------------|-------------------|
| Daily reminder | 8-15% | 40-55% |
| Streak risk | 20-35% | 55-70% |
| Milestone | 25-40% | N/A (celebration, not action) |
| Re-engagement (Day 1) | 10-18% | 30-40% |
| Re-engagement (Day 7) | 5-10% | 20-30% |
| Re-engagement (Day 14) | 3-6% | 15-25% |
| Social proof | 6-12% | 35-45% |

### Attribution Window

Count a notification as "converted" if the user completes a lesson within 2 hours of opening the notification. Beyond 2 hours, the completion was likely organic, not notification-driven.
