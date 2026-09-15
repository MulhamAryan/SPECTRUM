---
name: conformance-governance
description: Contrôler les affirmations de conformité à ISO 29148 en vérifiant leur périmètre, leur mode et leurs preuves.
type: component
role: governance
---

# Conformance Governance

## Responsibility

Vérifier que toute affirmation de conformité possède un périmètre, un mode de conformité et des éléments de preuve explicitement établis.

## Trigger

Utiliser lorsqu'un résultat, une documentation ou une communication affirme une conformité à ISO/IEC/IEEE 29148.

## Inputs

Required: `conformance_claim`, `assessment_evidence`
Optional: `implemented_controls`

## Preconditions

- Une affirmation de conformité est présente.

## Operations

- Identifier le périmètre de l'affirmation.
- Identifier le mode de conformité revendiqué.
- Examiner les preuves d'évaluation associées.

## Rules

- `ISO29148-R017`

## Outputs

- `conformance_observation`
- `findings`

## Findings

- `unsupported_conformance_claim`

## Evidence

La revendication doit être reliée à son périmètre d'évaluation et aux preuves correspondantes.

## Handoff

Valide ou invalide le support d'une revendication de conformité ; il ne transforme pas les contrôles sélectionnés en conformité formelle.

## Exit conditions

- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals

- Ne pas déclarer une conformité formelle par simple présence de contrôles sélectionnés.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôle : `ISO29148-R017`
- Source : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation

Couvrir : `nominal`, `evidence_insufficient`, `not_applicable`, `regression`.
