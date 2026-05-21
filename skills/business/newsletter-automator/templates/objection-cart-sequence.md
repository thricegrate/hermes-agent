# Objection-Handling + Self-Segmentation Cart Sequences

Two net-new sequence types from the Bustamante 6-Figure Launch Playbook. These run IN PARALLEL with your launch sequence, targeting behavioral segments (not your full list).

Source: `references/bustamante-launch-playbook.md`

---

## Sequence A: Objection-Handling PM Emails (4 Emails)

**Audience:** Sales page clickers who have NOT purchased
**Timing:** Once daily during launch, afternoon/evening (4-6 PM)
**Duration:** Runs alongside the launch sequence (Days 2-5)
**Send type:** Manual send to segment (not automation)

### Beehiiv Setup

1. Create segment: "Clicked [SALES PAGE URL]" AND "Does NOT have tag: [PURCHASE TAG]"
2. Schedule emails for 4-6 PM (separate from morning launch emails)
3. Update segment daily to exclude new purchasers
4. Send as broadcasts to this segment only

---

### Email A1: Price Objection
**Subject:** A quick thought on the investment
**Alt Subject:** Is $[PRICE] worth it?
**Preview:** Here's how I'd think about it
**Send:** Day 2 of launch, 4-6 PM, to clickers-only segment

---

Hey [First Name],

I noticed you were checking out [PRODUCT NAME] earlier.

And I totally get it if the price gave you pause.

$[PRICE] isn't nothing. So let me share how I think about it:

**The math:**
If [PRODUCT NAME] helps you [PRIMARY OUTCOME], that's worth $[OUTCOME VALUE] over the next [TIMEFRAME].

That means your $[PRICE] investment pays for itself in [PAYBACK PERIOD].

**The alternative:**
You could figure this out on your own. Plenty of people do. But it usually takes [LONGER TIMEFRAME] of trial and error, and the cost of [STAYING STUCK / LOST REVENUE / WASTED TIME] adds up fast.

**The safety net:**
[PRODUCT NAME] comes with a [GUARANTEE]. If it doesn't work for you, [GUARANTEE DETAILS].

[If applicable: And if $[PRICE] upfront feels like a lot, we have a [2-PAY / PAYMENT PLAN] option: [PAYMENT DETAILS].]

[X] people have already joined. I'd love for you to be next.

**[CTA: Join [PRODUCT NAME] Now: sales page link]**

[SIGNATURE]

---

### Email A2: "Will It Work For Me?" Objection
**Subject:** Will this actually work for you?
**Alt Subject:** "But my situation is different..."
**Preview:** Let me show you
**Send:** Day 3 of launch, 4-6 PM, to clickers-only segment

---

Hey [First Name],

The #1 question I get about [PRODUCT NAME] is:

"This sounds great, but will it work for someone like ME?"

Let me answer that with 3 real examples:

**[ARCHETYPE 1: The Complete Beginner]**
[NAME/DESCRIPTION] had [ZERO EXPERIENCE / NO AUDIENCE / NO IDEA WHERE TO START]. After [PRODUCT NAME], they [SPECIFIC RESULT]. [Optional: brief quote]

**[ARCHETYPE 2: The Stuck Intermediate]**
[NAME/DESCRIPTION] had been [TRYING FOR X MONTHS/YEARS] but couldn't [BREAK THROUGH / GROW / MONETIZE]. After [PRODUCT NAME], they [SPECIFIC RESULT]. [Optional: brief quote]

**[ARCHETYPE 3: The Experienced Pro]**
[NAME/DESCRIPTION] already had [EXISTING SUCCESS] but wanted to [LEVEL UP / SYSTEMATIZE / SCALE]. After [PRODUCT NAME], they [SPECIFIC RESULT]. [Optional: brief quote]

The common thread? None of them were "ready." They all had doubts. They all wondered if their situation was different.

It wasn't. And yours isn't either.

If you have [MINIMUM REQUIREMENT, e.g., "a laptop and something to say"], [PRODUCT NAME] will work for you.

**[CTA: Join [PRODUCT NAME] Now: sales page link]**

[SIGNATURE]

---

### Email A3: Comparison Objection
**Subject:** Why not just [ALTERNATIVE]?
**Alt Subject:** [PRODUCT NAME] vs. figuring it out yourself
**Preview:** Fair question. Here's my honest answer.
**Send:** Day 4 of launch, 4-6 PM, to clickers-only segment

---

Hey [First Name],

Fair question: why [PRODUCT NAME] instead of [COMMON ALTERNATIVES]?

**vs. Free content (YouTube, blogs, podcasts):**
Free content gives you tactics. Isolated tips. You'll spend [TIMEFRAME] assembling the pieces, and you'll still have gaps. [PRODUCT NAME] gives you the complete system, in order, with [TEMPLATES / FEEDBACK / SUPPORT].

**vs. [COMPETITOR / OTHER COURSE]:**
Most [ALTERNATIVES] teach [GENERIC APPROACH]. [PRODUCT NAME] is built specifically for [YOUR SPECIFIC AUDIENCE/NICHE]. [SPECIFIC DIFFERENTIATOR, e.g., "It's live, with feedback, on YOUR actual project."]

**vs. Figuring it out yourself:**
Absolutely possible. But it takes [LONGER TIMEFRAME]. [PRODUCT NAME] compresses that into [PRODUCT DURATION]. [SPECIFIC PROOF: "That's exactly what happened for [NAME], who went from [BEFORE] to [AFTER] in [TIMEFRAME]."]

The question isn't whether you CAN figure it out alone. It's whether you WANT to spend [TIMEFRAME] doing it.

**[CTA: Join [PRODUCT NAME] Now: sales page link]**

[SIGNATURE]

---

### Email A4: Offer-Specific Objection
**Subject:** [OBJECTION-SPECIFIC SUBJECT LINE]
**Alt Subject:** [VARIANT]
**Preview:** [PREVIEW]
**Send:** Day 5 of launch, 4-6 PM, to clickers-only segment

---

Hey [First Name],

[Address the most common offer-specific objection. Common ones:]

**If time commitment:** "I know you're busy. Here's exactly how much time [PRODUCT NAME] requires: [SPECIFIC HOURS/WEEK]. And everything is [RECORDED / SELF-PACED / ASYNC] so you can [FLEXIBILITY DETAIL]."

**If technical ability:** "You don't need to be [TECHNICAL SKILL]. [PRODUCT NAME] walks you through [THING] step by step. [PROOF: NAME went from [ZERO SKILL] to [RESULT].]"

**If "I've tried before and failed":** "That's actually the BEST reason to join. You've already proven you want this. You just didn't have [THE SYSTEM / THE SUPPORT / THE ACCOUNTABILITY]. That's exactly what [PRODUCT NAME] provides."

**If timing:** "There will never be a 'perfect' time. But there IS a deadline: [DATE]. After that, [SCARCITY ELEMENT]."

**[CTA: Join [PRODUCT NAME] Now: sales page link]**

[SIGNATURE]

---
---

## Sequence B: Self-Segmentation Abandoned Cart (3 Emails)

**Audience:** Clicked sales page 2+ times without purchasing
**Timing:** Automated, triggered by behavior
**Duration:** 3 emails over 48 hours
**Send type:** Beehiiv automation

### Beehiiv Setup

1. Automation trigger: Clicked [SALES PAGE URL] >= 2 times AND does NOT have tag [PURCHASE TAG]
2. Wait 20-30 minutes after 2nd click
3. Send Email B1
4. Wait 24 hours
5. Send Email B2 (survey with 3 tagged links)
6. Wait 12-24 hours
7. Branch based on link click:
   - Clicked "price" link -> Tag "cart-objection-price" -> Send Email B3a
   - Clicked "time" link -> Tag "cart-objection-time" -> Send Email B3b
   - Clicked "not ready" link -> Tag "cart-objection-ready" -> Send Email B3c
   - No click -> Send Email B3a (default to price, most common objection)

### Link tagging for Email B2
Create 3 unique URLs for each option. In Beehiiv, use tagged links or redirect URLs that apply automation tags on click. Example:
- `[DOMAIN]/cart-feedback-price` -> applies tag "cart-objection-price"
- `[DOMAIN]/cart-feedback-time` -> applies tag "cart-objection-time"
- `[DOMAIN]/cart-feedback-ready` -> applies tag "cart-objection-ready"

---

### Email B1: Story-Based Nudge
**Subject:** Why I built [PRODUCT NAME]
**Alt Subject:** The real reason behind [PRODUCT NAME]
**Preview:** It started with a moment I'll never forget
**Send:** 20-30 minutes after 2nd sales page click (no purchase)

---

Hey [First Name],

I wanted to share something personal with you.

[ORIGIN STORY: 2-3 paragraphs about the moment that led you to create this product]

I was [SITUATION]. I knew I wanted [DESIRED OUTCOME] but I couldn't figure out [OBSTACLE].

Then I [DISCOVERY / BREAKTHROUGH / REALIZATION].

[WHAT HAPPENED NEXT: brief transformation]

That's why I built [PRODUCT NAME]. Because I know what it's like to [PAIN POINT]. And I know what it feels like when [TRANSFORMATION].

If you're on the fence, I get it. But I want you to know: this was built for people exactly like you.

**[CTA: Check out [PRODUCT NAME] one more time: checkout link]**

[SIGNATURE]

---

### Email B2: Survey / Self-Segmentation
**Subject:** Quick question for you
**Alt Subject:** Can I ask you something?
**Preview:** Just one question, takes 2 seconds
**Send:** 24 hours after Email B1

---

Hey [First Name],

I noticed you've been thinking about [PRODUCT NAME].

And I respect that you haven't pulled the trigger yet. Seriously.

But I'd love to help if I can.

**So, what's holding you back?**

Click the one that fits:

-> [It's the price](link-tagged-price)

-> [I don't have time right now](link-tagged-time)

-> [I'm not sure I'm ready](link-tagged-not-ready)

Whichever one it is, I think I can help.

Just click the one that fits and I'll follow up with something useful.

[SIGNATURE]

---

### Email B3a: Price Response
**Subject:** About the investment...
**Alt Subject:** Let's talk about the $[PRICE]
**Preview:** Here's how the math works out
**Send:** 12-24 hours after clicking "price" in Email B2

---

Hey [First Name],

Thanks for being honest about the price. I appreciate that.

Here's how I'd think about the $[PRICE]:

**The ROI math:**
[PRODUCT NAME] is designed to help you [PRIMARY OUTCOME]. If that generates even $[CONSERVATIVE MONTHLY VALUE]/month, your investment pays for itself in [X] months.

**The cost of waiting:**
Every month you DON'T [SOLVE THIS PROBLEM] costs you [SPECIFIC COST: lost revenue, wasted time, missed opportunities].

Over the next year, that adds up to $[ANNUAL COST OF INACTION].

**The safety net:**
You're protected by our [GUARANTEE: X-day money-back guarantee]. If [PRODUCT NAME] doesn't deliver, you get [REFUND DETAILS]. Zero risk.

[If applicable: **The payment plan:** If $[PRICE] upfront is a stretch, you can split it into [X] payments of $[AMOUNT]. Same access, same everything.]

I'd hate to see money be the thing that keeps you from [TRANSFORMATION].

**[CTA: Join [PRODUCT NAME]: checkout link]**

[SIGNATURE]

---

### Email B3b: Time Response
**Subject:** I hear you on the time thing
**Alt Subject:** It's actually less time than you think
**Preview:** Here's the real time commitment
**Send:** 12-24 hours after clicking "time" in Email B2

---

Hey [First Name],

I totally understand the time concern.

So let me be straight with you about what [PRODUCT NAME] actually requires:

**The real time commitment:**
[SPECIFIC HOURS PER WEEK]. That's it. [CONTEXT: "Less than [RELATABLE COMPARISON, e.g., 'one Netflix episode a night.'"]

**Everything is [RECORDED / AVAILABLE ON DEMAND]:**
If you miss [A SESSION / A MODULE], you have lifetime access to [REPLAYS / THE CONTENT]. Go at your own pace.

**The quick wins:**
You don't need to finish everything to see results. [SPECIFIC QUICK WIN: "By Day [X], you'll already have [TANGIBLE RESULT]."]

**The time you're losing NOW:**
Every [WEEK / MONTH] you spend [STRUGGLING WITH / RESEARCHING / GUESSING ABOUT] [PROBLEM] is time you could have spent [MAKING PROGRESS / EARNING REVENUE / BUILDING].

[PRODUCT NAME] compresses [MONTHS/YEARS] of trial and error into [PRODUCT DURATION].

**[CTA: Join [PRODUCT NAME]: checkout link]**

[SIGNATURE]

---

### Email B3c: Not Ready Response
**Subject:** When IS the right time?
**Alt Subject:** You don't need to feel ready
**Preview:** Action creates readiness
**Send:** 12-24 hours after clicking "not ready" in Email B2

---

Hey [First Name],

"I'm not sure I'm ready."

I hear you. And I want to be honest:

**Nobody feels ready.**

Not [NAME who now has RESULT]. Not [NAME who went from ZERO to SUCCESS]. And definitely not me when I [YOUR OWN "NOT READY" MOMENT].

Here's what I've learned:

**Readiness is a myth.** You'll never feel 100% ready to [DO THE HARD THING]. That feeling you're waiting for? It comes AFTER you start, not before.

**Waiting makes it harder, not easier.** Every day you don't [TAKE ACTION] is a day the problem gets more entrenched. The gap between where you are and where you want to be doesn't shrink on its own.

**You don't need to be ready. You need to start.** [PRODUCT NAME] is built for people who don't feel ready. That's the whole point. We give you the [SYSTEM / STRUCTURE / SUPPORT] so you don't have to figure it out alone.

If you're waiting for the "right time," this is it. [PRODUCT NAME] [STARTS ON DATE / IS AVAILABLE UNTIL DATE].

**[CTA: Join [PRODUCT NAME]: checkout link]**

[SIGNATURE]

PS - [GUARANTEE]. If it doesn't work for you, [GUARANTEE DETAILS]. You literally have nothing to lose except the status quo.
