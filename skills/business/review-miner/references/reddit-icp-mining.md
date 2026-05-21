# Reddit ICP Pain Point Mining

Reddit is the most honest focus group. People describe their problems without knowing a brand is listening. This is where the unfiltered top-of-funnel language lives.

Customer reviews (Amazon, Shopify, app stores, post-purchase surveys) capture the language of people who already bought. That language is product-aware and solution-aware. Best for middle and bottom of funnel.

Reddit threads capture the language of people who have not bought yet. That language is unaware and problem-aware. Best for top of funnel.

A complete creative system needs both. This file covers Reddit. For Amazon/Shopify/app-store mining, see [`mining-playbook.md`](mining-playbook.md).

## When to mine Reddit

- Launching a new product and you have no review data yet
- Top of funnel is starved (problem-aware angle bank is thin)
- A new audience segment that does not match the existing customer base
- A category you are entering for the first time
- Quarterly refresh to catch shifting community language

## Subreddit selection

The biggest mistake is mining 1 subreddit. Different subreddits use different dialects for the same pain. Mine 3 to 5 per category for representative language.

Selection criteria:

- Activity: minimum 50K subscribers, multiple threads per day
- Honesty: communities where users openly criticize products (look for "skincare gatekeeping" threads, "what scammed me" threads)
- Specificity: niche subreddits beat broad ones. r/HormonalAcne beats r/SkincareAddiction for hormonal-acne products.

Examples by category:

| Category | Recommended subreddits |
|---|---|
| Skincare | r/SkincareAddiction, r/Skincare_Help, r/HormonalAcne, r/AsianBeauty |
| Fitness | r/Fitness, r/loseit, r/xxfitness, r/bodyweightfitness |
| Sleep | r/insomnia, r/sleep, r/melatonin, r/Sleep_Apnea |
| Mental health | r/anxiety, r/getdisciplined, r/decidingtobebetter, r/MentalHealth |
| SaaS / B2B | r/Entrepreneur, r/smallbusiness, r/sweatystartup, r/SaaS |
| Money / finance | r/personalfinance, r/financialindependence, r/povertyfinance |
| Pets | r/dogs, r/dogtraining, r/Pets, breed-specific subs |

## Thread filtering

Not all threads are equally useful. Mine threads with:

- 100+ comments (high engagement = layered language)
- "What worked / did not work" framing in the title
- Negative feedback threads ("I wasted $X on Y")
- Question threads where the OP gets detailed answers
- "Help me decide" threads where commenters compare alternatives

Skip:

- Pure venting threads with few comments
- Memes and screenshots
- Threads that are clearly promotional (covert affiliate marketing)
- Threads under 6 months old in evergreen categories (the language has not stabilized)

## What to extract

The Reddit ICP mining prompt (`skills/ads-creative/templates/reddit-icp-mining.md`) produces 5 sections:

1. **Pain point map**: every distinct pain expressed, tagged by frequency (dominant / common / occasional / rare) and awareness level.
2. **Failed solution library**: every mention of something tried that did not work. Each one is a ready-to-test hook for solution-aware audiences.
3. **Emotional language extraction**: charged phrases, metaphors, hyperbole, vivid descriptions. These feed hook writing.
4. **Community dialect**: slang, shorthand, insider phrases. The words the audience uses with each other.
5. **Weak signals**: pain points or desires mentioned once or twice but with high hook potential. The contrarian angles that nobody else is running.

## Workflow

1. Identify 3 to 5 subreddits.
2. Pull 5 to 10 threads per subreddit. Save the post body + top 20 comments per thread.
3. Run the Reddit ICP mining prompt once per category (not per subreddit; the prompt synthesizes across subreddits).
4. Save the output in `private project research/`.
5. Feed the pain point map into `skills/ads-creative/templates/angle-bank-builder.md`.
6. Feed the failed solution library into `skills/ads-creative/templates/hook-writer.md`.
7. Pin the community dialect somewhere accessible to the creative team. Hooks that use community dialect outperform hooks that translate the dialect into "business speak."

## Tools

- Manual: browse the subreddit, copy post + comments into a text file. Slow but high-fidelity.
- Reddit search via Old Reddit (old.reddit.com): better than New Reddit for keyword search.
- Reddit JSON API: append `.json` to any thread URL to get structured data. Useful for bulk extraction.
- Third-party tools: GummySearch, Reddit Pro, or build a custom scraper. Pay attention to Reddit's API limits and terms of service.

The mining workflow is high-value even when done manually. The friction forces you to actually read the threads, which surfaces patterns you would miss in a bulk extraction.

## Calibration: problem language vs solution language

The same Reddit user posting at different points in their journey produces different language:

- "I am so tired all the time and I do not know why" (unaware)
- "I think it might be my cortisol levels, has anyone else dealt with this" (problem-aware)
- "I tried adaptogens and they did nothing for me" (solution-aware, failed solution)
- "Does anyone have experience with [specific product]" (product-aware)

The mining prompt asks the model to distinguish. Pay attention to the awareness-level distribution in the output. If 80% of mined language is solution-aware, the subreddit is biased toward people deeper in the funnel. Add a different subreddit for top-of-funnel balance.

## Common mistakes

- Mining one subreddit only. Single-source language is biased.
- Pasting post titles only. The comments are where the language lives.
- Mining without thread filtering. Pure venting threads produce emotional language without actionable angles.
- Treating dialect as cute. Community dialect is the moat. Use it verbatim in hooks.
- Skipping the weak signals. The contrarian angles that scale are usually flagged in the weak signal section.

## Cross-references

- [`mining-playbook.md`](mining-playbook.md): Amazon, Shopify, app store mining workflow
- `skills/ads-creative/templates/reddit-icp-mining.md`: ready-to-paste prompt
- `skills/ads-creative/references/meta-ads-master-workflow.md`: Phase 1 of the 5-phase Meta workflow
- `skills/ads-creative/references/awareness-and-angle-system.md`: how awareness levels map to subreddit dialects
- `skills/ads-creative/templates/angle-bank-builder.md`: where mined pain points become tagged angles
