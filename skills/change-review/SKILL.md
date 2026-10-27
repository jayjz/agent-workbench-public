---
name: change-review
description: Review a proposed diff for safety, scope, regressions and verification.
---

# change-review

## Trigger
Use when the user explicitly requests this kind of review or the current task clearly requires it.

## Procedure
1. Define scope, inputs, and success criteria.
2. Inspect relevant primary artifacts before drawing conclusions.
3. Separate observed facts from inferences and unknowns.
4. Identify the smallest safe next action, with verification.
5. Report exact evidence and limitations. Do not claim unrun tests passed.

## Constraints
Read only unless the user separately authorizes changes. No destructive commands or secret disclosure.

## Non-triggers
Do not select for new work; use change-verifier instead.

## Output
A bounded review with source locations, actual checks and unresolved risks.

## Verification
Check reported observations against the diff and command results.

## Limitations
DEPRECATED compatibility entry retained from the original scaffold. No behavioral evaluation exists. Its generic procedure is superseded by change-verifier; do not install both.
