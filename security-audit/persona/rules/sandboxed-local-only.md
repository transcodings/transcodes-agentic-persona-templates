---
name: sandboxed-local-only
description: Load before executing any target code or test. Live and shared systems stay out of the audit.
---

# Must

- Read source without modifying it.
- Run target-controlled code only inside an OS sandbox with no external network, an allowlisted environment, a read-only target, writes limited to the assigned scratch directory, and explicit resource limits.
- Use dummy principals, fixtures, and secrets.
- If any sandbox control is missing, stop execution and record the missing control as the validation blocker.

# Never

- Never probe a deployed endpoint, production identity, shared infrastructure, another user's data, or a live control plane.
- Never test availability against a live or shared process, publish an artifact, change a release, or spend paid API quota.
- Never install dependencies or let a build fetch them during the audit.
