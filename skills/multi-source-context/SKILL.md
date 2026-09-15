---
name: multi-source-context
description: Rechercher le contexte pertinent dans les sources autorisées avant de conclure qu'une information manque, en conservant la provenance.
type: component
role: cross_cutting
---

# Multi-Source Context

## Responsibility

Rechercher et réunir le contexte autorisé avant de conclure qu'une information manque, tout en conservant la provenance des sources.

## Trigger

Utiliser lorsqu'une conclusion sur le ticket dépend d'informations absentes du ticket mais potentiellement présentes dans des sources autorisées.

## Inputs

Required: `ticket`, `authorized_sources`
Optional: `repository`, `documentation`, `related_tickets`, `tests`

## Preconditions

- Les sources autorisées sont connues.

## Operations

- Énumérer les sources autorisées.
- Rechercher le contexte pertinent.
- Enregistrer la provenance.
- Distinguer information trouvée et information réellement manquante.

## Rules

- `ISO29148-R016`

## Outputs

- `context_package`
- `provenance_records`
- `findings`

## Findings

- `context_not_sufficiently_established`

## Evidence

Pour chaque information importée, conserver la source et sa localisation.

## Handoff

Fournit le contexte aux Skills qui en dépendent.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `blocked_on_missing_context`

## Non-goals

- Ne pas accéder à une source non autorisée.
- Ne pas transformer une inférence en fait.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôle : `ISO29148-R016`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `missing_context`, `contradictory_context`, `regression`.
