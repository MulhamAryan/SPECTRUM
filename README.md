# SPECTRUM

SPECTRUM is a requirements engineering and developer-readiness plugin for AI coding agents.

The project is designed to use established requirements-engineering references and keep the following concerns separate:

- reference knowledge
- executable rules
- skills and workflows
- agents
- data models
- evidence and traceability
- decision logic
- outputs
- evaluation
- governance and provenance
- project policies

The first reference set to be mapped is ISO/IEC/IEEE 29148:2018, followed by INCOSE guidance and implementation references such as VNVSpec.

## Repository structure

- `core/` — SPECTRUM core runtime and orchestration foundations
- `knowledge/` — reference knowledge
- `rules/` — executable rules and checks
- `skills/` — reusable agent skills
- `workflows/` — analysis workflows
- `agents/` — specialized agent definitions
- `models/` — shared data models
- `evidence/` — evidence and traceability structures
- `decisions/` — decision logic
- `outputs/` — generated artifacts and output definitions
- `evaluation/` — evaluation and test assets
- `governance/` — provenance, versions, and source governance
- `policies/` — configurable project or organizational policies

## Agent integrations

SPECTRUM is intended to remain as model- and agent-agnostic as practical. Platform-specific packaging is kept separate from the core methodology.

- Claude Code: `.claude-plugin/`
- Agent Skills interoperability: `.agents/`
- Gemini CLI: `gemini-extension.json` and `.gemini/`
