---
name: mcp-setup
description: |
  Connects Claude Code to external tools and services via MCP (Model Context Protocol).
  Handles setup, configuration, authentication, scope management, and troubleshooting.
  Use this skill whenever the user wants to add a new MCP server, fix a broken MCP
  connection, check what MCPs are installed, manage MCP scopes, or integrate any
  external tool with Claude Code. Also use when user mentions "mcp", "mcp not working",
  "connect a tool", "add integration", "mcp auth", "mcp broken", "tools not showing",
  "configure mcp", "install mcp server", "external service", or asks how to give
  Claude access to something like GitHub, Notion, Slack, databases, or any API.
metadata:
  version: 1.0.0
  tags: mcp, setup, integration, tools, configuration, troubleshooting
---

# MCP Setup

MCP (Model Context Protocol) lets Claude Code talk to external tools. GitHub, databases, Notion, voice APIs, whatever. You add a server, Claude gets new tools.

Two flavors:

- **Cloud-hosted (OAuth):** Lives on someone else's infrastructure. You authenticate via browser. Examples: GitHub, Slack, Google services.
- **Local (stdio):** Runs as a process on your machine. Usually an npm or pip package. Examples: Playwright, ElevenLabs, filesystem tools.

Most of the time you're dealing with local ones.

## Before You Touch Anything

Check what's already installed first. No point adding something twice.

```bash
claude mcp list
```

Also check the project's example config for pre-configured servers:

```bash
cat .claude/mcp.example.json
```

If the MCP the user wants is already there, just verify it's working. If it shows in the list but tools aren't appearing, jump to the troubleshooting section.

## Setup Workflow

### Step 1: Figure out the type

Ask yourself: is this a cloud service with OAuth login, or a local tool that runs on the machine?

- Cloud service (GitHub, Slack, Google stuff) -> `claude mcp add-oauth`
- Local tool (npm/pip package, custom binary) -> `claude mcp add`

If you're not sure, check `references/popular-services.md` for common configs.

### Step 2: Get the install info

For local tools, you need the package name or binary path. Look for the service's MCP documentation. You want:

- The npm package name (like `@anthropic-ai/playwright-mcp@latest`)
- Or the pip package name (like `notebooklm-mcp`)
- Or the binary path if it's already installed
- Any required environment variables (API keys)

For cloud services, you need the OAuth URL or service identifier.

### Step 3: Add it

**Cloud service (OAuth):**

```bash
claude mcp add-oauth <name>
```

Some cloud services need a specific URL:

```bash
claude mcp add --transport http <name> <url>
```

With an auth header:

```bash
claude mcp add --transport http <name> <url> --header "Authorization: Bearer <token>"
```

**Local tool (npm package):**

```bash
claude mcp add <name> -- npx -y <package-name>
```

**Local tool (pip package / binary):**

```bash
claude mcp add <name> -- /full/path/to/executable
```

**With environment variables:**

```bash
claude mcp add <name> --env API_KEY=your-key-here -- npx -y <package-name>
```

All flags (`--transport`, `--env`, `--scope`, `--header`) go before the server name. Use `--` to separate the name from the command.

**Windows note:** If `npx` commands fail with "Connection closed", try `npx.cmd` instead of `npx`. For Python tools, always use the full `.exe` path (like `C:/Users/you/AppData/Roaming/Python/Python313/Scripts/tool-name.exe`).

### Step 4: Restart Claude Code

This is the step everyone forgets. MCP servers load at startup. After adding a new one, you must restart Claude Code or the tools won't appear.

Just close and reopen. That's it.

### Step 5: Authenticate (if needed)

Some MCPs need auth after the first connection. Inside Claude Code:

1. Type `/mcp`
2. Select the service
3. Choose "Authenticate"
4. Complete the browser login

For tools with API keys, the key was already set in Step 3 via `--env`. No extra auth needed.

### Step 6: Test it

Ask Claude something simple that uses the new tool:

- GitHub: "List my open pull requests"
- Playwright: "Navigate to google.com"
- ElevenLabs: "List available voices"
- Database: "Show me the tables"

If it works, you're done. If not, check `references/troubleshooting.md`.

## Scopes

Where the MCP config lives determines who can use it.

- **local** (default, no flag): Just you, just this project. Config goes in `.claude/mcp.json`. Not committed to git.
- **project** (`--scope project`): Shared with the team via `.mcp.json` in the repo root. Gets committed.
- **user** (`--scope user`): Just you, but across all your projects. Lives in `~/.claude/mcp.json`.

Example (add GitHub for all your projects):

```bash
claude mcp add --scope user github -- npx -y @anthropic-ai/mcp-github
```

## Management Commands

- `claude mcp list` -- see all connected servers
- `claude mcp get <name>` -- details for one server
- `claude mcp remove <name>` -- disconnect a server
- `/mcp` (inside Claude Code) -- interactive status and auth

## Quick Troubleshooting

Most common issues and their one-line fixes:

- **Tools not showing up after adding:** Restart Claude Code. Seriously, that's it 90% of the time.
- **"Connection closed" on Windows:** Use `npx.cmd` instead of `npx`, or use the full path to the executable.
- **Auth keeps failing:** Try `/mcp`, select the service, "Clear authentication", then re-authenticate.
- **Server in the list but zero tools:** Scope mismatch (project config might override user config) or the server started but crashed silently.
- **Timeout on startup:** Some servers are slow to initialize. Set `MCP_TIMEOUT=30000 claude` for a longer startup window.

For deeper issues, read `references/troubleshooting.md`.

## Project MCPs

This project uses several MCP servers configured in `.claude/mcp.example.json`:

- **NotebookLM:** Google NotebookLM for research and knowledge bases. Needs `notebooklm-mcp init` for auth.
- **ElevenLabs:** Text-to-speech, voice cloning, sound effects. Needs `ELEVENLABS_API_KEY` env var.
- **Excalidraw:** Diagram generation.
- **Playwright:** Browser automation. Uses `--autoConnect` and port 8053 for Chrome remote debugging (not default 9222).
- **Chrome DevTools:** DOM inspection and debugging. Also port 8053.

For verified install commands for these and other popular services, see `references/popular-services.md`.
