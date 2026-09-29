---
name: spec-implementation-drift-analysis
description: Confronter une spécification à des artefacts d'implémentation effectivement fournis pour établir ce qui est aligné, divergent, non démontré ou non comparable, sans inventer de comportement d'exécution.
type: component
role: analysis
---

# Skill — Analyse des écarts spécification / implémentation

## Objectif

Confronter une spécification disponible avec des artefacts d'implémentation effectivement fournis afin d'établir ce qui est aligné, partiellement aligné, divergent, non démontré ou non comparable.

Cette Skill répond notamment à la question : **ce qui est décrit comme comportement attendu est-il effectivement représenté par les artefacts d'implémentation disponibles dans le périmètre analysé ?**

Elle analyse des écarts observables. Elle ne reconstruit pas le système à partir d'hypothèses et ne déduit pas l'absence d'implémentation simplement parce qu'aucune correspondance textuelle n'a été trouvée.

## Entrées

Requises :

- `specification_refs`
- `implementation_refs`
- `comparison_scope`

Optionnelles :

- `requirement_refs`
- `business_rule_refs`
- `scenario_refs`
- `constraint_refs`
- `relationship_refs`
- `source_refs`
- `evidence_refs`
- `baseline_refs`
- `change_refs`
- `analysis_profile`

## Sorties

La Skill produit uniquement des résultats analytiques :

- `DriftAssessment` ;
- `Observation` ;
- `Evidence` dérivée lorsque nécessaire ;
- `Finding` ;
- `uncertainty_refs` lorsque les éléments disponibles ne permettent pas de conclure.

Aucune sortie de cette Skill n'est une décision de readiness.

## Procédure

### 1. Inventorier les deux côtés

Identifier séparément :

- les objets représentant l'intention ou la spécification ;
- les artefacts représentant l'implémentation ;
- les versions et baselines applicables ;
- les relations de mapping déjà établies.

Préserver l'identité de chaque élément. Ne jamais remplacer une spécification par son implémentation supposée ou inversement.

### 2. Déterminer la base de comparaison

Choisir uniquement les bases applicables et étayées :

- existence ;
- structure ;
- interface ;
- mapping de données ;
- comportement ;
- validation ;
- contrainte ;
- règle métier ;
- scénario ;
- gestion d'erreur ;
- autorisation ;
- temporalité ;
- cycle de vie ;
- traçabilité.

Une comparaison n'est valable que si les informations nécessaires sont disponibles des deux côtés.

### 3. Établir les correspondances

Utiliser en priorité les relations explicites, identifiants, mappings, conventions documentées et traces existantes.

Une correspondance peut être :

- une spécification vers un artefact ;
- une spécification vers plusieurs artefacts ;
- plusieurs spécifications vers un même artefact.

Ne pas transformer une similarité de nom, de texte ou de structure en relation certaine sans élément probant.

### 4. Examiner l'alignement

Pour chaque paire comparable, déterminer l'un des états :

- `aligned` ;
- `partially_aligned` ;
- `drift_observed` ;
- `specification_without_implementation_evidence` ;
- `implementation_without_specification_basis` ;
- `ambiguous_mapping` ;
- `not_comparable` ;
- `inconclusive`.

Une différence de représentation entre couches n'est pas automatiquement un drift.

### 5. Examiner les écarts de comportement

Lorsque la base comportementale est établie, comparer notamment :

- préconditions ;
- conditions ;
- effets attendus ;
- valeurs et bornes ;
- erreurs ;
- autorisations ;
- transitions d'état ;
- dépendances ;
- séquences ;
- temporalité ;
- comportement conditionnel.

Ne jamais inventer le comportement runtime d'un composant qui n'est pas observable dans les artefacts fournis.

### 6. Distinguer absence, drift et incertitude

Ne pas confondre :

- absence de preuve d'implémentation ;
- preuve d'une implémentation absente ;
- implémentation divergente ;
- mapping ambigu ;
- déviation explicitement documentée ;
- différence due à une version ou à un périmètre distinct.

Une recherche textuelle sans résultat ne constitue pas une preuve suffisante d'absence.

### 7. Tenir compte du contexte de livraison

Préserver :

- version ;
- baseline ;
- date d'effet ;
- feature flags lorsqu'ils sont explicitement fournis ;
- déviations approuvées ;
- générateurs et artefacts dérivés lorsqu'ils sont identifiés.

Une divergence temporelle ne doit pas être transformée en contradiction si les périodes sont explicitement distinctes.

### 8. Produire les findings

Chaque finding doit conserver :

- la spécification concernée ;
- l'artefact d'implémentation concerné lorsqu'il existe ;
- la base de comparaison ;
- les preuves ;
- le drift assessment ;
- les incertitudes éventuelles.

Les findings restent analytiques et sont transmis au Finding Engine.

## Faux positifs à éviter

- `absence_de_code_trouve` = implémentation absente ;
- nom de classe différent = drift ;
- camelCase / snake_case = drift ;
- champ calculé sans colonne SQL = drift ;
- comportement fourni par une bibliothèque = comportement absent ;
- code généré sans texte de l'exigence = absence d'implémentation ;
- implémentation conditionnelle derrière un feature flag = contradiction ;
- déviation documentée = drift non autorisé ;
- différence entre versions = contradiction immédiate ;
- absence de test visible = preuve que le comportement n'est pas implémenté.

## Critères d'évaluation

Une exécution correcte doit :

- préserver l'identité et la provenance des deux côtés ;
- déclarer la base de comparaison utilisée ;
- conserver les mappings explicites ;
- distinguer absence de preuve et absence démontrée ;
- gérer les mappings un-vers-plusieurs et plusieurs-vers-un ;
- conserver les versions, baselines et temporalités ;
- identifier les écarts observables sans inventer de runtime ;
- produire des findings traçables ;
- être reproductible à entrées et configuration équivalentes ;
- ne produire aucune décision de readiness.

## Handoff

Les résultats peuvent être transmis vers :

- `cross-artifact-analysis` pour une analyse structurée des correspondances entre artefacts ;
- `verification-analysis` pour analyser la preuve de vérification d'un comportement ;
- `validation-analysis` pour confronter le comportement observé au besoin d'usage ;
- `multi-source-reasoning` lorsque plusieurs sources attribuables décrivent l'intention ou l'implémentation ;
- `finding-engine` pour la consolidation ;
- `ticket-readiness` uniquement via le workflow et sa politique explicite.

## Non-objectifs

Cette Skill ne :

- modifie pas le code ou la spécification ;
- ne prétend pas connaître le runtime lorsqu'il n'est pas fourni ;
- ne remplace pas les analyses de sécurité, performance ou qualité de code spécialisées ;
- ne décide pas si un ticket est prêt ;
- ne transforme pas automatiquement un drift en blocage ;
- ne remplace pas `Cross-Artifact Analysis`, `Business Rule Analysis`, `Multi-Source Reasoning`, `Finding Engine` ou `Decision Engine`.
