---
name: use-desktop-app
description: Install and navigate Transcodes Desktop — use when they ask how to open the app, where a screen is, how to sign in, connect an AI, change settings, 사이드바, 설정, or 로그인.
---

# Prerequisites
- They have Transcodes Desktop, or they need the download.
- Whether they only need local work, or also organization sync.

# Steps
1. Install and open Transcodes Desktop on this computer. The library of Personas and Knowledge Bases lives here, not in the project until Apply.
2. First launch may run onboarding: pick a language, create the first Persona from a template or by hand, then Apply it to a workspace. They can skip Apply, but then no AI has the Persona yet.
3. The sidebar is the map:
   - Personas — create, edit Instruction / Guideline / Skill, link Knowledge Bases, Apply.
   - Knowledge Base — documents, contents, keywords, link to Personas.
   - Organization — members, team Personas, team Knowledge Bases, plan.
   - Settings (profile menu) — account, billing, theme, language, connected AI agents, plugin.
4. Profile menu → How To Use / 사용법 알아보기 has seven chapters with videos. Point them there if they want the pictures. This Persona teaches the same topics.
5. Sign-in is optional for local create and Apply. Use the profile menu. Finish the browser login; the app updates when it completes. Sign in when they need Sync to Cloud, Get Latest, invites, or paid AI.
6. Settings → AI Agent connects Claude, ChatGPT, or Antigravity with an API key or OAuth. Credentials stay on this device. Needed for Transcodes AI chat and for verifying Apply from chat.
7. Settings → Plugin installs the plugin per agent. Walk install-plugin: Install on each AI they use, fully quit that AI, then `/transcodes` or `$transcodes`. First-run may show Install the plugin before Settings exists.
8. Settings → Theme and Language are this-device only. Billing and organization name need sign-in.

# Gotchas
- Closing the apply dialog in onboarding saves the Persona but does not put it in a project.
- Switching organization in the sidebar changes which remotes they see. Local files stay on the device.
- Transcodes AI chat can create or edit a Persona, but Apply still needs a folder and targets.
- Do not send them to hunt for library files on disk. Open Transcodes Desktop.

# Output
**Deliverable** — Which sidebar item to open, whether they must sign in, and the next chapter (usually create a Persona or Apply).
**Done when** — They can find Personas, Knowledge Base, Organization, and Settings without guessing.
