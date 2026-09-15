---
name: verification-analysis
description: Examiner ce qui doit être vérifié et si une preuve objective pertinente est disponible.
type: component
role: verification
---

# Verification Analysis

## Purpose
Déterminer si une exigence possède une base de vérification objectivement exploitable et si les preuves disponibles soutiennent les affirmations de vérification.

## When to use
Activer lorsqu'une exigence doit pouvoir être vérifiée, lorsqu'un test/preuve est cité ou lorsqu'une validation de conformité dépend d'une preuve objective.

## Inputs
Required: `requirements`, `available_evidence`
Optional: `tests`, `repository_evidence`

## Preconditions
- Une ou plusieurs exigences sont identifiées.

## Procedure
1. Identifier la cible exacte de chaque vérification.
2. Déterminer les propriétés, comportements, seuils ou conditions observables à vérifier.
3. Rechercher tests, résultats, mesures, rapports, logs ou autres preuves objectives disponibles.
4. Vérifier l'association entre preuve et exigence.
5. Vérifier que la preuve correspond à la version/contexte pertinent lorsqu'une telle information existe.
6. Évaluer la couverture : complète, partielle ou inexistante.
7. Vérifier que la preuve mesure réellement l'attribut attendu et ne constitue pas une simple affirmation.
8. Produire les findings et leurs evidence refs.

## Analysis logic
Une preuve est objective si un tiers peut l'examiner ou la reproduire à partir d'un artefact identifiable. Une phrase disant "testé" sans artefact n'est pas une preuve suffisante.

## Decision rules
- `verifiable`: cible et méthode observables, preuve suffisante ou vérification clairement dérivable.
- `partially_verifiable`: une partie seulement est vérifiable.
- `verification_basis_unavailable`: aucune base objective suffisante.
- `evidence_mismatch`: preuve existante mais ne correspondant pas à la cible.

## Rules
- `ISO29148-R009`

## Output
`verification_observations` contient `requirement_ref`, `verification_target`, `evidence_refs`, `coverage`, `evidence_quality`, `status` et `missing_evidence`.

## Findings
- `verification_basis_unavailable`
- `verification_evidence_insufficient`
- `verification_evidence_mismatch`
- `verification_partial_coverage`

## Evidence
Chaque observation doit référencer les tests ou artefacts utilisés et signaler explicitement les éléments non disponibles.

## Handoff
Vers le workflow ; les résultats alimentent la décision externe et peuvent être enrichis par `requirement-expression` et `requirement-relationship-traceability`.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`
- `blocked_on_missing_context`

## Non-goals
Ne pas déclarer un succès sans preuve ; ne pas inventer de résultat de test ; ne pas exécuter un test non demandé ou non autorisé.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R009`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : preuve suffisante, aucune preuve, preuve partielle, preuve non liée, test obsolète, régression.