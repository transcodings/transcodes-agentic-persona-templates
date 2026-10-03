---
name: explain-transcodes
description: Give the product map — use when asked what Transcodes is, what a Persona changes, 뭐야, 사용법, 기능, 예시, 디자이너, 기획자, or how this team uses it, before or after they have a project folder.
---

# Prerequisites
- Language of the request.
- Whether they have already Applied a Persona to a folder.

# Steps
1. One line: set a Persona and Knowledge Base in Transcodes Desktop, Apply them into the project folder, then every AI opened in that folder follows the same standard.
2. Before any feature list, explain with two roles on the same request. Do not skip this.

   Same request: “온보딩 버튼을 더 잘 보이게 해줘.” English: “Make the onboarding button stand out.”

   **Designer Persona** — the catalog template is UI/UX Designer.
   - Instruction / 지시 사항: a product designer. Designs the whole state set. Reaches for an existing component and its tokens first.
   - Guideline / 가이드라인: use tokens for colour and spacing. Never hardcode a hex or a pixel value a token already covers.
   - Skill / 업무 도구: `design-review`. Walk empty, loading, error. Report blocking / should-fix / polish, each with the file and the fix.
   - Knowledge Base they would link: design tokens, component names, accessibility target.
   - What the AI actually does: names the token, the missing state, and the label. It does not write a PRD.

   **Planner Persona** — there is no Planner template. They create this with Add Persona → Set up yourself.
   - Instruction / 지시 사항: a product planner. Turns a request into a decision, not a mock.
   - Guideline / 가이드라인: every spec includes problem, user, success metric, and non-goals. Never invent a ship date.
   - Skill / 업무 도구: `write-spec`. Draft problem → options → recommendation → open questions.
   - Knowledge Base they would link: past specs, who the product is for, pricing facts.
   - What the AI actually does: writes the decision and the open questions. It does not pick a token or restyle the button.

   One contrast line: same sentence, two Personas, two jobs. That is the value. A Marketer or Fullstack Developer Persona would answer a third way — say so only if they ask.
3. Cover the product in this order, only as far as they asked:
   - Desktop app — the library. Sidebar: Personas, Knowledge Base, Organization, Settings.
   - Persona — Instruction, Guideline, Skill. Point back to the Designer and Planner fill-in above.
   - Knowledge Base — documents and contents with required keywords, linked to a Persona.
   - Apply to a project — the required step. Folder + AIs + This workspace only → restart → check question. Apply the Designer Persona to the design repo, the Planner Persona to the spec folder. Same AI, different folder, different job.
   - Versioning — Organization tables. Personas get revisions. Knowledge Bases get one tagged latest copy.
   - Organization — members, invites, plan. Standard for cloud and seats.
   - Plugin — Desktop Settings → Plugin → Install on each AI, restart that AI, then `/transcodes` (Claude, Cursor, Antigravity) or `$transcodes` (ChatGPT).
4. Plans: Free is unlimited local Personas and Knowledge Bases, and local Apply. Standard is cloud sync, team invites, AI document summaries, and AI Persona edits. Standard is $6 per member per month. Do not invent another price.
5. How To Use / 사용법 알아보기 in the profile menu has seven chapters: confirm Apply, Persona parts, Knowledge Base, apply to agents, organization, versioning, plugin.
6. If they have no project Apply yet, go to apply-persona next. Do not end on a map.

# Gotchas
- Saved in Desktop ≠ used in the project. Apply is the line.
- Do not present Planner as a catalog template. UI/UX Designer is in the catalog. Planner is Set up yourself.
- This guide does not cover Guard, Admin API, or the authentication SDK.

# Output
**Deliverable** — Designer vs Planner on one request, then a short map and the next action, usually picking a workspace folder.
**Done when** — They can say which role they want, whether they still need to Apply, and to which folder.
