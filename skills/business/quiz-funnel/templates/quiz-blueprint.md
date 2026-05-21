# Quiz Blueprint: [Quiz Name]

## Overview

**Quiz Type:** [Product Match / Pricing Plan / Upsell Match / Diagnostic Awareness / Scorecard]
**Traffic Source:** [UGC reels / paid social / organic social / email / mixed]
**Current Conversion Rate:** [X% on product page, or "unknown"]
**Products/Tiers to Match:** [list all recommendation endpoints]

---

## Questions

### Q1: [Opening question -- establishes primary segmentation]
- A: [Answer text] -> maps to [Recommendation Bucket]
- B: [Answer text] -> maps to [Recommendation Bucket]
- C: [Answer text] -> maps to [Recommendation Bucket]
- D: [Answer text] -> maps to [Recommendation Bucket]

### Q2: [Narrows within segment]
- A: [Answer text] -> [how it affects recommendation]
- B: [Answer text] -> [how it affects recommendation]
- C: [Answer text] -> [how it affects recommendation]

### Q3: [Builds commitment -- past experience or constraints]
- A: [Answer text] -> [how it affects recommendation]
- B: [Answer text] -> [how it affects recommendation]
- C: [Answer text] -> [how it affects recommendation]

### Q4: [Context question -- usage, lifestyle, or situation]
- A: [Answer text] -> [how it affects recommendation]
- B: [Answer text] -> [how it affects recommendation]
- C: [Answer text] -> [how it affects recommendation]

### Q5: [Final discriminator -- what matters most]
- A: [Answer text] -> [how it affects recommendation]
- B: [Answer text] -> [how it affects recommendation]
- C: [Answer text] -> [how it affects recommendation]

### Q6 (optional): [Additional discriminator if needed]

### Q7 (optional): [Additional discriminator if needed]

---

## Contact Capture Strategy (Scorecard quizzes only)

**Approach:** [End-capture (default) / Contact-first (Priestley model)]

### If Contact-First:
- **Q1:** Name -- "First, what should we call you?"
- **Q2:** Email -- "Where should we send your personalized scorecard?"
- **Q3:** Phone (optional) -- "Want a personalized follow-up if your score qualifies? (totally optional)"
- **Q4:** Location -- [Auto-detect via IP / ask directly: ___]
- **Rationale for contact-first:** [Why this quiz benefits from upfront capture]

---

## Best Practices Scoring (Scorecard quizzes only)

### Yes/No Questions

| # | Question | Yes = | No = Gap In |
|---|----------|-------|-------------|
| Q5 | [Best practice question] | +10 points | [area] |
| Q6 | [Best practice question] | +10 points | [area] |
| Q7 | [Best practice question] | +10 points | [area] |
| Q8 | [Best practice question] | +10 points | [area] |
| Q9 | [Best practice question] | +10 points | [area] |
| Q10 | [Best practice question] | +10 points | [area] |
| Q11 | [Best practice question] | +10 points | [area] |
| Q12 | [Best practice question] | +10 points | [area] |
| Q13 | [Best practice question] | +10 points | [area] |
| Q14 | [Best practice question] | +10 points | [area] |

### Score Ranges
- **80-100:** [Label] -- [what this means for the prospect]
- **50-70:** [Label] -- [what this means]
- **0-40:** [Label] -- [what this means]

---

## Big 5 Qualification Questions (Scorecard quizzes only)

| # | Question Type | Question | Answer Options | Qualification Signal |
|---|---------------|----------|----------------|---------------------|
| Q15 | Current situation | [question] | [4-5 options] | [what each reveals] |
| Q16 | Desired outcome (90 days) | [question] | [3-4 options] | [urgency/ambition level] |
| Q17 | Obstacles | [question] | [3-4 options] | [pain severity + failed solutions] |
| Q18 | Solution preference | [question] | [map to your offer tiers] | [budget signal] |
| Q19 | Anything else? | [open text] | Free text (optional) | [unexpected insights] |

---

## Tiered CTA Routing (Scorecard quizzes only)

| Qualification Level | Score Range | Solution Preference (Q18) | CTA | Destination |
|---------------------|------------|---------------------------|-----|-------------|
| High | 60+ | Coaching or DFY | Book a call | [booking URL] |
| Mid | 40-70 | Course or Community | Join webinar/workshop | [registration URL] |
| Low | 0-50 | Free resources | Download guide | [lead magnet URL] |

---

## Recommendation Buckets

### Bucket 1: [Product/Tier/Diagnosis Name]

**Triggered when:** [answer combination logic, e.g., "Q1=A + Q2=B or C + Q5=A"]
**Headline:** "[Personalized headline referencing their answers]"
**Why this fits:** [2-3 sentences explaining the match based on what they told us]
**Key selling point:** [the one thing about this product that matches their #1 stated need]
**Social proof:** [testimonial from someone with a similar profile]
**CTA:** [button text + destination]

### Bucket 2: [Product/Tier/Diagnosis Name]

**Triggered when:** [answer combination logic]
**Headline:** "[Personalized headline]"
**Why this fits:** [2-3 sentences]
**Key selling point:** [matches their stated need]
**Social proof:** [relevant testimonial]
**CTA:** [button text + destination]

### Bucket 3: [Product/Tier/Diagnosis Name]

**Triggered when:** [answer combination logic]
**Headline:** "[Personalized headline]"
**Why this fits:** [2-3 sentences]
**Key selling point:** [matches their stated need]
**Social proof:** [relevant testimonial]
**CTA:** [button text + destination]

*(Add more buckets as needed, max 5 recommended)*

---

## Email Capture

**Placement:** Between Q[last] and recommendation screen
**Value exchange:** "[Enter your email and we'll send you your personalized [results/plan/recommendation]]"
**Fields:** Email only (name is optional, adds friction)

---

## Follow-Up Sequences (hand off to `email-sequence`)

### Bucket 1 Sequence (3-5 emails over 5 days)
- **Email 1:** Reinforce recommendation -- "Here's why [Product] is the right fit based on what you told us about [specific answer]"
- **Email 2:** Handle primary objection for this product/tier -- [what objection?]
- **Email 3:** Social proof from someone with a similar quiz profile
- **Email 4:** Additional value or educational content related to their stated goal
- **Email 5:** Purchase incentive + urgency

### Bucket 2 Sequence
- **Email 1:** [customize per bucket]
- **Email 2:** [primary objection for this tier]
- **Email 3:** [relevant social proof]
- **Email 4:** [value content]
- **Email 5:** [incentive + urgency]

*(Repeat for each bucket)*

---

## Tool Choice

**Platform:** [Typeform / Interact / Octane AI / ScoreApp]
**Reason:** [why this platform fits this quiz type and tech stack]
**Email integration:** [which email platform, how connected]

---

## Success Metrics

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Quiz start rate | [X%] | Weekly |
| Quiz completion rate | [X%] | Weekly |
| Email capture rate | [X%] | Weekly |
| Recommendation-to-purchase rate | [X%] | Weekly |
| Email sequence recovery rate (30d) | [X%] | Monthly |
| Quiz-attributed monthly revenue | $[X] | Monthly |

---

## Content Feedback Loop (review monthly)

- Top pain points from quiz responses: [update after 30 days of data]
- Most common "previously tried" approaches: [update after 30 days]
- Transformation language visitors use: [update after 30 days]
- Action: Feed insights back into content production via `content-social`
