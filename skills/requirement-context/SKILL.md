---
name: requirement-context
description: Établir l'item d'intérêt, le contexte de l'exigence, les contraintes, conditions, états et le niveau de spécification lorsque pertinent.
type: component
role: requirement_analysis
---

# Requirement Context

## Purpose
Construire une représentation factuelle du sujet auquel l'exigence s'applique avant d'évaluer sa qualité ou sa suffisance.

## When to use
Utiliser pour toute analyse où le ticket ou l'exigence doit être interprété par rapport à un système, une capacité, un comportement, un besoin, une contrainte, une condition, un état ou un niveau de spécification.
Ne pas l'utiliser pour inventer un item d'intérêt absent des sources.

## Inputs
Required: `ticket`, `available_context`
Optional: `prior_findings`, `prior_decisions`

## Preconditions
- Le ticket ou l'exigence est disponible.
- Les sources accessibles sont identifiables.

## Procedure
1. Extraire les expressions candidates qui portent une obligation, un besoin ou une attente.
2. Identifier l'item d'intérêt explicitement nommé ou démontré par les sources.
3. Relier chaque exigence à son sujet, système, sous-système, fonction ou autre objet pertinent.
4. Identifier séparément, lorsqu'ils existent, le besoin, la contrainte, la condition et l'état.
5. Déterminer le niveau de spécification seulement lorsqu'il est justifié par le contexte.
6. Comparer ces éléments aux sources disponibles pour détecter contradictions, absences ou ambiguïtés de contexte.
7. Marquer chaque élément comme `established`, `partial` ou `not_established`.
8. Produire un résultat traçable, sans compléter silencieusement les informations manquantes.

## Analysis logic
- Une information trouvée uniquement par supposition reste `not_established`.
- Une condition n'est pas fusionnée avec une contrainte si les deux sont distinguables.
- Un nom de composant n'est pas considéré comme un item d'intérêt suffisant sans relation explicite avec l'exigence.
- Un niveau de spécification n'est conclu que si le contexte permet de le justifier.
- Toute contradiction entre sources est conservée comme finding plutôt que résolue arbitrairement.

## Decision rules
- `established`: support direct ou convergent par les sources autorisées.
- `partial`: information présente mais incomplète ou conditionnelle.
- `not_established`: aucune preuve suffisante.
- `contradictory`: deux sources autorisées produisent des interprétations incompatibles.

## Rules
- `ISO29148-R001`
- `ISO29148-R002`
- `ISO29148-R013`
- `ISO29148-R015`

## Output
Produit `requirement_context` contenant :
- `items_of_interest`
- `needs`
- `constraints`
- `conditions`
- `states`
- `requirement_level`
- `status`
- `evidence_refs`

Chaque item doit indiquer son statut et ses références d'origine.

## Findings
- `missing_item_of_interest`
- `requirement_context_incomplete`
- `condition_constraint_state_unclear`
- `requirement_level_unclear`
- `contradictory_requirement_context`

## Evidence
Conserver le texte ou artefact source, sa localisation et la relation exacte avec l'élément extrait.

## Handoff
Vers `elicitation-gap` pour les éléments non établis ; vers `requirement-expression`, `requirement-relationship-traceability`, `verification-analysis` et `validation-analysis` pour les analyses dépendantes.

## Exit conditions
- `completed`: contexte suffisamment établi pour la suite.
- `completed_with_gaps`: contexte exploitable mais incomplet.
- `not_applicable`: aucune exigence/contextualisation pertinente.

## Non-goals
Ne pas décider de readiness, ne pas créer de besoin, ne pas réécrire la spécification métier.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R001`, `R002`, `R013`, `R015`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : contexte nominal, item absent, contrainte ambiguë, sources contradictoires, niveau non établi, régression.