---
name: change-verifier
description: Verify a bounded code or documentation change against its requirements using diff inspection and applicable checks. Use before handoff; excludes full repository and specialized security audits.
---

# change-verifier

## Trigger
Use to verify a working-tree change, commit range or proposed patch before handoff.

## Non-triggers
Whole-repository maturity audits, vulnerability discovery, deployment execution and unrelated refactoring.

## Procedure
1. Identify the exact target, base/head or working-tree state and acceptance criteria. Record staged, unstaged and untracked paths using Git status and inspect their contents within scope. If a base is ambiguous, resolve it before claiming complete coverage.
2. Read applicable instructions and changed runtime paths plus relevant callers, schemas and tests. Map each behavior requirement to a source change and an observable check. Include documentation, install behavior and compatibility contracts when affected.
3. Select checks from the repository's actual manifests, CI or instructions. Inspect commands before execution; keep checks bounded to authorized local resources. Run relevant tests, lint/types or deterministic document checks and record exact command, exit code and result. If unavailable, state why and what remains unverified.
4. Review the complete diff for accidental files, sensitive data, broken references, scope expansion, behavior changes and recovery/rollback implications. Examine ignored/generated output names without reading credentials. A pattern scan is only a limited screen, never proof of no secrets.
5. Compare final status with the starting snapshot to detect verification side effects. Do not fix unrelated failures or stage, commit, push or deploy merely because verification passed. If a check fails, report its impact and a bounded next step; retry only when a changed condition justifies it.

## Output
Report reviewed revision/scope, requirement-to-check mapping, commands/results, concrete findings with locations, skipped checks and residual risk. Distinguish verified behavior from inference and incomplete checks.

## Verification
Every claimed pass must have an executed check and successful exit. Account for every changed path or state why it was excluded. Ensure requirements with no observable check remain explicitly unresolved.

## Limitations
Passing checks cover only exercised behavior. This skill does not establish production acceptance, approve publication or replace a requested security review. External effects require task-specific authorization.
