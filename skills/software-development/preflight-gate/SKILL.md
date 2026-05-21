---
name: preflight-gate
description: Use before any commit to determine required checks based on risk tiers, dispatch them, enforce SHA-tied evidence, and block commit until all checks pass
---

# Preflight Gate

The automated quality gate. Reads the risk contract, figures out what checks your changes need, dispatches them, and blocks the commit until everything passes for the current HEAD SHA.

**Core principle:** No commit without passing evidence for the current SHA.

## When to Use

Before ANY commit. This is not optional. The gate determines what's required so you don't have to guess.

**Skip only when:**
- Zero code changes (e.g., updating `private project notes/` operational state)
- User explicitly says "force" or "ship it" (log as OVERRIDE, see Escape Hatch below)

## The Process

```dot
digraph preflight {
    rankdir=TB;

    "Get changed files (git diff --name-only)" [shape=box];
    "Read rules/risk-contract.json" [shape=box];
    "Match files to tiers, take highest" [shape=box];
    "Determine required checks for tier" [shape=box];
    "Check existing evidence for current HEAD SHA" [shape=diamond];
    "All checks have valid evidence?" [shape=diamond];
    "Dispatch missing checks in parallel" [shape=box];
    "Fix any issues found" [shape=box];
    "Re-run gate (loop back)" [shape=box];
    "Log evidence to private project notes [shape=box];
    "GATE PASS - commit allowed" [shape=box style=filled fillcolor=lightgreen];
    "GATE BLOCKED - list missing checks" [shape=box style=filled fillcolor=lightcoral];

    "Get changed files (git diff --name-only)" -> "Read rules/risk-contract.json";
    "Read rules/risk-contract.json" -> "Match files to tiers, take highest";
    "Match files to tiers, take highest" -> "Determine required checks for tier";
    "Determine required checks for tier" -> "Check existing evidence for current HEAD SHA";
    "Check existing evidence for current HEAD SHA" -> "All checks have valid evidence?";
    "All checks have valid evidence?" -> "Log evidence to private project notes [label="yes"];
    "Log evidence to private project notes -> "GATE PASS - commit allowed";
    "All checks have valid evidence?" -> "Dispatch missing checks in parallel" [label="no"];
    "Dispatch missing checks in parallel" -> "Fix any issues found" [label="issues found"];
    "Dispatch missing checks in parallel" -> "Log evidence to private project notes [label="all pass"];
    "Fix any issues found" -> "Re-run gate (loop back)";
    "Re-run gate (loop back)" -> "Check existing evidence for current HEAD SHA";
}
```

## Step by Step

### 1. Identify Changed Files

```bash
# For staged changes (pre-commit)
git diff --name-only --cached

# For all changes since base (feature work)
git diff --name-only HEAD~N  # or origin/main
```

### 2. Read the Risk Contract

Read `rules/risk-contract.json`. Match each changed file against tier path patterns.

**Matching rules:**
- `path_match: "highest-tier-wins"` -- if ANY changed file hits a higher tier, that tier applies to the whole commit
- Glob patterns: `**` matches directories, `*` matches filenames
- `default_tier: "MEDIUM"` -- anything not matching an explicit pattern

**Tier priority:** CRITICAL > HIGH > MEDIUM > LOW

### 3. Determine Required Checks

Look up `required_checks` for the detected tier in the contract. Each check maps to:
- `code-review` -> dispatch code-reviewer subagent
- `qa-tests` -> dispatch qa subagent
- `safety-audit` -> dispatch safety-audit agent
- `content-review` -> run content-review skill
- `human-approval` -> ask user for explicit approval

### 4. Check Existing Evidence

Before dispatching checks, see if valid evidence already exists for this session:
- Evidence must be for the **current HEAD SHA**
- If code changed after a check ran (SHA mismatch), that evidence is **STALE**
- Stale evidence does not count. Re-run required.

**Smart invalidation:** Only invalidate when changed files overlap with reviewed files. A README typo after a code review of `agents/autoresearch/` does NOT invalidate that review.

### 5. Dispatch Missing Checks

Use `run_in_background: true` for parallel dispatch where possible:
- code-review + qa-tests can run in parallel
- safety-audit can run in parallel with the above
- human-approval waits for the user (sequential)
- content-review runs independently

### 6. Handle Results

**All checks pass:** Log evidence, proceed to commit.

**Issues found:** Fix them. Then re-run the gate (loop back to step 1). The fix may have changed the SHA, which means fresh evidence is needed.

**Remediation loop cap:** If the same issue appears 3 times across remediation loops, stop and escalate to the user. Something deeper is wrong.

### 7. Log Evidence

Write evidence to private project notes.json`:

```json
{
  "session": "2026-03-15-feature-name",
  "head_sha": "abc123",
  "tier": "MEDIUM",
  "changed_files": ["agents/autoresearch/loops/trend_scanner.py"],
  "checks": {
    "code-review": {
      "status": "PASS",
      "sha": "abc123",
      "timestamp": "2026-03-15T14:30:00-05:00",
      "verdict": "PASS WITH NOTES",
      "findings": {"critical": 0, "important": 0, "minor": 2}
    },
    "qa-tests": {
      "status": "PASS",
      "sha": "abc123",
      "timestamp": "2026-03-15T14:35:00-05:00",
      "tests_run": 12,
      "tests_passed": 12
    }
  },
  "gate_result": "PASS",
  "committed_sha": "def456"
}
```

## SHA Discipline

This is the single most important enforcement mechanism. Without it, you can merge using stale "clean" evidence.

**Rules:**
1. Every check result is tagged with the HEAD SHA at the time it ran
2. Evidence is valid ONLY when its SHA matches the current HEAD
3. After ANY code change (fix, rebase, amend), re-check whether evidence is still valid
4. Smart invalidation: only re-run checks whose reviewed files overlap with the new changes

**Example:**
```
HEAD: abc123
  code-review ran at abc123 -> VALID
  qa-tests ran at abc123 -> VALID

Developer fixes a typo in README.md
HEAD: def456
  code-review ran at abc123 (reviewed agents/autoresearch/) -> STILL VALID (no overlap)
  qa-tests ran at abc123 -> STALE (tests should cover new state)
```

## Escape Hatch

When the user explicitly says "force", "ship it", or "override":
- Log the override in evidence: `"gate_result": "OVERRIDE_BY_USER"`
- Record which checks were skipped and why
- Proceed with the commit
- The override is permanent audit trail for the harness-gap tracker

**Never** auto-override. Never silently skip checks. The escape hatch is user-initiated only.

## Tier Quick Reference

| Tier | When | Checks Required |
|------|------|----------------|
| CRITICAL | Safety system changes | code-review + qa + safety-audit + human |
| HIGH | Publishing, money, shell exec | code-review + qa + human |
| MEDIUM | Agent logic, rules, superpowers | code-review + qa |
| LOW | Docs, skill text, templates | content-review |

## Integration

**Required by:**
- `superpowers:subagent-driven-development` -- runs gate before marking task complete
- `superpowers:finishing-a-development-branch` -- runs gate before merge
- `superpowers:verification-before-completion` -- references gate as concrete verification

**Dispatches:**
- `code-reviewer` subagent (agents/code-reviewer.md)
- `qa` subagent (agents/qa.md)
- `safety-audit` agent (agents/safety-audit/)
- `content-review` skill (skills/content-review/)

**Reads:**
- `rules/risk-contract.json` (the machine-readable contract)

**Writes:**
- private project notes.json` (evidence logs)

## Red Flags

| Thought | Reality |
|---------|---------|
| "It's just a small change" | Small changes break things. The gate handles this -- LOW tier is fast. |
| "I already reviewed it mentally" | Mental review is not evidence. Run the gate. |
| "The checks are slowing me down" | Bugs found later slow you down more. |
| "I'll run it after the commit" | Post-commit evidence proves nothing about pre-commit state. |
| "Same code, different SHA" | Different SHA = different state. Evidence must match. |

## Common Patterns

**Quick documentation change:**
```
Changed: skills/newsletter-writer/SKILL.md
Tier: LOW
Required: content-review only
Time: ~1 minute
```

**Agent logic change:**
```
Changed: agents/autoresearch/loops/trend_scanner.py
Tier: MEDIUM
Required: code-review + qa-tests
Time: ~5 minutes (parallel dispatch)
```

**Publishing agent change:**
```
Changed: agents/cybercorsairs-newsletter/newsletter.py
Tier: HIGH
Required: code-review + qa-tests + human-approval
Time: ~5 minutes + user confirmation
```

**Safety system change:**
```
Changed: rules/risk-contract.json
Tier: CRITICAL
Required: code-review + qa-tests + safety-audit + human-approval
Time: ~10 minutes + user confirmation
```
