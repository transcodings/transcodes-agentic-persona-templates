---
name: update-knowledge-base
description: Explain saving a conversation or a generated file into a linked Knowledge Base, and cleaning that library — use when asked about transcodes-knowledge-save, transcodes-knowledge-maintenance, saving chat, checkpoints, creation guides, or duplicates.
---

# Prerequisites
- A Persona already Applied to the project folder, with **Ask to save conversations and outputs** left on.
- A Knowledge Base linked to that Persona. If none is linked, they link one in Transcodes Desktop, then Apply again.
- The check lives in **Settings → Advanced**. It is on unless they turned it off. The Apply dialog's **Advanced options** can turn it off for one Apply only. Say this setting name in English.

# Steps
1. Tell them this check adds two Skills to the project. They are not Skills they author. Apply replaces them.
   - `transcodes-knowledge-save` — asks once, then saves.
   - `transcodes-knowledge-maintenance` — asks once, then cleans the Desktop library.
2. Save happens in the project chat, after the current answer:
   - A long conversation, a finished stage, or the end of a session can be one document. It is a checkpoint. It has no original file.
   - A reusable image, PDF, video, or other generated file is two items: the original file, plus one document that records how it was made.
   - The agent names the Knowledge Base and every item, then waits for one yes. That yes also updates the project. It does not ask again before Apply.
3. On yes, the save goes to the Knowledge Base in Transcodes Desktop. Apply then refreshes the copy in the project, including `.agents/knowledge`. If one item fails, the project copy stays as it was and the agent says which item failed.
4. Cleaning is separate. They ask to clean, organize, or remove duplicates, or a save fails because storage is full. The agent audits the Desktop library, lists keep, merge, or delete, and waits for one yes. It changes only those items in Desktop, then Applies again. It never deletes the whole Knowledge Base.
5. If the project does not have these Skills, open Apply, leave this check on, and Apply again. Changing only Settings → Advanced does not update a project that was already Applied.

# Gotchas
- Do not edit `.agents/knowledge`, AGENTS.md, or CLAUDE.md to update the library. Those are copies. The source is the Knowledge Base in Desktop.
- A checkpoint and a generated file are not the same package. Do not store one piece of work as both.
- Same bytes can be a duplicate. The same title with different bytes is only a candidate. Original files are not merged.
- A large library is not a reason to clean it. Clean when they ask, or when storage actually blocks a save.

# Output
**Deliverable** — Which check must stay on, which of the two Skills they will see, and whether they still need to link a Knowledge Base and Apply.
**Done when** — They know a yes saves or cleans the Desktop library first, and the project copy updates only after that Apply succeeds.
