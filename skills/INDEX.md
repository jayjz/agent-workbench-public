# Skills registry

Search by name, trigger, runtime or related repository. Each JSON block is one canonical registry record, read by the validator and installer. Local sources resolve relative to this index; external sources are links only. `last_verified: null` means no recorded successful verification date. Mechanical verification does not establish behavioral effectiveness. External `UNRESOLVED` is an unknown lifecycle, not a local promotion state.

## source-integrity-audit

```json
{
  "name": "source-integrity-audit",
  "job_trigger": "Audit research citations for claim fit, independent provenance, primary sources, AI-generated or circular sourcing and counterevidence. Excludes style-only editing.",
  "source": "source-integrity-audit/SKILL.md",
  "ownership": "local",
  "state": "EXPERIMENTAL",
  "dependencies": [
    "Readable cited sources; research tools where authorized"
  ],
  "runtimes": [
    "Codex CLI/IDE (instruction compatible; live invocation untested)"
  ],
  "validation": "Not yet mechanically or behaviorally evaluated; see ../knowledge/verification.md",
  "last_verified": null,
  "related_repositories": [
    "jayjz/biblemap",
    "jayjz/black-lantern"
  ],
  "limitations": "No live discovery, mechanical validation or controlled behavioral evaluation yet; cannot reliably detect undisclosed AI authorship."
}
```

## repo-audit

```json
{
  "name": "repo-audit",
  "job_trigger": "Assess repository maturity and implementation gaps when asked to audit or onboard to a codebase. Excludes vulnerability hunting and reviews limited to a diff.",
  "source": "repo-audit/SKILL.md",
  "ownership": "local",
  "state": "EXPERIMENTAL",
  "dependencies": [
    "Git and repository check tools"
  ],
  "runtimes": [
    "Codex CLI/IDE (instruction compatible; live invocation untested)"
  ],
  "validation": "Mechanical checks only; see ../knowledge/verification.md",
  "last_verified": "2026-10-26",
  "related_repositories": [
    "jayjz/shopclose",
    "jayjz/black-lantern"
  ],
  "limitations": "No controlled behavioral evaluation or performance claim."
}
```

## evidence-contract

```json
{
  "name": "evidence-contract",
  "job_trigger": "Build or audit an evidence ledger for consequential claims in research, evaluations or engineering decisions. Excludes ordinary editing and unsupported requests for confidence scores.",
  "source": "evidence-contract/SKILL.md",
  "ownership": "local",
  "state": "EXPERIMENTAL",
  "dependencies": [
    "Readable source artifacts"
  ],
  "runtimes": [
    "Codex CLI/IDE (instruction compatible; live invocation untested)"
  ],
  "validation": "Mechanical checks only; see ../knowledge/verification.md",
  "last_verified": "2026-10-26",
  "related_repositories": [
    "jayjz/evidence-strategy-skills"
  ],
  "limitations": "No controlled behavioral evaluation or performance claim."
}
```

## change-verifier

```json
{
  "name": "change-verifier",
  "job_trigger": "Verify a bounded code or documentation change against its requirements using diff inspection and applicable checks. Use before handoff; excludes full repository and specialized security audits.",
  "source": "change-verifier/SKILL.md",
  "ownership": "local",
  "state": "EXPERIMENTAL",
  "dependencies": [
    "Git and repository check tools"
  ],
  "runtimes": [
    "Codex CLI/IDE (instruction compatible; live invocation untested)"
  ],
  "validation": "Mechanical checks only; see ../knowledge/verification.md",
  "last_verified": "2026-10-26",
  "related_repositories": [
    "jayjz/shopclose",
    "jayjz/black-lantern"
  ],
  "limitations": "No controlled behavioral evaluation or performance claim."
}
```

## change-review

```json
{
  "name": "change-review",
  "job_trigger": "Legacy diff review; prefer change-verifier.",
  "source": "change-review/SKILL.md",
  "ownership": "local",
  "state": "DEPRECATED",
  "dependencies": [
    "Git"
  ],
  "runtimes": [
    "Codex (untested)"
  ],
  "validation": "Mechanical checks only",
  "last_verified": "2026-10-26",
  "related_repositories": [],
  "limitations": "Preserved original generic procedure; overlaps change-verifier. Not installable."
}
```

## security-audit

```json
{
  "name": "security-audit",
  "job_trigger": "Specialized vulnerability audit; inspect upstream before invoking.",
  "source": "https://github.com/jayjz/security-audit-skill",
  "ownership": "external",
  "state": "UNRESOLVED",
  "dependencies": [
    "Tool-capable agent with parallel agents",
    "Node.js",
    "OS-enforced sandbox; see upstream README"
  ],
  "runtimes": [
    "Upstream coding-agent claim; not verified here"
  ],
  "validation": "README inspected 2026-10-26; root SKILL.md retrieval returned 404",
  "last_verified": null,
  "related_repositories": [
    "jayjz/security-audit-skill"
  ],
  "limitations": "Exact manifest location and current upstream/fork relationship unresolved; never installed by this registry."
}
```

## market-sentiment-research

```json
{
  "name": "market-sentiment-research",
  "job_trigger": "Proposed business strategy workflow; not executable here.",
  "source": "https://github.com/jayjz/evidence-strategy-skills/tree/main/skills/market-sentiment-research",
  "ownership": "external",
  "state": "PROPOSED",
  "dependencies": [
    "Not established"
  ],
  "runtimes": [
    "Not established"
  ],
  "validation": "README identifies placeholder directories; manifests not verified",
  "last_verified": null,
  "related_repositories": [
    "jayjz/evidence-strategy-skills"
  ],
  "limitations": "No implementation or evaluation inferred from README aspirations."
}
```

## customer-job-discovery

```json
{
  "name": "customer-job-discovery",
  "job_trigger": "Proposed business strategy workflow; not executable here.",
  "source": "https://github.com/jayjz/evidence-strategy-skills/tree/main/skills/customer-job-discovery",
  "ownership": "external",
  "state": "PROPOSED",
  "dependencies": [
    "Not established"
  ],
  "runtimes": [
    "Not established"
  ],
  "validation": "README identifies placeholder directories; manifests not verified",
  "last_verified": null,
  "related_repositories": [
    "jayjz/evidence-strategy-skills"
  ],
  "limitations": "No implementation or evaluation inferred from README aspirations."
}
```

## market-entry

```json
{
  "name": "market-entry",
  "job_trigger": "Proposed business strategy workflow; not executable here.",
  "source": "https://github.com/jayjz/evidence-strategy-skills/tree/main/skills/market-entry",
  "ownership": "external",
  "state": "PROPOSED",
  "dependencies": [
    "Not established"
  ],
  "runtimes": [
    "Not established"
  ],
  "validation": "README identifies placeholder directories; manifests not verified",
  "last_verified": null,
  "related_repositories": [
    "jayjz/evidence-strategy-skills"
  ],
  "limitations": "No implementation or evaluation inferred from README aspirations."
}
```

## strategy-red-team

```json
{
  "name": "strategy-red-team",
  "job_trigger": "Proposed business strategy workflow; not executable here.",
  "source": "https://github.com/jayjz/evidence-strategy-skills/tree/main/skills/strategy-red-team",
  "ownership": "external",
  "state": "PROPOSED",
  "dependencies": [
    "Not established"
  ],
  "runtimes": [
    "Not established"
  ],
  "validation": "README identifies placeholder directories; manifests not verified",
  "last_verified": null,
  "related_repositories": [
    "jayjz/evidence-strategy-skills"
  ],
  "limitations": "No implementation or evaluation inferred from README aspirations."
}
```
