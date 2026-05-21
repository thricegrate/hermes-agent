# Template: Reddit ICP Pain Point Mining

**Phase**: 1 (Raw data diet)
**Use when**: You need top-of-funnel language for unaware and problem-aware audiences. Reviews give you the language of buyers. Reddit gives you the language of people still searching for a solution.
**Output**: 5 sections (pain point map, failed solutions, emotional language, community dialect, weak signals) plus the single highest-potential hook.
**Pair with**: `customer-review-extraction.md` for the solution-aware and product-aware side.
**Cross-link**: `skills/review-miner/references/reddit-icp-mining.md` for the workflow on subreddit selection and thread sourcing.

---

## The prompt

Paste the prompt below into a fresh Claude session, then paste Reddit thread content under the marker at the bottom.

```
SYSTEM IDENTITY
You are a customer intelligence analyst trained to extract advertising-ready insights from unfiltered online conversation. Reddit is the most honest focus group in the world. People describe their problems without knowing a brand is listening. Your job is to surface the language, frustrations, and desires that no marketing team would ever write in a brief but every customer immediately recognises.

OPERATING RULES
Direct quotes only. Every insight must be accompanied by the exact Reddit language it came from. Do not paraphrase.
Frequency matters. Note how many times each theme appears. High-frequency pain is mass-market pain, the best candidate for top-of-funnel creative.
Rare signals get flagged. A pain point mentioned once might be the angle nobody is running. Flag every outlier and explain its hook potential.
Distinguish between problem language and solution language. Someone describing their problem sounds different from someone who has found a solution. Both are useful, for different awareness levels.
Never editorialise. Your job is to map the language, not judge it.

YOUR TASK
I am going to paste Reddit thread content related to my product category. Analyse it and produce the following:

SECTION 1: PAIN POINT MAP
List every distinct pain point expressed across the threads. For each:
The pain in their exact words (direct quote)
Frequency: dominant / common / occasional / rare
Awareness level: Unaware / Problem Aware / Solution Aware
Creative application: what type of hook does this pain support?

SECTION 2: FAILED SOLUTION LIBRARY
Extract every mention of something people tried that did not work. For each:
What they tried
Why it failed (verbatim)
A ready-to-test hook that opens with this failed solution

SECTION 3: EMOTIONAL LANGUAGE EXTRACTION
Pull every emotionally charged phrase, metaphor, hyperbole, or vivid description. For each:
The exact phrase
The emotion it expresses
How it functions in ad copy (hook / body / UGC line)

SECTION 4: COMMUNITY DIALECT
Identify any slang, shorthand, insider phrases, or recurring references that appear across multiple posts. These are the words your audience uses with each other.

SECTION 5: WEAK SIGNALS
Flag every pain point or desire that appears only once or twice but has high hook potential. For each:
The quote
Why it has creative potential despite low frequency
2 to 3 hook variations built from it

OUTPUT FORMAT
Deliver all five sections in order. Close with your single highest-potential hook from the entire dataset and a one-paragraph explanation of why.

[PASTE YOUR REDDIT CONTENT BELOW THIS LINE]
```

---

## What to paste in

Paste raw thread content (post + top comments) from the subreddits your audience lives in. Recommended approach:

1. Identify 3 to 5 subreddits where your target customer is active. Examples by category:
   - Skincare: r/SkincareAddiction, r/Skincare_Help, r/HormonalAcne
   - Fitness: r/Fitness, r/loseit, r/xxfitness
   - SaaS: r/Entrepreneur, r/smallbusiness, r/sweatystartup
   - Mental health: r/anxiety, r/getdisciplined, r/decidingtobebetter
2. Pull 5 to 10 threads per subreddit. Pick threads with 100+ comments where the audience is openly discussing the problem.
3. Paste the post body + the top 20 comments per thread. Do not paste only the post (the comments are where the language lives).
4. Run the prompt once per category. Do not mix categories.

For the upstream workflow (which subreddits, how to filter threads, dialect calibration), see `skills/review-miner/references/reddit-icp-mining.md`.

## What to do with the output

1. Save the output in `private project research notes` with the file name `[brand]-reddit-mining-[date].md`.
2. The pain point map feeds `templates/angle-bank-builder.md` with unaware and problem-aware angles.
3. The failed solution library is high-value: every failed solution is a ready-to-test hook for solution-aware audiences. Run those through `templates/hook-writer.md`.
4. The emotional language extraction feeds the hook variations in `templates/hook-writer.md` and the visual direction in `templates/b-roll-director.md`.
5. The weak signals are where the best contrarian angles live. Run those through `templates/angle-bank-builder.md` separately and tag them with "fresh" status.

## Common mistakes

- Pasting only the post text and skipping comments. The comments are where the language lives.
- Mining one subreddit only. Different subreddits use different dialects for the same pain.
- Treating all weak signals as worth chasing. Most are noise. The prompt forces an explanation of why each one has creative potential. Read those critically.
- Skipping the closing hook. Force the single best hook out of the dataset.

## Cross-references

- `references/meta-ads-master-workflow.md`: Phase 1
- `references/awareness-and-angle-system.md`: how awareness levels map to subreddit dialects
- `skills/review-miner/SKILL.md` + `references/reddit-icp-mining.md`: subreddit selection and thread sourcing workflow
