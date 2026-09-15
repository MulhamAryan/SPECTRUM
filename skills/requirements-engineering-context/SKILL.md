---
name: requirements-engineering-context
description: Vérifier que le périmètre d'analyse couvre les activités de Requirements Engineering pertinentes et le contexte de gestion dans le temps lorsqu'applicable.
type: component
role: cross_cutting
---

# Requirements Engineering Context

## Responsibility

Identifier les activités de Requirements Engineering pertinentes au ticket et les éventuelles lacunes de gestion du cycle de vie.

## Trigger

Utiliser lorsqu'il faut vérifier la couverture des activités RE pertinentes ou le contexte de gestion dans le temps.

## Inputs

Required: `ticket`, `available_context`
Optional: `workflow_state`, `requirement_history`

## Preconditions

- Le ticket est disponible.

## Operations

- Évaluer les activités RE pertinentes.
- Examiner le contexte de gestion lorsqu'applicable.
- Signaler les lacunes de couverture.

## Rules

- `ISO29148-R010`
- `ISO29148-R011`

## Outputs

- `re_context_assessment`
- `findings`

## Findings

- `requirements_engineering_coverage_gap`
- `requirements_management_context_gap`

## Evidence

Conserver le contexte qui justifie chaque activité jugée pertinente.

## Handoff

Fournit l'évaluation de couverture au workflow.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals

- Ne pas imposer toutes les activités à tous les tickets.
- Ne pas imposer un cycle de vie unique.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôles : `ISO29148-R010`, `ISO29148-R011`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `missing_context`, `not_applicable`, `regression`.
