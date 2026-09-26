---
name: ship-feature-slice
description: Implement a feature across data, API, and UI in one reviewable slice — use when asked to "add a feature", "build this endpoint and screen", or "wire this up end to end".
---

# Prerequisites
- The user-visible behaviour, including what happens on the error path.
- Whether the data model changes, and if a migration is required.
- The commands for the type checker and the test suite in this repo.

# Steps
1. Map the slice: list the files you expect to touch per layer, and confirm the plan before writing code.
2. Update the contract first — schema, types, DTOs — and run the type checker to collect every affected call site.
3. Implement the data and service layer, then its tests, and get those green before moving up.
4. Implement the API surface with input validation and the error responses the UI will render.
5. Implement the UI against the real contract, including the loading and error states.
6. Run the type checker and the full affected test suite, then summarize the slice and the commands you ran.

# Gotchas
- A passing type check is not a passing test run — the compiler cannot see a wrong query.
- Migrations that rename or drop a column break the running version during deploy; add the new shape first and remove the old one in a follow-up.
- Optimistic UI updates silently diverge from server state unless the failure path rolls them back.

# Output
**Deliverable** — A working slice with tests, plus a summary listing each layer changed and the verification commands and results.
**Done when** — The type checker passes, the affected tests pass, and both the happy path and the error path have been exercised.
