# Sub-Agent Pattern for Heavy Tasks

**Origin:** Extracted from Cyber-Corsairs `tools/subagent`
**Date:** 2026-05-20
**Status:** Documentation only (original code kept private)

## The Problem

Long-running or context-heavy tasks (email classification, research, memory consolidation, coaching prep) can bloat the main conversation context and slow down the primary agent.

## The Pattern

Spawn an **isolated sub-agent** for focused tasks:

1. Main agent identifies a heavy or specialized task.
2. Spawns a fresh sub-agent with a narrow system prompt and minimal context.
3. Sub-agent completes the task and returns a concise result.
4. Main agent receives the result without carrying the full sub-task history.

## Benefits

- Keeps the main context window lean
- Allows parallel execution of independent tasks
- Reduces cost and token usage on the primary thread
- Improves reliability (sub-agent failures don't corrupt main state)

## Recommended Hermes Approach

Hermes already supports this pattern through:

- `delegate_task` with `role: "leaf"`
- Task-specific toolsets
- Bounded `max_iterations` and `iteration_budget`

For very heavy work, consider:
- Using `enabled_toolsets` to restrict the sub-agent to only necessary tools
- Passing minimal context via `context` parameter
- Setting reasonable cost/turn limits when available

## When to Use

- Email classification or triage
- Deep research or data analysis
- Memory consolidation / summarization
- Coaching session preparation
- Any task that would require many tool calls or large context

## When Not to Use

- Simple, quick questions
- Tasks that require tight coupling with the main conversation state
- One-off calculations that are faster to do directly

---

**Note:** The original implementation was built for Claude Code. The pattern itself is portable to any agent system that supports isolated sessions or delegation.
