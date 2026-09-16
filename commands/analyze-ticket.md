---
description: Analyse un ticket SPECTRUM de bout en bout et produit un verdict de readiness traçable.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Analyse de ticket

Analyse le ticket fourni pour répondre à une seule question : **un développeur peut-il commencer l’implémentation sans reconstruire une exigence matérielle manquante, ambiguë ou contradictoire ?**

## Entrée

`$ARGUMENTS` est soit un chemin vers un fichier contenant le ticket, soit le texte du ticket. Si c’est un chemin, lis le fichier avant toute analyse.

Charge comme références du moteur :
- `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`
- `${CLAUDE_PLUGIN_ROOT}/policies/ticket-readiness-v1.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/canonical-data-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/evidence-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/finding-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`

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

## Triage obligatoire avant readiness

Pour chaque finding candidat, classe-le :
- `blocking` : empêche matériellement un démarrage sans reconstruire une exigence ;
- `clarification` : utile ou nécessaire à confirmer, mais le ticket reste interprétable sans choisir arbitrairement ;
- `observation` : problème de qualité, risque ou amélioration sans impact de blocage démontré.

Un scénario adversarial, une hypothèse ou une dépendance possible ne devient `blocking` que si son applicabilité est établie par le ticket ou une source autorisée.

## Règles spécifiques

### Contradictions
Une contradiction est `blocking` seulement lorsque les deux éléments sont :
- applicables au même comportement ou périmètre ;
- suffisamment établis ;
- incompatibles pour l’implémentation ou les tests.

### Libellés / wording
Un changement de libellé devient `blocking` seulement si ce libellé change réellement le comportement, le rôle métier, les permissions ou une condition d’acceptation. Un wording ancien dans un commentaire n’est pas bloquant à lui seul si la formulation actuelle est explicite.

### Dépendances
Une dépendance est bloquante uniquement lorsque l’implémentation dépend de sa valeur, de son contrat ou de sa disponibilité et que cette information reste indéterminée. La simple mention « à confirmer » doit être analysée selon son impact matériel.

### Cas limites
Ne bloque jamais un ticket uniquement parce qu’un cas limite est plausible, fréquent ou imaginable. Il faut une preuve qu’il appartient au périmètre attendu ou qu’une décision métier est nécessaire pour choisir le comportement.

### Vérification / tests
La présence d’un détail de test manquant ne bloque que si le résultat attendu ou la condition de vérification ne peut pas être déterminée. N’invente jamais de test, seuil ou comportement.

## Décision

Applique strictement `ticket-readiness-v1`.

Les seuls outcomes autorisés sont :
- `ready_for_implementation`
- `not_ready_for_implementation`
- `assessment_inconclusive`

N’utilise aucun score numérique.

## Sortie obligatoire

Retourne **toutes** les sections ci-dessous, dans cet ordre.

### SPECTRUM RESULT
- **Outcome:** ...
- **Evidence quality:** `high` | `medium` | `low` — qualité de la preuve disponible, pas probabilité de vérité.
- **Blocking:** `yes` | `no`

### Executive summary
2 à 4 phrases expliquant la situation et la conséquence pratique.

### Direction
Donne **la prochaine action opérationnelle**, pas seulement le diagnostic.
Choisis une seule direction principale :
- `START_IMPLEMENTATION` : les éléments nécessaires sont suffisamment établis ;
- `RESOLVE_BEFORE_DEV` : un ou plusieurs blocages matériels doivent être résolus avant le développement ;
- `CLARIFY_WITH_PRODUCT` : une décision métier/produit ciblée doit être obtenue ;
- `PREPARE_QA` : le périmètre est suffisamment défini pour préparer les tests mais pas pour développer ;
- `INSUFFICIENT_INPUT` : il manque des informations permettant même de préparer correctement le travail.

Ajoute ensuite `why`, `next_owner` et `next_actions` ordonnées. Cette section ne remplace pas l’outcome de readiness ; elle traduit le résultat en action.

### Dimensions
Les 9 dimensions, dans l’ordre exact de la policy. Pour chacune :
`status` parmi `satisfied | insufficient | contradictory | not_applicable` + justification factuelle courte.

### Findings
Présente tous les findings significatifs, regroupés par :
1. `BLOCKING`
2. `CLARIFICATION`
3. `OBSERVATION`

Pour chaque finding :
- `id`
- `type`
- `problem`
- `evidence`
- `required_resolution`
- `implementation_impact`

La section `BLOCKING` doit être vide lorsqu’aucun blocage matériel n’est démontré.

### Developer action plan
Transforme les findings et la direction en actions exécutables.
Pour chaque action :
- `id`
- `owner`: `product | analyst | developer | qa | unknown`
- `action`
- `depends_on`
- `done_when`

N’ajoute pas de travail générique de gestion de projet sans lien avec un finding, une exigence ou une nécessité de test.

### Test cases
Les **test cases font partie de la sortie standard** de SPECTRUM. Ils ne doivent jamais être omis simplement parce que le ticket est `not_ready`.

Produis les cas directement dérivés des exigences, critères d’acceptation, règles métier et comportements effectivement établis.

Catégories à couvrir lorsqu’elles sont applicables :
- `happy_path`
- `negative`
- `boundary`
- `validation`
- `error_handling`
- `permissions_or_roles`
- `regression`

Chaque cas :
- `id`
- `title`
- `category`
- `priority`: `critical | high | medium | low`
- `preconditions`
- `steps`
- `expected_result`
- `source_refs`

Règles strictes :
- aucun test inventé ;
- ne pas inventer de données, valeurs, seuils ou messages ;
- si un test est attendu mais impossible à spécifier, créer un item `test_not_derivable` avec la cause et le finding associé ;
- les contradictions doivent générer des tests distincts uniquement lorsque les deux comportements sont réellement spécifiés et comparables ; sinon demander la clarification.

### QA review
La QA reçoit une section dédiée, séparée du verdict de readiness.

Inclure :
- `testability_status`: `testable | partially_testable | not_testable`
- `coverage_summary`
- `ready_for_test_execution`: `yes | no`
- `test_cases_to_execute`: références des cas dérivés
- `missing_test_inputs`
- `environment_or_dependency_needs`
- `high_risk_scenarios`
- `regression_scope`
- `qa_blockers`

La QA doit identifier ce qu’elle peut tester maintenant et ce qui doit être défini avant exécution. Elle ne choisit pas arbitrairement le comportement manquant.

### Implementable now
Liste uniquement les comportements, règles, champs, flux et tests réellement établis par les sources analysées.

### Open questions for Product / Analysis
Questions **décisionnelles**, courtes et actionnables. Chaque question doit être reliée à un finding, une dimension ou un test non dérivable.

### Sources consulted
Liste précise des sources réellement utilisées.

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
- la décision est dérivée de la policy ;
- aucune information métier n’a été inventée ;
- aucune confiance de type probabilité n’est affichée.

## Limites

Ne pas réécrire silencieusement le ticket, inventer des critères d’acceptation, seuils, règles métier, données de test ou comportements, déclarer une conformité normative sur la seule formulation, ni produire un score global de qualité.