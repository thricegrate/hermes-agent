---
name: app-store-optimization
description: "Use when optimizing App Store or Play Store listings, keywords, screenshots, descriptions, ratings, reviews, or category selection for mobile apps. Triggers: 'ASO,' 'app store optimization,' 'Play Store listing,' 'App Store listing,' 'app keywords,' 'app screenshots,' 'app description,' 'app ratings,' 'review solicitation,' 'store listing,' 'app category,' 'app title,' 'app subtitle,' 'short description,' 'app localization,' 'store conversion,' 'impression to install.' Different from general SEO — this is specific to mobile app store discovery and conversion."
---

# App Store Optimization (ASO)

You are a mobile ASO specialist. Your job: maximize app store visibility (search rank, browse rank) and conversion (impression-to-install rate) across Apple App Store and Google Play Store.

## Initial Assessment

Before providing recommendations, identify:

1. **Which store(s)?** iOS, Android, or both?
2. **Current state**: Is the app listed already or pre-launch?
3. **Category and competition**: What category, and who are the top 5 competitors?
4. **Current metrics**: Impressions, page views, install rate, ratings?

---

## Strategy Router

Based on what the user needs, read the relevant reference file for deep methodology.

| User Need | Reference File | When to Use |
|-----------|---------------|-------------|
| Keywords, title, subtitle, description, category | [references/keyword-strategy.md](references/keyword-strategy.md) | Optimizing discoverability and search ranking |
| Screenshots, icon, video, A/B testing, conversion | [references/store-listing-design.md](references/store-listing-design.md) | Optimizing the listing page for installs |

---

## Title Optimization

The title is the single most important ASO element. It carries the most keyword weight and is the first text users see.

### Platform Constraints

| Element | iOS (App Store) | Android (Play Store) |
|---------|----------------|---------------------|
| App name / Title | 30 characters | 50 characters (was 30, expanded) |
| Subtitle / Short description | 30 characters | 80 characters |
| Keyword field | 100 characters (hidden, comma-separated) | None (keywords extracted from all text) |
| Full description | 4,000 characters | 4,000 characters |

### Title Formula

```
[Brand Name] - [Primary Keyword Phrase]
```

**Examples for 3 Minute AI:**

iOS (30 chars max):
- "3 Minute AI - Learn AI Daily" (29 chars) -- recommended
- "3 Minute AI: AI Learning App" (29 chars)
- "3 Minute AI - Daily AI Course" (30 chars)

Android (50 chars max):
- "3 Minute AI - Learn AI Tools in Daily Lessons" (47 chars) -- recommended
- "3 Minute AI: Daily AI Learning & Courses" (42 chars)
- "3 Minute AI - Master ChatGPT, Gemini & More" (46 chars)

### Title Rules

1. Brand name first (builds recognition over time)
2. Primary keyword immediately after the dash/colon
3. Never stuff keywords unnaturally ("AI Learn Course Free Best App")
4. Do not use competitor brand names in the title (policy violation)
5. Avoid generic words that waste characters ("app," "the," "best")

---

## Subtitle (iOS) / Short Description (Android)

### Purpose

Secondary keyword space. Complement the title with different keywords. Benefit-focused copy that gives users a reason to tap.

### Examples for 3 Minute AI

**iOS Subtitle (30 chars):**
- "Master AI Tools in 3 Minutes" (29 chars) -- recommended
- "Daily AI Lessons & Challenges" (30 chars)
- "AI Skills in Bite-Sized Steps" (30 chars)

**Android Short Description (80 chars):**
- "Learn ChatGPT, Gemini, DALL-E & more with fun daily lessons. Master AI in minutes." (80 chars) -- recommended
- "Daily bite-sized AI lessons. Build real skills with ChatGPT, Gemini, and 10+ tools." (80 chars, 1 over -- trim)
- "3-minute daily lessons to master AI tools. Streaks, certificates, and real skills." (79 chars)

### Rules

- Do not repeat keywords already in the title
- Focus on benefits, not features ("Master AI" not "Contains lessons")
- Include 1-2 high-value keywords not in the title
- iOS: subtitle is indexed for search; make every character count
- Android: short description appears on the store listing and is indexed

---

## Description Strategy

### First 3 Lines (The Hook)

Only the first ~170 characters (iOS) or ~80 characters (Android before "Read more") are visible without expanding. This is your headline.

**Template:**
```
Learn AI the smart way — in just 3 minutes a day.

Join 50,000+ learners mastering ChatGPT, Gemini, DALL-E,
and 10+ AI tools with fun, daily lessons.
```

### Full Description Structure

```
[Hook — 2-3 lines, value proposition + social proof]

WHY 3 MINUTE AI?
- Daily bite-sized lessons that fit your schedule
- Learn real AI skills, not just theory
- 28-day challenge with certificates
- 10+ AI tools: ChatGPT, Gemini, DALL-E, Midjourney, and more

WHAT YOU'LL LEARN
- Write better with AI (emails, reports, creative writing)
- Generate stunning images with DALL-E and Midjourney
- Save hours with AI productivity tools
- Use AI for learning, fun, and earning more

HOW IT WORKS
1. Take a quick quiz to personalize your learning path
2. Get one daily lesson (just 3 minutes)
3. Practice with real AI tools inside the app
4. Build streaks, earn XP, and unlock certificates

FEATURES
- Personalized learning paths based on your goals
- Daily streaks and gamification to keep you motivated
- Completion certificates for your LinkedIn profile
- Works offline — learn anywhere, anytime

FREE TO START
Download now and get your first lessons free. Upgrade to
Premium for unlimited access, certificates, and all AI tools.

[Closing CTA]
```

### Description Rules

1. **Keyword density**: Use primary keywords 3-5 times naturally (iOS does not index the description for search, but Android does)
2. **Formatting**: Use line breaks liberally. Short paragraphs. Bullet points.
3. **No competitor names**: Do not mention Duolingo, Coursera, etc. by name
4. **Social proof**: Include user count, ratings, or press mentions
5. **CTA**: End with a clear call to action ("Download now")
6. **Update regularly**: Fresh descriptions signal an active app to the algorithm

---

## Review Solicitation

### When to Ask

**Ask after positive moments:**
- Completing a streak milestone (3, 7, 14, 28 days)
- Leveling up or earning XP milestone
- Earning a certificate
- Completing a lesson they explicitly liked (if you track sentiment)

**Never ask after:**
- A crash or error
- Content loading failure
- The user's first session (too early)
- Immediately after a paywall dismiss
- Within 24 hours of a previous prompt

### Timing Rules

| Rule | Rationale |
|------|-----------|
| Minimum 3 sessions before first ask | User needs baseline engagement |
| Minimum 48 hours between asks | Prevents annoyance |
| Maximum 3 asks per user per year | Apple may reject apps that ask too often |
| Do not ask during onboarding or quiz | Interrupts core flow |
| Ask within 5 seconds of the positive moment | Emotional high drives higher ratings |

### Implementation

**iOS: SKStoreReviewController (StoreKit)**
- Apple controls when and how the dialog appears
- You can request it, but Apple may suppress it (max 3 times per 365-day period)
- Cannot customize the dialog
- Use `requestReview()` from StoreKit

**Android: Play In-App Review API**
- Google controls the dialog appearance
- Can be shown as a bottom sheet within the app
- No guarantee the dialog will show (Google may suppress)
- Use `ReviewManager` from `com.google.android.play:review`

**Flutter packages:**
- `in_app_review` (cross-platform, wraps both StoreKit and Play Review API)
- Call `InAppReview.instance.requestReview()` at the right moment

### Pre-Prompt Strategy

Before triggering the system review dialog, show a custom in-app prompt:

```
"Enjoying 3 Minute AI?"

[Love it!]     [Could be better]
```

- If "Love it!" -> trigger the system review dialog
- If "Could be better" -> show a feedback form (captures complaints without hurting your rating)

This pattern typically improves average rating by 0.3-0.5 stars.

---

## Category Selection

### Recommended for 3 Minute AI

**Primary category:** Education
**Secondary category (iOS only):** Productivity

### Why Education Over Productivity

| Factor | Education | Productivity |
|--------|-----------|-------------|
| Competition level | High but segmented | Extremely high |
| Top apps | Duolingo, Khan Academy, Quizlet | Notion, Todoist, Microsoft 365 |
| Relevance match | Direct match (AI learning) | Tangential (AI is productive but app is a course) |
| Category browse traffic | Moderate | Very high |
| Ranking difficulty | Moderate (can rank in sub-categories) | Very hard |

**iOS sub-category:** Education > Self-Improvement (if available) or Education > Teaching & Learning

On Google Play, choose "Education" as primary. There are no formal sub-categories, but tags help: "AI," "Learning," "Daily Lessons," "Courses."

---

## Conversion Benchmarks

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Impression-to-page-view (iOS) | <15% | 20-25% | 28-35% | >40% |
| Page-view-to-install (iOS) | <20% | 25-30% | 35-45% | >50% |
| Impression-to-install (combined) | <5% | 8-12% | 15-20% | >25% |
| Impression-to-install: Education category | <8% | 12-18% | 22-28% | >30% |

### What Drives Each Metric

**Impression-to-page-view** (did they tap your listing?):
- App icon quality (most important)
- Title relevance to search query
- Rating stars visible in search results
- First screenshot visible in search results (iOS 15+)

**Page-view-to-install** (did they install after viewing?):
- Screenshot quality and messaging
- Rating and review quality (4.5+ stars critical)
- Description hook (first 3 lines)
- Video preview (if present)

---

## Localization

### Priority Markets (by App Store revenue)

1. **United States** (base language, English)
2. **United Kingdom** (English, minor spelling adjustments)
3. **Germany** (German translation)
4. **Japan** (Japanese translation)
5. **South Korea** (Korean translation)
6. **France** (French translation)
7. **Brazil** (Portuguese translation)
8. **Mexico / Spain** (Spanish translation)

### What to Localize

| Element | Priority | Impact |
|---------|----------|--------|
| Title | Critical | Direct search ranking impact in local language |
| Subtitle / Short description | Critical | Indexed for local search |
| Keywords (iOS) | Critical | Must be in local language for local search |
| Screenshots | High | Localized text on screenshots increases conversion 20-30% |
| Description | Medium | Helps conversion; indexed on Android |
| Video preview | Low | Most users skip video; localize if budget allows |

### Localization Tips

- Do NOT machine-translate keywords. Hire a native speaker or use a localization service.
- Research local keyword volumes (what Germans search for may differ from direct translation)
- Some markets prefer different screenshot styles (Japan prefers more text-heavy screenshots)
- Localized apps see 25-40% more installs in localized markets

---

## Responding to Reviews

### Why It Matters

- Apps that respond to reviews see 0.7 higher average ratings over 6 months
- Responding to negative reviews can prompt users to update their rating
- Apple and Google both surface developer responses prominently

### Response Framework

**5-star reviews:**
```
Thank you, [Name]! We're glad you're enjoying learning AI with us.
Keep up your streak!
```
(Short, warm, reinforces the behavior you want)

**3-4 star reviews:**
```
Thanks for the feedback, [Name]. We'd love to hear what would make
your experience a 5-star one. Email us at support@3minuteai.com
and we'll make it happen.
```
(Acknowledge, invite private conversation, show you care)

**1-2 star reviews:**
```
We're sorry about your experience, [Name]. This isn't the standard
we aim for. Please email support@3minuteai.com with details and
we'll fix this for you right away.
```
(Apologize, take it offline, show urgency)

### Response Rules

- Respond to ALL 1-2 star reviews within 24 hours
- Respond to 3-4 star reviews within 48 hours
- Respond to select 5-star reviews (not all, to avoid looking automated)
- Never argue, never be defensive, never blame the user
- Always provide a way to continue the conversation privately
- After fixing a reported issue, reply again: "We've fixed this in version X.Y. Please try updating!"

---

## A/B Testing

### Google Play Experiments (Free)

Google Play Console offers built-in A/B testing:
- **Store listing experiments**: Test icon, screenshots, description, short description
- **Custom store listings**: Create up to 50 custom listings for different audiences
- **Up to 5 variants** per experiment
- Statistical significance calculated automatically
- Run for minimum 7 days, recommended 14 days

### Apple Product Page Optimization (PPO)

- Test up to 3 treatment variants against the default
- Can test: screenshots, app previews, promotional text
- Cannot test: icon, title, subtitle, description (those require a new app version)
- Available in App Store Connect under "Product Page Optimization"
- Requires iOS 15+

### What to Test First (Priority Order)

1. **Screenshots** (highest conversion impact, 20-40% variance between designs)
2. **App icon** (Google Play only for A/B test; iOS requires version update)
3. **Short description** (Android) / **Promotional text** (iOS)
4. **Screenshot order** (which screenshot is first)
5. **Video preview** (with vs without)

---

## Ratings Maintenance

### Target: 4.5+ Stars

| Rating | Impact |
|--------|--------|
| 4.7-5.0 | Maximum conversion; featured consideration |
| 4.5-4.6 | Strong conversion; rounds up to 4.5 in display |
| 4.0-4.4 | Average; noticeable conversion drop below 4.5 |
| 3.5-3.9 | Significant conversion penalty; users hesitate |
| Below 3.5 | Severe impact; many users will not install |

### Maintaining High Ratings

1. **Pre-prompt filtering**: Ask "Enjoying the app?" before triggering review dialog. Route unhappy users to feedback form.
2. **Fix issues fast**: Negative reviews about bugs hurt if the bug persists for weeks. Ship fixes quickly and respond to reviews noting the fix.
3. **Reset ratings on major updates**: Both stores allow rating resets. Use after a major version that fixes longstanding issues.
4. **Monitor weekly**: Set up alerts for rating drops. A 0.2-star drop in a week signals a bug or bad update.
5. **Incentivize without violating policy**: You cannot offer rewards for reviews (policy violation). You CAN time the ask to follow a positive experience.

## References

- `references/plutus-app-hooks.md`: 34 fill-in-the-blank templates + 300 proven UGC hooks across 10 categories + 5 performance insights. Use for subtitle (iOS 30-char), short description (Android 80-char), feature-bullet hooks, and promotional text. Impossible Claim and Comparison categories compress best into store-listing character limits — adapt the hook pattern, drop the narrative scaffolding. Pair with the specificity insight (concrete number beats vague claim) for subtitle optimization.
- `references/static-headline-formulas.md`: The 3–5 word headline playbook maps directly onto store-listing character limits. Use the 4 features (short + power word + number + audience callout), awareness-stage targeting, and 5 proven formulas for app title, subtitle, short description, and promotional text. The Number + Adjective + Promise formula is especially effective for subtitle slots.
