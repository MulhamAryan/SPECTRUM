---
name: requirement-expression
description: Examiner la formulation d'une exigence pour sa spécificité, sa précision et son absence d'ambiguïté.
type: component
role: quality_analysis
---

# Requirement Expression

## Purpose
Déterminer si une expression présentée comme exigence peut être interprétée de manière stable et produire ultérieurement une vérification objective.

## When to use
Activer lorsqu'un ticket ou une exigence contient une expression normative, comportementale ou contraignante à analyser.

## Inputs
Required: `requirement`
Optional: `requirement_context`, `available_context`, `prior_findings`

## Preconditions
- L'expression candidate est disponible.

## Procedure
1. Découper l'expression en obligations atomiques lorsqu'elle contient plusieurs attentes.
2. Identifier l'objet, l'action, la condition et le résultat attendu lorsqu'ils sont présents.
3. Rechercher les termes vagues, subjectifs, non bornés ou dépendants d'une interprétation implicite.
4. Rechercher les formulations permettant plusieurs interprétations raisonnables.
5. Vérifier si les quantités, seuils, états ou conditions nécessaires sont définis.
6. Vérifier si le contenu est observable et exploitable par un futur mécanisme de vérification.
7. Comparer avec le contexte disponible pour détecter les termes cohérents en théorie mais ambigus dans ce projet.
8. Produire un finding distinct pour chaque défaut significatif.
9. Conserver l'expression originale comme evidence.

## Analysis logic
Le Skill analyse la formulation ; il ne choisit pas la valeur métier manquante. Une exigence peut être syntaxiquement claire mais insuffisante si son contexte laisse plusieurs interprétations. La réécriture est optionnelle et ne remplace pas le finding.

## Decision rules
- `clear`: interprétation unique et contenu exploitable.
- `unclear`: plusieurs interprétations plausibles.
- `underspecified`: information nécessaire absente.
- `not_verifiable_from_expression`: l'objectif est formulé sans condition observable suffisante.

## Rules
- `ISO29148-R003`

## Output
`requirement_expression_observation` contient `requirement_ref`, `atomic_obligations`, `ambiguities`, `missing_bounds`, `verification_implications`, `status`, `evidence_refs`.

## Findings
- `requirement_expression_unclear`
- `requirement_expression_underspecified`
- `requirement_expression_not_objectively_verifiable`
- `multiple_interpretations_possible`

## Evidence
Toujours conserver l'expression d'origine et les éléments contextuels qui justifient un finding.

## Handoff
Vers `verification-analysis` et le workflow.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals
Ne pas inventer une valeur cible ; ne pas décider READY ; ne pas transformer automatiquement un finding en réécriture métier.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R003`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : exigence claire, terme vague, valeur manquante, ambiguïté contextuelle, exigence composée, régression.