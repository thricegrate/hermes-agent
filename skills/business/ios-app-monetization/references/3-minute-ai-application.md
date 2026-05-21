# 3 Minute AI Application

How the iOS app monetization playbook applies to **3 Minute AI** (the actual app project at `C:\Users\thric\Claude Code\3minuteai`, live at 3minute.ai, Flutter + Firebase + RevenueCat).

This file translates the generic playbook into 3 Minute AI-specific decisions. Use it as the worked example of how the 5-mode loop (strategy → paywall → ads → campaigns → metrics) lands in this real launch.

For the project's full state and roadmap, read `C:\Users\thric\Claude Code\3minuteai\README.md` first.

## The 3 Minute AI concept (per project state)

Per `C:\Users\thric\Claude Code\3minuteai\README.md` (v7.0, April 18 2026):

- **Pitch**: "Learn AI in 3 minutes a day. No experience needed."
- **What it does**: AI learning platform that teaches AI tools through personalized bite-sized daily lessons
- **Stack**: Flutter + Firebase (cross-platform) + RevenueCat (subscription management)
- **Web**: live at 3minute.ai (auto-deploys on every push to master)
- **Audience**: 45+ newbies (older audience that wants outcomes, not tools)
- **MVP course library**: 10 outcome-focused courses (money, time, safety, life, health, travel, writing, habits)
- **Free tier**: Your First Win (1 lesson) + Your AI Toolkit (5 lessons) = 6 free lessons
- **Paid tier**: 8 outcome courses (44 paid lessons)

This is a real, shipping app at v7.0. Not a pre-launch project. The playbook below applies to the iOS launch and TikTok-driven user acquisition for the existing app.

## Mode 1: App Strategy applied to 3 Minute AI

### What core human desire does the app target?

The 45+ audience wants to learn AI but feels overwhelmed. The deeper desires underneath are:

- **Status / not falling behind**: "everyone younger than me is using AI; I am being left behind"
- **Identity protection**: "I am the kind of person who keeps up with technology, even now"
- **Fear**: "AI is going to take over and I will be obsolete"
- **Specific outcomes**: make money, save time, stay safe, feel less behind (per the 10-course pillar mapping in v7.0)

The course names confirm the audience-tested desire mapping:
- "Extra $100 with AI" → wealth (specifically "concierge gigs", a tangible side-money angle)
- "Save 5 Hours" → productivity (with a specific time number, not vague "be more productive")
- "Never Get Scammed" → safety (fear of being a target)
- "Health Navigator" → health (older audience health concerns)

This is unusually well-developed for an app concept. The pillar mapping is already validated by audience research per the README.

### The viral feature (the reveal moment) for 3 Minute AI

The app's existing reveal moments (per v7.0):

- **Mini AI Lab "Try it live"**: the bottom-sheet chat where users see AI respond to their prompt inside a lesson
- **Course completion celebration**: the +100 XP, badge unlock, certificate flow
- **The first lesson** ("Your First Win"): the onboarding hook that gets the user to a working AI moment fast

For TikTok ads, the strongest screen-recordable moment is probably **the Mini AI Lab's "Try it live"** because:

- It is fast (a few seconds from prompt to AI response)
- It is personal (the user enters their own input)
- It is visual (shows the AI response in a clean bottom sheet)
- It works on mute (the response appears as text)

The before/after format adapted for this:
- **Before**: a 45+ user struggling with a specific task (writing an email, planning a trip, researching a health question)
- **App reveal**: opens 3 Minute AI, taps a lesson, hits the Mini AI Lab "Try it live"
- **After**: the AI handles the task, the user looks impressed

### Apps to study

For 3 Minute AI specifically, study:

1. **Headway** (book summaries): sells learning to a similar age band, has a strong onboarding paywall, $40-60/year pricing
2. **Blinkist**: same shape as Headway, learning subscription
3. **Lumosity / Elevate**: brain training with daily routines and streaks (similar gamification model to 3 Minute AI)
4. **DuoLingo**: daily streak mechanics, free tier + paid tier, mass-market learning app
5. **Calm / Headspace**: meditation, sells to a similar emotional audience (people who want to "improve themselves"), ~$70/year

The first two are the closest learning-subscription analogues. The last two are the strongest gamification + pricing tier studies.

3 Minute AI's "10 outcome courses + Mini AI Lab + streak" structure is more like Lumosity/DuoLingo than the typical face-rating viral app. The TikTok ad strategy needs to reflect that.

## Mode 2: Paywall applied to 3 Minute AI

### The current paywall situation (per README)

- **RevenueCat native paywall** is wired in
- **6 free lessons** (Your First Win + Your AI Toolkit)
- **44 paid lessons** behind the paywall
- **Trial offered**: yes, "Try for $0" routing to RevenueCat trial flow
- **Onboarding sequence**: Quiz → Certificate preview → signup → streak commit → trial guide → paywall → Learn

This is NOT the playbook's default "hard paywall, no trial." It is a freemium-with-trial structure that gives 6 lessons free before the paywall.

### Should 3 Minute AI switch to hard paywall?

The playbook recommends hard paywall. The current 3 Minute AI structure has:
- 6 free lessons (substantial preview)
- A trial flow on the paywall

Two reasons the current structure may be correct for this specific app:

1. **The audience is 45+ and freebie-prone** (per `private project notes/MEMORY.md`: "40% want free trial first, 25% free-only"). Hard paywall on day 1 may filter too aggressively for this audience.

2. **The app is a learning subscription, not a viral reveal.** Face rating apps work with hard paywall because the reveal IS the product. 3 Minute AI's value compounds across multiple lessons; users need to experience the daily-lesson rhythm before they will subscribe.

### Recommended paywall test for 3 Minute AI

Run the existing freemium structure as the control. Test these as variants:

- **Variant A (control)**: 6 free lessons → trial → paywall (current state)
- **Variant B (less free)**: 1 free lesson (Your First Win only) → hard paywall, no trial
- **Variant C (hard paywall + trial)**: 1 free lesson → trial → paywall (no extended free)

The test reveals which structure converts the 45+ audience best. The standard playbook bias toward hard paywall may be wrong for this specific app + audience combination. Let the data decide.

### Pricing for 3 Minute AI

The playbook default is $12.99/week + $59.99/year + $44.99 retention.

For 3 Minute AI specifically (45+ audience, learning subscription, RevenueCat already wired):

- **Annual emphasis**: 45+ audiences typically convert better on annual than weekly. If the current pricing is weekly-default, test annual-default.
- **Annual price**: $59.99/year aligns with Headway/Blinkist range. Test against $79.99/year (premium positioning) and $39.99/year (value positioning).
- **Retention offer**: $44.99/year as a discount from $59.99 is the playbook standard. Apply to RevenueCat's offer system.

The exact prices to test depend on what is currently configured. Check RevenueCat dashboard for current setup. The RevenueCat docs handle paywall A/B testing natively.

## Mode 3: AI Ad Creation applied to 3 Minute AI

### The before/after format adapted for an AI learning app

The standard before/after (face transformation, body transformation) does not map directly. The transformation is cognitive and outcome-driven.

Adapted formats:

#### Format A: Outcome before/after (recommended)

Each of the 10 courses has a specific outcome. The ad shows that specific outcome.

- **"Extra $100 with AI"**: Before = user staring at credit card bill. After = user counting cash from their AI side hustle.
- **"Save 5 Hours"**: Before = user buried in tasks at 7pm. After = user closing laptop at 4pm with a happy expression.
- **"Never Get Scammed"**: Before = user almost clicking a phishing email. After = user catching the scam, deleting it, smug expression.
- **"Health Navigator"**: Before = user confused at the pharmacy. After = user confidently explaining their medication situation.

Each course produces 2-3 ads. Across 10 courses, that is 20-30 distinct ad concepts.

#### Format B: Mini AI Lab reveal

Show the user inside the Mini AI Lab using AI to handle a task in real-time.

- **Hook**: "I asked AI to help me with [specific task] and the answer was crazy"
- **Reveal**: phone screen showing the Mini AI Lab response
- **After**: the user using the answer in real life

This format leverages the app's existing Mini AI Lab feature. Strong because the AI moment is real, not just claimed.

#### Format C: Streak / progress reveal

Show the user's streak or progress dashboard. The "I learned X new things in 30 days" format.

- **Hook**: "I learned more about AI in 30 days than I did the whole year before"
- **Reveal**: the streak screen, the badges, the certificates
- **After**: the user demonstrating something they learned

### AI personas for 3 Minute AI ads

Z-Image Turbo prompts for the 45+ demographic:

- 45-65 year old men and women
- Casual home settings (kitchen, home office, living room)
- "Mid-career" or "late-career" wardrobe (not Gen Z, not boardroom)
- Slightly behind-the-curve aesthetic in "before"; capable / confident in "after"

Important: the audience is 45+, NOT 35-50 (an earlier note in MEMORY had the wrong age band). Match the AI personas to the actual audience age.

The course-specific ads benefit from age + outcome variation:
- "Extra $100" can show a 50-year-old wishing for extra income
- "Health Navigator" can show a 60-year-old confused at a doctor's office
- "Save 5 Hours" can show a 45-year-old swamped at work
- "Travel Planner" can show a 55-year-old planning a trip without help

### Hook angles for 3 Minute AI

The standard playbook hook angles (status, fear, peer comparison) need adapting for the older audience and learning context:

- **Status / not being left behind**: "If you are over 50 and you have not really learned AI yet..."
- **Fear / being obsolete**: "POV: your kids/grandkids use AI better than you"
- **Specific outcome promise**: "I made an extra $100 this week using AI. I am 58."
- **Peer comparison**: "My retired friend uses AI for [X] and I had no idea"
- **Curiosity**: "What is the easiest way to learn AI if you are over 50?"

Avoid hooks that feel patronizing or that emphasize the user's age in a negative way. The 45+ audience is sensitive to "aging" framing. Frame in terms of capability, not decline.

## Mode 4: TikTok Smart+ Campaign applied to 3 Minute AI

### The TikTok 45+ audience reality

The 45+ TikTok audience exists and is growing. It is smaller than the Gen Z audience but it is also less competed-for in the AI learning niche. Smart+ targeting will find this audience automatically.

If TikTok Smart+ does not produce results for the 45+ audience after 2 weeks, consider:

1. **Meta (Facebook + Instagram Reels)** as a parallel platform. The 45+ audience is more concentrated on Facebook than on TikTok.
2. **YouTube Shorts** as another parallel. The audience has migrated from regular YouTube to Shorts and converts well.

For 3 Minute AI specifically, consider running TikTok + Meta in parallel from week 1 rather than waiting. The audience split warrants it.

### Optimization event setup for 3 Minute AI

Optimize for the **subscription event** in RevenueCat. Wire the iOS App Events SDK to fire when RevenueCat confirms a successful trial start or paid subscription.

Test this BEFORE running ads:
1. Make a test subscription on a test device
2. Verify the subscription event appears in TikTok Ads Manager
3. Verify the same in Meta Events Manager (if running parallel campaigns)

### Budget for 3 Minute AI

Standard playbook: $50/day starting.

For 3 Minute AI with the team context:

- The team is small (Yar + Oleg + Julia per MEMORY)
- The TikTok ad credit applies (use it aggressively)
- Apply for Apple Small Business Program if not already enrolled

Recommended starting budget: $50/day TikTok + $50/day Meta = $100/day total split across platforms for 2 weeks. Whichever platform produces a winner first becomes the primary; the other becomes secondary.

### LTV calibration for 3 Minute AI

Standard playbook LTV: ~$30/paying user with $12.99/week + $59.99/year + $44.99 retention.

For 3 Minute AI specifically:

- The 45+ audience may retain longer than younger audiences (older buyers churn slower)
- Annual subscribers in this category typically retain 60-70% year-1 (vs ~40% for weekly subscribers)
- Mini AI Lab usage and streak completion correlate with retention; track these as leading indicators

If the audience converts mostly annual ($59.99/year), LTV is closer to $40-50 in year 1. CPA can be higher.

If the audience churns fast (cancellation rate > 40% in month 1), the app needs a retention fix (push notifications, streak rescue, content cadence) BEFORE scaling ad spend.

## Mode 5: Metrics applied to 3 Minute AI

### What to track that is specific to this app

In addition to the playbook standards (CPI, CTR, CPA, LTV):

- **Onboarding completion rate** (quiz → signup → streak → trial → paywall): how many install-to-paywall conversions
- **Trial-to-paid conversion**: how many trial users convert to paid at the end of trial
- **Lesson 1 completion rate** (Your First Win): leading indicator of retention
- **Streak retention at day 3, day 7, day 14, day 30**: health of the daily-lesson loop
- **Mini AI Lab usage rate**: percentage of users who try the live AI feature in their first session

These app-specific metrics tell you WHERE in the funnel revenue is being lost. Standard CPI/CTR/CPA tells you WHETHER the funnel is working overall.

### Weekly review for 3 Minute AI

Every Monday:

1. **Top 3 ads by CPA** (which creatives are converting?)
2. **Top 3 ads by CTR** (which hooks are landing?)
3. **Bottom 3 ads** (kill candidates)
4. **Onboarding funnel** (where is drop-off happening?)
5. **Streak retention** (are users coming back?)
6. **Trial-to-paid conversion** (is the paywall working?)

The first 3 are about the ads. The last 3 are about the app. Both move the LTV-to-CPA ratio.

## Apple compliance for 3 Minute AI

The standard Apple compliance checklist applies (see [apple-compliance.md](apple-compliance.md)). Specifically for this app:

- **RevenueCat handles most subscription compliance** automatically (Restore Purchases, auto-renewal disclosure, terms links). Verify they are wired correctly in the build.
- **Retention offer**: if implementing the $44.99/year retention offer, ensure it ONLY appears in the cancellation flow inside Settings, never as a popup or banner.
- **Trial flow disclosure**: the "Try for $0" CTA must clearly show what happens after the trial (auto-renewal, charge amount, when the charge happens). RevenueCat's native paywall handles this automatically; verify it.
- **Privacy section**: 3 Minute AI handles user data (lessons, progress, AI Lab usage). Ensure the App Store Connect privacy section accurately reflects what is collected.

The app is at v7.0 and likely already passes Apple review. The compliance check is a verification, not a re-build.

## What to do differently from the generic playbook for 3 Minute AI

### Things to follow exactly

- Apply for Apple Small Business Program if not already enrolled
- Use TikTok ad credit
- Optimize ads for subscription event, not installs
- USA only at start (test other markets after profitable)
- Daily metric check + weekly review

### Things to adapt

- Run TikTok + Meta in parallel from week 1 (45+ audience splits across both)
- AI personas in ads: 45+ demographic, mid-career to retired styling
- Hook angles: status / fear of being left behind, NOT vanity / face / body
- Paywall: test current freemium structure as control vs hard paywall variants
- Ad format: outcome-based before/after by course (10 courses × 2-3 ads each = 20-30 concepts)

### Things to watch carefully

- Trial-to-paid conversion (the freemium-with-trial model is conversion-sensitive)
- Streak retention (the daily-lesson loop is the LTV multiplier)
- Mini AI Lab usage (proxy for engagement quality)
- Course-specific ad performance (some outcomes may convert dramatically better than others; weight ad spend toward winners)

## Cross-references

- App project: `C:\Users\thric\Claude Code\3minuteai`
- App README (current state, v7.0): `C:\Users\thric\Claude Code\3minuteai\README.md`
- App master plan: `C:\Users\thric\.claude\plans\so-in-this-our-recursive-salamander.md`
- App strategy generic playbook: [app-strategy.md](app-strategy.md)
- Paywall and pricing generic playbook: [paywall-and-pricing.md](paywall-and-pricing.md)
- TikTok Smart+ campaigns generic playbook: [tiktok-smartplus-campaigns.md](tiktok-smartplus-campaigns.md)
- Before/after ad workflow generic playbook: [before-after-ad-workflow.md](before-after-ad-workflow.md)
- Apple compliance checklist: [apple-compliance.md](apple-compliance.md)
- Project audience profile (45+ Americans wanting to learn AI): `private project notes/MEMORY.md`
- App design (separate concern): `skills/app-design/SKILL.md`
