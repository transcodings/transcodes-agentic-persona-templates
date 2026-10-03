---
name: use-plugin
description: Use an already-installed Transcodes plugin from chat — use when /transcodes or $transcodes is available and they want to create, edit, apply, or sync from Claude, Cursor, ChatGPT, or Antigravity.
---

# Prerequisites
- The plugin is installed for that agent. If the command is missing, run install-plugin first.
- Exact Persona name for any apply, edit, or delete.

# Steps
1. Open a new chat in that agent. Claude, Cursor, Antigravity: `/transcodes`. ChatGPT: `$transcodes`.
2. They can list, create, read, edit, apply, and sync Personas, and list, create, read, and sync Knowledge Bases.
3. Require the exact Persona name. Never pick from list order.
4. To apply to a project: confirm the folder, this-workspace only unless they asked for this device, and the apps. Cursor is project-only. Dry-run when they only want to preview the Apply.
5. Document writes need complete Markdown with name, description, and aliases. Choosing a file from disk still happens in Desktop.
6. Push and pull need Desktop sign-in. If auth is missing, stop and send them to sign in.
7. If there is no command for the request, say it may not be in the plugin and finish it in Desktop.

# Gotchas
- The plugin edits the Desktop library. It does not skip Apply into the project folder.
- Global apply from chat must omit Cursor.
- An old chat window may not see a plugin that was just installed — new chat after a full quit.

# Output
**Deliverable** — The command they choose, the confirmation (name, folder, apps), and any step that still needs Desktop.
**Done when** — The chat command finishes the request, or they know the Desktop screen that can.
