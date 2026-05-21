# MCP Troubleshooting

Organized by what you see (the symptom), not what's wrong underneath. Start with the symptom, follow the fix.

## "Server disconnected" or tools vanish mid-session

The server process crashed. Most common causes:

- The npm/pip package wasn't installed globally and the temp install expired
- The server hit an unhandled error and exited
- System went to sleep and the process didn't survive

Fix: Restart Claude Code. If it keeps happening, install the package globally instead of relying on `npx -y`:

```bash
npm install -g @package/name
claude mcp add tool-name -- package-command
```

## Tools not appearing after adding an MCP

The #1 cause: you didn't restart Claude Code. MCP servers load at startup. Close and reopen.

If you did restart and still nothing:

- Run `claude mcp list` and confirm the server is there
- Check if the server name has a typo
- Check scope: if you added to `--scope user` but the project has a `.mcp.json` that overrides it, the project config wins
- Try `claude mcp get <name>` to see the full config and spot issues

## "Connection closed" error (Windows)

Windows and `npx` don't always play nice. Three fixes in order of preference:

1. Use `npx.cmd` instead of `npx` in the command
2. Install the package globally and use the full path to the executable
3. For Python MCPs, always use the full `.exe` path:

```
C:/Users/you/AppData/Roaming/Python/Python313/Scripts/tool-name.exe
```

Never rely on just the command name on Windows. Full paths are more reliable.

## "spawn ENOENT" error

The binary Claude is trying to run doesn't exist at that path or isn't on PATH.

Fix: Find the actual path to the executable and update the MCP config:

```bash
where tool-name        # Windows
which tool-name        # Mac/Linux
```

Then update with the full path:

```bash
claude mcp remove tool-name
claude mcp add tool-name -- /full/path/to/executable
```

## Authentication keeps failing

- Run `/mcp` inside Claude Code, select the service, choose "Clear authentication"
- Re-authenticate from scratch
- For browser-based OAuth: make sure you're signed into the right account. Multiple Google accounts are a common source of confusion.
- For API key auth: double-check the key is correct and not expired. Re-add the MCP with the correct `--env` value.

## Server shows in list but returns errors

The server started but can't do its job. Usually a missing or expired API key.

- Check the env vars: `claude mcp get <name>` shows the config
- Regenerate the API key if it might be expired
- Remove and re-add with the correct env vars

## Timeout on startup ("MCP server failed to start")

Some servers take a while to initialize, especially on first run when npm is downloading packages.

Fix: Give it more time:

```bash
MCP_TIMEOUT=30000 claude
```

Or on Windows PowerShell:

```powershell
$env:MCP_TIMEOUT=30000; claude
```

## Project-specific issues

### NotebookLM

- **Cookie expiry:** Auth cookies expire periodically. Run `notebooklm-mcp init <notebook-url>` again to re-authenticate.
- **Multiple Google accounts:** Sign out of all accounts in Chrome first, then run init with only the target account signed in.
- **v1 vs v2 confusion:** The `~/.notebooklm-mcp/auth.json` file is from v1 and no longer used. v2 uses Chrome profile-based auth.

### Playwright

- **Chrome remote debugging must be enabled.** Go to `chrome://inspect/#remote-debugging` and turn it on.
- **This project uses port 8053** (not the default 9222). Make sure Chrome is configured for 8053.
- **After enabling remote debugging**, restart Claude Code for the MCP to connect.
- **`--autoConnect`** flag discovers Chrome automatically. No `--browserUrl` needed if Chrome is running with debugging enabled.

### ElevenLabs

- **API key location:** Must be set as `ELEVENLABS_API_KEY` in the MCP env config, not just in `.env`.
- **Output path:** `ELEVENLABS_MCP_BASE_PATH` controls where generated files land. Set to `.tmp` to keep them in the project temp directory.

## Nuclear option

If nothing else works:

1. `claude mcp remove <name>`
2. Restart Claude Code
3. Re-add from scratch following the setup steps in SKILL.md
4. Restart Claude Code again
5. Test

If it still doesn't work, check that the underlying tool actually runs outside of Claude:

```bash
npx -y @package/name --help
```

If that fails too, the problem is the package itself, not the MCP config.
