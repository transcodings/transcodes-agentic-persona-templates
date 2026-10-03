---
name: set-up-persona
description: Create or edit a Persona in Desktop — use when asked to make, generate, or change Instruction, Guideline, or Skill, or 페르소나 만들기, before applying it to a project.
---

# Prerequisites
- The role in one sentence.
- Template or blank.
- Standard sign-in only if they want Generate or Edit with AI.

# Steps
1. Open Transcodes Desktop → Personas.
2. Add Persona. Choose Transcodes template (open-source GitHub catalog) or Set up yourself.
3. Name it in any language, up to 30 characters. That exact name is what Apply and the plugin require later.
4. Instruction first: role, always-on context, how it works, output. This is what the check question must repeat after Apply. Show the fill-in with examples:
   - Designer: “I review UI against the design system. I name tokens and missing states, not a PRD.”
   - Planner: “I turn a request into a spec — problem, user, success, non-goals, then a recommendation.”
5. Add Guidelines as must / never policy. One file per standing standard. The description line is when that Guideline loads. Example: Designer never hardcodes hex. Planner never invents a ship date.
6. Add a Skill per repeatable job. The Skill name is lowercase kebab-case and matches its folder. Include trigger, steps, and a done check. Example: Designer `design-review`. Planner `write-spec`.
7. On Standard, Generate or Edit with AI is a draft. They read and correct it before Apply.
8. Link every Knowledge Base this Persona should read. Linking is on the Persona, not implied by creating a library.
9. Save. Tell them the Persona is only in the Desktop library until Apply. Next skill is apply-persona.

# Gotchas
- A template does not ship a Knowledge Base. Create documents in the Knowledge Base tab, then link.
- Instruction is identity. Guideline is policy. Skill is a procedure.
- Rename or delete in Desktop does not remove an already Applied copy. Apply again to replace it, or remove that Apply from the project if they meant to take it out.
- If they will use it in a repo today, do not linger on polish. Apply a first version, then edit; a remembered folder auto-applies later saves.

# Output
**Deliverable** — Persona name, what was filled, linked libraries, and that Apply to a workspace is required next.
**Done when** — The Persona is saved and they are ready to pick a project folder.
