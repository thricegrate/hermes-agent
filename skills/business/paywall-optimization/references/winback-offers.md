# Winback Offer Sequences for Lapsed Subscribers

## Why Winback Matters

Reactivating a lapsed subscriber costs 5-10x less than acquiring a new one. A lapsed subscriber already understands your product, has formed some habit, and has payment credentials on file. The barrier to resubscription is psychological, not logistical.

---

## Churn Reasons and Corresponding Winback Strategy

| Churn Reason | % of Churners | Winback Strategy | Expected Recovery Rate |
|-------------|--------------|------------------|----------------------|
| Forgot to use the app | 30-40% | Re-engagement push + content preview | 15-25% |
| Too expensive | 20-30% | Discount offer (50-60% off) | 10-20% |
| Not enough value | 15-20% | Feature update announcement + free preview | 5-10% |
| Found alternative | 5-10% | Competitive comparison + exclusive offer | 3-7% |
| Accidental cancellation | 5-10% | Simple resubscribe prompt | 40-60% |
| Billing issue (involuntary) | 10-15% | Grace period + payment update prompt | 50-70% |

---

## The 3-Touch Winback Sequence

### Touch 1: Day 3 Post-Expiry (The Gentle Reminder)

**Goal:** Catch users who cancelled accidentally or impulsively.

**Channel:** Push notification + in-app message (if they open the app)

**Offer:** 50% off first month back

**Push notification copy:**
```
Title: We miss you at 3 Minute AI
Body: Your premium access expired. Come back with 50% off your first month. Your streak data is still here.
```

**In-app message (if they return):**
```
Welcome back! We saved your progress.

Your 14-day streak is waiting for you.
Your certificates are safe.
Your learning path is right where you left it.

Reactivate Premium: 50% off your first month
[$4.99 instead of $9.99]

[Reactivate Now]        [Maybe Later]
```

**Key elements:**
- Acknowledge their absence warmly, not desperately
- Remind them of their investment (streak, progress, certificates)
- Lead with loss aversion (your data is still here)
- Clear, specific discount with crossed-out original price

---

### Touch 2: Day 7 Post-Expiry (The Value Reminder)

**Goal:** Re-engage users who are drifting away but still have the app installed.

**Channel:** Push notification + email

**Offer:** 60% off first month OR 40% off annual plan

**Push notification copy:**
```
Title: New lessons this week in 3 Minute AI
Body: You're missing out on [specific lesson topic]. Premium members are learning [specific skill]. Come back with 60% off.
```

**Email copy:**
```
Subject: What you missed this week at 3 Minute AI

Hi [Name],

While you were away, premium members learned:
- How to use AI for [specific skill 1]
- [Specific tool] tips that save 2 hours/week
- [New feature or lesson] just launched

Your learning path was 68% complete. Pick up where you left off.

Special offer: 60% off your first month back
Or save even more: 40% off the annual plan ($59.99/year instead of $99.99)

[Reactivate My Account]

Your streak was at 14 days. Let's rebuild it together.
```

**Key elements:**
- Specific content they missed (FOMO, not guilt)
- Progress reminder (68% complete creates completion desire)
- Escalated discount (shows increasing willingness to negotiate)
- Two options (monthly discount or annual discount) to capture different buyer types

---

### Touch 3: Day 14 Post-Expiry (The Final Offer)

**Goal:** Last attempt before the user is classified as fully churned.

**Channel:** Email (push notifications may be disabled by now)

**Offer:** Best possible deal — 70% off first month OR 50% off annual OR $0.99 reactivation month

**Email copy:**
```
Subject: Your final offer from 3 Minute AI (expires in 48 hours)

Hi [Name],

This is your last chance to come back at a discount.

We're offering you our best deal ever:
$0.99 for your first month back (normally $9.99)

After that, you can stay on at the regular price or cancel anytime.

Here's what's waiting for you:
- Your saved progress and [X] completed lessons
- [New feature] we just launched
- Your certificates and badges

[Reactivate for $0.99]

This offer expires in 48 hours.

If this isn't for you, no hard feelings. Your account and progress
will stay saved in case you want to come back later.
```

**Key elements:**
- Urgency (48-hour expiration)
- "Final offer" framing (scarcity)
- Lowest possible price point ($0.99 removes all financial objection)
- Graceful exit (no guilt, door stays open)
- Account preservation promise (reduces deletion anxiety)

---

## Discount Tier Summary

| Timing | Discount | Price Example (Monthly) | Expected Recovery |
|--------|----------|------------------------|-------------------|
| Day 3 | 50% off first month | $4.99 | 8-15% of lapsed |
| Day 7 | 60% off first month | $3.99 | 5-10% of remaining |
| Day 14 | $0.99 reactivation month | $0.99 | 3-8% of remaining |
| Day 30+ | Seasonal/event-based | Varies | 1-3% of remaining |

**Cumulative recovery rate:** 15-30% of all churned subscribers within 30 days.

---

## In-App Winback (When Lapsed Users Return Organically)

If a lapsed subscriber opens the app without clicking a winback offer, show a contextual re-engagement screen:

### Screen Structure

```
[Their profile photo or avatar]

"Welcome back, [Name]!"

Your stats:
- 14-day best streak
- 23 lessons completed
- 3 certificates earned

"Premium expired 5 days ago"

What you're missing:
[Scrollable preview of 2-3 premium lessons they haven't done]

[Reactivate Premium — 50% off]
[Continue as Free User]
```

**Rules for in-app winback:**
- Never block the app entirely (let them use free features)
- Show once per session, not every screen
- Dismiss gracefully with "Continue as Free User" (not "No Thanks")
- Personalize with their actual stats and progress
- Update the discount based on days since expiry

---

## Involuntary Churn Recovery (Billing Failures)

Involuntary churn (failed payment) is different from voluntary churn. These users did NOT choose to leave.

### Grace Period Configuration

| Platform | Default Grace Period | Recommended | Action During Grace |
|----------|---------------------|-------------|-------------------|
| Apple | 16 days (6 retry attempts) | Keep default | Maintain premium access, show payment update banner |
| Google | 7 days (configurable to 3, 7, 14, or 30) | 14 days | Maintain premium access, show payment update prompt |

### Billing Retry + Communication Sequence

1. **Payment fails (Day 0):** In-app banner: "Payment issue detected. Update your payment method to keep premium access." Link to device payment settings.
2. **Day 3:** Push notification: "Action needed: update your payment to keep your streak protection and unlimited lessons."
3. **Day 7:** Email: "Your premium access will expire soon. Update payment in 7 days to avoid interruption."
4. **Grace period ends:** Downgrade to free. Immediately trigger voluntary winback sequence (Touch 1 at day 0, not day 3).

**Key insight:** Involuntary churn recovery rates are 50-70% with proper grace periods and communication. This is the highest-ROI winback investment.

---

## Platform-Specific Winback Tools

### Apple Offer Codes

- Generate one-time-use promotional offer codes in App Store Connect
- Distribute via email winback campaigns
- Supports: free trial, pay-as-you-go, pay-up-front discounts
- Limit: 150,000 codes per app per quarter

### Google Play Winback Offers

- Configure in Play Console under Subscriptions > Offers
- Target lapsed subscribers specifically
- Supports: discounted price for N billing periods, free trial extension
- Can be surfaced automatically on Play Store listing

### RevenueCat Experiments

If using RevenueCat for subscription management:
- Create promotional offers for specific user segments
- A/B test winback discount levels
- Track recovery rate by offer type and timing
- Automate the winback sequence with webhooks

---

## Winback Analytics

### Metrics to Track

| Metric | Formula | Target |
|--------|---------|--------|
| Winback rate | Resubscribed / Total lapsed (30-day window) | 15-30% |
| Winback revenue per lapsed user | Total winback revenue / Total lapsed users | $2-5 |
| Time to resubscribe | Average days from expiry to resubscription | <10 days |
| Winback LTV | Average revenue from resubscribed users over 12 months | >60% of original subscriber LTV |
| Offer redemption rate | Offers redeemed / Offers sent | 5-15% |
| Discount ROI | (Winback revenue - Discount cost) / Discount cost | >3x |

### Cohort Analysis

Track winback cohorts separately from new subscribers:
- Do winback subscribers churn again at higher rates? (Typical: 20-30% higher)
- What discount level produces the best LTV? (Not always the deepest discount)
- Which touch point drives the most recoveries? (Usually Touch 1 or in-app)
- Does the churn reason affect winback success? (Billing failures recover best)

---

## Copy Templates

### Push Notification Templates

**Gentle reminder (Day 1-3):**
- "Your premium access expired. Your [X]-day streak is waiting. Tap to reactivate."
- "We saved your progress. Come back and pick up where you left off."

**Value reminder (Day 5-7):**
- "New this week: [lesson topic]. Premium members are already learning. 60% off to rejoin."
- "You were 68% through your learning path. Finish what you started — 60% off."

**Urgency (Day 12-14):**
- "Last chance: $0.99 to reactivate premium. Offer ends tomorrow."
- "Final offer: Come back for less than $1. Your certificates and progress are waiting."

### Email Subject Lines (Sorted by Open Rate)

1. "Your final offer from 3 Minute AI" (32-38% open rate — curiosity + urgency)
2. "What you missed this week" (28-34% — FOMO)
3. "We saved your progress" (25-30% — personal, relief)
4. "$0.99 to come back" (22-28% — clear value, price in subject)
5. "We miss you" (18-22% — emotional, but lower performer)

### CTA Button Text

- "Reactivate for $0.99" (specific price performs best)
- "Get 60% Off" (discount-forward)
- "Resume My Learning" (action-forward, good for engaged users)
- "Claim My Offer" (ownership language)
- Avoid: "Subscribe Again" (feels like starting over, not resuming)
