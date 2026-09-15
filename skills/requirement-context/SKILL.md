---
name: requirement-context
description: Établir l'item d'intérêt, le contexte de l'exigence, les contraintes, conditions, états et le niveau de spécification lorsque pertinent.
type: component
role: requirement_analysis
---

# Requirement Context

## Responsibility

Établir ce qui est explicitement identifiable dans l'exigence et son contexte immédiat avant toute conclusion de qualité ou de readiness.

## Trigger

Utiliser lorsqu'un ticket ou une exigence doit être interprété par rapport à son sujet, son niveau, son besoin, ses contraintes, ses conditions ou ses états.

## Inputs

Required: `ticket`, `available_context`
Optional: `prior_findings`, `prior_decisions`

## Preconditions

- Le ticket ou l'exigence est disponible.

## Operations

- Identifier l'item d'intérêt.
- Identifier le contexte de l'exigence.
- Distinguer besoin, contrainte, condition et état lorsqu'applicable.
- Déterminer le niveau de spécification lorsqu'il est pertinent.

## Rules

- `ISO29148-R001`
- `ISO29148-R002`
- `ISO29148-R013`
- `ISO29148-R015`

## Outputs

- `requirement_context`
- `requirement_level_observation`
- `findings`

## Findings

- `missing_item_of_interest`
- `requirement_context_incomplete`
- `condition_constraint_state_unclear`
- `requirement_level_unclear`

## Evidence

Chaque affirmation factuelle doit pointer vers une source ou être marquée comme information non établie.

## Handoff

Fournit le contexte aux Skills d'élicitation, d'expression et de relations. Il ne rend aucune décision finale de readiness.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals

- Ne pas inventer un item d'intérêt.
- Ne pas produire `READY`, `READY WITH INVESTIGATION` ou `NOT READY/BLOCKED`.
- Ne pas faire une déclaration formelle de conformité.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôles : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`
- Sections principalement utilisées : `3.1.19`, `3.1.6`, `3.1.7`, `3.1.30`, `3.1.29`, `3.1.33`

## Evaluation

Couvrir au minimum : `nominal`, `missing_context`, `not_applicable`, `regression`.
