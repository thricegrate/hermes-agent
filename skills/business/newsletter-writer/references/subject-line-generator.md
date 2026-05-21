# Reddit-Style Subject Line Generator

Generate 20 clickbait subject line ideas from any newsletter text. This is a complementary tool to `references/subject-line-swipe-file.md` (which has frameworks and CC performance data). Use this generator for short, punchy, Reddit-style subject lines.

---

## Rules

- 20 total variants: 10 standard + 10 punchier "Reddit-style"
- 5 words or less per subject line
- Informal, spicy, emotional, friend-to-friend tone
- Evoke strong emotions: curiosity, interest, FOMO
- Better be clear than smart
- Do not make offensive or provocative statements for the reader
- Use numbers in some variants
- Sentence case: capitalize first word only + proper nouns/acronyms (Google, ChatGPT, etc.)
- Every variant must use a completely different angle
- First 10 can sound standard; last 10 must be extra punchy "Reddit-style"
- Check all output against `references/banned-words.md` subject line section

## Process

1. Analyze the newsletter text
2. Find the central idea
3. Generate 10 standard clickbait variants (different angles)
4. Generate 10 punchier "Reddit-style" variants (even more different angles)

## When to Use

After the newsletter body is written, run this generator against the finished text. Use alongside (not instead of) the frameworks in `subject-line-swipe-file.md` and the A/B testing guidance in SKILL.md Step 6.

---

## Ready-to-Use Prompt Template

Paste the newsletter text after "TEXT:" and run:

```
Let's think differently. Think in steps. Now analyse the text, find the central idea, and give me 20 ideas for the clickbait title of this newsletter. Informal, spicy and emotional like a friend would write to a friend. Short, 5 words or less, simple, straightforward. Evoke strong emotions, curiosity, interest, FOMO. Better be clear than smart. Do not make offensive, provocative statements for the reader. Try using numbers in some. Use lowercase for all words but the first and any acronyms or proper nouns (Google, ChatGPT etc.). Make all the variants very different, using completely different angles. Leave first 10 as they might sound boring. Give me even punchier "Reddit-style" variants.  AVOID THESE WORDS: money, gold, cash, offer, now, today, sales, profits, profit, hidden, millionaire, deal, subscribe, millions, income, here, financial, success, satisfaction, cost, all, get, life, action, stop, chance, click below, freedom, immediately, here, spam, winning, opportunity, please, act, boss, prize, off, phone, won't, great, offer, earn, rate, $, %, open rate, avoid, get, save, now, guarantee, the best, performance, compare, affordable, open, terms, access, new, claims. TEXT:
```
