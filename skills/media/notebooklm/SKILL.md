---
name: notebooklm
description: |
  Integrates Google NotebookLM as a knowledge base and research tool via MCP server.
  Use when user wants to create notebooks, add sources, query notebooks, generate
  studio content (audio, reports, flashcards, quizzes), or use NotebookLM as
  persistent project memory. Triggers: "notebooklm", "notebook", "knowledge base",
  "research notebook", "add to my notebook", "query my sources".
metadata:
  version: 1.0.0
---

# NotebookLM MCP Integration

Query, create, and manage Google NotebookLM notebooks directly from Claude Code. Use notebooks as persistent knowledge bases that survive across sessions.

## Prerequisites

- Python 3.11+
- Google account with NotebookLM access
- Chrome browser (for cookie-based authentication)
- `notebooklm-mcp-server` package installed

## Setup

### 1. Install the MCP server

```bash
pip install notebooklm-mcp-server
```

### 2. Add to Claude Code

```bash
claude mcp add notebooklm -- notebooklm-mcp-server
```

If the executable isn't on PATH, use the full path:

```bash
claude mcp add notebooklm -- /path/to/notebooklm-mcp.exe
```

### 3. Authenticate

```bash
notebooklm-mcp-auth
```

This opens Chrome for Google login. Sign into the account that has NotebookLM access. Cookies are cached at `~/.notebooklm-mcp/auth.json`.

If you have multiple Google accounts, sign out of others first to avoid conflicts.

### 4. Restart Claude Code

The MCP server loads on startup. Restart after adding it.

## Capabilities

### Notebook Management
- `notebook_list`: list all notebooks
- `notebook_create`: create a new notebook
- `notebook_delete`: delete a notebook
- `notebook_rename`: rename a notebook
- `notebook_get`: get notebook details

### Source Management
- `source_add_url`: add a web page or YouTube video as a source
- `source_add_text`: add raw text as a source
- `source_add_drive`: add a Google Drive document
- `source_list`: list all sources in a notebook
- `source_describe`: get source description
- `source_sync_drive`: sync Drive sources
- `source_delete`: remove a source

### Querying
- `notebook_query`: ask questions against your sources (AI-powered)
- `chat_settings`: configure chat behavior

### Research
- `research_start`: start a web or Drive research task
- `research_status`: check research progress
- `research_import`: import discovered sources

### Studio Content Generation
- Audio overviews, video overviews, infographics
- Slide decks, reports, flashcards, quizzes
- Data tables, mind maps
- `studio_status`: check generation progress
- `studio_delete`: remove generated content

## Usage Patterns

### As Project Memory
1. Create a notebook per project
2. Add key documents as sources (architecture docs, strategy docs, meeting notes)
3. Query during work sessions for context that would otherwise be lost to conversation compression

### As Research Hub
1. Create a notebook for a research topic
2. Add URLs, papers, articles as sources
3. Query across all sources to synthesize findings

### As Content Pipeline
1. Load reference material into a notebook
2. Generate studio content (reports, flashcards, slide decks)
3. Use outputs as inputs for other skills

## Limitations

- Free tier: ~50 queries/day
- Uses unofficial APIs via browser cookies (not an official Google integration)
- Auth cookies may expire: re-run `notebooklm-mcp-auth` to refresh
- Windows support is unofficial but functional

## Integration

- **Feeds into:** Any skill that needs persistent knowledge or reference material
- **Complements:** `.claude/memory/`: memory for quick facts, NotebookLM for large documents
- **Works with:** `research` subagent for deep investigation tasks
