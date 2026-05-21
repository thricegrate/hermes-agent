# Retention Benchmarks

## Industry Benchmarks by App Category

### Education Apps

| Metric | Bottom 25% | Median | Top 25% | Top 10% |
|--------|-----------|--------|---------|---------|
| D1 | <15% | 22-28% | 35-45% | >50% |
| D7 | <8% | 12-18% | 22-30% | >35% |
| D14 | <5% | 8-12% | 15-22% | >25% |
| D30 | <2% | 5-8% | 12-18% | >20% |
| D90 | <1% | 2-4% | 6-10% | >12% |

### Reference Apps (Education + Habit)

| App | D1 | D7 | D30 | Key Retention Mechanic |
|-----|-----|-----|------|----------------------|
| Duolingo | ~55% | ~35% | ~20% | Streaks, leagues, push notifications |
| Headspace | ~45% | ~25% | ~12% | Daily reminders, streak, progressive content |
| Brilliant | ~40% | ~22% | ~10% | Daily problems, streak, difficulty progression |
| Blinkist | ~35% | ~18% | ~8% | Daily picks, reading streaks |
| Coursera (mobile) | ~30% | ~15% | ~7% | Course progress, deadlines, certificates |
| Khan Academy | ~28% | ~14% | ~6% | Mastery system, streaks |

### Other Relevant Categories

**Health/Fitness (for habit mechanics comparison):**

| Metric | Median | Top 25% |
|--------|--------|---------|
| D1 | 30% | 45% |
| D7 | 18% | 30% |
| D30 | 8% | 18% |

**Subscription Apps (for churn context):**

| Metric | Median | Top 25% |
|--------|--------|---------|
| Trial → Paid | 15-25% | 35-50% |
| Month 1 churn | 15-20% | 8-12% |
| Month 3 churn | 30-40% | 18-25% |

---

## What Drives Each Retention Metric

### D1 (Day 1 Return) — "Did they come back?"

**The question:** Did the first session create enough pull to overcome the default (forgetting the app exists)?

**Primary drivers ranked by impact:**

| Driver | Impact | How to Implement |
|--------|--------|-----------------|
| Push notification (morning after) | +15-25% D1 | Permission priming → daily reminder at selected time |
| Aha moment in first session | +10-20% D1 | Before/after comparison that makes user think "I need this" |
| Curiosity gap for Day 2 | +5-10% D1 | Tomorrow preview with a hook they can't stop thinking about |
| Streak = 1 (loss aversion) | +3-5% D1 | "Don't break your streak" psychology starts at 1 |
| Unfinished progress | +2-5% D1 | If they see 1/28 completed, the incompleteness nags |

**D1 target for 3 Minute AI: 40% at launch, 50% at 6 months**

**How to diagnose poor D1:**
- If notification opt-in is low (<50%): fix permission priming
- If opt-in is high but D1 is low: notification copy/timing is wrong
- If non-notified users have 0% D1: the in-app experience alone isn't sticky enough
- If completion rate of first lesson is <70%: first lesson is too long or too hard

### D7 (Week 1 Return) — "Did they form a habit?"

**The question:** Did the daily pattern take hold, or did the novelty wear off?

**Primary drivers ranked by impact:**

| Driver | Impact | How to Implement |
|--------|--------|-----------------|
| Consistent daily notifications | +10-15% D7 | Same time every day, never miss a send |
| Streak counter (visible, celebrated) | +8-12% D7 | Streak prominently displayed, streak milestone celebrations at 3 and 7 |
| Content variety (no two days feel same) | +5-8% D7 | Category rotation: Writing → Images → Save Time → etc. |
| Progressive difficulty (not boring) | +3-5% D7 | Week 1 exercises get slightly harder each day |
| Day 3 feature unlock (learning path) | +2-4% D7 | New feature discovery creates "what else is here?" curiosity |
| Day 7 feature unlock (badges) | +2-3% D7 | Achievement system appears right when motivation dips |

**D7 target for 3 Minute AI: 20% at launch, 28% at 6 months**

**How to diagnose poor D7:**
- If D1 is good but D3 drops sharply: Day 2-3 content isn't compelling enough
- If D3 is good but D5-7 drops: notification fatigue or content getting repetitive
- If streak users have much higher D7: streak is working, but not enough users start streaks
- If the drop is gradual (D1 40%, D3 30%, D5 25%, D7 20%): normal decay, optimize content quality
- If the drop is sharp (D1 40%, D3 15%): something breaks on Day 2-3 (investigate that specific content)

### D14 (Two-Week Return) — "Are they committed?"

**The question:** Has the daily learning session become part of their routine?

**Primary drivers ranked by impact:**

| Driver | Impact | How to Implement |
|--------|--------|-----------------|
| Certificate progress visible | +5-8% D14 | "You're 50% to your AI Skills Certificate" |
| Streak count as identity | +5-7% D14 | At 14 days, the streak itself becomes the motivation |
| Content quality escalation | +3-5% D14 | Week 3 content must be noticeably more interesting than Week 1 |
| Spaced repetition feeling | +2-4% D14 | User notices they remember concepts from Week 1 ("this is working") |
| Community/social features | +2-3% D14 | Unlocked at Day 14, creates new engagement vector |

**D14 target for 3 Minute AI: 12% at launch, 18% at 6 months**

### D30 (Month Return) — "Are they retained?"

**The question:** Is this a lasting behavior change?

**Primary drivers ranked by impact:**

| Driver | Impact | How to Implement |
|--------|--------|-----------------|
| 28-day completion (certificate) | +8-10% D30 | Completers have highest D30+ retention |
| Habit formed (opens without prompt) | +5-8% D30 | Track organic opens vs. notification opens |
| Post-28-day content | +3-5% D30 | "Advanced" lessons, tool updates, new tools |
| Subscription lock-in | +2-4% D30 | Paid users churn less due to sunk cost |
| Achievement collection | +1-3% D30 | Badge hunters keep coming back |

**D30 target for 3 Minute AI: 10% at launch, 15% at 6 months**

---

## Cohort Analysis Framework

### How to Run Retention Analysis

Track each user by their signup date (cohort). Compare cohorts to measure improvement.

```
Cohort: March 2026 signups (1,000 users)
D0 (signup day): 1,000 (100%)
D1: 420 (42%)
D3: 310 (31%)
D7: 220 (22%)
D14: 140 (14%)
D21: 95 (9.5%)
D28: 70 (7%)
D30: 65 (6.5%)
```

### Retention Curve Shape

**Healthy curve:** Steep drop D0-D3, then flattens into a gradual slope.
```
100% ██████████
 42% ████
 31% ███
 22% ██
 14% █▌
  9% █
  7% ▊     ← Curve flattening = good
  6% ▊
```

**Unhealthy curve:** Continuous steep drop with no flattening.
```
100% ██████████
 42% ████
 25% ██▌
 15% █▌
  8% ▊
  4% ▍
  2% ▏     ← Still dropping fast = bad
  1% ▏
```

**The flattening point** is your "retained core." For education apps, this typically happens around D7-D14. If your curve hasn't flattened by D14, your product-market fit for the retained segment may be weak.

---

## Segmented Retention Benchmarks

### By Notification Status

| Segment | D1 | D7 | D30 |
|---------|-----|-----|------|
| Notifications enabled | 55% | 30% | 15% |
| Notifications disabled | 20% | 8% | 3% |
| **Delta** | **+35pp** | **+22pp** | **+12pp** |

Notifications are the single largest retention lever. This is why permission priming is so critical.

### By First Session Completion

| Segment | D1 | D7 | D30 |
|---------|-----|-----|------|
| Completed first lesson + exercise | 50% | 28% | 14% |
| Started but didn't complete first lesson | 18% | 6% | 2% |
| Never started first lesson | 5% | 1% | 0% |
| **Lesson completion uplift** | **+32pp** | **+22pp** | **+12pp** |

### By Quiz Comfort Level

| Comfort Level | D1 | D7 | D30 | Insight |
|--------------|-----|-----|------|---------|
| Low (1-2) | 45% | 25% | 12% | High motivation, everything is new |
| Medium (3) | 40% | 22% | 10% | Solid baseline |
| High (4-5) | 30% | 18% | 8% | Content may feel too basic initially |

Users with low comfort levels retain better because every lesson teaches them something new. High-comfort users need more advanced first-lesson selection to avoid boredom.

### By Subscription Status

| Segment | D7 | D30 | D90 |
|---------|-----|------|------|
| Paid (any plan) | 45% | 28% | 18% |
| Free | 18% | 8% | 3% |
| **Paid uplift** | **+27pp** | **+20pp** | **+15pp** |

Paid users retain dramatically better due to:
1. Self-selection (more motivated to begin with)
2. Sunk cost effect (paid, so want to use it)
3. Full content access (no paywall friction)

---

## Retention Improvement Playbook

### Quick Wins (Implement First)

| Action | Expected D7 Impact | Effort |
|--------|-------------------|--------|
| Pre-primed notification permissions | +8-12pp | Medium (1 screen) |
| Auto-start first lesson (no choice screen) | +3-5pp | Low (remove a screen) |
| Tomorrow preview with curiosity hook | +2-4pp | Low (add 1 screen) |
| Streak counter visible on home screen | +2-3pp | Low (UI element) |

### Medium-Term Improvements

| Action | Expected D30 Impact | Effort |
|--------|-------------------|--------|
| Personalized first lesson from quiz data | +3-5pp | Medium |
| Day 3/7/14 feature unlocks | +2-4pp | Medium |
| Streak milestone celebrations (3, 7, 14, 21, 28) | +2-3pp | Medium |
| Spaced repetition reviews embedded in lessons | +2-3pp | High |

### Long-Term Investments

| Action | Expected D90 Impact | Effort |
|--------|-------------------|--------|
| Certificate at Day 28 completion | +3-5pp | Medium |
| Post-28-day advanced content | +5-8pp | High (content creation) |
| Community features (sharing, discussion) | +2-4pp | High |
| AI-personalized lesson recommendations | +3-5pp | High |

---

## Tracking Dashboard Requirements

### Essential Metrics (Daily View)

```
Today's Metrics:
- DAU: [number]
- New signups: [number]
- First lesson completion rate: [%]
- Notification opt-in rate: [%]
- Streak distribution: 1-day [%], 3-day [%], 7-day [%], 14+ [%]

Retention (Rolling):
- D1: [%] (vs. target: 40%)
- D7: [%] (vs. target: 20%)
- D30: [%] (vs. target: 10%)

Alerts:
- D1 drops below 35%: investigate first-session flow
- D7 drops below 15%: investigate Day 2-7 content
- Notification opt-in drops below 60%: investigate priming screen
- First lesson completion drops below 70%: investigate lesson length/difficulty
```

### Firestore Collections for Retention Tracking

```
retention_events:
  - user_id: String
  - cohort_date: Date (signup date)
  - event_date: Date
  - event_type: app_open | lesson_started | lesson_completed |
                streak_continued | streak_broken | notification_opened
  - days_since_signup: Integer
  - session_duration_seconds: Integer
  - notification_driven: Boolean (did they come from a notification?)
  - platform: web | ios | android
```

### Key Segmentation Dimensions

Always slice retention data by:
1. **Notification status** (enabled vs. disabled)
2. **First session completion** (completed vs. bounced)
3. **Quiz comfort level** (low/medium/high)
4. **Subscription status** (free vs. paid)
5. **Platform** (web vs. iOS vs. Android)
6. **Acquisition source** (organic vs. paid vs. referral)
7. **Reminder time** (morning vs. lunch vs. evening)
