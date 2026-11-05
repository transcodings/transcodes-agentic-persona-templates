---
name: source-boundary-evidence
description: Load before calling any security issue a finding. A candidate needs a trust boundary and source evidence.
---

# Must

- Name the lower-trust principal, the accepted input, the control that should hold, the boundary that was crossed, the affected resource, and the concrete result.
- Ground the path in source you opened in this review. Quote the file and the decision point.
- Keep a blocked but source-grounded lead as needs validation, with the exact fact that is still missing. Do not assign it a severity.
- Say when deployment, proxy, identity, or provider behavior is absent from the repository instead of assuming it.

# Never

- Never report a checklist gap, a missing second layer, or a style issue as a vulnerability when an existing control already stops the action.
- Never treat a same-principal or self-only effect as a cross-boundary finding.
- Never raise a parser or runtime result above the effect you actually observed.
