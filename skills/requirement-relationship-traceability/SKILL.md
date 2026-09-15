---
name: requirement-relationship-traceability
description: Analyser les relations de dérivation, d'allocation et de traçabilité disponibles entre exigences et niveaux associés.
type: component
role: relationship_traceability
---

# Requirement Relationship & Traceability

## Purpose
Établir quelles relations entre exigences existent, lesquelles sont démontrées et lesquelles sont manquantes lorsqu'une relation est attendue ou utile.

## When to use
Activer lorsque des exigences sont dérivées, allouées, liées à un niveau supérieur ou inférieur, ou lorsqu'un artefact de traçabilité existe.

## Inputs
Required: `requirements`, `available_traceability`
Optional: `ticket`, `repository_evidence`, `related_artifacts`

## Preconditions
- Au moins une exigence ou relation candidate est disponible.

## Procedure
1. Identifier les exigences source et cible impliquées.
2. Rechercher les relations explicites de dérivation, allocation ou traçabilité.
3. Vérifier que chaque relation relie réellement deux objets existants.
4. Rechercher les exigences orphelines lorsque leur niveau supérieur ou inférieur est pertinent.
5. Inspecter les matrices ou registres de traçabilité lorsqu'ils existent.
6. Vérifier la cohérence directionnelle des liens.
7. Distinguer l'absence d'un artefact de traçabilité de l'absence d'une relation réellement requise.
8. Signaler les liens non établis, incohérents ou incomplets.
9. Conserver source, cible, relation et evidence pour chaque observation.

## Analysis logic
La traçabilité est un résultat de relations établies ; une simple proximité de texte ne constitue pas un lien. Une matrice n'est pas rendue universellement obligatoire si aucune source ou politique applicable ne l'exige.

## Decision rules
- `trace_established`: source, cible et nature du lien sont établies.
- `trace_missing`: relation attendue mais non établie.
- `trace_incomplete`: artefact existe mais ne couvre pas le périmètre nécessaire.
- `trace_contradictory`: différents artefacts donnent des liens incompatibles.

## Rules
- `ISO29148-R004`
- `ISO29148-R005`
- `ISO29148-R006`

## Output
`relationship_records` avec `from_ref`, `to_ref`, `relation`, `direction`, `status`, `evidence_refs` et `traceability_scope`.

## Findings
- `derived_requirement_relationship_missing`
- `traceability_relationship_missing`
- `incomplete_traceability_artifact`
- `contradictory_traceability`

## Evidence
Conserver les références de la source et de la cible pour chaque relation et l'artefact de traçabilité lorsqu'il est utilisé.

## Handoff
Vers `verification-analysis`, `validation-analysis` et le workflow.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals
Ne pas créer artificiellement un parent ou une relation ; ne pas imposer une matrice dans tous les cas.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R004`, `R005`, `R006`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : chaîne de traçabilité complète, relation manquante, matrice absente mais non requise, matrice incomplète, contradiction, régression.