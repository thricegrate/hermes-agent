# UGC-to-Quiz Integration

How the UGC content system connects to the quiz funnel as the primary conversion mechanism for cold traffic.

---

## The Core Principle

The reel is NOT the campaign. The reel is the top of a conversion architecture. The quiz funnel is the conversion mechanism. The email sequence is the follow-up. Content generates traffic. Architecture converts it.

Operators who treat the reel as the campaign and the product page as the destination leave the majority of their conversion potential on the table.

---

## How the 6-Section UGC Script Maps to Quiz Entry

The UGC Cold Traffic script (from `video-scriptwriter`) builds emotional momentum across 6 sections. The CTA (Section 6) must preserve that momentum by routing to the quiz, not a cold product page.

### Script-to-Quiz Flow

```
Section 1: Persona Signal     -> Viewer identifies ("that's me")
Section 2: Pain Acknowledgment -> Viewer feels understood
Section 3: Mechanism Bridge    -> Viewer understands why past attempts failed
Section 4: Solution Intro      -> Viewer learns what's different
Section 5: Transformation      -> Viewer imagines the result
Section 6: CTA                 -> Viewer enters quiz

Quiz Q1: Matches viewer's situation  -> Continues the conversation
Quiz Q2-5: Deepens understanding     -> Builds commitment
Email capture: Before results        -> Low friction after investment
Recommendation: Personalized match   -> Converts with trust
```

The quiz continues the conversation the script started. The viewer should feel like the quiz is a natural next step, not a marketing funnel.

### CTA Variants for Quiz Entry

**Link-in-bio route:**
> "There's a quick quiz in the link below that'll tell you exactly which [product/approach] fits your specific situation."

**DM automation route:**
> "Comment QUIZ and I'll send you a 90-second assessment that matches you with the right [product/approach] for where you are right now."

**Story swipe-up route:**
> "Swipe up to take the quiz -- it's 90 seconds and tells you exactly what you need."

---

## Conversion Benchmarks by Traffic Source

Not all traffic converts the same way through the quiz. Cold UGC traffic has different benchmarks than warm or paid traffic.

| Traffic Source | Quiz Start Rate | Completion Rate | Recommendation CVR | Notes |
|----------------|-----------------|-----------------|---------------------|-------|
| Cold UGC organic (Reels/TikTok) | 40-50% | 60-70% | 4-6% | Baseline. Emotional momentum from content. |
| Cold UGC via DM automation | 55-70% | 70-80% | 6-10% | Higher intent (they commented). DM primes engagement. |
| Paid social (Meta/TikTok ads) | 50-60% | 65-75% | 5-8% | Pre-qualified by ad targeting. |
| Email traffic (to quiz) | 60-75% | 75-85% | 8-12% | Warmest traffic. Already on your list. |
| Retargeting (saw content, didn't convert) | 55-65% | 70-80% | 6-10% | Second chance. Higher completion. |

---

## The Scale Decision Threshold

Before scaling production investment (more accounts, more content volume, paid amplification), all 3 criteria must be met:

### Criterion 1: Revenue Consistency
The campaign has generated consistent revenue for **a minimum of 4 consecutive weeks** without a week-over-week decline greater than 15%.

### Criterion 2: Quiz Conversion Validation
The quiz funnel is demonstrating a **stable conversion rate above 5%** (recommendation-to-purchase) over **a minimum of 500 completions**.

Why 500? Below 500, statistical noise can make a 3% quiz look like 7% or vice versa. 500 completions provides enough data to trust the conversion rate as representative.

### Criterion 3: Creative Validation
**At least 3 avatar and hook combinations** have been validated as consistent performers across multiple accounts in the portfolio.

Why 3? A campaign dependent on a single winning creative is fragile. 3 validated combinations means the system has learned what works and can produce more of it reliably.

**A campaign that meets all 3 criteria** has demonstrated that the core system works and that additional production investment will produce proportional revenue increases.

**A campaign that doesn't meet all 3** has an unsolved problem in one or more layers that scaling will amplify rather than resolve.

---

## Revenue Per Quiz Completion: The North Star Metric

This is the single metric that captures the combined effectiveness of every element in the system.

```
Revenue Per Quiz Completion = Total Monthly Revenue / Total Monthly Quiz Completions
```

- **Increasing week over week:** The system is learning and improving.
- **Flat:** Optimization has stalled. Review quiz copy, recommendation screens, email sequences.
- **Declining:** Something broke. Diagnose: is it traffic quality (content), quiz conversion (funnel), or email recovery (sequences)?

Track this weekly. It's the one number that tells you if the entire pipeline is healthy.

---

## Quiz Data Feeding Back Into Content

The quiz is also a continuous audience research instrument. After 30+ days of data:

| Quiz Data | Feeds Into | How |
|-----------|-----------|-----|
| Most common pain points (Q1-Q2 responses) | `video-hook` hook angles | Priority hook categories for next production cycle |
| Most frequent failed alternatives (Q3 responses) | `video-scriptwriter` Section 3 | Mechanism bridge language in next script batch |
| Transformation language (Q5 responses) | `video-scriptwriter` Section 5 | Exact wording in next generation of reels |
| Quiz path distribution (which buckets get most traffic) | `product-offer` | Tells you which product/tier resonates most with your audience |
| Drop-off by question | `quiz-funnel` optimization | Rewrite or remove high-drop-off questions |

---

## Integration Map

```
niche-finder (persona depth)
  -> video-scriptwriter (UGC 6-section script)
    -> video-hook (5 UGC hook variations)
      -> elevenlabs (voice production)
        -> jogg-ai (avatar video)
          -> content-social (distribution)
            -> quiz-funnel (THIS: conversion mechanism)
              -> email-sequence (segmented follow-up)
                -> product-offer (purchase)
                  -> cro-funnel (optimization)
```

The quiz sits at the critical junction between content (top of funnel) and conversion (bottom of funnel). Everything before it generates traffic. Everything after it converts traffic. The quiz's job is to bridge the two without losing the emotional momentum the content created.
