# Permission Priming

## Why Permission Priming Matters

### The iOS Problem
iOS gives you **one shot** at the system notification permission dialog per app install. If the user taps "Don't Allow," the only recovery path is: Settings > Notifications > Your App > Allow Notifications. Research shows **95% of users never do this.**

### The Android Difference
Android 13+ (API 33) introduced a similar runtime permission model for notifications. Prior versions granted notification permission by default. The priming strategy applies to both, but is critical for iOS.

### The Numbers

| Approach | Opt-In Rate | Source |
|----------|-------------|--------|
| Cold system dialog on first open | 35-40% | Industry average, Leanplum 2023 |
| Cold system dialog after onboarding | 45-50% | Slightly better context |
| Pre-primed (custom screen → system dialog) | 70-80% | CleverTap, OneSignal data |
| Pre-primed + value-first timing | 80-85% | Best-in-class (Duolingo, Headspace) |

**Pre-priming doubles your opt-in rate.** For an app where daily notifications are the primary retention mechanism, this is the single highest-leverage UX decision.

---

## The Two-Step Opt-In Pattern

### Step 1: Custom In-App Screen (Soft Ask)

Show a full-screen modal with:
1. **Benefit headline** (not "Allow notifications" — instead "Get your daily lesson reminder")
2. **Visual preview** of what the notification looks like
3. **Social proof stat** ("Users with reminders are 3x more likely to complete the challenge")
4. **Primary CTA:** "Yes, remind me daily"
5. **Secondary CTA:** "Maybe later" (not "No" — reduces finality)

### Step 2: System Dialog (Hard Ask)

Only triggered if the user taps "Yes" in Step 1. This means:
- Users who would tap "Don't Allow" never see the system dialog
- Your system dialog opt-in rate approaches 95%+ (only motivated users see it)
- You preserve the one-shot system dialog for users who actually want notifications

### The Math

```
Without priming:
  100 users → system dialog → 40 allow → 60 blocked forever
  Result: 40% notification reach

With priming:
  100 users → soft ask → 75 tap "Yes" → system dialog → 71 allow
                       → 25 tap "Maybe later" → re-ask Day 3
                       → 15 tap "Yes" on Day 3 → 14 allow
  Result: 85% notification reach
```

---

## Timing: When to Ask

### The Golden Rule
Ask for notification permission **immediately after the user has experienced value**, never before.

### Optimal Timing for 3 Minute AI

```
Timeline:
0s     App opens
5s     Welcome screen
5-100s First lesson (value delivery)
100s   Exercise completed ← USER HAS EXPERIENCED VALUE
100-115s Result reveal + XP
115-125s Celebration animation
125s   ← OPTIMAL PERMISSION ASK WINDOW
130s   Daily reminder time selection
135s   Pre-permission priming screen (if "Yes")
140s   System permission dialog
```

**Why this moment works:**
- User just completed something (accomplishment high)
- User just received XP (positive reinforcement)
- User has seen what a "daily lesson" contains (the ask is concrete, not abstract)
- The transition from "celebration" to "want to do this again tomorrow?" is natural

### When NOT to Ask

| Timing | Why It Fails | Opt-In Rate |
|--------|-------------|-------------|
| First app open, before anything | Zero value context | ~30% |
| During quiz funnel | Interrupts acquisition flow | ~25% |
| During first lesson | Breaks learning flow | ~35% |
| On home screen after lesson | Feels disconnected from the moment | ~45% |
| Days later via banner | Too easy to dismiss | ~20% |

---

## Copy Templates

### Pre-Permission Screen (Day 1, After First Lesson)

**Version A: Benefit-First**
```
Get your daily 3-minute lesson reminder

[Notification Preview]
┌─────────────────────────────┐
│ 3 Minute AI        8:00 AM  │
│ Your lesson is ready:       │
│ "The Tone Dial — control    │
│ how ChatGPT sounds"         │
└─────────────────────────────┘

Users who set a reminder are 3x more
likely to finish the 28-day challenge.

[ Yes, remind me daily ]
       Maybe later
```

**Version B: Streak-First**
```
Keep your streak alive 🔥

You just started a streak! A daily
reminder helps you keep it going.

[Notification Preview]
┌─────────────────────────────┐
│ 3 Minute AI        12:00 PM │
│ Day 2 is ready! Keep your   │
│ streak alive: "Describe     │
│ What You See"               │
└─────────────────────────────┘

[ Set my daily reminder ]
      Maybe later
```

**Version C: Progress-First**
```
You're 1/28 of the way there!

A daily reminder keeps you on track
to earn your AI Skills Certificate.

[Progress bar: 1/28 filled]

[ Remind me to learn daily ]
       Maybe later
```

### Re-Ask Copy (Day 3, After Third Lesson)

```
You're on a 3-day streak!

Most learners who set a reminder
keep their streak all the way to
Day 28. Want to protect yours?

[ Yes, set a reminder ]
      Not right now
```

### Re-Ask Copy (Day 7, Final Ask)

```
7 days straight — you're in the
top 15% of learners!

A daily nudge is the #1 predictor
of completing the full challenge.

[ Remind me at [time] ]
      I'll remember on my own
```

---

## iOS vs. Android Differences

### iOS (14+)

**System dialog:**
```
"3 Minute AI" Would Like to Send
You Notifications

Notifications may include alerts,
sounds, and icon badges. These can
be configured in Settings.

[Don't Allow]  [Allow]
```

**Key constraints:**
- One-shot dialog per app install
- "Don't Allow" = permanent (unless user goes to Settings)
- Provisional notifications available (iOS 12+): delivered silently to Notification Center, no dialog needed
- Consider requesting provisional first, then upgrading to prominent when user is engaged

**Provisional notification strategy:**
1. Day 1: Request provisional permission (no dialog shown, auto-granted)
2. Send silent notifications to Notification Center for Days 1-3
3. Day 3-7: If user engages with a provisional notification, show pre-priming screen to upgrade to prominent (sounds, banners, badges)
4. This gives you a "warm" user for the system dialog

### Android (13+ / API 33+)

**System dialog:**
```
Allow 3 Minute AI to send you
notifications?

[Don't allow]  [Allow]
```

**Key constraints:**
- Runtime permission required (POST_NOTIFICATIONS)
- User can deny twice before "Don't ask again" is auto-checked
- After permanent denial: must redirect to Settings (same as iOS)
- Pre-13: notifications allowed by default, but users can disable in Settings

**Android-specific approach:**
1. Same pre-priming screen as iOS
2. After system allow: create a notification channel named "Daily Lessons"
3. Use exact alarms (AlarmManager) for precise delivery time
4. Fall back to WorkManager for devices that restrict exact alarms

### Web (PWA / Browser)

**Browser dialog:**
```
3minuteai.com wants to
[Show notifications]

[Block]  [Allow]
```

**Key constraints:**
- Browser-specific UI (Chrome, Safari, Firefox differ)
- Safari on iOS does NOT support web push (as of iOS 16.4+, limited support via Add to Home Screen)
- Chrome on desktop: most liberal, supports Service Workers
- User can block at browser level OR OS level

**Web-specific approach:**
1. Do NOT use the browser dialog on page load (Chrome penalizes this)
2. Show custom in-page prompt first
3. Only trigger browser dialog after affirmative in-page response
4. For iOS Safari: prompt user to "Add to Home Screen" first, then enable notifications

---

## Notification Content Templates

### Daily Lesson Reminder

**Morning (8 AM):**
```
Your 3-minute lesson is ready ☀️
"[Lesson Title]" — [1-line benefit]
```

**Lunch (12 PM):**
```
Quick AI lesson with your lunch? 🍽️
"[Lesson Title]" — takes 3 minutes
```

**Evening (7 PM):**
```
End your day 3 minutes smarter 🌙
"[Lesson Title]" — [1-line curiosity hook]
```

### Streak Protection (Sent 2 Hours Before Day Ends)

```
Your [N]-day streak ends at midnight! 🔥
Tap to complete today's 3-minute lesson.
```

### Re-Engagement (Missed 1 Day)

```
We saved your spot on Day [N] 📌
Pick up where you left off — 3 minutes.
```

### Re-Engagement (Missed 3+ Days)

```
Your AI learning path misses you
Resume Day [N]: "[Lesson Title]"
No judgment. Just 3 minutes. →
```

---

## Analytics Events to Track

```
permission_priming_shown         — Pre-permission screen displayed
permission_priming_accepted      — User tapped "Yes, remind me"
permission_priming_declined      — User tapped "Maybe later"
permission_priming_reask_day3    — Re-ask shown on Day 3
permission_priming_reask_day7    — Re-ask shown on Day 7
system_permission_shown          — OS dialog displayed
system_permission_granted        — User allowed notifications
system_permission_denied         — User denied notifications
reminder_time_selected           — morning | lunch | evening
notification_sent                — Daily notification dispatched
notification_opened              — User tapped notification
notification_to_lesson_started   — Notification → lesson began (conversion)
```

### Key Metrics to Monitor

| Metric | Target | Action if Below |
|--------|--------|-----------------|
| Pre-priming acceptance rate | >70% | Test new copy, adjust timing |
| System dialog allow rate (after priming) | >90% | Priming screen isn't convincing enough |
| Overall notification opt-in | >65% | Review timing and value proposition |
| Notification open rate (daily) | >15% | Test notification copy, send time |
| Notification → lesson completion | >60% | Deep link directly to lesson, not home screen |
