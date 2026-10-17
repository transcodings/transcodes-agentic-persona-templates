# transcodes-agentic-persona-templates

A template can include a Knowledge Base. List it in `metadata.json` under `knowledge`, with every file under `knowledge/`. Creating a Persona from the template writes that Knowledge Base and links it. Applying the Persona to a project copies the Knowledge Base with the Persona.

A list of markdown paths becomes one Knowledge Base named `<persona>-knowledge`:

```json
"knowledge": ["knowledge/product-overview.md"]
```

A named Knowledge Base can include documents and the original files:

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

Documents are Markdown. `name`, `description`, and `aliases` belong in frontmatter. Content files are stored as themselves. `aliases` are the keywords an agent uses to decide that file is needed. Set `counts.knowledge` in `index.json` to the number of Knowledge Bases.