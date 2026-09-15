---
name: validation-analysis
description: Examiner la base permettant d'établir que les exigences correspondent au bon système et à l'utilisation prévue.
type: component
role: validation
---

# Validation Analysis

## Responsibility

Examiner la base disponible permettant de juger que l'exigence correspond au bon système et à l'usage prévu.

## Trigger

Utiliser lorsqu'une validation est revendiquée ou lorsque l'adéquation au système et à l'utilisation prévue doit être établie.

## Inputs

Required: `requirements`, `system_context`, `usage_context`
Optional: `stakeholder_context`, `scenario_context`, `evidence`

## Preconditions

- Une revendication ou un besoin de validation est identifié.

## Operations

- Identifier la base de validation.
- Examiner l'adéquation système / usage.
- Évaluer les éléments de preuve disponibles.

## Rules

- `ISO29148-R008`

## Outputs

- `validation_observations`
- `findings`

## Findings

- `validation_basis_unavailable`

## Evidence

Conserver les références du contexte système, de l'usage et des preuves utilisées.

## Handoff

Transmet ses observations au workflow.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`
- `blocked_on_missing_context`

## Non-goals

- Ne pas confondre validation avec le simple contrôle de formulation.
- Ne pas déclarer une validation sans base établie.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôle : `ISO29148-R008`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `missing_context`, `evidence_insufficient`, `regression`.
