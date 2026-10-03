---
name: build-knowledge-base
description: Create documents and contents with required keywords, link them to a Persona, then Apply so the project can read them — use when asked about Knowledge Base, documents, contents, aliases, keywords, 지식 베이스, 문서, or 키워드.
---

# Prerequisites
- Library purpose and name.
- Document (readable Markdown) vs Content (other files).
- Which Persona will link it, and which project folder will Apply.

# Steps
1. Open Transcodes Desktop → Knowledge Base. Create one library per subject.
2. Document: write Markdown, or upload one PDF, Word, Excel, PowerPoint, CSV, Markdown, or text file. Name, description, and keywords are required. The agent finds the file through keywords, not the file name alone. Images inside an uploaded document are dropped.
3. Content: upload one image, font, JSON, YAML, or code file at a time, up to 10 MB. Description and keywords are required. Images and originals stay Content; they are not turned into Documents.
4. Standard can extract description and keywords on upload. The user reviews them. Free types both.
5. Link the library on each Persona that should read it. Unlinked libraries never appear after Apply.
6. Apply that Persona to the project folder. Linked documents and contents are what the agent can read after that.
7. After Apply, the agent finds a document through keywords, then reads that matching file before answering from it.
8. To change a document, edit it in Desktop, then Apply again (or save if the folder is already remembered and auto-apply runs). Do not edit the applied copy in the project.

# Gotchas
- File pickers exist only in Desktop. The plugin cannot choose a disk file.
- Apply fails if a linked Knowledge Base is missing locally. Pull it first, or the previous project copy stays.
- Knowledge sync has no old revision list. One latest organization copy, labeled with a tag.
- A Document without keywords will not save. Treat keywords as required, not optional.
- A Knowledge Base name cannot be changed after create.
- A library still linked to a Persona cannot be deleted. Unlink first.

# Output
**Deliverable** — Library name, files added, keywords present, Personas linked, and the project folder they still need to Apply.
**Done when** — The library is linked and they know they must Apply to the project before the agent can open those files.
