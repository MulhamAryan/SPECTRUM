---
name: conformance-governance
description: Contrôler les affirmations de conformité à ISO 29148 en vérifiant leur périmètre, leur mode et leurs preuves.
type: component
role: governance
---

# Conformance Governance

## Purpose
Empêcher qu'une sélection de contrôles ou qu'un résultat de workflow soit présenté comme une conformité normative sans périmètre, mode et preuves suffisants.

## When to use
Activer dès qu'un artefact ou un agent formule explicitement une affirmation de conformité à ISO/IEC/IEEE 29148.

## Inputs
Required: `conformance_claim`, `assessment_evidence`
Optional: `implemented_controls`, `scope_definition`, `assessment_method`

## Preconditions
- Une revendication de conformité est présente ou doit être revue.

## Procedure
1. Capturer la formulation exacte de la revendication.
2. Identifier son périmètre : produit, processus, artefact, organisation, partie de norme ou autre objet.
3. Identifier le mode de conformité revendiqué et la méthode d'évaluation.
4. Vérifier que les contrôles, preuves et résultats cités correspondent au périmètre.
5. Vérifier si des exclusions, limites ou dépendances sont explicites.
6. Rechercher les lacunes entre la portée revendiquée et les preuves réellement produites.
7. Produire un finding lorsque la revendication dépasse le support disponible.
8. Ne jamais élargir silencieusement le périmètre pour rendre la revendication acceptable.

## Analysis logic
La présence des contrôles `R001` à `R017` prouve la couverture de contrôles SPECTRUM sélectionnés, pas à elle seule la conformité à la norme. Le Skill contrôle le bien-fondé d'une revendication ; il ne certifie pas lui-même l'organisation ou le produit.

## Decision rules
- `supported_within_scope`: revendication supportée dans son périmètre explicite.
- `scope_limited`: support partiel, revendication à restreindre.
- `evidence_insufficient`: preuves insuffisantes.
- `unsupported`: affirmation non étayée.

## Rules
- `ISO29148-R017`

## Output
`conformance_observation` contient `claim`, `scope`, `mode`, `assessment_method`, `evidence_refs`, `limitations`, `status`.

## Findings
- `unsupported_conformance_claim`
- `conformance_scope_exceeds_evidence`
- `conformance_method_not_established`

## Evidence
Relier chaque élément de support à la revendication et à son périmètre.

## Handoff
Transmettre au workflow ou à la couche de gouvernance ; ne pas convertir ce résultat en décision finale de readiness.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals
Ne pas déclarer une conformité formelle sur la seule présence de contrôles ; ne pas remplacer une évaluation de conformité officielle.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R017`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : revendication bornée et étayée, revendication trop large, preuves insuffisantes, méthode absente, non-applicable, régression.