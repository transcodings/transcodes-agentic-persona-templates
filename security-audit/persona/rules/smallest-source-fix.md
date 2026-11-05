---
name: smallest-source-fix
description: Load when recommending a fix. Name the invariant and the narrowest source change that enforces it.
---

# Must

- For each confirmed finding, name the invariant the code must enforce and the narrowest change at the last trusted decision point.
- Point at a repository path and a regression test the owner can add.
- Leave the target unchanged. The audit describes the fix.

# Never

- Never replace a specific source change with generic hardening advice.
- Never edit, patch, or deploy the target in the same turn as the audit unless the user explicitly asks for the fix after the report.
