# Keyword Strategy for App Store Optimization

## Keyword Research Methodology

### Step 1: Seed Keywords

Start with the obvious terms your target user would search for. For 3 Minute AI:

**Primary seeds:**
- learn AI
- AI course
- AI learning
- AI tutorial
- learn ChatGPT
- AI tools
- artificial intelligence course

**Secondary seeds:**
- learn Gemini
- AI for beginners
- daily learning app
- AI productivity
- ChatGPT tutorial
- AI skills
- learn AI free

**Long-tail seeds:**
- how to use ChatGPT
- learn AI in 5 minutes
- AI course for beginners
- best app to learn AI
- daily AI lessons
- AI learning app free
- master artificial intelligence

### Step 2: Competitor Keyword Mining

Identify the top 5-10 competitors and extract their keywords:

| Competitor | Category | Keywords to Mine |
|-----------|----------|-----------------|
| Coursera | Education | online courses, learn skills, AI certification |
| Duolingo | Education | daily lessons, streaks, gamified learning |
| Khan Academy | Education | free learning, courses, education |
| Brilliant | Education | learn AI, math, science, daily challenges |
| Mimo | Education | learn coding, daily lessons, programming |
| ChatGPT (OpenAI) | Productivity | AI assistant, ChatGPT, AI chat |
| Google Gemini | Productivity | AI, Gemini, Google AI |

**How to extract competitor keywords:**
1. Search for each competitor in the store and note which keywords bring them up
2. Use ASO tools (App Annie, Sensor Tower, AppTweak) to see competitor keyword rankings
3. Read competitor reviews for language real users use ("I wanted to learn AI" = keyword: learn AI)
4. Check competitor descriptions for repeated terms

### Step 3: Keyword Evaluation Matrix

Score each keyword on three dimensions:

| Keyword | Search Volume (1-10) | Competition (1-10) | Relevance (1-10) | Priority Score |
|---------|---------------------|-------------------|------------------|---------------|
| learn AI | 8 | 7 | 10 | 25 |
| AI course | 7 | 8 | 9 | 24 |
| ChatGPT tutorial | 6 | 5 | 8 | 19 |
| AI for beginners | 5 | 4 | 9 | 18 |
| daily AI lessons | 3 | 2 | 10 | 15 |
| artificial intelligence | 9 | 10 | 7 | 26 |
| learn AI free | 4 | 3 | 9 | 16 |
| AI tools | 7 | 6 | 8 | 21 |
| AI learning app | 5 | 3 | 10 | 18 |

**Priority = Volume + (10 - Competition) + Relevance**

High volume + low competition + high relevance = target these first.

### Step 4: Keyword Mapping

Assign keywords to specific metadata fields:

```
TITLE (highest weight):
  Primary keyword: "Learn AI" or "AI Learning"

SUBTITLE / SHORT DESCRIPTION (high weight):
  Secondary keywords: "Daily Lessons", "AI Tools", "ChatGPT"

KEYWORD FIELD - iOS only (high weight):
  Remaining keywords, comma-separated, no spaces after commas:
  "course,tutorial,beginners,free,chatgpt,gemini,dalle,
   midjourney,productivity,skills,daily,challenge,certificate"

DESCRIPTION (Android: indexed; iOS: not indexed for search):
  All keywords naturally incorporated into readable copy
```

---

## iOS Keyword Field Optimization

The iOS keyword field is 100 characters, hidden from users, and heavily weighted for search.

### Rules

1. **Comma-separated, no spaces after commas** (spaces waste characters)
2. **No duplicates** of words already in the title or subtitle (Apple already indexes those)
3. **Singular form only** (Apple matches both singular and plural)
4. **No prepositions or articles** (the, a, an, for, with, in — waste characters)
5. **No competitor brand names** (policy violation, may cause rejection)
6. **No category name** (Apple already associates your app with its category)

### Example for 3 Minute AI

Title: "3 Minute AI - Learn AI Daily" (contains: minute, AI, learn, daily)
Subtitle: "Master AI Tools in 3 Minutes" (contains: master, tool, minute)

Keyword field (100 chars):
```
course,tutorial,chatgpt,gemini,dalle,midjourney,beginner,skill,
challenge,certificate,lesson,free,productivity,image,writing
```

Character count: 99 (leave 1 char buffer)

**Do NOT include:** AI (in title), learn (in title), daily (in title), master (in subtitle), tool (in subtitle), minute (in both)

---

## Android Keyword Strategy

Android has no hidden keyword field. Google extracts keywords from ALL visible text:
- Title (50 chars, highest weight)
- Short description (80 chars, high weight)
- Full description (4,000 chars, moderate weight)

### Keyword Density Guidelines for Android Description

| Keyword Type | Recommended Occurrences | Placement |
|-------------|------------------------|-----------|
| Primary (learn AI, AI course) | 4-5 times | Title, short desc, first paragraph, features, closing |
| Secondary (ChatGPT, daily lessons) | 3-4 times | Short desc, features section, how-it-works |
| Long-tail (AI for beginners) | 2-3 times | Description body, naturally |
| Related (productivity, skills) | 1-2 times | Feature bullets, closing |

**Over-optimization risk:** If Google detects keyword stuffing, it may penalize your ranking. Keep keyword density under 3% of total description word count. Every keyword usage must read naturally.

---

## Keyword Performance Tracking

### Metrics to Monitor Weekly

| Metric | What It Tells You | Action Threshold |
|--------|------------------|-----------------|
| Keyword rank (position for each keyword) | Are you rising or falling? | Drop of 5+ positions = investigate |
| Keyword search volume trends | Is demand growing or shrinking? | Shift to growing keywords |
| Impression share by keyword | Which keywords drive the most views? | Focus on top 10 impression drivers |
| Conversion rate by keyword | Which keywords bring high-intent users? | Prioritize high-conversion keywords |
| Competitor keyword changes | What are competitors targeting? | React to new competitor keywords within 2 weeks |

### Keyword Refresh Cadence

| Timeframe | Action |
|-----------|--------|
| Weekly | Check rank movement for top 20 keywords |
| Monthly | Evaluate keyword performance, swap underperformers |
| Quarterly | Full keyword research refresh, competitor re-analysis |
| After major update | Update keywords to reflect new features |
| Seasonal | Add trending/seasonal keywords (e.g., "new year goals" in January) |

---

## Seasonal Keyword Opportunities

| Season / Event | Keywords to Add | Duration |
|---------------|----------------|----------|
| January (New Year) | new year goals, learn new skill, self improvement, resolution | Jan 1 - Jan 31 |
| Back to school (Aug-Sep) | education, learning, study, school | Aug 1 - Sep 30 |
| AI news events (ongoing) | Latest AI tool names, trending AI terms | 1-2 weeks after event |
| Black Friday / Cyber Monday | deal, discount, sale (only if running a promo) | Nov 20 - Dec 1 |
| Summer | summer learning, bored, productive summer | Jun 1 - Aug 15 |

### How to Implement Seasonal Keywords

1. Keep 70% of your keyword field as evergreen (your core keywords)
2. Rotate 30% seasonally (swap in trending terms, swap out lowest performers)
3. Update subtitle/short description to match seasonal angle if relevant
4. Update first screenshot text to match seasonal messaging

---

## Competitor Analysis Framework

### Step-by-Step Process

1. **Identify top 10 competitors** in your category and adjacent categories
2. **For each competitor, document:**
   - Title and subtitle keywords
   - Rating and review count
   - Screenshot messaging (what benefits do they highlight?)
   - Description structure and keywords
   - Recent updates (what are they adding?)
   - Estimated downloads (use Sensor Tower or similar)

3. **Build a keyword overlap matrix:**

| Keyword | Your App | Competitor A | Competitor B | Competitor C |
|---------|----------|-------------|-------------|-------------|
| learn AI | Title | Description | Title | Not used |
| AI course | Subtitle | Title | Not used | Keywords |
| ChatGPT | Keywords | Title | Title | Title |
| daily lessons | Title | Not used | Subtitle | Keywords |

4. **Identify gaps:** Keywords competitors rank for that you don't target
5. **Identify opportunities:** Keywords with volume that NO competitor targets well
6. **Identify defensive keywords:** Your brand name, app name variations, common misspellings

### Defensive Keywords

Always include:
- Your brand name and variations ("3minuteai", "3 minute ai", "three minute ai")
- Common misspellings ("3 minuet AI", "3 minut AI")
- Abbreviations ("3min AI")

If you don't claim these, a competitor might rank for searches of YOUR brand name.
