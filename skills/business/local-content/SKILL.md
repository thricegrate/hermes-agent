---
name: local-content
description: |
  Generates local content for Naples, FL or Fort Myers, FL. Two modes: (1) Events newsletter
  from a Facebook events CSV, filtered by popularity, categorized, timezone-adjusted, with
  clickable links. (2) Curated local news from web search, filtered for 50+ residents,
  verified URLs, formatted as clean headline list.

  Use this skill when the user says "local events," "events newsletter," "Facebook events,"
  "events CSV," "weekly events," "what's happening this week," "Naples events," "Fort Myers
  events," "local news," "Naples news," "Fort Myers news," "SWFL news," "southwest Florida
  news," "what's happening in Naples," "what's happening in Fort Myers," "local-events,"
  or "local-news."
metadata:
  version: 2.0.0
  tags: events, newsletter, local, swfl, facebook, csv, news, curation
---

# Local Content

Generates two types of local content for Naples, FL or Fort Myers, FL: event newsletters from Facebook CSV data, and curated news from web search. Ask the user which mode they need, or infer from context (CSV file = events mode, "news" keyword = news mode).

---

## Mode 1: Events Newsletter

Reads a CSV of scraped Facebook events, filters for popular ones, and outputs a formatted newsletter ready for publication.

### Step 1: Collect Inputs

You need three things before starting. Ask for any that are missing:

1. **City**: Naples, FL or Fort Myers, FL
2. **CSV file path**: Path to the scraped Facebook events CSV
3. **Date range**: The newsletter week (e.g., "March 9-15" or "this week")

### Step 2: Parse the CSV

The CSV uses obfuscated column names from Facebook's DOM:

| Column | Contains |
|--------|----------|
| `x1i10hfl href` | Facebook event URL (full, with query params) |
| `x1rg5ohu src` | Event cover image URL (ignore this column) |
| `x193iq5w` | Date/time string, e.g. `Sat, 14 Mar at 12:00 -03` |
| `x1i10hfl` | Event name |
| `x193iq5w 2` | Location |
| `x1lliihq` | Popularity, e.g. `1.8K interested . 164 going` |

Read the entire CSV and parse each row into structured event records.

### Step 3: Filter by Date Range

- Parse dates like `Sat, 14 Mar at 12:00 -03` to determine the event day.
- Multi-day events use a range format: `Mon, 9 Mar-13 Mar`. Include these if any day overlaps with the newsletter week.
- Keep only events whose date falls within the user-specified week.
- `Happening now` entries: include only if the current date falls within the newsletter range.
- Drop rows with unparseable or missing dates.

### Step 4: Filter by Popularity

Parse the popularity column to calculate total engagement:

- `1.8K interested . 164 going` = 1800 + 164 = 1964
- `581 interested . 24 going` = 581 + 24 = 605
- `3 going` = 3 (no interested count)
- **"K" suffix** means thousands (1.8K = 1800)

Sort by total engagement descending. Aim for 15-25 events. Look for a natural drop-off point. If fewer than 8 events after filtering, include all regardless of popularity.

### Step 5: Convert Times

CSV times use UTC-3. Florida events are EST (UTC-5). **Subtract 2 hours**, then format as US AM/PM:
- `12:00` = 10:00 AM
- `19:00` = 5:00 PM
- `20:30` = 6:30 PM

### Step 6: Clean Facebook URLs

Strip everything after `?` from each event URL. If an event ID appears in scientific notation (e.g., `1.83927e+15`), convert to full integer form.

### Step 7: Categorize Events

Categorize by name and location into these groups (in this exact order):

1. **Food & Drink Events** -- restaurants, breweries, wine tastings, food festivals
2. **Family-Friendly Activities** -- kids events, outdoor markets, educational programs
3. **Music & Entertainment** -- concerts, live music, DJs, open mic nights
4. **Arts & Special Events** -- theater, comedy, galas, fundraisers, art walks
5. **Community & Outdoor** -- parades, car shows, fitness, wellness (only if events don't fit above)

Each event in exactly one category. Skip Community & Outdoor if empty.

### Step 8: Generate the Newsletter

**Header** (adjust city and county: Fort Myers = Lee County, Naples = Collier County):

```
Major Events & Celebrations in {City}

Your Weekly Events Schedule

Your inside look at {County}'s standout events for the week ahead.
Here's what local organizers have planned for you.

We recommend confirming with the event hosts for complete details and current schedules.
```

**Intro**: Fresh, inspiring 3-sentence intro specific to the week and city. Reference the season and notable themes.

**Event format:**
```
#### [Event Name](https://www.facebook.com/events/XXXXXXXXX/)
Date: Friday, March 14, 2025
Time: 5:00 PM
Location: 2224 Bay St, Fort Myers, FL 33901
Details: One to two sentence description in an inviting tone.
```

**Rules:**
- Facebook URL ONLY in the event name heading link
- Use a contextual emoji for the Details line
- Full date format: day of week, month name, day, year
- Never mention the number of people interested or going
- For multi-day events, show date range and omit time line

---

## Mode 2: News Curation

Curates 12+ local news items from web search, filtered for relevance, with verified URLs.

### Step 1: Determine City

If not specified, ask: Naples, FL or Fort Myers, FL?

### Step 2: Determine Date Range

Monday through Saturday of the **current week**. If today is Sunday, use the previous week.

### Step 3: Search for News

Run multiple WebSearch queries to cast a wide net. Aim for 20+ raw results:

- `"{city} FL" news this week {year}`
- `"{city} Florida" local news {month} {year}`
- `"Southwest Florida" news {month} {year}`
- `"{city} FL" community news {month} {year}`
- `"Collier County" OR "Lee County" news {month} {year}`

### Step 4: Filter Results

**Include:** Community, real estate, health, local government, business openings/closings, infrastructure, environment, wildlife, crime/safety, cost of living. Prefer "long living" stories still relevant next week.

**Exclude:** Events that already happened, expired road closures, weather forecasts, sports scores, national/international news without local angle.

### Step 5: Blacklisted Domains

Never use (paywalled):
- `news-press.com`
- `naplesnews.com`
- `naplesdailynews.com`

Prefer: `winknews.com`, `nbc-2.com`, `fox4now.com`, `gulfcoastnewsnow.com`, `wgcu.org`, `floridaweekly.com`, `businessobserverfl.com`, local `.gov` sites.

### Step 6: Verify Every URL

Use **WebFetch** to confirm each link loads, contains actual article content (not paywall/login), and headline matches. Drop unverified links and find replacements.

### Step 7: Format Output

```
[Headline Text Here](https://verified-url.com/article)
One to two sentence summary. Factual and concise.

[Next Headline Here](https://verified-url.com/another-article)
Summary sentence here.
```

Rules:
- Minimum 12 items
- URL only inside the headline markdown link
- No source names, no date stamps, no intro/closing text
- One blank line between items

---

## Delivery

After displaying either newsletter or news in chat, ask:

> Want me to send this to Telegram?

If yes, send via Telegram.

## Notes

- Both modes produce external-facing content. Before final delivery, run through `humanizer` and `content-review` per project rules.
- Events CSV is a point-in-time scrape. Events may have changed. The header disclaimer covers this.

## Related Skills

- `newsletter-writer` -- general newsletter structure and methodology
- `humanizer` -- required post-processing for external publication
- `content-review` -- required review for external publication
- `content-strategy` -- content planning
