# Banned Words & Phrases Registry

Centralized list of forbidden words, phrases, and visual concepts across all newsletters. Check output against this file before publishing.

---

## Global Rules (All Newsletters)

- **No em-dashes** (project-wide rule, see `rules/no-em-dashes.md`)
- **Coffee Shop Rule**: every sentence must sound like talking to a friend at a cafe table
- **No low-frequency words**: keep vocabulary simple and conversational
- **No AI slop words**: leverage, utilize, implement, optimize, delve, tapestry, landscape, paradigm, synergy, elevate, foster, robust, seamless, cutting-edge, groundbreaking, game-changer, unlock, empower, harness, navigate, realm, testament, pivotal, holistic, embark, excels, solely, portray, ongoing, vigilance, unleash, multi-faceted, spark, ignite, transformative, revolutionary, supercharge
- **Full AI slop + filler + banned patterns reference**: See `skills/content-review/references/banned-patterns.md` for the complete list (30+ filler phrases, weak transitions, adverb combos, bloated constructions, AI slop markers, AI slop phrases). All patterns in that file also apply to newsletter content.

---

## Subject Line Banned Words

These words trigger spam filters or reduce open rates. Never use in subject lines:

money, gold, cash, offer, now, today, sales, profits, profit, hidden, millionaire, deal, subscribe, millions, income, here, financial, success, satisfaction, cost, all, get, life, action, stop, chance, click below, freedom, immediately, here, spam, winning, opportunity, please, act, boss, prize, off, phone, won't, great, offer, earn, rate, $, %, open rate, avoid, get, save, guarantee, the best, performance, compare, affordable, open, terms, access, new, claims

Additional subject line spam words (from email-optimizer): unlock, discover, revolutionary, game-changing, don't miss, act now, click here, buy now, guaranteed, risk-free, limited time, urgent, congratulations, winner, selected, exclusive deal

---

## 349+ Spam Trigger Words by Category

Source: Mailmeteor 2026 Guide + `skills/email-optimizer/references/subject-line-frameworks.md`. Using one or two won't auto-spam you, but stacking multiple triggers will. Avoid in both subject lines AND email body.

### Money & Financial (highest risk)
$$$, 50% off, accept credit cards, affordable deal, avoid bankruptcy, bad credit, bargain, billion dollars, billionaire, cash, cash bonus, cash out, cents on the dollar, claim your discount, credit card offers, debt, discount, double your wealth, earn $, earn cash, earn extra income, earn from home, easy income, easy terms, for just $, free access, free gift, free investment, free membership, free money, free trial, full refund, get out of debt, giveaway, guaranteed deposit, increase revenue, increase sales, instant earnings, instant income, investment advice, loans, make $, money-back guarantee, mortgage rates, one hundred percent free, only $, price protection, profits, quote, refinance, save $, save big money, subject to credit, why pay more, your income

### Scam & Too-Good-to-Be-True
100% guaranteed, act fast, amazing deal, apply now, as seen on, best deal, big profit, can't miss, click below, click here, deal ending soon, don't delete, double your money, exclusive deal, fantastic offer, get it now, great news, guaranteed results, important information, instant savings, limited time, must read, new customers only, no catch, no cost, no credit check, no obligation, no strings attached, once in a lifetime, only available here, order now, potential earnings, pure profit, risk-free, special invitation, special offer, this won't last, urgent, will not believe

### Marketing & Sales Overpromises
#1, 100% free, 100% off, 100% satisfied, additional income, amazed, amazing, be amazed, be surprised, be your own boss, best bargain, best offer, best price, best rates, big bucks, bonus, can't live without, consolidate debt, double your cash, double your income, drastically reduced, earn extra cash, earn money, expect to earn, extra cash, extra income, fantastic, fast cash, financial freedom, get paid, incredible deal, join millions, lowest price, make money, million dollars, prize, promise, satisfaction guaranteed, save up to, special promotion, the best, thousands, unbeatable offer, unbelievable, unlimited, wonderful, you will not believe your eyes

### Urgency, Clickbait & Pressure
access now, act immediately, act now, action required, apply here, apply now, before it's too late, buy, buy direct, buy now, buy today, call free, call now, can we have a minute of your time, cancel now, cancellation required, claim now, click me to download, click now, click this link, click to get, click to remove, contact us immediately, deal ending soon, do it now, do it today, don't hesitate, don't waste time, expire, expires today, final call, for instant access, for only, for you, get it away, get started now, great offer, hurry up, immediately, info you requested, instant, limited time, now only, offer expires, once in lifetime, order today, please read, purchase now, sign up free, sign up free today, supplies are limited, take action, take action now, this won't last, time limited, top urgent, trial, urgent, what are you waiting for, while supplies last, you are a winner

### Health & Pharma
100% natural, all natural, certified organic, clinical trial, cure for, diet pill, doctor recommended, double blind study, fat burner, fast weight loss, free consultation, get slim, guaranteed weight loss, hair growth, lose weight fast, medical breakthrough, miracle cure, natural remedy, no prescription needed, online pharmacy, over-the-counter, pain relief, prescription drugs, reverse aging, safe and effective, scientifically proven, secret formula, weight loss, youthful skin

### Tech & Security (phishing signals)
access your account, account update, action required, activate now, antivirus, change password, click to verify, confirm your details, confidential information, data breach, download now, final notice, free antivirus, important update, immediate action required, improve security, install now, last warning, log in now, new login detected, online account, password reset, payment details needed, phishing alert, secure payment, security breach, security update, update account, verify identity, warning message

### Gambling, Adult & Blacklisted
adult content, bet now, big win, blackjack, casino bonus, cash out now, click to win, double your money, exclusive access, free chips, free spins, gamble online, hot deal, instant winnings, jackpot, live dealer, lottery winner, lucky chance, online betting, online casino, online gaming, poker tournament, risk-free bet, slots jackpot, spin to win, try for free, VIP offer, winner announced, winning numbers, XXX

---

## Email Deliverability Rules

These rules complement the spam word list. Source: 2026 Mailmeteor guide + our own email-optimizer skill.

### Subject Lines
- No ALL CAPS words. "HUGE SALE" = spam. Sentence case always.
- No excessive punctuation (!!!, ???, $$$). One exclamation mark max, rarely.
- "Free" is context-dependent: "FREE GIFT ACT NOW" = spam. "Your free template is ready" = fine.
- Under 50 characters ideal.
- 1 emoji max, at the end. Avoid flagged emojis (💰🔞🏆🎰).
- Use personalization (recipient name) to boost engagement.

### Email Body
- Text-to-image ratio: at least 60% text, 40% images. Image-only emails get flagged.
- Link count: 2-3 links per email is safe. No URL shorteners (bit.ly, tinyurl).
- Display URL must match actual link destination (no deceptive anchor text).
- Always use HTTPS links.
- Unsubscribe link always visible (required by CAN-SPAM/GDPR).

### Technical
- SPF, DKIM, DMARC configured and passing.
- Bounce rate below 2%.
- Spam complaint rate below 0.1%.
- Clean sending domain reputation (check with Google Postmaster Tools).
- No purchased or scraped lists.

### Free Spam-Check Tools
- **Mail Tester** (mail-tester.com): Full spam analysis including domain auth and content
- **GlockApps**: Tests inbox placement across Gmail, Outlook, Yahoo
- **SpamAssassin**: Open-source spam filter scoring
- Run subject lines through a spam checker before A/B testing

Also see `skills/email-optimizer/references/subject-line-frameworks.md` for the original deliverability section with our CC-specific data.

---

## Feel Better Live Better Banned Words

Same as subject line banned words above, plus these additional terms:

fast, for you, call to action

---

## Grow Monetize Forbidden Mentions

Never mention these terms or near-synonyms that point back to original sources:

Smart Pixel, Chris, podcast, podcasts, guests, host, interview, episode

---

## Banned Visual Concepts (Preview Images)

Never use these overused visual concepts in image prompts:

cathedral, storm, commute, roof-top, prism, conveyor, origami, maze, control room, split screen, sticky notes
