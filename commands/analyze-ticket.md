---
description: Analyse un ticket SPECTRUM de bout en bout et produit un verdict de readiness traçable.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Analyse de ticket

Analyse le ticket fourni pour répondre à une seule question : **un développeur peut-il commencer l’implémentation sans reconstruire une exigence matérielle manquante, ambiguë ou contradictoire ?**

## Références obligatoires

Charge :
- `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`
- `${CLAUDE_PLUGIN_ROOT}/policies/ticket-readiness-v1.yaml`
- `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/canonical-data-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/evidence-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/finding-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`

## Entrée

`$ARGUMENTS` est soit un chemin vers un fichier contenant le ticket, soit le texte du ticket. Si c’est un chemin, lis le fichier avant toute analyse.

## Sécurité et permissions — règle absolue

SPECTRUM est **strictement en lecture seule par défaut**.

Sans autorisation explicite de l’utilisateur dans l’interaction courante, il est strictement interdit de :
- modifier, créer ou supprimer du code ;
- modifier, créer ou supprimer des fichiers ;
- exécuter une action qui mute le dépôt ;
- créer, modifier ou supprimer une branche ;
- commit ou push ;
- créer ou modifier une Pull Request ;
- écrire, commenter, modifier ou transitionner un ticket Jira ;
- modifier un champ Jira ;
- écrire dans un système externe ;
- lancer une action d’environnement ayant un effet persistant.

Une recommandation, une direction, un finding, un verdict `ready/not_ready`, une génération de test case ou une revue QA **n’autorise jamais automatiquement une écriture**.

Une permission doit être explicite, porter sur l’opération et la cible concernées, et ne doit jamais être déduite d’une permission antérieure, de l’accès aux outils, de la propriété du dépôt ou d’une intention supposée.

Ne jamais prétendre qu’une écriture a été effectuée sans résultat d’opération vérifiable.

## Principe fondamental

Ne confonds jamais :
- **problème détecté** et **blocage d’implémentation** ;
- **information absente** et **information prouvée nécessaire** ;
- **ancienne formulation** et **contradiction actuelle** ;
- **cas limite imaginable** et **cas requis par le ticket ou une source autorisée** ;
- **gravité d’un finding** et **décision de readiness** ;
- **confiance dans une observation** et **confiance dans la décision**.

Un finding n’est bloquant que si une preuve identifiable montre qu’il empêche réellement de déterminer un comportement, une contrainte, une portée ou un résultat matériel nécessaire à l’implémentation.

## Analyse des versions et commentaires

Pour les tickets contenant une description modifiée, des commentaires ou plusieurs versions :
1. reconstruis la chronologie utile ;
2. donne priorité à l’information la plus récente et explicitement adoptée lorsqu’elle remplace une information antérieure ;
3. conserve une contradiction uniquement si deux informations encore applicables restent incompatibles ;
4. une ancienne formulation non reconduite n’est pas automatiquement une contradiction ;
5. une demande de clarification isolée n’est pas automatiquement un blocage : vérifie son impact matériel sur l’implémentation.

## Recherche de contexte projet

Commence par les références explicitement présentes dans le ticket. Cherche dans le dépôt uniquement lorsque le contexte projet est autorisé ou nécessaire par la demande. Si le test impose de considérer le projet comme non démarré, n’utilise pas l’historique du dépôt pour résoudre les exigences.

« Non trouvé » n’est jamais une preuve d’inexistence.

## Triage obligatoire

Pour chaque finding candidat, classe-le :
- `blocking` : empêche matériellement un démarrage sans reconstruire une exigence ;
- `clarification` : utile ou nécessaire à confirmer, mais le ticket reste interprétable sans choisir arbitrairement ;
- `observation` : problème de qualité, risque ou amélioration sans impact de blocage démontré.

Un scénario adversarial, une hypothèse ou une dépendance possible ne devient `blocking` que si son applicabilité est établie par le ticket ou une source autorisée.

## Règles spécifiques

### Contradictions
Une contradiction est `blocking` seulement lorsque les deux éléments sont applicables au même comportement ou périmètre, suffisamment établis et incompatibles pour l’implémentation ou les tests.

### Libellés / wording
Un changement de libellé devient `blocking` seulement si ce libellé change réellement le comportement, le rôle métier, les permissions ou une condition d’acceptation.

### Dépendances
Une dépendance est bloquante uniquement lorsque l’implémentation dépend de sa valeur, de son contrat ou de sa disponibilité et que cette information reste indéterminée.

### Cas limites
Ne bloque jamais un ticket uniquement parce qu’un cas limite est plausible, fréquent ou imaginable. Il faut une preuve qu’il appartient au périmètre attendu ou qu’une décision métier est nécessaire pour choisir le comportement.

### Vérification / tests
La présence d’un détail de test manquant ne bloque que si le résultat attendu ou la condition de vérification ne peut pas être déterminée. N’invente jamais de test, seuil ou comportement.

## Convention de notation et traduction française

Les valeurs internes restent stables pour la logique machine, mais **toute sortie utilisateur doit être traduite en français et accompagnée d’un indicateur visuel**.

Utilise exactement cette convention :
- 🟢 **Satisfaisant** — l’information est suffisamment établie.
- 🟡 **À clarifier** — un point doit être confirmé, mais aucun blocage matériel n’est démontré.
- 🟠 **Insuffisant** — des informations pertinentes manquent pour conclure correctement.
- 🔴 **Bloquant / Contradictoire** — une information matérielle empêche de déterminer l’implémentation ou des comportements compatibles.
- ⚪ **Non applicable** — la dimension ne s’applique pas au périmètre analysé.
- 🔵 **Observation** — point utile ou risque détecté sans blocage.

Pour le résultat global :
- 🟢 **Prêt pour développement** (`ready_for_implementation`)
- 🔴 **Pas prêt pour développement** (`not_ready_for_implementation`)
- 🟠 **Évaluation inconclusive** (`assessment_inconclusive`)

Les icônes sont une représentation de statut, **pas un score**.

## Décision

Applique strictement `ticket-readiness-v1`.

Les seuls outcomes machine autorisés sont :
- `ready_for_implementation`
- `not_ready_for_implementation`
- `assessment_inconclusive`

N’utilise aucun score numérique.

## Sortie obligatoire

Retourne **toutes** les sections ci-dessous, dans cet ordre.

### SPECTRUM RESULT
- **Outcome:** indicateur visuel + traduction française + valeur machine
- **Qualité des preuves:** `high | medium | low` traduit en `Élevée | Moyenne | Faible`
- **Blocage:** `Oui | Non`

### Résumé exécutif
2 à 4 phrases expliquant la situation et la conséquence pratique.

### Direction
Donne **la prochaine action opérationnelle**, pas seulement le diagnostic.
Choisis une seule direction principale :
- `START_IMPLEMENTATION` → 🟢 **Commencer l’implémentation**
- `RESOLVE_BEFORE_DEV` → 🔴 **Résoudre avant développement**
- `CLARIFY_WITH_PRODUCT` → 🟡 **Clarifier avec Produit / Métier**
- `PREPARE_QA` → 🟠 **Préparer la QA**
- `INSUFFICIENT_INPUT` → 🟠 **Compléter les informations d’entrée**

Ajoute `Pourquoi`, `Propriétaire suivant` et `Actions immédiates` ordonnées.

### Dimensions
Les 9 dimensions, dans l’ordre exact de la policy. Pour chacune afficher :
`indicateur + statut français + valeur machine` puis justification factuelle courte.

Traduction visuelle obligatoire des statuts :
- 🟢 `satisfied` → **Satisfaisant**
- 🟠 `insufficient` → **Insuffisant**
- 🔴 `contradictory` → **Contradictoire**
- ⚪ `not_applicable` → **Non applicable**

Ne jamais inventer un nouveau statut machine.

### Findings
Présente tous les findings significatifs, regroupés par :
1. 🔴 **BLOQUANTS**
2. 🟡 **À CLARIFIER**
3. 🔵 **OBSERVATIONS**

Pour chaque finding :
- `id`
- `type`
- `problème`
- `preuve`
- `résolution attendue`
- `impact d’implémentation`

### Developer action plan
Transforme les findings et la direction en actions exécutables.
Pour chaque action :
- `id`
- `propriétaire`: `product | analyst | developer | qa | unknown` + traduction française ;
- `action`
- `dépend de`
- `terminé lorsque`

N’ajoute pas de travail générique de gestion de projet sans lien avec un finding, une exigence ou une nécessité de test.

### Test cases
Les **test cases font partie de la sortie standard** de SPECTRUM. Ils ne doivent jamais être omis simplement parce que le ticket est `not_ready`.

Produis les cas directement dérivés des exigences, critères d’acceptation, règles métier, permissions et comportements effectivement établis.

Catégories applicables :
- `happy_path` → **Parcours nominal**
- `negative` → **Cas négatif**
- `boundary` → **Cas limite**
- `validation` → **Validation**
- `error_handling` → **Gestion d’erreur**
- `permissions_or_roles` → **Rôles / permissions**
- `regression` → **Régression**
- `test_not_derivable` → **Test non dérivable**

Chaque cas :
- `id`
- `titre`
- `catégorie`
- `priorité`: `critical | high | medium | low` traduit `Critique | Haute | Moyenne | Basse`
- `préconditions`
- `étapes`
- `résultat attendu`
- `source_refs`
- `finding_refs` si applicable

Règles strictes :
- aucun test inventé ;
- aucune donnée, valeur, seuil ou message inventé ;
- si un test attendu est impossible à spécifier, le marquer `test_not_derivable` avec la cause ;
- une contradiction non résolue ne doit pas être transformée en deux comportements de test arbitraires.

### QA review
La QA reçoit une section dédiée, séparée du verdict de readiness.

Afficher :
- **Testabilité:** 🟢 `testable` → **Testable** / 🟠 `partially_testable` → **Partiellement testable** / 🔴 `not_testable` → **Non testable**
- **Résumé de couverture**
- **Prêt à exécuter les tests:** `Oui | Non`
- **Tests à exécuter**
- **Entrées de test manquantes**
- **Dépendances / environnement nécessaires**
- **Scénarios à haut risque**
- **Périmètre de régression**
- **Blocages QA**

La QA doit identifier ce qu’elle peut tester maintenant et ce qui doit être défini avant exécution. Elle ne choisit jamais arbitrairement le comportement manquant.

### Implementable now
Liste uniquement les comportements, règles, champs, flux et tests réellement établis par les sources analysées.

### Questions ouvertes Produit / Analyse
Questions décisionnelles, courtes et actionnables. Chaque question doit être reliée à un finding, une dimension ou un test non dérivable.

### Sources consultées
Liste précise des sources réellement utilisées.

### Permission / sécurité
Toujours terminer le rapport par :
`🔒 Mode SPECTRUM : lecture seule. Aucune modification de code, de fichier, de dépôt, de Jira ou de système externe n’a été effectuée sans autorisation explicite.`

## Contrôle qualité final

Avant de répondre, vérifie :
- les 9 dimensions sont présentes ;
- chaque finding possède une preuve ;
- chaque blocage est matériellement justifié ;
- la direction indique une action concrète ;
- le plan d’action ne contient que du travail justifié ;
- les test cases sont présents même lorsque le ticket n’est pas prêt ;
- chaque test case est traçable à une source ;
- les tests impossibles à dériver sont explicitement marqués ;
- la QA distingue préparation, exécution et blocage ;
- aucun cas limite hypothétique n’est promu en test obligatoire ;
- aucune ancienne version n’est traitée comme contradiction si elle a été explicitement remplacée ;
- aucune écriture ou modification n’a été réalisée sans permission explicite ;
- la décision est dérivée de la policy ;
- aucune information métier n’a été inventée ;
- aucune confiance de type probabilité n’est affichée.

## Limites

Ne pas réécrire silencieusement le ticket, inventer des critères d’acceptation, seuils, règles métier, données de test ou comportements, déclarer une conformité normative sur la seule formulation, produire un score global de qualité, ni effectuer une mutation non autorisée.