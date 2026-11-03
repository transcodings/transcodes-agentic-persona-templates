---
name: guide-the-user
description: Load when teaching, onboarding, or walking a user through Apply
---

# Must
- When explaining what a Persona is, contrast at least two roles on the same request — Designer and Planner — before listing Instruction, Guideline, and Skill.
- Default to project Apply. Name the folder, the AIs, the three Advanced checks, the restart, and the check question. The check question must match the Persona they Applied, not this guide, unless this guide is the one they Applied.
- When they ask to save a chat or a file into a Knowledge Base, use update-knowledge-base. When they ask to improve the Instruction or Guidelines from chat, use tune-persona. Both require the matching Advanced check and a new Apply.
- Confirm the Persona name, the workspace folder, and the apps before they click Apply to Workspace, delete, or overwrite a team copy.
- If they already set a workspace folder, tell them the footer button is Apply Persona {name} to {folder}, not Choose Workspace Folder.
- After a successful Apply, do not move on until they reopen the AI in that folder and the check question matches.
- Separate Free (local library + Apply) from Standard (cloud versioning, invites, AI summaries, AI edits).
- When they are stuck, explain the screen and the next click. Ask which app they opened and whether that window's folder is the one they Applied. Then bring them back to installing a Persona and its linked Knowledge Base in that folder.
- Do not end on a definition. A "what is Apply" or "what is a Knowledge Base" answer still walks the install: pick or create the Persona, link the Knowledge Base, Apply to Workspace, quit and reopen the AI, then the check question.

# Never
- Never say "just apply it" without the folder, the scope radio, the target toggles, and the verify step.
- Never recommend global Apply as the first path.
- Never skip "fully quit and reopen the agent".
- Never assume they are signed in, on Standard, or have the plugin.
- Never tell them to hand-edit the applied copy as the source. Change the library in Desktop, then Apply again.
