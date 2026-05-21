# Popular MCP Services

Verified configs for commonly used MCP servers. Each entry has the install command and the `claude mcp add` command ready to copy.

## Project MCPs (already in .claude/mcp.example.json)

### Playwright (Browser Automation)

Does: Navigate pages, click elements, fill forms, take screenshots, save PDFs. Uses accessibility tree for reliable element targeting.

```bash
claude mcp add playwright -- npx -y @anthropic-ai/playwright-mcp@latest --autoConnect
```

Requires Chrome with remote debugging enabled. This project uses port 8053 (not the default 9222). Enable at `chrome://inspect/#remote-debugging`.

After enabling remote debugging, restart Claude Code for the MCP server to connect.

### Chrome DevTools (Inspection/Debugging)

Does: DOM inspection, console access, network monitoring, performance profiling. Read-only, cannot navigate or interact.

```bash
claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest
```

Also uses port 8053 in this project.

### ElevenLabs (Voice/Audio)

Does: Text-to-speech, speech-to-text, voice cloning, sound effects, audio isolation.

```bash
claude mcp add ElevenLabs --env ELEVENLABS_API_KEY=your-key-here --env ELEVENLABS_MCP_BASE_PATH=.tmp --env ELEVENLABS_MCP_OUTPUT_MODE=both -- elevenlabs-mcp
```

Needs `pip install elevenlabs-mcp`. API key from elevenlabs.io dashboard.

On Windows, use the full exe path if `elevenlabs-mcp` isn't on PATH:

```bash
claude mcp add ElevenLabs --env ELEVENLABS_API_KEY=your-key -- C:/Users/you/AppData/Roaming/Python/Python313/Scripts/elevenlabs-mcp.exe
```

### NotebookLM (Knowledge Base)

Does: Create/query Google NotebookLM notebooks, add sources, generate audio overviews, reports, flashcards.

```bash
pip install notebooklm-mcp
notebooklm-mcp init <notebook-url>
claude mcp add notebooklm -- notebooklm-mcp server --transport stdio --headless
```

Auth is Chrome profile-based. The `init` command creates a Chrome profile and authenticates. If you have multiple Google accounts, sign out of others first.

On Windows, use the full path:

```bash
claude mcp add notebooklm -- C:/Users/you/AppData/Roaming/Python/Python313/Scripts/notebooklm-mcp.exe server --transport stdio --headless
```

### Excalidraw (Diagrams)

Does: Generate and edit Excalidraw diagrams programmatically.

```bash
claude mcp add excalidraw -- node /path/to/excalidraw-mcp/dist/index.js --stdio
```

Replace `/path/to/` with the actual install location.

## Common External MCPs

### GitHub

Does: List repos, PRs, issues, create branches, read files from repos.

```bash
claude mcp add github -- npx -y @anthropic-ai/mcp-github
```

Needs a GitHub personal access token. Set via env:

```bash
claude mcp add github --env GITHUB_TOKEN=ghp_your-token-here -- npx -y @anthropic-ai/mcp-github
```

### Filesystem

Does: Read/write files, list directories, search files. Useful for giving Claude access to directories outside the project.

```bash
claude mcp add filesystem -- npx -y @anthropic-ai/mcp-filesystem /path/to/allowed/directory
```

The path argument restricts access to that directory and its children.

### Slack

Does: Read channels, post messages, search messages, manage threads.

Cloud-hosted with OAuth:

```bash
claude mcp add-oauth slack
```

### Sentry

Does: Search issues, get error details, view stack traces, manage alerts.

```bash
claude mcp add-oauth sentry
```

### Linear

Does: Create/update issues, search projects, manage sprints.

```bash
claude mcp add-oauth linear
```

### Postgres (Database)

Does: Query tables, inspect schema, run SQL.

```bash
claude mcp add postgres -- npx -y @anthropic-ai/mcp-postgres "postgresql://user:pass@localhost:5432/dbname"  # pragma: allowlist secret
```

### SQLite

Does: Query SQLite databases.

```bash
claude mcp add sqlite -- npx -y @anthropic-ai/mcp-sqlite /path/to/database.db
```

## Tips

- For npm-based MCPs on Windows, if `npx` fails, try `npx.cmd` or install globally and use the full path
- Always restart Claude Code after adding a new MCP
- Use `--scope user` for tools you want across all projects (like GitHub)
- Use `--scope project` for team-shared tools (adds to `.mcp.json` in repo root)
- Check `claude mcp list` after restart to confirm the server loaded
