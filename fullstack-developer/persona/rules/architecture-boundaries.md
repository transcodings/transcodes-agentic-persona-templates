---
description: Load when adding or moving modules, services, controllers, or data access code
---

# Must
- Keep each feature owning its own routes, services, and data access; share only through an explicit public entry point.
- Validate and narrow every external input — request bodies, query params, webhook payloads — at the boundary before it reaches business logic.
- Put database access behind the repository or data layer so services stay testable without a live database.
- Ship the migration together with the code that depends on it, and keep it backwards compatible for one release.

# Never
- Never import another feature's internal file directly; go through its public entry point or lift the shared piece out.
- Never let a controller or a React component contain business rules — move them into a service or a pure function.
- Never widen a type with `any` or a cast to make an error disappear; fix the contract instead.
