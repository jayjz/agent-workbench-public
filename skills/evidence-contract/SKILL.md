---
name: evidence-contract
description: Build or audit an evidence ledger for consequential claims in research, evaluations or engineering decisions. Excludes ordinary editing and unsupported requests for confidence scores.
---

# evidence-contract

## Trigger
Use when a decision or report needs traceable claims, provenance, contradictions or an explicit evidence contract.

## Non-triggers
Routine code edits, stylistic rewrites and requests that do not depend on evidence assessment.

## Procedure
1. Define the decision, scope, time horizon and claims being evaluated. Split compound claims so evidence can support or contradict each independently.
2. Inspect the raw artifacts available under the task's permissions. Record source identity (path/revision or URL), relevant location, observation and retrieval date when freshness matters. Record model/runtime, fixture identity and exact commands for evaluation claims. Never invent access to missing sources.
3. Assign each claim one state: SUPPORTED (available evidence supports this bounded claim), INFERRED (reasoned beyond observations), UNRESOLVED (insufficient evidence), or CONFLICTED (credible evidence disagrees). SUPPORTED is not proof of universal truth. Explain the inference connecting evidence to conclusion.
4. Test material alternative explanations. Check whether sources share an origin, whether a cited test actually exercises the claimed behavior, and whether missing/failed runs were excluded. An agent's summary is not independent verification of its own execution.
5. Retain contradictory and negative observations. For each unresolved claim specify the missing fact and a feasible discriminating check. Reclassify only when new evidence warrants it; preserve the prior result when it matters to interpretation.

## Output
Return a ledger with claim ID, bounded claim, state, source/location, direct observation, inference or conflict, limitations and next check. Follow it with the decision implications and checks actually performed. Link canonical sources instead of importing private material.

## Verification
Trace each material conclusion back to a ledger row. Confirm cited artifacts were inspected, quotes match sources and test results distinguish execution from expectation. Check dates and source independence. Explicitly list inaccessible evidence.

## Limitations
This is a reasoning and provenance procedure, not an enforcement mechanism, truth oracle, legal opinion or guarantee of representativeness. Do not invent numerical confidence. Do not expand research or external actions beyond the user's authorized scope.
