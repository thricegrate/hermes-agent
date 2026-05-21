# Cyber-Corsairs Integration Plan — Sanitized Public Stub

The full path-specific/private migration plan was moved to the Cyber-Corsairs Hermes profile-local migration archive.

Public-safe summary:

- Keep memory, credentials, runtime databases, logs, and bot state out of public Hermes Git.
- Import only sanitized reusable skills/tools into the Hermes repo.
- Keep private operational wrappers and gateway/runtime configuration profile-local.
- Use Obsidian/private notes for memory corpus migration; do not copy raw memory into the public repo.
- Validate every imported batch with frontmatter checks, internal-link checks, and secret/private-reference scans.

See the sanitized import log for durable public-safe status:
`docs/plans/2026-05-20-cyber-corsairs-import-log.md`
