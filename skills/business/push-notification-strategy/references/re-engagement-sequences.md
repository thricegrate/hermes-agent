# Re-engagement Sequences

Complete escalation flows, win-back copy, and rules for when to stop sending notifications to disengaged users.

---

## The Escalation Framework

Re-engagement is a 5-stage sequence triggered when a user stops completing their daily lesson. Each stage has a specific goal, tone, and notification.

```
Timeline:

Day 0:  User completes lesson (last active day)
Day 1:  MISS — no lesson completed
Day 2:  Stage 1: Light Touch
Day 3:  Stage 2: Value Reminder
Day 4-6: Silence (let them breathe)
Day 7:  Stage 3: Fresh Start
Day 8-13: Silence
Day 14: Stage 4: Final Touch
Day 15-28: Stage 5: Reduced Frequency (1/week)
Day 29+: Stop notifications. Move to email-only.
```

**Total push notifications over 28 days: 7-8** (4 in the escalation sequence + 3-4 weekly touches)

---

## Stage 1: Light Touch (Day 2)

### Goal
Gently remind without pressure. Many users miss one day and return on their own. This is a safety net.

### Timing
- Send at the user's habitual learning time
- If they didn't have a habitual time yet (< 5 days of data), send at 10:00 AM local

### Copy Options

**Option A (soft reminder):**
```
Title: We missed you today
Body:  Your next AI lesson is ready whenever you are. Just 2 minutes.
Action: [Continue Learning]
```

**Option B (progress reference):**
```
Title: Your progress is waiting
Body:  {name}, you've completed {lessons_completed} lessons. Ready for the next one?
Action: [Pick Up Where You Left Off]
```

**Option C (streak-aware, if streak was active):**
```
Title: Your streak took a pause
Body:  No worries — you can start a new one today. Your {lessons_completed} lessons are still on your record.
Action: [Start a New Streak]
```

### Rules
- Do NOT mention the missed day as a failure
- Do NOT say "you missed yesterday" or "you broke your streak" — they know
- DO reference their total progress (it never resets, even if the streak did)
- Keep it under 80 characters in the body

---

## Stage 2: Value Reminder (Day 3)

### Goal
Remind the user WHY they signed up. Reconnect them with their original motivation.

### Timing
- Same habitual time, or 30 minutes earlier (slightly more urgency)

### Copy Options

**Option A (goal reminder, if quiz data exists):**
```
Title: Remember your goal?
Body:  You told us you wanted to {quiz_goal}. Today's lesson gets you closer.
Action: [Continue Your Journey]

{quiz_goal} examples:
- "save time at work with AI"
- "learn to create AI images"
- "understand AI before it's too late"
- "boost your income with AI skills"
```

**Option B (content tease):**
```
Title: Today's lesson: {lesson_title}
Body:  Learn {lesson_hook} in under 2 minutes. It's one of our most popular.
Action: [Start Lesson]

{lesson_hook} examples:
- "how to make ChatGPT write like you"
- "the AI tool that transcribes meetings for free"
- "how to generate professional images in 30 seconds"
```

**Option C (social proof):**
```
Title: {daily_count} learners completed today
Body:  {name}, others are building their AI skills. A 2-minute lesson keeps you in the game.
Action: [Join Today's Learners]
```

### Rules
- Use quiz data if available (personalized goal reminders convert 25-40% higher than generic)
- If no quiz data, use content tease (specific lesson title/hook)
- Social proof as fallback if neither is available

---

## Stage 3: Fresh Start (Day 7)

### Goal
Acknowledge the absence and offer a clean reset. By day 7, the user has consciously decided not to engage. Pretending nothing happened feels tone-deaf.

### Timing
- 10:00 AM local time (fresh morning energy)
- Monday or Tuesday if possible (start-of-week reset psychology)

### Copy Options

**Option A (fresh start):**
```
Title: Fresh start?
Body:  It's been a week. We picked an easy lesson for your comeback — just 90 seconds.
Action: [Start Fresh]
```

**Option B (low commitment):**
```
Title: Just one lesson
Body:  {name}, forget the streak, forget the score. Just try one lesson today and see how it feels.
Action: [Try One Lesson]
```

**Option C (reverse psychology — adapted from Duolingo):**
```
Title: We'll stop bugging you
Body:  If now isn't the right time, no pressure. We'll check in less often. Your progress is saved.
Action: [Come Back] [That's OK]
```

### Rules
- Option C is powerful but risky. Test it against A/B before rolling out broadly.
- Acknowledge the absence directly. "It's been a week" is honest.
- Lower the commitment bar: "just one lesson," "just 90 seconds," "just try it"
- If user has a long history (20+ lessons completed), reference it: "Your 23 completed lessons aren't going anywhere."

---

## Stage 4: Final Touch (Day 14)

### Goal
One last notification before stepping back. This is the "we respect your decision" message. It must leave the door open without begging.

### Timing
- 10:00 AM local time
- Any day of the week

### Copy Options

**Option A (respectful retreat):**
```
Title: Still here when you're ready
Body:  We'll send fewer reminders from now on. Your progress is saved — come back anytime.
Action: [Return to Learning]
```

**Option B (progress summary):**
```
Title: Your AI learning journey so far
Body:  {lessons_completed} lessons completed. Level {level}. {badges_earned} badges. Pick up where you left off anytime.
Action: [See My Progress]
```

**Option C (one surprising fact):**
```
Title: Did you know?
Body:  Since you started learning, {fact_about_ai}. Stay sharp — your next lesson awaits.
Action: [Learn More]

{fact_about_ai} examples:
- "AI can now generate videos from text descriptions"
- "Companies are paying 30% more for AI-skilled workers"
- "ChatGPT added 3 new features you haven't tried yet"
```

### Rules
- This is the LAST proactive push for two weeks. Make it count.
- Never use guilt: not "You're falling behind" or "Your skills are getting rusty"
- After this notification: move to Stage 5 (reduced frequency)

---

## Stage 5: Reduced Frequency (Day 15-28)

### Goal
Maintain minimal presence without annoying. One notification per week, each with a specific hook.

### Schedule

| Day | Notification | Hook |
|-----|-------------|------|
| 15-21 (Week 3) | 1 notification | New content: "New lesson: {title}" |
| 22-28 (Week 4) | 1 notification | Milestone of peers: "{count} learners graduated this week" |

### Copy Templates

**Week 3:**
```
Title: New: {lesson_title}
Body:  Fresh content just added. Worth 2 minutes of your time.
Action: [Check It Out]
```

**Week 4:**
```
Title: {count} learners graduated this week
Body:  The 28-day challenge is still open. Ready to get back to it?
Action: [Resume Challenge]
```

### After Day 28
- **Stop all push notifications.** The user has made their choice.
- Move to email-only re-engagement (monthly, for up to 90 days)
- If user returns organically after day 28: treat as a new user for notification purposes (restart with light daily reminders)

---

## Special Sequences

### Post-Streak-Loss Sequence

When a user loses a streak they've held for 7+ days, run a special 48-hour recovery sequence:

```
Hour 0:    Streak breaks at midnight
Hour 8:    "Your streak took a break. Your record was {streak_count} days — that's impressive."
Hour 24:   "Day 1 of your next streak starts with one lesson. Your knowledge didn't reset."
Hour 48:   (If not returned) Roll into standard Day 3 re-engagement
```

**Key insight:** Users who lose long streaks are at extreme churn risk. The 48-hour window is critical. If they don't return within 48 hours of a streak loss, they follow the same trajectory as any other churned user.

### Post-Milestone-Then-Drop Sequence

When a user achieves a milestone (badge, level up, 28-day completion) and then stops engaging:

```
Day 2 after milestone: "Congrats again on {milestone}! Ready for what's next?"
Day 5: "You finished {milestone} — but there's more to explore. Check out {next_content}."
Day 10: "Your {milestone} was impressive. Come back and see what others are working on."
```

**Key insight:** Post-milestone drop-off is common. The user achieved their goal and has no new one. The sequence must establish a NEW goal to re-engage them.

### Free-to-Premium Upsell Integration

Notifications should NEVER be primarily about upselling. But re-engagement sequences can include a premium offer when appropriate:

```
Day 7 re-engagement (free user who hit the paywall before leaving):
Title: Welcome back offer
Body:  {name}, we saved your progress. Start your free trial and pick up where you left off — no interruptions.
Action: [Start Free Trial] [Continue Free]
```

**Rules:**
- Only offer premium in re-engagement if the user previously saw or interacted with the paywall
- Always include a free option alongside the premium CTA
- Never make the re-engagement notification ONLY about payment
- Max 1 upsell notification per re-engagement sequence

---

## Copy Principles

### Tone Progression

| Stage | Tone | Feels Like |
|-------|------|-----------|
| Light Touch | Warm, casual | A friend texting "Hey, you coming?" |
| Value Reminder | Motivating, specific | A coach saying "Remember why you started" |
| Fresh Start | Honest, low-pressure | A gym buddy saying "No judgment, let's just go once" |
| Final Touch | Respectful, door-open | A mentor saying "I'll be here when you're ready" |
| Reduced | Informational only | A newsletter with relevant updates |

### Words to Use

- "Ready" (empowering — puts the user in control)
- "Whenever" (no pressure, no deadline)
- "Your progress" (it's theirs, it still exists)
- "Just 2 minutes" (low commitment)
- "Pick up where you left off" (continuity, not restart)

### Words to Avoid

- "You missed..." (accusatory)
- "You failed..." (judgmental)
- "You need to..." (bossy)
- "Don't forget..." (patronizing)
- "We're disappointed..." (guilt — save for parody, not product)
- "Last chance..." (unless it genuinely is — false urgency erodes trust)
- "Act now..." (salesy, not appropriate for learning apps)

---

## When to Stop: The Notification Sunset Rule

### Hard Stops

| Condition | Action |
|-----------|--------|
| User disables notifications at OS level | Stop immediately. You have no choice. |
| User taps "Unsubscribe" or "Stop" in any notification | Stop immediately. Respect the request. |
| 28 days of zero engagement + zero notification opens | Stop all push. Move to email-only. |
| User uninstalls the app | Push delivery will fail. Clean from notification queue. |

### Soft Stops

| Condition | Action |
|-----------|--------|
| 5 consecutive notifications with no open | Reduce to 1/week for 2 weeks, then stop |
| User opens notifications but doesn't complete lessons | Continue sending, but switch to Facilitator type (make it easier, shorter) |
| User completes after re-engagement | Reset to normal daily reminder cadence. They're back. |

### The Re-engagement ROI Cutoff

Track the cost-per-reactivated-user for each stage:

| Stage | Typical Reactivation Rate | Worth It? |
|-------|--------------------------|----------|
| Day 2 (Light Touch) | 30-45% return | Absolutely |
| Day 3 (Value Reminder) | 15-25% return | Yes |
| Day 7 (Fresh Start) | 8-15% return | Yes |
| Day 14 (Final Touch) | 3-8% return | Borderline |
| Day 15-28 (Weekly) | 1-3% return | Only if notification infra is free |
| Day 29+ (Email only) | 0.5-2% per email | Yes, email is cheap |

**Key insight:** The overwhelming majority of re-engagement happens in the first 7 days. After that, each additional touchpoint has sharply diminishing returns. Invest your effort in perfecting Stages 1-3, not in increasingly desperate Stage 4-5 messaging.

---

## Implementation Checklist

When building the notification system:

- [ ] User timezone captured at signup (from device/browser)
- [ ] Habitual usage time tracked (median of last 5 session start times)
- [ ] Notification preferences screen (daily reminder on/off, time picker)
- [ ] Streak-risk detection running on backend (checks at streak_expiry - 6h and - 3h)
- [ ] Deep links configured for every notification type
- [ ] Frequency cap enforcement on backend (not just client-side)
- [ ] Quiet hours enforced (8am-9pm local time only)
- [ ] Opt-out honored immediately (< 1 minute propagation)
- [ ] Analytics tracking: sent, delivered, opened, converted (lesson completed)
- [ ] A/B test framework for copy variants
- [ ] Stage progression tracked per user (what stage of re-engagement are they in?)
- [ ] Sunset rule automated (stop after 28 days of zero engagement)
