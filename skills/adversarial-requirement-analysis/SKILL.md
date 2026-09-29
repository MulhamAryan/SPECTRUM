---
name: adversarial-requirement-analysis
description: Soumettre exigences, règles métier, contextes et scénarios à des défis structurés (hypothèses implicites, cas limites, exceptions, transitions d'état, échecs, frontières d'autorisation) pour révéler gaps et contradictions sans promouvoir une hypothèse en fait.
type: component
role: analysis
---

# Skill — Analyse adversariale des exigences

## Objectif

Soumettre une exigence, un ensemble d'exigences, une règle métier ou un périmètre fonctionnel à des challenges structurés afin d'identifier les hypothèses implicites, conditions limites, exceptions, chemins de sortie, transitions d'état, comportements sous contrainte et dépendances susceptibles de révéler des gaps ou contradictions.

La Skill cherche volontairement les situations dans lesquelles l'interprétation courante pourrait devenir insuffisante. Elle ne suppose pas qu'un cas non décrit est nécessairement un défaut.

## Entrées

Requises :

- `target_refs`
- `analysis_scope`
- `challenge_categories`

Optionnelles :

- `requirement_refs`
- `business_rule_refs`
- `context_refs`
- `scenario_refs`
- `constraint_refs`
- `relationship_refs`
- `source_refs`
- `evidence_refs`
- `baseline_refs`
- `change_refs`
- findings déjà produits

## Sorties

La Skill produit uniquement des résultats analytiques :

- `Challenge` ;
- `Observation` ;
- `Evidence` dérivée lorsque nécessaire ;
- `Finding` ;
- `uncertainty_refs`.

Aucune sortie de cette Skill n'est une décision de readiness.

## Procédure

### 1. Définir la cible et le périmètre

Identifier précisément les exigences, règles, contextes ou artefacts soumis au challenge.

Ne pas élargir l'analyse à des comportements non déclarés comme pertinents.

### 2. Sélectionner les challenges applicables

Examiner, selon les données disponibles :

- hypothèses implicites ;
- valeurs ou conditions limites ;
- entrées inattendues ;
- exceptions ;
- mauvais usage ou abus d'un acteur applicable ;
- conflits de règles ;
- transitions d'état ;
- temporalité et expiration ;
- cycle de vie ;
- dépendances défaillantes ;
- perte de service ou dégradation ;
- volume et montée en charge lorsqu'un contexte de volume existe ;
- autorisation et frontières d'accès ;
- abandon, sortie et parcours incomplet.

### 3. Formuler la question adversariale

Chaque challenge doit être explicite et relié à sa cible.

Exemples de formulation :

- « Que se passe-t-il lorsque la condition limite est atteinte ? »
- « Quel comportement est attendu lorsque cette dépendance devient indisponible ? »
- « Quelle est la règle si deux contraintes applicables se contredisent ? »
- « Le scénario prévoit-il une sortie intermédiaire ou un abandon ? »
- « L'autorisation reste-t-elle définie lorsque l'acteur change d'état ? »

Ne pas injecter de valeurs ou comportements hypothétiques comme des faits du projet.

### 4. Chercher les éléments de réponse existants

Avant de déclarer un gap, examiner les exigences, règles métier, contextes, scénarios, contraintes, relations, sources et preuves disponibles.

Une réponse peut être portée par un autre artefact que le ticket initial.

### 5. Distinguer les résultats

Utiliser explicitement :

- `supported` lorsque le comportement est suffisamment étayé ;
- `concern_identified` lorsqu'une préoccupation doit être remontée ;
- `contradiction_identified` lorsqu'une incompatibilité est démontrée ;
- `gap_identified` lorsqu'un élément nécessaire n'est pas établi dans le périmètre ;
- `not_applicable` lorsqu'il n'existe pas de base d'application ;
- `inconclusive` lorsque les éléments ne permettent pas de conclure ;
- `insufficient_evidence` lorsque la question est pertinente mais que les preuves manquent.

### 6. Contrôler les faux positifs

Une absence de scénario négatif n'est pas automatiquement un défaut.

Une hypothèse adversariale n'est pas un fait projet.

Un cas à fort volume ne peut pas être qualifié d'échec sans contexte permettant d'établir que le volume est applicable.

Une différence entre versions ou périodes n'est pas automatiquement une contradiction.

Une portée explicitement différée ne doit pas être présentée comme une exigence actuelle manquante.

### 7. Produire les observations et findings

Chaque observation conserve :

- cible ;
- challenge ;
- statut ;
- justification ;
- preuves ;
- incertitudes ;
- relations pertinentes.

Chaque finding conserve la chaîne :

`Finding → Observation / Challenge → Evidence → Source / Artifact`

lorsque ces éléments existent.

### 8. Handoff

Transmettre les résultats vers :

- `cross-artifact-analysis` pour confronter les divergences révélées avec d'autres artefacts ;
- `verification-analysis` lorsqu'une vérification du comportement est explicitement définie ;
- `validation-analysis` lorsqu'un résultat attendu ou un contexte utilisateur est concerné ;
- `multi-source-context` / `multi-source-reasoning` pour comparer des informations attribuables ;
- `finding-engine` pour consolidation ;
- `ticket-readiness` uniquement via le workflow et sa politique explicite.

## Non-objectifs

Cette Skill ne :

- décide pas si un ticket est prêt ;
- ne classe pas les tickets avec un score global ;
- ne suppose pas qu'un comportement non écrit est incorrect ;
- ne déclare pas une implémentation en échec sans preuve d'implémentation ;
- ne remplace pas les analyses de vérification, validation ou cohérence inter-artefacts ;
- ne réécrit pas les sources ou exigences ;
- ne choisit pas silencieusement entre des règles contradictoires.

## Critères d'évaluation

Une exécution correcte doit :

- couvrir uniquement les catégories déclarées et applicables ;
- conserver les hypothèses comme hypothèses lorsqu'elles ne sont pas établies ;
- distinguer gap, incertitude et contradiction ;
- conserver la temporalité et le périmètre ;
- éviter les faux positifs liés aux cas limites ;
- produire des findings traçables ;
- être reproductible à entrées et configuration équivalentes ;
- ne produire aucune décision de readiness.