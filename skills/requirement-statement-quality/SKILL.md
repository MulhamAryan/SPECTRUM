---
name: requirement-statement-quality
description: Analyser la qualité d'une expression individuelle de besoin ou d'exigence au regard des caractéristiques et règles de formulation du GtWR v4 explicitement reliées.
type: component
role: quality_analysis
---

# Requirement Statement Quality

## Purpose
Évaluer une expression individuelle de besoin ou d'exigence contre les caractéristiques de qualité individuelles C1–C9 et les règles de formulation du Guide to Writing Requirements v4 (GtWR v4) qui lui sont explicitement reliées par la matrice officielle.

## Source boundary
La base source de ce Skill est exclusivement le corpus officiel INCOSE GtWR v4 enregistré dans `knowledge/sources/incose-gtwr-v4-2023/`.

Le Skill doit distinguer :
- `source_fact` : caractéristique ou règle INCOSE identifiée dans la source officielle ;
- `spectrum_observation` : résultat de l'analyse effectuée par ce Skill ;
- `business_gap` : information métier manquante qui ne peut pas être inventée.

Aucune formulation générée par le modèle n'est une source INCOSE.

## When to use
Utiliser lorsqu'une expression individuelle présentée comme besoin ou exigence doit être examinée pour sa qualité de formulation, son adéquation observable aux règles de rédaction et les éléments contextuels nécessaires à l'évaluation des caractéristiques individuelles.

Ne pas utiliser ce Skill seul pour conclure à la nécessité métier, à la faisabilité complète, à la correction par rapport à la source métier, à la validation globale ou à la qualité d'un ensemble de besoins/exigences lorsque ces conclusions dépendent d'analyses externes à la formulation.

## Inputs
Required: `requirement_expression`

Optional:
- `requirement_context`
- `available_sources`
- `prior_findings`
- `source_language_conventions`

## Preconditions
- L'expression candidate est disponible.
- La source INCOSE GtWR v4 est référencée par son identifiant canonique.
- Les sources de projet utilisées pour interpréter les termes, unités, acronymes, niveaux, sources ou conventions sont identifiables.

## Procedure
1. Conserver l'expression originale comme evidence immuable de l'analyse.
2. Déterminer si l'expression contient une seule obligation ou plusieurs pensées/obligations.
3. Identifier les éléments observables de la formulation : sujet, action, objet, conditions, qualifications, quantités, unités, temporalité, termes définis, modalités logiques et marqueurs de structure lorsqu'ils sont présents.
4. Lire le périmètre des règles depuis `rules.yaml` et la matrice officielle `Rules → Characteristics` dans `matrices.yaml` ; ne jamais reconstruire ce périmètre à partir du nom d'une règle.
5. Examiner les règles individuelles applicables à l'expression : R1–R28 et R30–R40. R29, R41 et R42 sont exclus car ils concernent le niveau des ensembles dans la matrice officielle.
6. Pour chaque règle applicable, rechercher une preuve textuelle de conformité, une violation observable ou un besoin de contexte empêchant le jugement.
7. Relier les observations aux caractéristiques individuelles C1–C9 lorsqu'elles sont couvertes par la matrice officielle.
8. Pour C1 Necessary, C6 Feasible et C8 Correct, rechercher explicitement les sources ou le contexte nécessaires ; ne jamais déduire ces propriétés du texte seul.
9. Ne pas transformer l'absence d'une information métier en valeur inventée ; produire un finding ou un gap lorsque cette information est nécessaire.
10. Distinguer un défaut de formulation d'un défaut d'analyse ou de connaissance sous-jacente.
11. Produire un finding séparé pour chaque problème significatif et conserver les `evidence_refs` correspondantes.
12. Indiquer explicitement les règles ou caractéristiques qui n'ont pas pu être évaluées faute de contexte ou de preuve.

## Analysis logic
Le GtWR v4 indique que les caractéristiques des besoins et exigences résultent à la fois des règles d'écriture et des activités d'analyse sous-jacentes. Ce Skill traite la **qualité observable de l'expression** et les éléments contextuels nécessaires à certains jugements ; il ne prétend pas établir à lui seul la qualité complète d'un besoin ou d'une exigence.

La matrice officielle relie certaines règles à C1, C2, C6 et C8 en plus de C3, C4, C5, C7 et C9. Ces caractéristiques ne doivent pas être artificiellement réduites à des contrôles syntaxiques. Une absence de preuve doit produire un état inconclusif ou dépendant du contexte, pas un verdict fabriqué.

Une règle INCOSE n'est pas appliquée mécaniquement lorsqu'elle dépend d'une convention de projet, d'un glossaire, d'une unité, d'un modèle, d'une source de référence ou d'un contexte de niveau. Dans ce cas, l'état doit refléter l'insuffisance de preuve.

## Decision semantics
- `conformant_observed`: aucune non-conformité observable identifiée pour les contrôles applicables et les preuves disponibles.
- `non_conformant_observed`: au moins une violation observable est étayée par l'expression ou une source autorisée.
- `inconclusive_missing_context`: l'analyse dépend d'informations non établies.
- `inconclusive_source_conflict`: des sources autorisées se contredisent.
- `not_applicable`: aucune règle ou caractéristique de cette Skill n'est applicable à l'expression analysée.

## Rule scope
Les règles couvertes ici proviennent du catalogue officiel structuré dans `knowledge/sources/incose-gtwr-v4-2023/rules.yaml` et de la matrice officielle transcrite dans `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`.

Périmètre des règles individuelles :
- `R1–R28`
- `R30–R40`

Hors périmètre de cette Skill :
- `R29` Classification — relation de niveau ensemble dans la matrice ;
- `R41` Related Needs and Requirements — niveau ensemble ;
- `R42` Structured Sets — niveau ensemble.

Les caractéristiques individuelles couvertes sont `C1–C9`. Le Skill peut collecter des observations utiles à chacune, mais doit distinguer les caractéristiques directement observables de celles exigeant des sources de contexte ou de transformation.

Le nom canonique de chaque règle doit être lu depuis le corpus source et non recréé dans le Skill. La divergence officielle R14 doit rester conservée : l'identité canonique de la règle est `Correct Punctuation`, tandis que la ligne correspondante de la matrice page 4 affiche `Correct Condition`.

## Output
Produire `requirement_statement_quality_observation` contenant au minimum :
- `requirement_ref`
- `status`
- `applicable_rules`
- `characteristics_assessed`
- `rule_observations`
- `findings`
- `missing_context`
- `evidence_refs`

Chaque `rule_observation` doit contenir :
- `rule_id`
- `source_name`
- `applicability`
- `observation`
- `evidence_refs`
- `status`

Chaque caractéristique évaluée doit indiquer le niveau de preuve permettant le jugement.

## Findings
Exemples de types de findings produits par le Skill :
- `rule_non_conformity_observed`
- `statement_ambiguous`
- `statement_incomplete`
- `multiple_thoughts_detected`
- `verification_basis_not_observable`
- `defined_term_missing`
- `quantification_or_range_missing`
- `condition_not_explicit`
- `language_convention_conflict`
- `necessary_context_not_established`
- `feasibility_evidence_missing`
- `source_alignment_not_established`
- `analysis_blocked_by_missing_context`

Les identifiants de findings sont des artefacts SPECTRUM ; ils ne doivent pas être présentés comme des identifiants INCOSE.

## Evidence
Toujours conserver :
- l'expression analysée ;
- la règle INCOSE concernée ;
- la caractéristique concernée lorsqu'elle est applicable ;
- la source de contexte utilisée lorsque nécessaire ;
- le passage ou élément précis justifiant le finding.

Une affirmation du type « conforme à INCOSE » sans référence à une règle, une caractéristique et une preuve n'est pas une evidence suffisante.

## Handoff
Vers :
- `requirement-context` lorsque le résultat dépend du contexte de l'entité, des conditions, de l'état ou du niveau ;
- `verification-analysis` lorsque la vérifiabilité doit être approfondie ;
- `validation-analysis` lorsque la pertinence par rapport au besoin ou aux objectifs doit être établie ;
- `elicitation-gap` lorsque l'analyse est bloquée par une information métier absente ;
- une future analyse de niveau ensemble pour C10–C15.

## Exit conditions
- `completed`
- `completed_with_findings`
- `completed_with_gaps`
- `blocked_on_missing_context`
- `not_applicable`

## Non-goals
- Ne pas inventer une valeur cible, un seuil, une condition ou une décision métier.
- Ne pas déduire C1 Necessary, C6 Feasible ou C8 Correct de la seule forme du texte.
- Ne pas décider `READY`, `NOT READY` ou toute autre décision globale du produit.
- Ne pas déclarer une conformité formelle à INCOSE.
- Ne pas remplacer les analyses de faisabilité, de nécessité, de validation ou d'ensemble.
- Ne pas modifier silencieusement l'expression source.

## References
Official INCOSE sources used by this Skill:
- `INCOSE Guide to Writing Requirements v4`, INCOSE-TP-2010-006-04, version/revision 4, 2023-07-01.
- `INCOSE Guide to Writing Requirements v4 – Summary Sheet`, June 2023.
- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/rules.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

## Evaluation
Évaluer au minimum :
- formulation claire et singulière ;
- règle applicable identifiée depuis la matrice officielle ;
- ambiguïté lexicale ou contextuelle ;
- terme non défini ;
- pronom ou référence insuffisante ;
- condition implicite ;
- quantité sans borne ou plage ;
- performance non mesurable ;
- formulation multi-pensées ;
- convention de langage incohérente ;
- absolu ou quantification inadéquate ;
- solution imposée sans contexte de justification ;
- nécessité non établie ;
- faisabilité non établie ;
- exactitude par rapport à la source non établie ;
- expression impossible à examiner faute de contexte ;
- faux positif lorsqu'une source autorisée établit l'information ailleurs ;
- régression par rapport aux résultats d'une version précédente.
