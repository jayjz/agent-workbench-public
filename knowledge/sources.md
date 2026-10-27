# Sources and discovery

Retrieved/inspected 2026-10-26. A README observation establishes what a repository documents, not that its implementation or tests meet that claim.

## Local discovery (SUPPORTED)

The original repository had no commits or remote and eleven untracked scaffold files. All were inspected and preserved in the initial feature-branch commit before modifications. Three manifests (repo-audit, evidence-contract, change-review) had identical generic procedures. The installer copied global instructions and installed every skill into the legacy ~/.codex/skills location. No validator or tests existed. Hidden runtime directories and an empty projects directory were present; no credentials were read.

Local ShopClose README, AGENTS.md and three manifests under `.agents/skills/` were read without modification: hvac-fsm-integrator, commercial-strategy-auditor and deterministic-control-plane. They are project-owned, not installed or copied here. Their invocation ranges are broad. The control-plane manifest prescribes a universal ledger/state machine and contains unverified runtime/provider assumptions; the commercial manifest assumes zero marginal local-GPU cost. These need review before generic reuse. ShopClose's own approval boundaries remain authoritative.

## Official sources (SUPPORTED documentation)

- [Build skills](https://learn.chatgpt.com/docs/build-skills), reached from `https://developers.openai.com/codex/skills/`: required name/description front matter; `.agents/skills` user/repository discovery; symlink support. Used to choose installer paths. Live discovery on this machine remains UNRESOLVED.
- Installed system skill-creator SKILL.md: read locally for scope, progressive disclosure and mechanical validation. Instruction-only procedures were sufficient; no optional UI scaffolding was needed.

## Remote discovery

The GitHub connector fetched all six default-branch READMEs. File blob identities below make the inspected content identifiable; default branches may subsequently change. No target code or tests were executed.

| Canonical source | README blob | Observation and limits |
| --- | --- | --- |
| [evidence-strategy-skills](https://github.com/jayjz/evidence-strategy-skills) | `2a8b346d39545b06a01a9cac4d8c91697ee7e040` | Foundation/methodology stage; four named skills explicitly placeholders. Evaluation claims not independently established. |
| [black-lantern](https://github.com/jayjz/black-lantern) | `bcdd845703ce9c9414086e25388f9b025547b39d` | Documents synthetic authorization experiments and inconclusive comparisons. README also mentions an open PR alongside historical main status; merge state and results not independently verified. |
| [shopclose](https://github.com/jayjz/shopclose) | `d14a47f016187a041f1f9a2cbf88a1a83fad834f` | Documents bootstrap and human invoice review boundaries, no production integrations. Local manifests observed separately. |
| [biblemap](https://github.com/jayjz/biblemap) | `0c4a51fe1d4f11bb48b24880f78106fbb8f4bb9b` | Documents Next.js reading preview, provenance/editorial gates; no reusable manifest verified. |
| [automated_social](https://github.com/jayjz/automated_social) | `a409c1290fb8f89e691e6600c174dccffd67972d` | Documents local generation and revision-bound approval; publishing disabled. Private voice/archive files not accessed. |
| [security-audit-skill fork](https://github.com/jayjz/security-audit-skill) | `c80305c88cd5087db37f76a0d230c1fc092c864c` | README describes Node validators, isolated agents and sandbox requirements, and points installation at Cloudflare upstream. Root SKILL.md request returned 404. Exact manifest path and fork/upstream relationship remain UNRESOLVED. |

A broad repository metadata search was accessible but does not establish implementations. No external skills were copied. The registry differentiates executable local procedures from external proposals and unresolved source pointers.

## Private-source handling

Private workspace pointers and unpublished personal research are intentionally excluded from this public-facing source index. External evidence should be linked only when sharing is authorized.
