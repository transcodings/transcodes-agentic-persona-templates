---
name: install-plugin
description: Install the Transcodes plugin into Claude, Cursor, ChatGPT, or Antigravity from Desktop — use when they ask how to install the plugin, /transcodes, $transcodes, or why the command is missing.
---

# Prerequisites
- Transcodes Desktop is installed and open.
- Which agents they actually use: Claude, Cursor, ChatGPT, Antigravity. Install only those.

# Steps
1. Open Transcodes Desktop. Two entry points:
   - First-run screen **Install the plugin** — pick agents and connect.
   - Any time later: profile menu → **Settings** → **Plugin**.
2. On Plugin, the section is **Transcodes Plugin**. Four rows:
   - Claude
   - Cursor
   - ChatGPT (OpenAI)
   - Antigravity (Google)
3. Each row shows status and the command they will type after install:
   - Claude, Cursor, Antigravity — `/transcodes`
   - ChatGPT — `$transcodes`
4. Status **Not Installed** (red): click **Install**. Wait for **{name} plugin installed**.
5. Status **Installed** (green): already done. **Update** refreshes the plugin. **Remove** uninstalls it from that agent only. Removing does not delete Personas or an already Applied Persona.
6. Use **Refresh** if the row looks stale after an install.
7. **How does it work?** opens the official pictures: slash command for Claude, Cursor, Antigravity; dollar command for ChatGPT.
8. Fully quit that AI and reopen it. An already-open chat often will not see a new plugin.
9. In a new chat, choose the command:
   - Claude, Cursor, Antigravity — type `/transcodes` and select it.
   - ChatGPT — type `$transcodes` and select it.
10. Then give a Persona command, for example list Personas, or apply a named Persona to a project folder. If the command does not appear, the plugin is not in that app — return to step 4.

# Gotchas
- The plugin talks to the Desktop library on this computer. Desktop must stay installed. The plugin does not replace Apply; it can trigger Apply.
- Install is per agent. Installing Claude does not install Cursor.
- They do not need to be signed in to install. Sign-in is required later for push, pull, and remotes.
- Do not tell them to download a plugin from a marketplace or to paste MCP JSON by hand. Desktop Install writes it.
- Cursor is project-only for Apply even after the plugin is installed.

# Output
**Deliverable** — Which Plugin row to open, Install vs already Installed, the exact command for that agent, and that they must quit and reopen the AI.
**Done when** — That agent shows `/transcodes` or `$transcodes` in a new chat.
