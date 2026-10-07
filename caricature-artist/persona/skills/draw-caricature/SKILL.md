---
name: draw-caricature
description: "Use when asked to draw a caricature, cartoon portrait, or redraw a photo in a caricature style. Also for 캐리커처, 캐리커쳐, and 사진 캐리커처."
---

# Prerequisites
- A photo of the person to draw. If the user has not provided one, ask for it and stop.
- A linked Knowledge Base applied to this project. Style references are image contents, found by description and keywords.
- The image tool available in the current app. If this app cannot generate or edit images, say so and stop. Do not describe a picture in place of the file.

# Steps
1. Read the request and separate two things: the subject photo, and the style the user named. A style name is not a subject.
2. Search the linked Knowledge Base contents for that style. Open every image whose description or keywords match. Ignore documents, because images inside documents are dropped.
3. If the user named a style and no content image matches it, stop. Ask which style they want, and ask them to add a reference image to the Knowledge Base when they have one. Do not draw in this turn.
4. If the user did not name a style and the Knowledge Base has style images, list those images by name and description and ask which one to use. If it has none, ask them to name the style or add a reference image. Stop until they answer.
5. Generate the caricature only after a subject photo and one chosen style image are both in hand. Pass the photo as the subject and the style image as the reference. Keep the person recognizable and push the exaggeration toward that reference.
6. Check the result against the photo and the reference. If the person is no longer recognizable, or the rendering misses the reference, generate again with a tighter instruction. Do not deliver the first miss.

# Gotchas
- A Knowledge Base that is not linked to this Persona, or not applied to this project, is invisible. Say that and ask the user to link and apply it. Do not guess the style.
- Several images can share a style name. Ask which one when more than one matches. Do not pick silently.
- The style reference shows how to draw. It is not a second person to merge into the portrait unless the user says so.

# Output
**Deliverable** — The caricature image, the Knowledge Base content name or the reference the user supplied, and one line naming what was exaggerated.
**Done when** — The subject matches the user's photo, the rendering matches the chosen style image, and no image was generated before that style was confirmed.
