# Skill — Analyse indépendante

## Objectif

Produire une analyse indépendante d'un périmètre déjà analysé afin de fournir un résultat analytique distinct et comparable, tout en conservant l'identité de l'exécution, ses entrées, sa provenance, ses incertitudes et ses limites.

L'indépendance porte sur le mécanisme d'analyse et son périmètre, pas sur la vérité des données d'entrée. Deux analyses utilisant les mêmes sources peuvent donc partager le même biais d'entrée.

## Entrées

Requises :

- `target_refs`
- `analysis_scope`
- `independence_basis`
- `input_refs`

Optionnelles :

- `primary_analysis_ref`
- `source_refs`
- `evidence_refs`
- `context_refs`
- `requirement_refs`
- `business_rule_refs`
- `artifact_refs`
- `prior_findings`
- `analysis_profile`

## Sorties

La Skill produit uniquement des résultats analytiques :

- `IndependentAnalysis` ;
- `OpinionResult` lorsqu'une comparaison avec une analyse de référence est possible ;
- `Observation` ;
- `Evidence` dérivée ;
- `Finding` ;
- `uncertainty_refs`.

Aucune sortie de cette Skill ne constitue une décision de readiness.

## Procédure

### 1. Déclarer l'indépendance

Enregistrer :

- identité du mécanisme ;
- version ;
- configuration pertinente ;
- analyste ou agent lorsque applicable ;
- frontière d'isolation ;
- entrées effectivement disponibles.

Une analyse n'est pas indépendante uniquement parce qu'elle est exécutée plus tard ou par une autre fenêtre de contexte.

### 2. Isoler l'analyse

Définir explicitement ce que l'analyse indépendante peut consulter.

Ne pas importer silencieusement :

- conclusions d'une analyse précédente ;
- findings comme s'ils étaient des faits ;
- décisions ;
- hypothèses non sourcées.

Les sources et preuves autorisées restent consultables lorsqu'elles appartiennent explicitement au périmètre d'entrée.

### 3. Exécuter l'analyse

Appliquer le même périmètre déclaré au mécanisme indépendant.

Selon le profil, examiner :

- qualité des exigences ;
- règles métier ;
- contraintes ;
- scénarios ;
- relations ;
- cohérence entre artefacts ;
- vérification et validation ;
- risques ou ambiguïtés pertinents.

Le mécanisme ne doit pas chercher à reproduire artificiellement la conclusion d'une autre analyse.

### 4. Comparer avec l'analyse de référence

Lorsque `primary_analysis_ref` est fourni et comparable, comparer :

- cibles ;
- périmètre ;
- révisions ;
- observations ;
- findings ;
- preuves ;
- hypothèses explicites ;
- conclusions analytiques.

Les statuts autorisés sont :

`corroborated`, `divergent`, `partially_corroborated`, `inconclusive`, `not_comparable`, `insufficient_evidence`.

Un accord ne prouve pas la vérité. Une divergence ne prouve pas qu'une analyse est erronée.

### 5. Investiguer les divergences

Lorsqu'une divergence apparaît, tester d'abord :

- différence de périmètre ;
- différence de version ;
- différence d'entrée ;
- différence de source accessible ;
- hypothèse explicite ;
- définition ou mapping différent ;
- différence de méthode.

Ne qualifier de contradiction que ce qui reste incompatible dans une base comparable et étayée.

### 6. Préserver l'incertitude

Lorsque les preuves ne permettent pas de départager deux analyses, conserver l'état inconclusif et les éléments non résolus.

Ne jamais supprimer une divergence uniquement pour produire une synthèse cohérente.

### 7. Handoff

Transmettre les résultats vers :

- `multi-source-reasoning` lorsque les analyses ou leurs sources doivent être comparées avec d'autres informations attribuables ;
- `cross-artifact-analysis` lorsque la divergence porte sur plusieurs artefacts ;
- `finding-engine` pour la consolidation ;
- `ticket-readiness` uniquement au travers du workflow et d'une politique explicite.

## Faux positifs à éviter

- considérer deux analyses identiques comme indépendantes lorsqu'elles partagent le même mécanisme et la même exécution ;
- considérer un accord de conclusion comme une preuve indépendante de vérité ;
- considérer toute divergence textuelle comme une divergence sémantique ;
- considérer une sortie plus confiante comme prioritaire sur une preuve traçable ;
- transformer une hypothèse d'analyse en fait projet ;
- transformer un échec de l'outil en désaccord analytique ;
- comparer des analyses de versions ou périmètres différents sans le déclarer ;
- donner à l'analyse indépendante une autorité de décision.

## Critères d'évaluation

Une exécution correcte doit :

- déclarer l'identité et la frontière d'indépendance ;
- préserver les entrées et leur provenance ;
- ne pas hériter silencieusement de conclusions antérieures ;
- produire des observations et findings traçables ;
- distinguer accord, divergence et inconclusivité ;
- conserver les différences de version et de périmètre ;
- préserver les conflits non résolus ;
- être reproductible avec la même configuration et les mêmes entrées ;
- ne produire aucune décision de readiness.

## Non-objectifs

Cette Skill ne :

- ne désigne pas l'analyse la plus correcte ;
- ne remplace pas `Multi-Source Reasoning` ;
- ne remplace pas le `Finding Engine` ;
- ne crée pas de politique de décision ;
- ne réécrit pas les analyses ou sources précédentes ;
- ne fournit pas un score global de confiance ou de qualité.
