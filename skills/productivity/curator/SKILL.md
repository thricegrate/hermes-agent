---
name: curator
description: |
  Track skill usage in a sidecar (private project notes/skills/.usage.json), classify
  skills as active/stale/archived, and surface what's actually being used
  vs collecting dust. Use when running a skill audit, deciding which
  skills to prune, designing a curator/self-improvement loop, or after
  importing skills from another repo.
---

# Curator: Skill Usage Telemetry

Phase 1 of the Curator pattern from Hermes (`skills/hermes/tools-converted/curator-skill-management/`). This is the telemetry foundation. Provenance ContextVar, manifest sync, hub adapters, and security scanner are deferred to later phases.

## When to use

- After importing skills from another repo (run `init_usage.py` to track them).
- Quarterly audit: "which of our skills are actually being used?" Run `classify_skills.py`.
- Designing a skill self-improvement loop — read this first to understand the data shape.
- Deciding what to merge / prune after collisions (e.g., the 13 `-hermes` collisions from the Hermes import).

## Data model

`private project notes/skills/.usage.json`:

```json
{
  "version": 1,
  "config": {"stale_after_days": 90, "archive_after_days": 180},
  "skills": {
    "<skill-id>": {
      "use_count": 0,
      "view_count": 0,
      "patch_count": 0,
      "last_used_at": null,
      "last_viewed_at": null,
      "last_patched_at": null,
      "created_at": "2026-05-05T17:39:13+00:00",
      "pinned": false,
      "state": "active",
      "agent_created": false
    }
  }
}
```

`<skill-id>` is the path under `skills/` with forward slashes — e.g. `humanizer`, `hermes/core/github/github-pr-workflow`.

**Why a sidecar, not frontmatter?** Per the Hermes pattern: keep `SKILL.md` authorial (content + intent), keep operational data mutable + atomic. Avoids merge conflicts on bundled skills. Atomic writes via `tempfile + os.replace`.

## Commands

All scripts live in `tools/curator/scripts/`. Run with system Python (`/c/Python313/python.exe` on Windows or `python3` elsewhere).

### Bootstrap or refresh the sidecar

```bash
python tools/curator/scripts/init_usage.py            # add missing entries
python tools/curator/scripts/init_usage.py --prune    # also drop entries for deleted skills
```

Idempotent. Counters never reset.

### Bump counters manually

```bash
python tools/curator/scripts/log_skill_use.py --skill humanizer --event use
python tools/curator/scripts/log_skill_use.py --skill humanizer --event view
python tools/curator/scripts/log_skill_use.py --skill humanizer --event patch
```

### Bump counters from a Claude Code hook

```bash
echo '{"tool_name":"Skill","tool_input":{"skill":"humanizer"}}' | \
  python tools/curator/scripts/log_skill_use.py --hook-stdin
```

The script extracts skill + event from `Skill` (use), `Read` of `skills/*/SKILL.md` (view), and `Edit`/`Write` of files under `skills/*/` (patch). Unknown tools are no-ops.

To wire it into Claude Code: add a PostToolUse hook in `.claude/settings.json` that pipes the hook payload into `log_skill_use.py --hook-stdin`. See `tools/curator/_README.md` for the JSON snippet.

### Classify skills

```bash
python tools/curator/scripts/classify_skills.py            # dry run
python tools/curator/scripts/classify_skills.py --apply    # write states back
```

Logic:
- `active` — recent activity within `stale_after_days` (default 90).
- `stale` — no activity for `stale_after_days` to `archive_after_days`.
- `archived` — no activity for more than `archive_after_days` (default 180).

**Pin protection:** `pinned: true` skills can transition active <-> stale, but never reach `archived`. Pin protects against loss, not natural lifecycle staleness.

## Workflow

1. Once: run `init_usage.py` to seed the sidecar from current `skills/`.
2. Continuous: PostToolUse hook bumps counters automatically (or run manually during audits).
3. Periodic (weekly/monthly/quarterly): `classify_skills.py` (dry run first), inspect transitions, then `--apply`.
4. Audit output answers: which skills should we keep, merge, archive, or rewrite to our voice?

## How to apply to the 13 hermes collisions

After 30+ days of telemetry, run `classify_skills.py`. For each pair `<name>` vs `<name>-hermes`:
- Both active and used regularly? Merge content.
- Ours unused, theirs active? Replace ours with theirs (after voice rewrite).
- Theirs unused (stale/archived), ours active? Delete `<name>-hermes`.
- Both stale? Probably archive both.

## Roadmap (deferred to Phase 2+)

- **Provenance** — ContextVar (or env var) marking writes as `foreground` vs `background_review`. Foreground writes belong to the user; only background-review writes are eligible for auto-curation.
- **Manifest sync** — Track `name:hash` for bundled/imported skills. Update only unmodified user copies. Never re-add deleted skills.
- **Hub adapters** — Pluggable sources (GitHub, marketplaces, optional-skills). We did this manually for hermes; formalize the pattern.
- **Security scanner** — Trust-tiered (builtin / trusted / community / agent-created) regex scan for exfiltration, injection, destructive, persistence, network, obfuscation patterns.
- **Auto-archive** — When confidence is high (months of telemetry), have the curator move archived skills to `.archive/` and clean SKILLS.md.

## Source

Distilled from `skills/hermes/tools-converted/curator-skill-management/SKILL.md` which itself wraps 7 upstream Python modules. See `tools/hermes-ref/{skills_hub.py, skill_manager_tool.py, skill_provenance.py, skills_sync.py, skills_tool.py, skill_usage.py, skills_guard.py}` for full upstream implementation.
