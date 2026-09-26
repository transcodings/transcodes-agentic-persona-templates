---
name: publish-landing-page
description: Build or update a marketing landing page end to end — use when asked to "create a landing page", "update the pricing page", "add a section", or "ship the campaign page".
---

# Prerequisites
- The positioning brief: audience, the one job the page must do, and the primary call to action.
- Approved copy points and any metric or customer name that will appear on the page.
- The route to create or edit, and whether it replaces an existing page.

# Steps
1. Read the closest existing page and list the sections and tokens you can reuse. Do not invent a new section vocabulary when one already fits.
2. Draft the copy block first — headline, subhead, three proof points, and the call to action — and confirm it before touching layout.
3. Compose the page from existing components, adding new ones only for a section that genuinely has no equivalent.
4. Fill in page metadata: title, description, canonical URL, and Open Graph image.
5. Run the production build, then a Lighthouse run against the built page, and fix anything below the performance budget.
6. Report the preview URL, the scores, and any copy still waiting on human approval.

# Gotchas
- Copy edits in a CMS do not appear until the page is revalidated — trigger the revalidation instead of assuming a deploy is enough.
- A page that scores well on desktop can still fail mobile LCP; only the throttled mobile run counts.
- Redirects for a renamed route must land in the framework config, not in a client-side effect.

# Output
**Deliverable** — A page (or diff) that builds cleanly, with metadata filled in and Lighthouse numbers attached.
**Done when** — The build passes, mobile Lighthouse performance and accessibility are both at or above 90, and no placeholder copy remains.
