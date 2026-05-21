# Cyber-Corsairs Hold-Review Triage

Generated from the sanitized manifest. This report intentionally lists only relative artifact paths, counts, labels, and decisions; it does not quote private file contents, secrets, or memory text.

## Summary

- Hold-review records triaged: 125
- sanitize-and-import-candidate: 63
- sanitized-imported: 2
- manual-review-superpowers: 16
- profile-local-tooling: 15
- do-not-import-attribution: 1

## Decision buckets

### sanitize-and-import-candidate
Reusable skills that may be worth importing after removing private references and checking for overlap with existing Hermes skills. Do not bulk-copy these yet.

- `skills/ads-analyst` — files=1, private-ref-files=1, duplicate-files=0, labels=telegram-or-chat
- `skills/ads-creative` — files=37, private-ref-files=26, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/ads-designer` — files=7, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/ads-meta` — files=4, private-ref-files=1, duplicate-files=0, labels=telegram-or-chat
- `skills/ads-strategy` — files=8, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/analytics-tracking` — files=4, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, memory-store
- `skills/app-design` — files=8, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/app-store-optimization` — files=5, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/autoresearch-diagrams` — files=87, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file
- `skills/captain-yar` — files=1, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file
- `skills/competitor-alternatives` — files=5, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/content-review` — files=5, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file
- `skills/content-social` — files=18, private-ref-files=5, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/content-strategy` — files=7, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/copy-editing` — files=3, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/copy-writing` — files=14, private-ref-files=7, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/course-launcher` — files=1, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/creative-brief` — files=2, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/cro` — files=12, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/cro-funnel` — files=8, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/curator` — files=1, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/daily-operations` — files=1, private-ref-files=1, duplicate-files=0, labels=memory-store, telegram-or-chat
- `skills/design-page` — files=5, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/directory-submissions` — files=4, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/doc-coauthoring` — files=1, private-ref-files=1, duplicate-files=0, labels=private-local-path
- `skills/docx` — files=61, private-ref-files=1, duplicate-files=1, labels=none-detected-by-label-scan
- `skills/elevenlabs` — files=10, private-ref-files=9, duplicate-files=0, labels=env-or-secret-file
- `skills/email-optimizer` — files=3, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, memory-store
- `skills/email-outreach` — files=12, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/email-sequence` — files=18, private-ref-files=4, duplicate-files=0, labels=env-or-secret-file, memory-store
- `skills/firebase-deploy` — files=2, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file
- `skills/free-tool-strategy` — files=6, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/gamification-design` — files=4, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, memory-store
- `skills/growth-referral` — files=5, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/growth-retention` — files=5, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/high-ticket-closer` — files=10, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/infographic-gen` — files=24, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, memory-store, telegram-or-chat
- `skills/ios-app-monetization` — files=11, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/jogg-ai` — files=12, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file
- `skills/launch-ops` — files=5, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file
- `skills/launch-strategy` — files=8, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/linkedin-profile` — files=4, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/local-content` — files=1, private-ref-files=1, duplicate-files=0, labels=telegram-or-chat
- `skills/market_pulse` — files=20, private-ref-files=3, duplicate-files=3, labels=env-or-secret-file, legacy-agent-ops, memory-store, private-local-path, telegram-or-chat
- `skills/marketing-ads` — files=2, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/marketing-foundations` — files=11, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/marketing-orchestrator` — files=1, private-ref-files=1, duplicate-files=0, labels=telegram-or-chat
- `skills/mcp-setup` — files=3, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, memory-store, private-local-path
- `skills/nb2-image-gen` — files=3, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/newsletter-ad-creator` — files=3, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, private-local-path
- `skills/newsletter-analyst` — files=5, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/newsletter-automator` — files=14, private-ref-files=7, duplicate-files=0, labels=env-or-secret-file, telegram-or-chat
- `skills/newsletter-brainstorm` — files=4, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/newsletter-grower` — files=12, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/newsletter-monetizer` — files=9, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/newsletter-positioner` — files=5, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file
- `skills/newsletter-writer` — files=35, private-ref-files=10, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/notebook-lm` — files=3, private-ref-files=1, duplicate-files=0, labels=none-detected-by-label-scan
- `skills/notebooklm` — files=1, private-ref-files=1, duplicate-files=0, labels=memory-store, private-local-path
- `skills/pdf` — files=12, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file
- `skills/pptx` — files=59, private-ref-files=1, duplicate-files=2, labels=none-detected-by-label-scan
- `skills/presell-validator` — files=10, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/product-context` — files=1, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/product-frontend` — files=20, private-ref-files=2, duplicate-files=0, labels=memory-store
- `skills/product-offer` — files=12, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store, telegram-or-chat
- `skills/production-manager` — files=2, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/prompt-master` — files=6, private-ref-files=3, duplicate-files=0, labels=none-detected-by-label-scan
- `skills/push-notification-strategy` — files=3, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/quiz-funnel` — files=10, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/remotion` — files=69, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store, private-local-path, telegram-or-chat
- `skills/review-miner` — files=3, private-ref-files=2, duplicate-files=0, labels=memory-store
- `skills/sales-page-writer` — files=13, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/seo` — files=3, private-ref-files=2, duplicate-files=0, labels=env-or-secret-file, memory-store
- `skills/seo-content` — files=5, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/skill-creator` — files=21, private-ref-files=1, duplicate-files=1, labels=legacy-agent-ops
- `skills/storyteller` — files=8, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, memory-store
- `skills/tiktok-slideshow` — files=14, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/trading` — files=37, private-ref-files=7, duplicate-files=1, labels=env-or-secret-file, legacy-agent-ops, memory-store, private-local-path, telegram-or-chat
- `skills/tree-brain` — files=1, private-ref-files=1, duplicate-files=0, labels=env-or-secret-file
- `skills/ugc-production` — files=18, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/user-research` — files=4, private-ref-files=1, duplicate-files=0, labels=legacy-agent-ops, memory-store
- `skills/vibe-security` — files=16, private-ref-files=10, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/video-editor` — files=37, private-ref-files=13, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store, telegram-or-chat
- `skills/video-hook` — files=7, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/video-scriptwriter` — files=24, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, memory-store
- `skills/webinar-funnel` — files=5, private-ref-files=3, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops
- `skills/website-brand-analysis` — files=1, private-ref-files=1, duplicate-files=0, labels=telegram-or-chat
- `skills/xlsx` — files=54, private-ref-files=1, duplicate-files=1, labels=none-detected-by-label-scan
- `skills/youtube-clipper` — files=21, private-ref-files=4, duplicate-files=0, labels=env-or-secret-file, legacy-agent-ops, private-local-path
- `skills/youtube-producer` — files=8, private-ref-files=1, duplicate-files=0, labels=memory-store
- `skills/youtube-strategist` — files=8, private-ref-files=1, duplicate-files=0, labels=memory-store

### sanitized-imported
These were sanitized after the hold-review pass and imported into Hermes. Private memory/project references were rewritten to generic private-note/profile-local guidance.

- `skills/coach-core` → `skills/productivity/coach-core`
- `skills/coach-business` → `skills/business/coach-business`

### profile-local-tooling
Operational wrappers/tools. Keep out of the public Hermes repo unless rewritten as generic, credential-free plugins or docs. Good candidates for the private `cyber-corsairs` Hermes profile.

- `tools/REGISTRY.md` — files=1, private-ref-files=1, labels=env-or-secret-file, memory-store, private-local-path, telegram-or-chat
- `tools/clis` — files=54, private-ref-files=53, labels=env-or-secret-file, legacy-agent-ops, private-local-path, telegram-or-chat
- `tools/curator` — files=4, private-ref-files=4, labels=memory-store, private-local-path
- `tools/deploy` — files=1, private-ref-files=1, labels=legacy-agent-ops, memory-store
- `tools/drive-sync` — files=1, private-ref-files=1, labels=legacy-agent-ops, memory-store, private-local-path, telegram-or-chat
- `tools/gmail` — files=4, private-ref-files=3, labels=env-or-secret-file, telegram-or-chat
- `tools/hermes-ref` — files=90, private-ref-files=50, labels=env-or-secret-file, legacy-agent-ops, memory-store, telegram-or-chat
- `tools/hooks` — files=3, private-ref-files=3, labels=memory-store, telegram-or-chat
- `tools/integrations` — files=59, private-ref-files=37, labels=env-or-secret-file
- `tools/memory` — files=7, private-ref-files=5, labels=memory-store
- `tools/obsidian` — files=4, private-ref-files=4, labels=memory-store
- `tools/security` — files=2, private-ref-files=2, labels=env-or-secret-file, legacy-agent-ops, memory-store, private-local-path, telegram-or-chat
- `tools/skill-packager` — files=4, private-ref-files=2, labels=env-or-secret-file
- `tools/subagent` — files=6, private-ref-files=2, labels=memory-store
- `tools/telegram-send` — files=2, private-ref-files=2, labels=telegram-or-chat

### manual-review-superpowers
Superpowers framework artifacts. Hold for manual semantic comparison with Hermes built-in skills before importing or merging.

- `skills/superpowers/brainstorming` — files=8, note=superpowers hold/manual review
- `skills/superpowers/dispatching-parallel-agents` — files=1, note=superpowers hold/manual review
- `skills/superpowers/executing-plans` — files=1, note=superpowers hold/manual review
- `skills/superpowers/finishing-a-development-branch` — files=1, note=superpowers hold/manual review
- `skills/superpowers/hooks` — files=3, note=superpowers hold/manual review
- `skills/superpowers/preflight-gate` — files=1, note=superpowers hold/manual review
- `skills/superpowers/receiving-code-review` — files=1, note=superpowers hold/manual review
- `skills/superpowers/requesting-code-review` — files=2, note=superpowers hold/manual review
- `skills/superpowers/subagent-driven-development` — files=4, note=superpowers hold/manual review
- `skills/superpowers/systematic-debugging` — files=11, note=superpowers hold/manual review
- `skills/superpowers/test-driven-development` — files=2, note=superpowers hold/manual review
- `skills/superpowers/using-git-worktrees` — files=1, note=superpowers hold/manual review
- `skills/superpowers/using-superpowers` — files=3, note=superpowers hold/manual review
- `skills/superpowers/verification-before-completion` — files=1, note=superpowers hold/manual review
- `skills/superpowers/writing-plans` — files=2, note=superpowers hold/manual review
- `skills/superpowers/writing-skills` — files=7, note=superpowers hold/manual review

### do-not-import-attribution
- `skills/_ATTRIBUTION.md` — not a skill; preserve provenance privately if needed.

## Recommended next actions

1. Import `coach-core` and `coach-business` only after sanitizing private references and fixing `coach-personal` cross-links.
2. Pick one domain cluster at a time for sanitized import: ads/marketing, newsletter, product/mobile, video/youtube, or document/media tooling.
3. Move operational tools to a private Hermes profile or rewrite them as generic plugins; do not commit legacy wrappers that reference `.memory`, Task Scheduler, local paths, Telegram, or Google Drive.
4. Compare `skills/superpowers/**` against existing Hermes software-development skills and merge concepts manually instead of copying the framework wholesale.


## Sanitized-imported marketing/growth batch

The following 28 records were sanitized and imported into Hermes after this triage report was first generated: ads/content/copy/CRO/email/growth/launch/marketing/social profile skills. Private memory paths and project-specific examples were generalized before validation.
