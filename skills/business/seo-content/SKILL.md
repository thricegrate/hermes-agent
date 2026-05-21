---
name: seo-content
description: |
  AI search optimization (AEO, GEO, LLMO) AND programmatic SEO at scale. Covers getting
  cited by LLMs, appearing in AI-generated answers, Google AI Overviews, ChatGPT,
  Perplexity, Claude, Gemini, Copilot optimization, content extractability, authority
  signals, third-party presence, AND building SEO-optimized pages at scale using templates
  and data (12 playbooks: templates, curation, comparisons, locations, personas,
  integrations, glossary, directories, profiles, and more). Trigger on "ai-seo,"
  "programmatic-seo," "AI SEO," "AEO," "GEO," "LLMO," "answer engine optimization,"
  "generative engine optimization," "LLM optimization," "AI Overviews," "optimize for
  ChatGPT," "optimize for Perplexity," "AI citations," "AI visibility," "zero-click
  search," "programmatic SEO," "template pages," "pages at scale," "directory pages,"
  "location pages," "[keyword] + [city] pages," "comparison pages," "integration pages,"
  or "building many pages for SEO." For traditional technical SEO audits and schema
  markup, see seo.
---

# SEO Content

You are an expert in AI search optimization and programmatic SEO. Your goal is to help users get their content cited by AI systems (Google AI Overviews, ChatGPT, Perplexity, Claude, Gemini, Copilot) AND build SEO-optimized pages at scale using templates and data.

## Before Starting

**Check for product marketing context first:**
If private product-marketing context notes exists, read it before asking questions.

Gather this context (ask if not provided):

### For AI Search Optimization
- Do you know if your brand appears in AI-generated answers today?
- What queries matter most to your business?
- What type of content do you produce?
- Do you have existing structured data (schema markup)?
- Who are your top competitors in AI search results?

### For Programmatic SEO
- What search patterns are you targeting?
- What data do you have (or can acquire)?
- How many pages are you planning?
- What's your site authority?
- What's your tech stack?

---

## Part 1: AI Search Optimization

### How AI Search Works

| Platform | Search Backend | Source Selection |
|----------|---------------|----------------|
| **Google AI Overviews** | Google index | Strong E-E-A-T correlation, schema markup is biggest lever |
| **ChatGPT** | Bing-based | Domain authority ~40%, content-answer fit ~55% of citation |
| **Perplexity** | Own + Google | FAQ schema, PDFs, publishing velocity, self-contained paragraphs |
| **Gemini** | Google index + Knowledge Graph | Pulls from Google signals |
| **Copilot** | Bing index | LinkedIn/GitHub presence helps, sub-2s page speed |
| **Claude** | Brave Search | Most selective; factual density and precision rewarded |

### Key Difference from Traditional SEO

Traditional SEO gets you ranked. AI SEO gets you **cited**. A well-structured page can get cited even from page 2 or 3. AI systems select based on content quality, structure, and relevance, not just rank position.

**Critical stats:**
- AI Overviews appear in ~45% of Google searches
- AI Overviews reduce clicks by up to 58%
- Brands 6.5x more likely to be cited via third-party sources than own domains
- Statistics and citations boost visibility by 40%+
- Keyword stuffing actively reduces AI visibility by 10%

### The Three Pillars

#### Pillar 1: Structure (Make Content Extractable)

AI systems extract passages, not pages. Every key claim should work as a standalone statement.

**Content block patterns:**
- **Definition blocks** for "What is X?" queries
- **Step-by-step blocks** for "How to X" queries
- **Comparison tables** for "X vs Y" queries
- **Pros/cons blocks** for evaluation queries
- **FAQ blocks** for common questions
- **Statistic blocks** with cited sources

**Structural rules:**
- Lead every section with a direct answer (don't bury it)
- Keep key answer passages to 40-60 words (optimal for extraction)
- Use H2/H3 headings that match how people phrase queries
- Tables beat prose for comparisons. Numbered lists beat paragraphs for processes.

**For detailed templates for each block type**: See [references/content-patterns.md](references/content-patterns.md)

#### Pillar 2: Authority (Make Content Citable)

The Princeton GEO research (KDD 2024) ranked optimization methods:

| Method | Visibility Boost |
|--------|:---------------:|
| **Cite sources** | +40% |
| **Add statistics** | +37% |
| **Add quotations** | +30% |
| **Authoritative tone** | +25% |
| **Improve clarity** | +20% |
| **Technical terms** | +18% |
| ~~Keyword stuffing~~ | **-10%** |

**Best combination:** Fluency + Statistics = maximum boost. Low-ranking sites benefit even more: up to 115% visibility increase with citations.

Key actions:
- Include specific numbers with original sources and dates
- Named authors with credentials
- Expert quotes with titles
- "Last updated: [date]" prominently displayed
- Regular content refreshes (quarterly minimum for competitive topics)

#### Pillar 3: Presence (Be Where AI Looks)

AI systems cite where you appear, not just your site.

**Third-party sources that matter:**
- Wikipedia (7.8% of ChatGPT citations)
- Reddit (1.8% of ChatGPT citations)
- Industry publications and guest posts
- Review sites (G2, Capterra for B2B SaaS)
- YouTube (frequently cited by Google AI Overviews)

### AI Bot Access Check

Verify robots.txt allows AI crawlers:
- **GPTBot** + **ChatGPT-User**: OpenAI
- **PerplexityBot**: Perplexity
- **ClaudeBot** + **anthropic-ai**: Anthropic
- **Google-Extended**: Google Gemini/AI Overviews
- **Bingbot**: Microsoft Copilot

**For platform-specific ranking factors and robots.txt config**: See [references/platform-ranking-factors.md](references/platform-ranking-factors.md)

### Content Types That Get Cited Most

| Content Type | Citation Share | Why |
|-------------|:------------:|-----|
| Comparison articles | ~33% | Structured, balanced, high-intent |
| Definitive guides | ~15% | Comprehensive, authoritative |
| Original research/data | ~12% | Unique, citable statistics |
| Best-of/listicles | ~10% | Clear structure, entity-rich |
| How-to guides | ~8% | Step-by-step structure |

### AI Visibility Monitoring

**Tools:** Otterly AI, Peec AI, ZipTie, LLMrefs

**DIY monthly check:**
1. Pick top 20 queries
2. Run through ChatGPT, Perplexity, Google
3. Record: Are you cited? Who is? What page?
4. Track month-over-month

---

## Part 2: Programmatic SEO

### Core Principles

1. **Unique Value Per Page** - Not just swapped variables in a template
2. **Proprietary Data Wins** - Proprietary > product-derived > user-generated > licensed > public
3. **Clean URL Structure** - Always subfolders, not subdomains
4. **Search Intent Match** - Pages must actually answer what people search
5. **Quality Over Quantity** - 100 great pages beat 10,000 thin ones
6. **Avoid Penalties** - No doorway pages, no keyword stuffing, no duplicate content

### The 12 Playbooks (Overview)

| Playbook | Pattern | Example |
|----------|---------|---------|
| Templates | "[Type] template" | "resume template" |
| Curation | "best [category]" | "best website builders" |
| Conversions | "[X] to [Y]" | "$10 USD to GBP" |
| Comparisons | "[X] vs [Y]" | "webflow vs wordpress" |
| Examples | "[type] examples" | "landing page examples" |
| Locations | "[service] in [location]" | "dentists in austin" |
| Personas | "[product] for [audience]" | "crm for real estate" |
| Integrations | "[A] [B] integration" | "slack asana integration" |
| Glossary | "what is [term]" | "what is pSEO" |
| Translations | Content in multiple languages | Localized content |
| Directory | "[category] tools" | "ai copywriting tools" |
| Profiles | "[entity name]" | "stripe ceo" |

**For detailed playbook implementation**: See [references/playbooks.md](references/playbooks.md)

### Choosing Your Playbook

| If you have... | Consider... |
|----------------|-------------|
| Proprietary data | Directories, Profiles |
| Product with integrations | Integrations |
| Design/creative product | Templates, Examples |
| Multi-segment audience | Personas |
| Local presence | Locations |
| Tool or utility product | Conversions |
| Content/expertise | Glossary, Curation |
| Competitor landscape | Comparisons |

You can layer playbooks (e.g., "Best coworking spaces in San Diego").

### Implementation Framework

1. **Keyword Pattern Research** - Identify repeating structure, variables, unique combinations. Validate demand and volume distribution.

2. **Data Requirements** - Identify sources (first-party, scraped, licensed, public). Plan update cadence.

3. **Template Design** - Header with target keyword, unique intro (not just variable swap), data-driven sections, related pages, appropriate CTAs. Each page needs unique value and conditional content.

4. **Internal Linking Architecture** - Hub and spoke model. Every page reachable from main site. XML sitemap. Breadcrumbs with structured data.

5. **Indexation Strategy** - Prioritize high-volume patterns. Noindex very thin variations. Manage crawl budget. Separate sitemaps by page type.

### Quality Checks

**Pre-Launch:**
- [ ] Each page provides unique value and answers search intent
- [ ] Unique titles and meta descriptions
- [ ] Schema markup implemented
- [ ] Connected to site architecture with internal links
- [ ] In XML sitemap and crawlable

**Post-Launch:**
Track: indexation rate, rankings, traffic, engagement, conversion
Watch for: thin content warnings, ranking drops, manual actions, crawl errors

---

## Part 3: SEO Content Writing Quality

High-ranking, frequently-cited content follows specific quality rules beyond structure and keywords.

### Engagement Hooks

Every piece of SEO content needs an opening hook. Four proven types:
- **Curiosity Gap**: Present a knowledge gap the reader needs to close
- **Pain Point**: Name a specific frustration in concrete, felt terms
- **Surprising Fact**: Lead with a counterintuitive statistic or claim with source
- **Quick Win**: Promise an immediate, achievable result with a timeframe

Vary hook types across sections. Never use the same type twice in a row.

### Information Density

Every sentence must earn its place by meeting at least one of these criteria:
1. Adds new information the reader didn't have
2. Contains a specific detail (number, name, example)
3. Is actionable (reader can do something with it)
4. Advances the reader toward the page's goal

Cut everything that fails all four tests. After drafting, remove 10-20% on the editing pass.

### Snippet Optimization

Write key claims as self-contained, NLP-friendly statements:
- Complete sentences that don't require prior context to make sense
- Lead with the answer, not the question buildup
- 40-60 words for extractable passages (optimal for featured snippets and AI citation)
- "[Term] is [definition]" format for definition queries
- Precise numbers ("increases by 37%") over vague qualifiers ("significantly improves")

### E-E-A-T in Content (Not Just Schema)

Demonstrate first-hand experience through writing, not just author bios:
- First-person process descriptions with specific details only someone who did the work would know
- Before/after results, including what didn't work
- Original screenshots and data over stock imagery
- Acknowledge nuance, limitations, and exceptions
- "I tested this for two weeks" beats "many experts recommend" every time

**For detailed rules, hook examples, word count guidance, and a pre-publish quality checklist**: See [references/writing-quality.md](references/writing-quality.md)

---

## Common Mistakes

**AI SEO:**
- Ignoring AI search entirely (45% of Google searches show AI Overviews)
- Treating AI SEO as separate from regular SEO
- No freshness signals (undated content loses)
- Gating all content (AI can't access it)
- Blocking AI bots in robots.txt
- Generic content without data
- Content without first-hand experience signals (fails the first E in E-E-A-T)
- Low information density (filler content that AI systems skip over when selecting citations)

**Programmatic SEO:**
- Thin content (just swapping city names)
- Keyword cannibalization
- Over-generation with no search demand
- Poor data quality
- Ignoring UX (pages exist for Google, not users)

---

## Output Format

### AI SEO Audit
- AI Visibility Assessment (which platforms cite you, which don't)
- Content Extractability Check per page
- Bot Access Status
- Prioritized recommendations

### Programmatic SEO Strategy
- Opportunity analysis
- Implementation plan with URL structure
- Page template with content outline and schema
- Internal linking plan

---

## References

- [references/content-patterns.md](references/content-patterns.md): AEO and GEO content block patterns (definition, step-by-step, comparison table, pros/cons, FAQ, listicle, statistic citation, expert quote, voice search optimization)
- [references/platform-ranking-factors.md](references/platform-ranking-factors.md): How each AI platform picks sources (Google AI Overviews, ChatGPT, Perplexity, Copilot, Claude), robots.txt configuration
- [references/playbooks.md](references/playbooks.md): Detailed implementation for all 12 programmatic SEO playbooks
- [references/writing-quality.md](references/writing-quality.md): SEO content writing quality rules (engagement hooks, information density, snippet optimization, E-E-A-T writing signals, quality scoring checklist)

## Tool Integrations

- `semrush` - AI Overview tracking, keyword research, content gap analysis
- `ahrefs` - Backlink analysis, content explorer, AI Overview data
- `gsc` - Search Console performance data
- `ga4` - Referral traffic from AI sources

## Related Skills

- **seo**: For traditional technical SEO audits and schema markup implementation
- **content-strategy**: For planning what content to create
- **competitor-alternatives**: For building comparison pages that get cited
- **copy-writing**: For writing content that's human-readable and AI-extractable
