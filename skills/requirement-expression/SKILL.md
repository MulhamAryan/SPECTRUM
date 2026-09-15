---
name: requirement-expression
description: Examiner la formulation d'une exigence pour sa spécificité, sa précision et son absence d'ambiguïté.
type: component
role: quality_analysis
---

# Requirement Expression

## Responsibility

Examiner l'expression d'une exigence et signaler les formulations qui ne sont pas suffisamment spécifiques, précises ou non ambiguës pour être interprétées de manière stable.

## Trigger

Utiliser lorsqu'un ticket ou une exigence contient une formulation normative à analyser.

## Inputs

Required: `requirement`
Optional: `requirement_context`, `available_context`, `prior_findings`

## Preconditions

- L'expression de l'exigence est disponible.

## Operations

- Évaluer la spécificité.
- Évaluer la précision.
- Détecter les ambiguïtés ou interprétations concurrentes.
- Produire les constats d'analyse.

## Rules

- `ISO29148-R003`

## Outputs

- `requirement_expression_observation`
- `findings`

## Findings

- `requirement_expression_unclear`

## Evidence

Conserver la référence vers le texte de l'exigence et vers le contexte utilisé pour l'interprétation.

## Handoff

Fournit ses observations au Skill de vérification et au workflow.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals

- Ne pas imposer une réécriture automatique.
- Ne pas inventer le contenu métier attendu.
- Ne pas décider de readiness.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôle : `ISO29148-R003`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `missing_context`, `contradictory_context`, `insufficient_evidence`, `regression`.
