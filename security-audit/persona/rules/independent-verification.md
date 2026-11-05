---
name: independent-verification
description: Load before accepting a candidate into the report. The finder does not confirm its own finding.
---

# Must

- Give every candidate to a fresh verifier that tries to disprove it.
- Put only confirmed, needs-validation, and rejected records in `findings.json`, and validate that file with the skill's schema and validator.
- Assign severity only to a confirmed record, and keep that severity within the impact that was demonstrated.
- Make the written report match the verified records. Prose does not add, drop, or upgrade a finding.

# Never

- Never let the agent that found a candidate be the agent that confirms it.
- Never give a severity to a needs-validation record.
- Never call a run complete while a validator fails or a required phase is unfinished. Record the run as incomplete and name the gap.
