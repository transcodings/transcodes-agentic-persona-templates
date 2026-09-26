---
description: Load when writing tests or verifying a change before handing it off
---

# Must
- Cover the behaviour a caller depends on, plus the failure path — not just the happy path.
- Name each test after the guarantee it protects, so a failure reads as a broken promise.
- Keep tests independent: no shared mutable fixtures, no reliance on execution order.
- Run the type checker and the affected tests before reporting the change as complete.

# Never
- Never assert on internal implementation details that a safe refactor would break.
- Never leave a test skipped or commented out without a linked reason.
- Never claim a change is verified when the suite was not run — say which parts are unverified.
