# Transcodes - Make AI Work the Way You/Team Do

<a href="https://transcodes.io"><img src="https://transcodes.io/web-app-manifest-512x512.png" alt="Transcodes" width="22" height="22" align="absmiddle" /></a> <a href="https://transcodes.io">transcodes.io</a> | <a href="https://www.youtube.com/@hellotranscodes"><img src="https://cdn.simpleicons.org/youtube/FF0000" alt="YouTube" width="16" height="16" align="absmiddle" /></a> <a href="https://www.youtube.com/@hellotranscodes">YouTube</a> | <a href="https://www.instagram.com/transcodes_ai/"><img src="https://cdn.simpleicons.org/instagram/E4405F" alt="Instagram" width="16" height="16" align="absmiddle" /></a> <a href="https://www.instagram.com/transcodes_ai/">Instagram</a> | <a href="https://x.com/hellotranscodes"><img src="https://cdn.simpleicons.org/x/000000" alt="X" width="14" height="14" align="absmiddle" /></a> <a href="https://x.com/hellotranscodes">Twitter</a> | <a href="https://discord.gg/VQ4qjVbnTw"><img src="https://cdn.simpleicons.org/discord/5865F2" alt="Discord" width="16" height="16" align="absmiddle" /></a> <a href="https://discord.gg/VQ4qjVbnTw">Discord</a>

Transcodes is a desktop app for AI Agentic Personas, and team hub where teammates share that AI agent and its Knowledge Base. Persona is an onboarding manual made of an Instruction, Rules, Skills, and a Knowledge Base. Apply the same Persona to Claude, Cursor, ChatGPT, and Antigravity.

# Agentic Persona Templates

Persona templates above are designed to be applied the same way. Transcodes app makes it much easier.

## 1. Install Transcodes Desktop app - Easy Way (Recommended)

1. Download [Mac](https://github.com/transcodings/transcodes-desktop-release-v1/releases/latest/download/Transcodes-mac-universal.dmg) or [Windows](https://github.com/transcodings/transcodes-desktop-release-v1/releases/latest/download/Transcodes-windows-setup.exe).
2. **Personas** → **Add Persona** → **Transcodes template**. Pick one and name it. The Knowledge Base comes with that Persona.
3. **Apply Persona** to the project folder and the apps you use.
4. For your own knowledge or custom template data, create a **Knowledge Base**, add it there, and link it to that Persona.
5. Restart the AI app.

## 2. DIY Way - Apply AGENTS.md, Rules, and Skills manually

Use this when you are not installing the app. Copy one template folder into the project the AI opens, then quit and reopen that AI.

Inside a template:

| File                     | What it is                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `persona/AGENTS.md`      | Instruction. Who the agent is and how it works.                                                                          |
| `persona/rules/*.md`     | Guidelines. One standing rule per file. Keep the frontmatter. `description` is when the AI should load that file.        |
| `persona/skills/<name>/` | A Skill. Copy the whole folder, including `SKILL.md`.                                                                    |
| `knowledge/`             | Knowledge Base, only when the template has this folder. Documents are Markdown. Other files are the original references. |

Put them here, in the project root:

| App         | Instruction                                  | Guidelines                              | Skills                   |
| ----------- | -------------------------------------------- | --------------------------------------- | ------------------------ |
| Claude      | `AGENTS.md` and the same text as `CLAUDE.md` | `.claude/rules/`                        | `.claude/skills/<name>/` |
| Cursor      | `AGENTS.md`                                  | `.cursor/rules/`, file extension `.mdc` | `.cursor/skills/<name>/` |
| ChatGPT     | `AGENTS.md`                                  | `.codex/rules/`                         | `.agents/skills/<name>/` |
| Antigravity | `AGENTS.md`                                  | `.agents/rules/`                        | `.agents/skills/<name>/` |

For a Knowledge Base, copy `knowledge/` into the project and add the paths to `AGENTS.md`, so the agent reads those files before it answers. `aliases` in a document’s frontmatter, or on a content file in `metadata.json`, are the keywords that say when that file is needed.

Example, the starter:

```text
starter/persona/AGENTS.md                           →  AGENTS.md
starter/persona/rules/persona-growth.md             →  .claude/rules/persona-growth.md
starter/persona/skills/handle-a-task/               →  .claude/skills/handle-a-task/
```

Repeat the Guideline and Skill copies for each app you use. Open that project in the AI and ask the same check question.

| Folder                                                     | What it does                                                                                                       |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [transcodes-guide](transcodes-guide)                       | Walks through Transcodes Desktop, then Apply into a real project folder. One sample document shows how to use the linked Knowledge Base. |
| [starter](starter)                                         | A general Persona that does the task, then updates its Instruction and Rules. One sample document shows how to add a file to the Knowledge Base. |
| [card-news-creator](card-news-creator)                     | Plans Instagram and LinkedIn card-news carousels in four visual systems. A sample image becomes the HTML template, index.html shows the render, and yes writes the PNG and LinkedIn PDF. |
| [presentation-deck-kit](presentation-deck-kit)             | Builds a 16:9 deck as HTML from four template skills. A sample image can become the template. index.html shows the render, and yes prints the PDF and, when asked, PowerPoint. |
| [landing-page-builder](landing-page-builder)               | Collects the complete brief, presents a production plan for approval, then builds and visually verifies a cinematic landing page. |
| [landing-seo-geo-aeo-checker](landing-seo-geo-aeo-checker) | Audits a landing site across technical SEO, relevance, authority, GEO, and AEO, then writes what to improve.       |

## Template format

The app reads `index.json` and each folder’s `metadata.json`.

`category` is a string array. The landing page keeps a row when any value matches the selected filter.

`counts.knowledge` in `index.json` is the number of Knowledge Bases.

A list of markdown paths becomes one Knowledge Base named `<persona>-knowledge`:

```json
"knowledge": ["knowledge/product-overview.md"]
```

A named Knowledge Base can include documents and the original files. Every path stays under `knowledge/`:

```json
"knowledge": {
  "id": "style-references",
  "name": "Style references",
  "description": "Reference files for this Persona.",
  "documents": ["knowledge/style-references/documents/ink-style.md"],
  "contents": [
    {
      "file": "knowledge/style-references/contents/ink.txt",
      "description": "Ink style notes",
      "aliases": ["ink"]
    }
  ]
}
```

Documents are Markdown. `name`, `description`, and `aliases` belong in frontmatter. Content files are stored as themselves.

## Contributing

Open a pull request on this repository.

## License

[GPL-3.0](LICENSE).

## Issues

Report a bug or a problem in [Issues](https://github.com/transcodings/transcodes-agentic-persona-templates/issues).
