---
name: repo-audit
description: Assess repository maturity and implementation gaps when asked to audit or onboard to a codebase. Excludes vulnerability hunting and reviews limited to a diff.
---

# repo-audit

## Trigger
Use for a repository health assessment, architecture inventory, or readiness review with prioritized gaps.

## Non-triggers
A single bug fix, diff review, penetration test, or request to certify security. Do not start a specialized security scan implicitly.

## Procedure
1. Establish target, revision, requested depth, and decision the audit should inform. Read applicable instructions, Git status and recent history. Inventory tracked files, manifests, tests, CI and deployment documentation; exclude credentials and generated directories.
2. Trace one representative entry point through its implementation, persistence and external effects. Record file/line evidence for architecture and authorization boundaries. Distinguish documentation claims from observed code.
3. Assess each applicable area: setup reproducibility, architecture, test coverage of critical behavior, dependency handling, authorization/data handling, CI, deployment/rollback and operational diagnostics. Mark absent evidence as unknown; do not infer that an undocumented control is absent.
4. Inspect available verification commands before running them. Run only bounded checks within authorized resources; do not install dependencies, execute untrusted build hooks or contact live services without the needed authorization. Record command, environment, exit code and observed result. Leave the target unchanged except authorized disposable check outputs.
5. Prioritize actionable gaps by concrete consequence and evidence. Separate defects, hardening suggestions and questions. Stop at the agreed scope; recommend deeper investigation where source inspection cannot settle a claim.

## Output
Report target/revision, scope, architecture trace, assessment table (area, observation, evidence, consequence), prioritized next actions, commands/results and skipped checks. Give the evidence state for material conclusions: SUPPORTED, INFERRED, UNRESOLVED or CONFLICTED.

## Verification
Every material finding must identify a reproducible observation or source location, its practical consequence and the smallest next check or remedy. Reconcile the report with actual command exits and the final Git status. Do not report maturity scores without an agreed rubric.

## Limitations
Static inspection and passing tests cannot establish production reliability or security. No exploit execution, production changes, commits, publishing or exhaustive security review is authorized by this skill.
