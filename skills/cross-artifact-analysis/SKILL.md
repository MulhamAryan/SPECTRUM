---
name: cross-artifact-analysis
description: Analyser la cohérence entre plusieurs artefacts liés d'un même périmètre et produire des observations et findings traçables sans créer de décision globale.
type: component
role: cross_artifact_analysis
---

# Analyse inter-artefacts

## Purpose
Examiner plusieurs artefacts liés afin d'établir ce qui est aligné, partiellement aligné, divergent, contradictoire, non comparable ou non établi. Le Skill vise à détecter les incohérences qui apparaissent uniquement lorsqu'un ticket ou une exigence est confronté à son contexte documentaire et technique.

## Source boundary
Le Skill utilise uniquement les artefacts, relations, sources, fragments, contextes et preuves explicitement fournis par l'exécution.

Il distingue strictement :
- `source_fact` : information provenant d'une source identifiée ;
- `project_fact` : information de projet explicitement fournie ;
- `project_artifact` : contenu d'un artefact de projet ;
- `observation_input` : entrée fournie pour l'analyse ;
- `derived_observation` : résultat dérivé de l'analyse ;
- `contradiction` : élément mettant en évidence des affirmations incompatibles ;
- `absence` : absence observée dans un périmètre donné, sans valeur automatique de non-conformité.

Aucune relation ou information non établie ne doit être créée comme un fait.

## When to use
Utiliser lorsqu'au moins deux artefacts ou objets partageant un périmètre peuvent être comparés : ticket/exigence, exigence/règle métier, exigence/API, exigence/données, exigence/tests, spécification/implémentation, baseline/change ou plusieurs versions d'un même artefact.

Ne pas utiliser lorsque les éléments ne disposent d'aucune base de comparaison pertinente. Dans ce cas, produire `not_comparable` ou transmettre vers l'analyse contextuelle nécessaire.

## Inputs
Required:
- `target_refs`
- `artifact_refs`
- `comparison_scope`

Optional:
- `relationship_refs`
- `source_refs`
- `evidence_refs`
- `context_refs`
- `baseline_refs`
- `change_refs`
- `prior_findings`

## Preconditions
- Les identités des artefacts et objets sont valides.
- Les références fournies peuvent être résolues.
- Le périmètre de comparaison est explicite.
- Une base de comparaison pertinente est identifiable ou l'analyse peut établir qu'elle ne l'est pas.
- Les conventions de représentation utilisées pour comparer les éléments sont connues lorsqu'elles sont nécessaires.

## Procedure
1. Recenser les artefacts réellement fournis et conserver leurs identités et versions.
2. Déterminer les paires ou groupes comparables à partir du périmètre déclaré et des relations existantes.
3. Charger les relations explicites avant toute inférence de correspondance.
4. Identifier la base de comparaison applicable : sémantique, terminologie, champs, comportement, contraintes, conditions, acceptation, traçabilité, version ou cycle de vie.
5. Comparer les éléments selon cette base sans confondre différence de représentation et différence de sens.
6. Vérifier les différences de périmètre, d'applicabilité, de temporalité et de version avant de qualifier une contradiction.
7. Distinguer les états `aligned`, `partially_aligned`, `mismatch`, `missing_correspondence`, `contradictory`, `not_comparable` et `inconclusive`.
8. Attacher à chaque résultat les preuves, relations et sources qui justifient effectivement la comparaison.
9. Produire une Observation pour le résultat de comparaison et un Finding lorsqu'une anomalie, lacune, contradiction ou incertitude analytique est établie.
10. Effectuer un contrôle anti-faux-positif : champ calculé, mapping de représentation, relation un-à-plusieurs, version indépendante ou périmètre explicitement différé.
11. Préserver les contradictions au lieu de choisir silencieusement une version.
12. Ne jamais transformer le résultat en décision de readiness.

## Analysis logic
Une correspondance n'est établie que lorsque les éléments comparés partagent une base suffisante et que cette relation peut être justifiée par les entrées disponibles.

Une absence de correspondance textuelle peut donner une observation `missing_correspondence`, mais ne prouve pas qu'une correspondance sémantique n'existe pas.

Une différence entre deux artefacts n'est un `mismatch` que lorsqu'elle est observable et pertinente au regard du périmètre. Si deux versions concernent des périodes différentes, l'analyse doit conserver cette distinction temporelle.

Une contradiction requiert des affirmations attribuables et incompatibles dans un même contexte applicable. Une différence de formulation, de nommage ou de représentation peut être compatible lorsqu'un mapping explicite l'explique.

L'analyse inter-artefacts ne déduit jamais le comportement réel d'une implémentation qui n'est pas fournie comme entrée.

## Decision semantics
- `aligned` : correspondance établie pour le périmètre déclaré.
- `partially_aligned` : correspondance partielle, avec partie non établie explicitement délimitée.
- `mismatch` : divergence observable et étayée.
- `missing_correspondence` : aucune correspondance établie dans le périmètre analysé.
- `contradictory` : affirmations incompatibles et attribuables dans un contexte commun.
- `not_comparable` : base de comparaison absente ou inappropriée.
- `inconclusive` : informations insuffisantes, contexte manquant ou désaccord non résolu.

Ces états sont des résultats analytiques et ne signifient pas à eux seuls `READY`, `NOT_READY`, `PASS` ou `FAIL`.

## Findings
Le Skill peut produire notamment :
- `cross_artifact_mismatch`
- `correspondence_missing`
- `terminology_drift`
- `condition_divergence`
- `constraint_divergence`
- `acceptance_alignment_gap`
- `traceability_gap`
- `version_alignment_uncertain`
- `cross_artifact_contradiction`
- `comparison_blocked_by_missing_context`

Ces identifiants sont propres à SPECTRUM.

## Evidence
Conserver au minimum :
- les artefacts ou objets comparés ;
- la base de comparaison ;
- les versions et périmètres applicables ;
- les relations utilisées ;
- les preuves localisables justifiant le résultat ;
- les sources lorsque le résultat dépend d'une information source-backed.

Une affirmation issue d'une simple recherche textuelle doit rester identifiable comme résultat de recherche, et non comme preuve sémantique certaine.

## Handoff
Vers :
- `requirements-context` si le résultat dépend d'un contexte métier ou d'une condition d'applicabilité absente ;
- `multi-source-context` ou `multi-source-reasoning` lorsqu'il existe plusieurs sources ou versions à confronter ;
- `verification-analysis` lorsque la divergence porte sur la base de vérification ;
- `validation-analysis` lorsque le désalignement concerne la validation au niveau ensemble ;
- `finding-engine` pour consolidation ;
- le workflow de ticket pour l'étape de décision éventuelle.

## Exit conditions
- `completed`
- `completed_with_findings`
- `completed_with_gaps`
- `blocked_on_missing_context`
- `not_comparable`

## Non-goals
- Ne pas décider la readiness.
- Ne pas inventer de relation ou de mapping.
- Ne pas modifier les artefacts comparés.
- Ne pas déduire le comportement d'un système absent des entrées.
- Ne pas transformer une absence textuelle en preuve de non-conformité.
- Ne pas résoudre silencieusement une contradiction.
- Ne pas créer de score global de cohérence.

## References
- `models/canonical-data-model.yaml`
- `models/finding-model.yaml`
- `models/evidence-model.yaml`
- `models/skill-execution-contract.yaml`
- `models/cross-artifact-analysis.yaml`
- `evaluation/contracts/cross-artifact-analysis.yaml`
- `evaluation/cases/cross-artifact-analysis.yaml`

## Evaluation
Vérifier au minimum :
- cohérence sémantique ;
- correspondance de champs ;
- terminologie et mappings de représentation ;
- alignement des conditions et contraintes ;
- alignement avec les critères d'acceptation ;
- traçabilité ;
- différences de version ;
- différences de temporalité ;
- différences d'applicabilité ;
- relations un-à-plusieurs ;
- champs calculés ;
- faux positifs dus à une absence de match textuel ;
- preuves insuffisantes ;
- contradictions conservées ;
- absence de décision globale générée par le Skill.
