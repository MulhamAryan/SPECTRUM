# Skill — Analyse des règles métier

## Objectif

Analyser les règles métier explicites applicables à un périmètre afin de déterminer ce qui est établi, partiellement établi, ambigu, contradictoire, incomplet, non applicable ou non concluant, avec une traçabilité vers les exigences, artefacts, sources et preuves disponibles.

Cette Skill répond notamment à la question : **les règles qui gouvernent le comportement métier attendu sont-elles identifiables, applicables, suffisamment formulées et correctement reliées aux éléments qu'elles contraignent ?**

## Entrées

Requises :

- `target_refs`
- `business_rule_refs` lorsque des règles sont déjà identifiées
- `analysis_scope`

Optionnelles :

- `requirement_refs`
- `source_refs`
- `relationship_refs`
- `evidence_refs`
- `context_refs`
- `constraint_refs`
- `scenario_refs`
- `baseline_refs`
- `change_refs`
- findings analytiques déjà produits

## Sorties

La Skill produit uniquement des résultats analytiques :

- `BusinessRule` lorsqu'une règle est explicitement établie à partir des entrées ;
- `RuleAssessment` ;
- `Observation` ;
- `Evidence` dérivée lorsque nécessaire ;
- `Finding` ;
- `uncertainty_refs` lorsque l'information ne permet pas de conclure.

Aucune sortie de cette Skill n'est une décision de readiness.

## Procédure

### 1. Inventorier les règles

Identifier les règles explicitement présentes dans les sources, exigences, artefacts ou autres objets fournis.

Pour chaque règle, préserver :

- identité ;
- formulation ;
- type de règle lorsqu'il est établi ;
- source et fragment source ;
- périmètre d'application ;
- relations ;
- dates d'effet ;
- niveau de priorité lorsqu'il est explicitement fourni.

Ne pas créer une règle uniquement parce qu'un comportement semble attendu.

### 2. Distinguer les concepts

Ne pas confondre :

- règle métier ;
- besoin ou exigence ;
- contrainte technique ;
- scénario ;
- critère d'acceptation ;
- politique de décision SPECTRUM.

Une exigence peut porter une règle métier, mais les deux objets restent distincts lorsqu'ils sont identifiables.

### 3. Établir l'applicabilité

Vérifier les éléments explicitement disponibles :

- entité concernée ;
- contexte ;
- condition ;
- scénario ;
- période d'effet ;
- exception ;
- dépendance ;
- relation vers les exigences ou artefacts concernés.

Une information absente produit une limitation ou une incertitude ; elle n'est pas automatiquement interprétée comme une contradiction.

### 4. Analyser la formulation

Examiner, selon les données disponibles :

- résultat attendu ;
- conditions d'activation ;
- interdictions ou obligations ;
- données nécessaires ;
- calcul ou dérivation ;
- exceptions ;
- classification ;
- ordre ou séquence ;
- temporalité.

Ne jamais inventer une valeur, un seuil, une formule ou une exception non fournie.

### 5. Examiner la cohérence

Comparer uniquement les règles partageant une base d'applicabilité pertinente.

Distinguer :

- ambiguïté ;
- absence de correspondance établie ;
- divergence ;
- contradiction.

Deux formulations différentes ne sont pas contradictoires sans preuve sémantique ou contextuelle suffisante.

Des règles incompatibles peuvent coexister lorsqu'elles sont explicitement séparées par leur période d'effet, leur périmètre ou leur version.

### 6. Examiner la traçabilité

Établir les liens connus entre :

`BusinessRule → Requirement → Scenario / Constraint / Artifact → Source / Evidence`

Une absence de lien dans les données disponibles ne prouve pas qu'aucun lien réel n'existe.

### 7. Produire les observations et findings

Chaque observation doit indiquer :

- cible ;
- statut ;
- justification ;
- preuves ;
- incertitudes ;
- relations pertinentes.

Chaque finding doit conserver les références vers la règle, l'assessment et les preuves qui le fondent.

### 8. Handoff

Transmettre les résultats vers :

- `cross-artifact-analysis` pour confronter règles et autres artefacts ;
- `verification-analysis` lorsque la règle possède une base de vérification explicite ;
- `validation-analysis` lorsque la règle dépend d'un contexte d'usage ou d'un résultat attendu ;
- `multi-source-context` / `multi-source-reasoning` pour comparer des sources attribuables ;
- `finding-engine` pour la consolidation ;
- `ticket-readiness` uniquement via le workflow et sa politique explicite.

## Faux positifs à éviter

- considérer l'absence d'une règle dans le ticket comme la preuve de son inexistence ;
- transformer une contrainte technique en règle métier sans base ;
- considérer deux versions temporelles comme contradictoires ;
- inventer un mapping entre une règle et une exigence ;
- inventer le comportement de l'implémentation ;
- déduire automatiquement `NOT_READY` d'un finding sévère ;
- attribuer une priorité non fournie ;
- supprimer une contradiction pour obtenir une sortie cohérente.

## Critères d'évaluation

Une exécution correcte doit :

- conserver l'identité et la provenance des règles ;
- distinguer règle, exigence et contrainte technique ;
- préserver conditions, exceptions et temporalité lorsqu'elles sont connues ;
- ne pas confondre ambiguïté et contradiction ;
- ne pas confondre absence de correspondance et absence de règle ;
- conserver les conflits entre sources ;
- produire des findings traçables ;
- être reproductible à entrées et configuration équivalentes ;
- ne produire aucune décision de readiness.

## Non-objectifs

Cette Skill ne :

- décide pas si un ticket est prêt ;
- ne réécrit pas les sources ;
- ne transforme pas une règle en décision ;
- ne déduit pas des règles métier non étayées ;
- ne réalise pas à elle seule l'analyse exhaustive d'une implémentation ;
- ne remplace pas `Cross-Artifact Analysis`, `Multi-Source Reasoning`, `Finding Engine` ou `Decision Engine`.
