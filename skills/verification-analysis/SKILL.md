---
name: verification-analysis
description: Examiner ce qui doit être vérifié et si une preuve objective pertinente est disponible.
type: component
role: verification
---

# Verification Analysis

## Responsibility

Examiner ce qui doit être vérifié et si une preuve objective pertinente est disponible.

## Trigger

Utiliser lorsqu'une exigence, un ticket ou une preuve contient ou implique une affirmation de vérification.

## Inputs

Required: `requirements`, `available_evidence`
Optional: `tests`, `repository_evidence`

## Preconditions

- Une revendication ou un besoin de vérification est identifié.

## Operations

- Identifier la cible de vérification.
- Examiner la preuve objective disponible.
- Évaluer la suffisance de la preuve.

## Rules

- `ISO29148-R009`

## Outputs

- `verification_observations`
- `findings`

## Findings

- `verification_basis_unavailable`

## Evidence

Toute affirmation de vérification doit pointer vers les éléments objectifs utilisés.

## Handoff

Transmet ses observations et evidence au workflow.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`
- `blocked_on_missing_context`

## Non-goals

- Ne pas déclarer un succès sans preuve.
- Ne pas exécuter automatiquement un test qui n'est pas requis.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôle : `ISO29148-R009`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `evidence_insufficient`, `missing_context`, `regression`.
