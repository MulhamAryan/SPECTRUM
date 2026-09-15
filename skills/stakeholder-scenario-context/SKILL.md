---
name: stakeholder-scenario-context
description: Établir les parties prenantes et les scénarios opérationnels pertinents à partir des sources autorisées.
type: component
role: contextualization
---

# Stakeholder & Scenario Context

## Responsibility

Établir les parties prenantes et scénarios opérationnels pertinents à partir des sources autorisées et signaler les contextes manquants.

## Trigger

Utiliser lorsque l'interprétation d'une exigence dépend des acteurs, parties prenantes, utilisateurs ou scénarios opérationnels pertinents.

## Inputs

Required: `ticket`, `available_context`
Optional: `repository_evidence`, `prior_findings`

## Preconditions

- Le contexte disponible est accessible.

## Operations

- Identifier les parties prenantes pertinentes.
- Déterminer si un scénario opérationnel est nécessaire.
- Détecter les contextes manquants.

## Rules

- `ISO29148-R012`
- `ISO29148-R014`

## Outputs

- `stakeholder_context`
- `scenario_context`
- `findings`

## Findings

- `stakeholder_context_gap`
- `operational_scenario_context_gap`

## Evidence

Toute partie prenante ou tout scénario utilisé comme fait doit être relié à une source autorisée.

## Handoff

Fournit le contexte au Skill de validation et au workflow.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals

- Ne pas déduire un rôle à partir d'un nom seul.
- Ne pas inventer un scénario.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôles : `ISO29148-R012`, `ISO29148-R014`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `missing_context`, `not_applicable`, `regression`.
