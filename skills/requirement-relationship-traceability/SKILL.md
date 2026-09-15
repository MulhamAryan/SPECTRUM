---
name: requirement-relationship-traceability
description: Analyser les relations de dérivation, d'allocation et de traçabilité disponibles entre exigences et niveaux associés.
type: component
role: relationship_traceability
---

# Requirement Relationship & Traceability

## Responsibility

Examiner les relations de dérivation et de traçabilité disponibles et signaler les liens manquants ou non établis.

## Trigger

Utiliser lorsqu'une exigence est dérivée, allouée, liée à un niveau supérieur ou inférieur, ou accompagnée d'une matrice ou autre trace.

## Inputs

Required: `requirements`, `available_traceability`
Optional: `ticket`, `repository_evidence`, `related_artifacts`

## Preconditions

- Des exigences ou relations à analyser sont disponibles.

## Operations

- Inspecter les relations de derived requirement.
- Inspecter les chemins de traçabilité.
- Inspecter une matrice lorsqu'elle existe.
- Signaler les orphelins ou liens manquants.

## Rules

- `ISO29148-R004`
- `ISO29148-R005`
- `ISO29148-R006`

## Outputs

- `relationship_records`
- `traceability_findings`

## Findings

- `derived_requirement_relationship_missing`
- `traceability_relationship_missing`
- `incomplete_traceability_artifact`

## Evidence

Pour chaque relation signalée, conserver les références vers la source et la cible.

## Handoff

Fournit les relations aux Skills de vérification, validation et au workflow.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals

- Ne pas créer artificiellement un parent.
- Ne pas imposer universellement une matrice de traçabilité.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôles : `ISO29148-R004`, `ISO29148-R005`, `ISO29148-R006`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `missing_context`, `contradictory_context`, `regression`.
