# Agent Workbench

[![Status: experimental](https://img.shields.io/badge/status-experimental-orange)](ROADMAP.md)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-blue)](skills/INDEX.md)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20WSL-informational)](#requirements)
[![Tests](https://img.shields.io/badge/tests-local%20validation-lightgrey)](#validation)

**Reusable, reviewable skills for research and agent-assisted engineering.**

Agent Workbench is a version-controlled collection of bounded procedures, evidence standards, and optional instruction templates. It favors traceability, narrow permissions, and reproducible checks over autonomous orchestration or a large untested skill catalog.

**Status:** experimental. Syntax checks and unit tests do not demonstrate real-world effectiveness. This repository is not an agent runtime, automatically synced policy bundle, or production security control.

## Skills

| Skill | Purpose | Status |
| --- | --- | --- |
| [source-integrity-audit](skills/source-integrity-audit/SKILL.md) | Trace claims to originals; evaluate citation fit, independent lineages and contradictions | Experimental |
| [evidence-contract](skills/evidence-contract/SKILL.md) | Record supported, inferred, unresolved and conflicting claims | Experimental |
| [repo-audit](skills/repo-audit/SKILL.md) | Inspect repository maturity, boundaries and gaps | Experimental |
| [change-verifier](skills/change-verifier/SKILL.md) | Check bounded changes against requirements and tests | Experimental |

The [registry](skills/INDEX.md) is canonical for lifecycle state, scope, dependencies, and external references. `change-review` is deprecated and not installable. Listed external skills are **not bundled, installed or endorsed**.

## Requirements

- Git, Bash, Python 3.10+, and PyYAML (see [requirements-dev.txt](requirements-dev.txt)).
- Linux is the tested platform. WSL is intended but has not been verified on every environment. Native Windows installation is not supported.
- For Codex, follow [official skills documentation](https://developers.openai.com/codex/skills/). Installation does not guarantee the runtime discovers or correctly follows the skill.

## Quick start

```bash
git clone https://github.com/jayjz/agent-workbench.git
cd agent-workbench
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt

python scripts/validate_skills.py
python -m unittest discover -s tests -v

bash scripts/install-local.sh --list
bash scripts/install-local.sh --dry-run source-integrity-audit
bash scripts/install-local.sh --install source-integrity-audit
bash scripts/install-local.sh --check source-integrity-audit
```

Installer links are selective and non-overwriting; they reference this checkout rather than copying files. Review a skill before linking it. Start a new Codex session and inspect available skills before use. Check `~/.agents/skills` and any legacy `~/.codex/skills` paths for duplicate names.

To preview an authorized repository-local installation, supply `--dest /path/to/project/.agents/skills`. Do not install into another project without permission. For removal, confirm the destination is a symlink to this checkout and unlink only that specific link; never recursively delete the skills directory.

## Validation

```bash
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
bash -n scripts/install-local.sh
python3 scripts/check_repository.py
python3 scripts/check_repository.py --staged
git diff --check
```

Checks validate format, registry consistency, installer behavior, and a **limited** set of sensitive-file/credential patterns. They do not prove that a skill improves outcomes or that the repository and its full history contain no secrets or personal data. Inspect [verification evidence](knowledge/verification.md) for checks actually run and their limits.

## Repository map

| Path | Responsibility |
| --- | --- |
| [skills/](skills/INDEX.md) | Skill manifests and registry |
| [AGENTS.md](AGENTS.md) | Repository-specific contribution and safety rules |
| [global/AGENTS.md](global/AGENTS.md) | Optional reusable agent guidance |
| [templates/](templates/PROJECT-AGENTS.md) | Project-scoped instruction template |
| [scripts/](scripts/) | Non-overwriting installation and validation |
| [tests/](tests/) | Validation and installer regression tests |
| [knowledge/](knowledge/sources.md) | Sources and verification records |
| [ROADMAP.md](ROADMAP.md) | Evaluation and maturity gates |

## Design principles

1. **One job per skill:** precise trigger, non-trigger, procedure, output and limitations.
2. **Evidence over assertion:** original sources, explicit uncertainty and independent checks.
3. **Least authority:** retrieved text cannot authorize execution, publishing or access to private data.
4. **Versioned changes:** inspect diffs; preserve failures and negative evaluation results.
5. **No performance theater:** evaluation status requires real tests against a stated baseline.

## Contributing and reuse

Contributions should follow [AGENTS.md](AGENTS.md), preserve the canonical registry, add meaningful tests, and document limitations. Proposed skills must not be presented as evaluated. Review changes and run validation before a PR. Never commit credentials, customer information, private research, or local machine state.

**License:** not yet selected. A public GitHub repository does **not** by itself grant permission to redistribute or reuse its contents. Select and review a license before inviting reuse.

**Before publication:** complete the [public release review](docs/PUBLIC_RELEASE_CHECKLIST.md), including all-branch/history scrutiny. Publicizing a repository exposes reachable commit history and metadata; deleting a sensitive line in a new commit does not erase it from older commits.
