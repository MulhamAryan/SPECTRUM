---
name: elicitation-gap
description: Détecter les informations nécessaires à l'analyse qui ne sont pas établies dans les sources disponibles et formuler un gap exploitable.
type: component
role: contextualization
---

# Elicitation Gap

## Responsibility

Identifier les lacunes qui nécessitent clarification, élicitation ou collecte supplémentaire sans fabriquer le contenu manquant.

## Trigger

Utiliser lorsqu'une analyse dépend d'un besoin ou d'une information qui n'est pas établi dans les sources actuellement disponibles.

## Inputs

Required: `requirement_context`, `available_sources`
Optional: `prior_findings`

## Preconditions

- Le contexte de l'exigence est disponible.

## Operations

- Détecter les informations nécessaires non établies.
- Classifier le gap.
- Formuler le suivi nécessaire.

## Rules

- `ISO29148-R007`

## Outputs

- `elicitation_gap`
- `findings`

## Findings

- `elicitation_gap`

## Evidence

Conserver les références de sources utilisées pour établir qu'une information est absente ou insuffisamment établie.

## Handoff

Transmet un gap structuré au workflow et conserve les références de provenance.

## Exit conditions

- `completed`
- `not_applicable`
- `blocked_on_missing_context`

## Non-goals

- Ne pas réaliser l'élicitation elle-même.
- Ne pas remplir le gap par inférence.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôle : `ISO29148-R007`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `missing_context`, `evidence_insufficient`, `regression`.
