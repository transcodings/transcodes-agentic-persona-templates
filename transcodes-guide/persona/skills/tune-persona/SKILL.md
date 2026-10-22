---
name: tune-persona
description: Explain improving a Persona's Instruction and Guidelines from the project chat — use when asked about transcodes-persona-tune, automatic improvement, or editing AGENTS.md from chat.
---

# Prerequisites
- A Persona already Applied to the project folder, with **Improve Persona Instruction and Rules Automatically** left on.
- The check lives in **Settings → Advanced**. It is on unless they turned it off. The Apply dialog's **Advanced options** can turn it off for one Apply only. Say this setting name in English.

# Steps
1. Tell them this check adds `transcodes-persona-tune` to the project. They do not write this Skill. Apply replaces it.
2. In the project chat, the agent finishes the request first. It then proposes an Instruction or Guideline change only when the preference should hold next time — for example “from now on” or the same correction coming back.
3. A direct request to change the Instruction or a Guideline is already approval. An inferred suggestion waits for one yes. A no ends that suggestion.
4. The change is saved to the Persona in Transcodes Desktop, then Applied again so this folder uses it. Language, tone, role, and output format go in the Instruction. A standing must or never goes in a Guideline.
5. If the project does not have this Skill, open Apply, leave this check on, and Apply again. Changing only Settings → Advanced does not update a project that was already Applied.

# Gotchas
- Do not edit AGENTS.md, CLAUDE.md, GEMINI.md, or the applied Guideline files in the project. Those are copies. The source is the Persona in Desktop.
- This Skill does not create or edit Skills, and it does not change a Knowledge Base or its link.
- A one-off request for this task is not a lasting Persona change.
- The other two Advanced checks are separate. Attribution only adds a line to replies. Ask to save conversations and outputs is update-knowledge-base.

# Output
**Deliverable** — That the check must stay on, that a lasting change is saved in Desktop and then Applied, and the next click if the Skill is missing.
**Done when** — They can tell a one-off task from a change that should govern the next session, and they know not to edit the applied copy.
