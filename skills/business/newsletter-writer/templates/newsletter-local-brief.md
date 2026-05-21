# Newsletter Template: Local Brief (Naples / Fort Myers)

Parameterized template for both **Naples Brief** and **Fort Myers Brief**. Set `[CITY]` to either "Naples, FL" or "Fort Myers, FL" before running.

---

## Sub-Template A: Weekly News Search

Use this to find and format last week's local news for `[CITY]`.

### Run this prompt (replace [CITY] and [DATES]):

```
Do a deep search on the internet for last week's (strictly for these dates) news for [CITY]. Select the news that might be interesting for a typical 50+ y.o. Resident. Select only "long living" news, not the ones that might not be relevant for the upcoming week (like road closures or festivals that already took place). Put the URLs to the sources in clickable headlines (source should be invisible). Do not mention the source at the end of each news snippet or anywhere in the headlines. Check availability of each URL as often you provide "page not found" pages. The news itself should be presented in 1-2 sentences. Give at least 12 news. IMPORTANT: Check links for availability before inserting. Avoid news-press.com as it has paywall. Remove dates and links in the end, keep urls only in the headline. Start from the new line after the headline. Remove the links at the end of each snippet, keep them only in the headlines. Remove your analysis before and after - keep only the news.
```

### Output Format Example:

```
🔗 [Fort Myers Hotel Evacuated After Early-Morning Fire](https://www.gulfcoastnewsnow.com/article/fort-myers-hotel-evacuated-after-fire-saturday/65453959)
A 3:45 a.m. blaze at the downtown Holiday Inn forced guests into the parking lot; firefighters contained the flames and no serious injuries were reported.

🔗 [Surfers for Autism Brings 30+ Kids Back to Fort Myers Beach](https://www.gulfcoastnewsnow.com/article/surfers-for-autism-annual-festival-fort-myers-beach/65454505)
After a multi-year hurricane pause, the festival returned with volunteers helping young surfers catch waves and raise autism awareness.

🔗 [FPL Warns Bills May Jump $11 a Month in 2026](https://www.gulfcoastnewsnow.com/article/fpl-rate-increase-fort-myers/65451084)
Florida Power & Light says growth-driven grid upgrades could mean double-digit rate hikes, with smaller increases through 2028.
```

### News Quality Rules:

- 12+ news items minimum
- 1-2 sentences per item
- "Long living" news only (relevant for the upcoming week, not expired events)
- Clickable URLs hidden in headlines only, nowhere else
- No source attribution in body text
- No dates in body text
- Verify every URL for availability before including
- Avoid paywalled sources (news-press.com)
- No analysis or commentary before/after the news

---

## Sub-Template B: Weekly Events Newsletter

Use this to format Facebook events from a CSV file into a categorized events newsletter for `[CITY]`.

### Run this prompt (attach the CSV file and replace [CITY] and [DATE RANGE]):

```
Analyse the CSV file. Do a detailed search for events and news in [CITY], and use only popular events (defined as # of "interested" and "going" in the x1lliihq column of the CSV file) from the attached CSV file to write a newsletter for [DATE RANGE]. Never mention # of interested or going (its internal metrics). Give me some inspiring 3 sentence intro for this newsletter. Do not put news into it, just events from the CSV file. Always start with food and dining, then family activities, concerts, and other categories. Add clickable links to the events on Facebook to the headlines of each happening. Put links to facebook into clickable headlines of the events and nowhere else - they should be hidden. Convert each scientific notation event ID to its full integer format and construct clean Facebook event URLs. These are the actual URLs as they appear in the CSV file. Rewrite the subject line and intro. Add the URL (verify before adding) to the events in the name of the events. Subtract 1 hour from the time of going. Write time of the event in US (AM/PM) format. Do not mention the number of those going or those interested. Verify the URLs. Use a URL in the headings. Use emojis and H4 font for subsections.
```

### Output Format Example:

```
🌴 Major Events & Celebrations in Fort Myers

Your Weekly Arts & Music Schedule

Your inside look at Lee County's standout events for the week ahead. Here's what local organizers have planned for you. We recommend confirming with the event hosts for complete details and current schedules.

🎵 Music & Entertainment

38 Special
📅 Date: Friday, March 14, 2025
⏰ Time: 5:00 PM
📍 Location: Caloosa Sound Amphitheater
🎸 Details: Don't miss legendary rock band 38 Special as they bring their Southern rock classics to Fort Myers.

DUELO
📅 Date: Saturday, March 15, 2025
⏰ Time: 7:00 PM
📍 Location: 2158 Colonial Blvd, Fort Myers, FL
🎤 Details: Experience the energy of popular Mexican group DUELO live in concert with their distinctive norteño sound.

🎭 Arts & Special Events

Edge of Couture: Spring Runway Show at SBDAC
📅 Date: Friday, March 14, 2025
⏰ Time: 6:00 PM
📍 Location: 2301 1st St, Fort Myers, FL 33901
👗 Details: Experience the latest in fashion at this exciting runway show featuring innovative designs and creative expression.

👨‍👩‍👧‍👦 Family-Friendly Activities

Family Night in the Planetarium
📅 Date: Thursday, March 13, 2025
⏰ Time: 6:00 PM
📍 Location: 3450 Ortiz Ave, Fort Myers, FL 33905
🌌 Details: Explore the wonders of the night sky with your family at this educational and entertaining planetarium experience.

🍻 Food & Drink Events

Firestone 5-Course Bourbon Pairing Dinner
📅 Date: Wednesday, March 12, 2025
⏰ Time: 5:00 PM
📍 Location: 2224 Bay St, Fort Myers, FL 33901
🥃 Details: Indulge in a sophisticated dining experience featuring five courses expertly paired with premium bourbons.
```

### Events Formatting Rules:

- Category order: Food & Dining first, then Family, Concerts, then other categories
- Use emojis for category headers and event detail lines
- H4 font for subsections
- Subtract 1 hour from all CSV times
- Time format: US AM/PM (not 24-hour)
- Facebook event URLs in clickable headlines only, hidden from display
- Convert scientific notation event IDs to full integers for URLs
- Never mention "interested" or "going" counts
- Verify all URLs before including
- 3-sentence inspiring intro
- No news in events newsletter, only events from CSV

---

## Quality Checklist

- [ ] All URLs verified and accessible
- [ ] No paywalled sources (news-press.com)
- [ ] Links only in headlines, nowhere else
- [ ] No source attribution in body
- [ ] 12+ items for news, all popular events for events
- [ ] Correct time format (AM/PM, minus 1 hour for events)
- [ ] Run through `humanizer` before publishing
- [ ] Run through `content-review` before publishing
