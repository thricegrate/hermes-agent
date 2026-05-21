# CLAUDE.md + SOUL.md Extraction & Sanitization Proposal

Date: 2026-05-20
Source: Cyber-Corsairs root files
Status: Sanitized proposal — no raw private content included

## 1. Executive Summary

I reviewed `CLAUDE.md` and `SOUL.md` from the Cyber-Corsairs project.  
Instead of bulk-importing them, I extracted the **reusable, high-value patterns** that could benefit the broader Hermes project while removing all project-specific, private, and personal references.

## 2. Recommended Destinations

| Content Type | Recommended Location | Rationale |
|--------------|----------------------|---------|
| Development workflow (planning, verification, preflight) | `AGENTS.md` (Hermes) | Generalizes well to all Hermes users |
| Self-improvement & bug reporting loops | `AGENTS.md` or new `skills/software-development/self-improvement.md` | Reusable pattern |
| Personal voice, tone, "buddy not butler" identity | Private profile note or Obsidian | Too personal for public repo |
| Coffee Shop Rule + Humanizer gate | `skills/creative/humanizer` or new skill note | Already partially exists in Hermes |
| Accountability guardrails | Private profile note | Very founder-specific |

## 3. Extracted & Sanitized Patterns from CLAUDE.md

### 3.1 Planning Discipline (Strongly Recommended for AGENTS.md)

**Original spirit:** Always plan first for non-trivial tasks.

**Sanitized version for Hermes:**

```markdown
## Planning Discipline

For any non-trivial task (3+ steps, architectural decisions, or multi-file changes):

1. Use a structured planning flow (e.g. brainstorming → writing plans → executing plans)
2. If execution goes off track, stop and re-plan instead of patching
3. Track multi-step work using a task list and update it live
4. Simple fixes (typos, one-liners, config tweaks) can skip formal planning
```

### 3.2 Verification & Preflight Culture

**Sanitized version:**

```markdown
## Verification Culture

Verification is the single highest-leverage practice.

- Always verify outputs (tests, screenshots, manual review)
- If you cannot verify something, do not ship it
- Ask: "Would a staff engineer approve this?"
- For non-trivial changes, pause and ask: "Is there a more elegant way?"
```

### 3.3 Self-Improvement Loop

**Sanitized version:**

```markdown
## Self-Improvement

After any correction or feedback from the user:
- Capture the pattern and prevention rule
- Review captured patterns at the start of relevant sessions
- Update skill documentation when better approaches are discovered
```

### 3.4 Bug Reporting Protocol

**Sanitized version:**

```markdown
## Bug Reporting

When given a bug:
- Fix it first, then explain
- Read logs, trace root cause, identify the gap
- Report what was found and what was fixed
- Only ask clarifying questions if the root cause genuinely cannot be determined
```

## 4. Extracted & Sanitized Patterns from SOUL.md

### 4.1 Communication Style (Private / Profile Note Recommended)

This section is highly personal. Recommended destination: private profile note or Obsidian.

Key reusable ideas:
- "Buddy, not butler" tone
- Direct, low-filler communication
- "Coffee Shop Rule" — every output should sound like talking to a friend across a table
- Strong preference for brevity and concrete numbers over vague language

### 4.2 Accountability Guardrail

Very founder-specific. Best kept private.

## 5. Proposed Next Steps

1. Merge the sanitized sections from section 3 into `AGENTS.md` (with attribution note)
2. Create a private profile note containing the voice/tone/identity patterns from SOUL.md
3. Optionally create a lightweight "Self-Improvement" skill or section in software-development

Would you like me to:
A) Write the sanitized patches for `AGENTS.md` now?
B) Create the private profile note for the SOUL.md patterns?
C) Both?


## 6. Actions Taken (2026-05-20)

### Public Contributions
- Added sanitized "Development Workflow & Quality Practices" section to `AGENTS.md`
  - Includes: Planning Discipline, Verification Culture, Self-Improvement Loop, Bug Reporting Protocol

### Private Profile Note
- Created: `C:/Users/thric/AppData/Local/hermes/profiles/cyber-corsairs/notes/soul-voice-identity.md`
  - Contains: Core Identity, Communication Principles, Coffee Shop Rule, Voice & Tone, Accountability Guardrail, Boundaries

Both extractions are now complete and separated by visibility.
