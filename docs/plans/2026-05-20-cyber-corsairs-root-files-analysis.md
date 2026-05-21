# Cyber-Corsairs Root Files Analysis

Sanitized analysis of root-level files. This report does not quote file bodies; it records filenames, sensitivity classification, heading inventory, and migration recommendations.

## Root file inventory

- `.env` — tracked=False, size=3767, class=sensitive/hold
- `.env.example` — tracked=True, size=1465, class=safe-catalog-candidate
- `.env.local.example` — tracked=True, size=285, class=safe-catalog-candidate
- `.env.team` — tracked=False, size=1404, class=sensitive/hold
- `.excalidraw` — tracked=True, size=294, class=review
- `.gitignore` — tracked=True, size=1241, class=review
- `.pre-commit-config.yaml` — tracked=True, size=473, class=safe-catalog-candidate
- `.secrets.baseline` — tracked=True, size=26541, class=sensitive/hold
- `BOTLAUNCH.md` — tracked=True, size=2806, class=safe-catalog-candidate
- `CLAUDE.md` — tracked=True, size=15105, class=safe-catalog-candidate
- `MEMORY.md` — tracked=True, size=5571, class=sensitive/hold
- `ONBOARDING.md` — tracked=True, size=3913, class=safe-catalog-candidate
- `README.md` — tracked=True, size=87178, class=safe-catalog-candidate
- `SKILLS.md` — tracked=True, size=85860, class=safe-catalog-candidate
- `SOUL.md` — tracked=True, size=5357, class=safe-catalog-candidate
- `TOOLS.md` — tracked=True, size=15928, class=safe-catalog-candidate

## Markdown/root docs reviewed

### `.env.example`
- Size: 1465 bytes
- Sensitivity signals: 6 label matches
- Headings:
  - Project - Shared Environment Variables
  - Copy to .env and fill in your API keys
  - USER TIMEZONE -- set your own, never committed to git
  - Examples: America/New_York, America/Chicago, America/Los_Angeles, Europe/Kyiv, Europe/London, UTC
  - GEMINI API (image gen + video analysis)
  - OPENAI API
  - META MARKETING API (ad publishing)
  - HIGGSFIELD API (video generation)
  - AssemblyAI (transcription)
  - ElevenLabs (TTS, voice)
  - Jogg AI (AI video ads)
  - GOOGLE SHEETS (AIBOS agents: content-pipeline, kpi-dashboard)
- Recommendation: profile-env-reference-only; do not import values; use key names to check private profile env completeness

### `.env.local.example`
- Size: 285 bytes
- Sensitivity signals: 6 label matches
- Headings:
  - Personal Environment Variables
  - Copy to .env.local and fill in YOUR keys
  - This file is never committed to git
  - Telegram Bot (create via @BotFather)
  - Gmail Integration (requires GCP project)
- Recommendation: profile-env-reference-only; do not import values; use key names to check private profile env completeness

### `.excalidraw`
- Size: 294 bytes
- Sensitivity signals: 0 label matches
- Headings: none
- Recommendation: editor/tool preference only; no import needed

### `.gitignore`
- Size: 1241 bytes
- Sensitivity signals: 4 label matches
- Headings:
  - Secrets
  - Working files
  - Large source files (reference material, kept local only)
  - IDE
  - Claude (user-specific, with exceptions)
  - Telegram bot (personal data)
  - Firebase
  - Node
  - design.md CLI build artifacts (source cloned and built locally; spec docs vendored separately in reference/design-md/)
  - Python
  - SQLite databases
  - Logs
- Recommendation: use as privacy boundary reference; compare with Hermes/profile ignores

### `.pre-commit-config.yaml`
- Size: 473 bytes
- Sensitivity signals: 2 label matches
- Headings:
  - Pre-commit hooks for secret scanning.
  - Install: pip install pre-commit && pre-commit install
  - Run manually: pre-commit run --all-files
- Recommendation: optional dev hygiene reference; no direct Hermes import needed

### `BOTLAUNCH.md`
- Size: 2806 bytes
- Sensitivity signals: 4 label matches
- Headings:
  - Telegram Bot Launch
  - Pre-flight Check
  - Quick Launch (single command)
  - First-Time Setup (only if .venv is missing or broken)
  - Remove broken venv if it exists
  - Create fresh venv from system Python
  - Install the bot and all dependencies
  - Verify
  - Config
  - Checking Status
  - Stopping
  - Troubleshooting
- Recommendation: use as private migration/runbook reference; import sanitized generic parts only

### `CLAUDE.md`
- Size: 15105 bytes
- Sensitivity signals: 5 label matches
- Headings:
  - Agent Instructions
  - Communication Style
  - Prerequisites
  - NORTH STAR PRIORITY
  - Architecture
  - Workflow
  - Planning
  - Verification
  - Self-Improvement
  - Bug Reports
  - gstack (Global Skills)
  - Markets / Investing / Trading
- Recommendation: extract reusable agent operating conventions only after sanitization; compare with Hermes AGENTS.md before merging

### `MEMORY.md`
- Size: 5571 bytes
- Sensitivity signals: 2 label matches
- Headings:
  - Project Memory
  - Hermes Import & Curator Telemetry (2026-05-05)
  - Marketing Skill Imports (2026-05-15)
  - Reddit Agent — Title Diversity (2026-02-25)
  - Daily Summary Agent
  - YouTube Agent — RapidAPI Transcript Failures (2026-02-25)
- Recommendation: treat as private memory policy/context; do not import into public repo; optionally convert to private profile note

### `ONBOARDING.md`
- Size: 3913 bytes
- Sensitivity signals: 6 label matches
- Headings:
  - Onboarding Guide
  - Prerequisites
  - Clone & Setup
  - 1. Shared API Keys
  - Edit .env and fill in your API keys
  - 2. MCP Servers (Optional)
  - Edit mcp.json with your local paths and API keys
  - 3. Node Dependencies
  - For infographic-gen skill
  - 4. Google Workspace CLI
  - Personal Setup (Optional)
  - 1. Personal Keys
- Recommendation: use as private migration/runbook reference; import sanitized generic parts only

### `README.md`
- Size: 87178 bytes
- Sensitivity signals: 7 label matches
- Headings:
  - AIBOS v7.6
  - Overview
  - Architecture
  - Project Structure
  - Prerequisites
  - Quick Start
  - Pipelines
  - 1. Marketing Pipeline
  - 2. Product Pipeline
  - 3. Newsletter Pipeline (8 skills)
  - 4. GTM/Sales Pipeline (7 skills)
  - Superpowers (15 development workflow skills)
- Recommendation: extract architecture/agent inventory into private profile migration notes; do not bulk-import whole README

### `SKILLS.md`
- Size: 85860 bytes
- Sensitivity signals: 5 label matches
- Headings:
  - Skills Catalog
  - Skill Anatomy
  - YAML Frontmatter (required)
  - Progressive Disclosure
  - Two Types of Skills
  - Skill Writing Principles
  - Markers
  - Pipelines
  - Marketing Pipeline
  - Product Pipeline
  - Newsletter Pipeline
  - YouTube Production Pipeline
- Recommendation: use as skill catalog cross-check against imported skills and hold-review clusters

### `SOUL.md`
- Size: 5357 bytes
- Sensitivity signals: 1 label matches
- Headings:
  - SOUL.md
  - Core Identity
  - Core Rules (top-loaded, never truncated)
  - Operating Style
  - Voice & Tone
  - The Coffee Shop Rule (MANDATORY, ALL OUTPUT)
  - Boundaries
  - Examples (copy this exact energy)
  - Anti-Patterns (never do these)
  - Language
  - Formatting
  - Continuity & Evolution
- Recommendation: treat as persona/voice source; import only profile-local if desired

### `TOOLS.md`
- Size: 15928 bytes
- Sensitivity signals: 7 label matches
- Headings:
  - TOOLS.md - API & Platform Setup Guide
  - Quick Start
  - Tools Directory
  - Structure
  - CLI Tools (52)
  - PDF Generator (Python)
  - Integration Guides (58)
  - MCP-Enabled Tools (8)
  - design.md CLI (Globally Linked)
  - Categories
  - Gemini API
  - Get Your API Key
- Recommendation: use as operational tool catalog for private-profile plugin backlog

## Pull-in decisions

- Pull into public Hermes repo now: none from root files. Root docs are mostly project-specific runbooks/catalogs and need sanitization or profile-local placement.
- Pull into private Cyber-Corsairs Hermes profile later: `MEMORY.md`, `SOUL.md`, selected `CLAUDE.md` conventions, `BOTLAUNCH.md`, `ONBOARDING.md`, and operational tool notes from `TOOLS.md`.
- Use for validation/cross-check: `.gitignore`, `.env.example`, `.env.local.example`, `SKILLS.md`, `TOOLS.md`.
- Never import: `.env`, `.env.team`, `.secrets.baseline` contents.
