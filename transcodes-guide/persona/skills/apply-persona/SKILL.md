---
name: apply-persona
description: Apply a Persona into a real project folder and prove the AI loaded it — use when asked to apply, deploy, put a Persona into Claude or Cursor, or "how do I actually use this in my repo".
---

# Prerequisites
- Exact Persona name.
- The workspace folder they will open in the AI (usually the git repo root).
- Which apps they use in that folder: Claude, Cursor, ChatGPT, Antigravity.
- Project scope unless they explicitly asked for this whole computer.

# Steps
1. Open Transcodes Desktop → Personas → that Persona.
2. Look at the footer:
   - No folder yet: **Choose Workspace Folder**. Pick the project root (the folder they open in Cursor or Claude).
   - Folder already set: **Apply Persona {name} to {folder}**.
3. The Apply Persona dialog opens. Current edits save first. Walk every control:
   - **Apply to** — toggle only the AIs they will open. Claude, ChatGPT, Antigravity, and Cursor (Cursor appears only for project scope).
   - **Target Workspace Directory** — confirm it is the folder they open in the AI. Use Change if it is wrong.
   - **Persona apply scope** — choose **This workspace only**. That is the normal path. The Persona is used only when they work in this folder.
   - Do not choose **This whole computer** unless they want one Persona in every session. Global skips Cursor and is easy to regret.
   - **Advanced options** — three checks. They start from **Settings → Advanced**. A change in this dialog applies only to this Apply. The device default stays until they change it in Settings.
4. Walk the three checks. Say these names in English. All three start on. Leave them on unless they ask to turn one off:
   - **Show the Persona used in every response** — each reply ends with the Persona name and the Guidelines, Skills, and Knowledge Base it used. Unused categories say none. This adds no Skill.
   - **Ask to save conversations and outputs** — after Apply, the project can use `transcodes-knowledge-save` and `transcodes-knowledge-maintenance`. See update-knowledge-base.
   - **Improve Persona Instruction and Rules Automatically** — after Apply, the project can use `transcodes-persona-tune`. See tune-persona.
5. Click **Apply to Workspace**. The dialog warns that an earlier Apply in that folder will be replaced. Files they wrote themselves are left alone. Turning a check off and Applying again removes the Skill Transcodes generated for it.
6. Fully quit the selected AIs and reopen them. A window that was already open often keeps the old Instruction.
7. In that AI, open the same workspace folder. Ask: “What is your role? What are your guidelines and skills?”
8. Pass: the answer matches the Persona they Applied. Fail: they opened a different folder, skipped that AI in Apply to, or did not restart. Fix that, do not rewrite the Persona first.
9. After a folder is remembered, later Desktop saves apply to that folder automatically. If they add a new project, run this skill again with the new folder. If they add Cursor later, open Apply and toggle Cursor — it cannot be applied globally. A change in Settings → Advanced applies only after they Apply again.

# Plugin path
- After Desktop Apply works once, they can also run `/transcodes` or `$transcodes` and ask to apply the same Persona to the same project folder with the same targets. Confirm name, folder, and apps. Never include Cursor on a this-device apply.

# Gotchas
- Apply is not git push and not a production deploy. It applies the Persona on this computer. They share it through the repo only if the team wants that.
- A missing local linked Knowledge Base stops Apply and keeps the previous project copy. Pull that library, then Apply again.
- Empty Apply to cannot submit. If they chose global, Cursor is hidden; they must pick Claude, ChatGPT, or Antigravity.
- The two chat Skills appear only after an Apply that left their checks on. Changing Settings → Advanced without Applying again leaves the project on the old choice.
- Checking from a parent folder, or a different folder, looks like Apply failed.
- Do not hand-edit the applied copy to “fix” the agent. Edit the Persona in Desktop, then Apply (or save, if auto-apply is on).

# Output
**Deliverable** — Persona name, folder, scope, AIs, which of the three Advanced checks stayed on, the restart, and the check question.
**Done when** — The AI opened in that folder states the same role, guidelines, and skills as the Persona.
