---
name: validation-analysis
description: Examiner la base permettant d'établir que les exigences correspondent au bon système et à l'utilisation prévue.
type: component
role: validation
---

# Validation Analysis

## Purpose
Examiner si l'exigence exprime ce que le bon système doit fournir pour l'utilisation et les parties prenantes prévues.

## When to use
Activer lorsque l'adéquation au système, au besoin, à l'usage ou à l'objectif opérationnel doit être établie.

## Inputs
Required: `requirements`, `system_context`, `usage_context`
Optional: `stakeholder_context`, `scenario_context`, `evidence`

## Preconditions
- Le besoin de validation est identifié.
- Le système ou l'usage de référence est au moins partiellement accessible.

## Procedure
1. Identifier le système et le périmètre auxquels l'exigence se rapporte.
2. Identifier l'utilisation prévue et les objectifs pertinents.
3. Relier les besoins/attentes des parties prenantes disponibles à l'exigence.
4. Examiner les scénarios ou contextes opérationnels pertinents.
5. Rechercher les contradictions entre exigence, système, usage et besoins établis.
6. Déterminer la base de validation disponible : source métier, scénario, besoin, décision ou autre evidence pertinente.
7. Évaluer si cette base est suffisante pour soutenir l'affirmation d'adéquation.
8. Produire les findings lorsqu'une base manque, est contradictoire ou ne couvre pas l'affirmation.

## Analysis logic
Validation répond à "construisons-nous le bon système / la bonne attente ?" et non simplement "pouvons-nous tester la formulation ?". L'absence d'un artefact nommé "validation" n'est pas à elle seule un échec si une base équivalente est établie.

## Decision rules
- `validation_supported`: adéquation soutenue par des sources et un contexte cohérents.
- `validation_partial`: éléments de contexte disponibles mais incomplets.
- `validation_basis_unavailable`: aucune base suffisante pour l'affirmation.
- `validation_contradicted`: exigence et contexte métier/systeme incompatibles.

## Rules
- `ISO29148-R008`

## Output
`validation_observations` contient `requirement_ref`, `system_context`, `usage_context`, `stakeholder_refs`, `scenario_refs`, `basis_evidence_refs`, `status`, `gaps`.

## Findings
- `validation_basis_unavailable`
- `validation_context_incomplete`
- `validation_contradiction`

## Evidence
Référencer les besoins, scénarios, parties prenantes, documents métier ou autres artefacts utilisés pour établir l'adéquation.

## Handoff
Vers le workflow et la décision externe.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`
- `blocked_on_missing_context`

## Non-goals
Ne pas confondre validation avec qualité syntaxique ; ne pas inventer l'objectif métier ; ne pas déclarer une validation formelle sans base suffisante.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R008`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : contexte complet, usage absent, acteur absent, contradiction métier, preuve partielle, régression.