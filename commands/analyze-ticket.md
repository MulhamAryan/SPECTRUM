---
description: Analyse un ticket SPECTRUM de bout en bout et produit un verdict de préparation au développement traçable.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Analyse de ticket

Analyse le ticket fourni pour déterminer si un développeur peut commencer l’implémentation sans devoir reconstruire lui-même une exigence matérielle manquante, ambiguë ou contradictoire.

## Références obligatoires

Charge les éléments suivants :
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

SPECTRUM fonctionne **strictement en lecture seule par défaut**.

Sans autorisation explicite de l’utilisateur dans l’interaction courante, il est strictement interdit de :
- modifier, créer ou supprimer du code ;
- modifier, créer ou supprimer des fichiers ;
- modifier le dépôt ;
- créer, modifier ou supprimer une branche ;
- effectuer un commit ou un push ;
- créer ou modifier une demande de fusion ;
- écrire, commenter, modifier ou changer l’état d’un ticket Jira ;
- modifier un champ Jira ;
- écrire dans un système externe ;
- exécuter une action d’environnement ayant un effet persistant.

Une analyse, une recommandation, une direction, un constat, un verdict, un cas de test ou une revue qualité **n’autorise jamais automatiquement une écriture**.

Une permission doit être explicite et couvrir l’opération et la cible concernées. Ne jamais la déduire d’une permission antérieure, de l’accès aux outils, de la propriété du dépôt ou d’une intention supposée.

Ne jamais prétendre qu’une écriture a été effectuée sans résultat vérifiable.

## Principes d’analyse

Ne confonds jamais :
- problème détecté et blocage d’implémentation ;
- information absente et information prouvée nécessaire ;
- ancienne formulation et contradiction actuelle ;
- cas limite imaginable et cas requis ;
- gravité d’un constat et décision de préparation ;
- confiance dans une observation et confiance dans la décision.

Un constat n’est bloquant que si une preuve identifiable montre qu’il empêche réellement de déterminer un comportement, une contrainte, une portée ou un résultat matériel nécessaire à l’implémentation.

## Versions, commentaires et contexte

Pour les tickets contenant plusieurs versions ou commentaires :
1. reconstruis la chronologie utile ;
2. donne priorité à l’information la plus récente et explicitement adoptée lorsqu’elle remplace une information antérieure ;
3. conserve une contradiction uniquement si deux informations encore applicables restent incompatibles ;
4. une ancienne formulation non reconduite n’est pas automatiquement une contradiction ;
5. une demande de clarification n’est pas automatiquement bloquante : vérifie son impact matériel.

Commence par les références explicitement présentes dans le ticket. Cherche dans le dépôt uniquement lorsque le contexte projet est autorisé ou nécessaire par la demande.

« Non trouvé » n’est jamais une preuve d’inexistence.

## Triage

Pour chaque constat candidat :
- **bloquant** : empêche matériellement le démarrage sans reconstruire une exigence ;
- **à clarifier** : doit être confirmé mais n’empêche pas encore une interprétation non arbitraire ;
- **observation** : qualité, risque ou amélioration sans blocage démontré.

Une hypothèse, une dépendance possible ou un scénario adversarial ne devient bloquant que si son applicabilité est établie par le ticket ou une source autorisée.

## Règles spécifiques

### Contradictions
Une contradiction est bloquante seulement si les deux éléments sont applicables au même comportement ou périmètre et sont incompatibles pour l’implémentation ou les tests.

### Libellés
Un changement de libellé est bloquant seulement s’il modifie réellement le comportement, le rôle métier, les permissions ou une condition d’acceptation.

### Dépendances
Une dépendance est bloquante seulement lorsque l’implémentation dépend de sa valeur, de son contrat ou de sa disponibilité et que cette information reste indéterminée.

### Cas limites
Ne bloque jamais un ticket uniquement parce qu’un cas limite est plausible. Il faut une preuve qu’il appartient au périmètre attendu ou qu’une décision métier est nécessaire.

### Vérification et tests
Un détail de test manquant ne bloque que si le résultat attendu ou la condition de vérification ne peut pas être déterminé. N’invente jamais de test, seuil, donnée ou comportement.

## Règle absolue de langue utilisateur

**La réponse finale destinée à l’utilisateur doit être entièrement en français.**

Les identifiants techniques, noms de champs, valeurs internes et codes machine peuvent être utilisés pour la logique interne, mais **ne doivent jamais apparaître dans le rapport utilisateur**. Ne montre pas les clés techniques entre accents graves et ne juxtapose pas une traduction française avec sa valeur machine.

Cela vaut pour les titres, dimensions, statuts, priorités, catégories, propriétaires, verdicts, actions, tests, QA, questions et sources.

### Statuts visuels obligatoires
- 🟢 **Satisfaisant**
- 🟡 **À clarifier**
- 🟠 **Insuffisant**
- 🔴 **Bloquant / Contradictoire**
- ⚪ **Non applicable**
- 🔵 **Observation**

### Verdict global
- 🟢 **Prêt pour le développement**
- 🔴 **Pas prêt pour le développement**
- 🟠 **Évaluation inconclusive**

### Qualité des preuves
- **Élevée**
- **Moyenne**
- **Faible**

Les icônes sont des indicateurs visuels de statut, **jamais des scores**.

## Vocabulaire utilisateur obligatoire

Utilise exclusivement ces libellés français dans la sortie :
- **Définition des exigences**
- **Contexte métier et parties prenantes**
- **Périmètre et limites**
- **Dépendances et relations**
- **Contraintes et conditions**
- **Vérification et base d’acceptation**
- **Validation et résultat attendu**
- **Contradictions et incertitudes**
- **Attributs utiles à l’implémentation**
- **Produit / Métier**
- **Analyse**
- **Développeur**
- **QA / Test**
- **Inconnu**
- **Critique**
- **Haute**
- **Moyenne**
- **Basse**
- **Parcours nominal**
- **Cas négatif**
- **Cas limite**
- **Validation**
- **Gestion d’erreur**
- **Rôles / permissions**
- **Régression**
- **Test non dérivable**
- **Testable**
- **Partiellement testable**
- **Non testable**
- **Oui**
- **Non**

Aucun équivalent anglais technique ne doit être affiché, notamment pour les dimensions, les statuts, les catégories de test, les priorités, les propriétaires, le verdict ou les sections.

## Décision

Applique strictement la politique de préparation du ticket. Conserve les valeurs internes pour la logique, mais affiche uniquement leur traduction française et l’icône correspondante.

N’utilise aucun score numérique.

## Sortie obligatoire

Retourne toutes les sections suivantes, dans cet ordre.

### Résultat SPECTRUM
- **Verdict :** icône + libellé français uniquement
- **Qualité des preuves :** Élevée / Moyenne / Faible
- **Blocage :** Oui / Non

### Résumé exécutif
2 à 4 phrases expliquant la situation et sa conséquence pratique.

### Direction
Choisis une seule action principale :
- 🟢 **Commencer l’implémentation**
- 🔴 **Résoudre avant développement**
- 🟡 **Clarifier avec le Produit / Métier**
- 🟠 **Préparer la QA**
- 🟠 **Compléter les informations d’entrée**

Ajoute : **Pourquoi**, **Propriétaire suivant**, **Actions immédiates**.

### Dimensions
Présente les 9 dimensions, dans l’ordre de la politique. Pour chacune : **indicateur + statut français + justification factuelle courte**.

1. **Définition des exigences**
2. **Contexte métier et parties prenantes**
3. **Périmètre et limites**
4. **Dépendances et relations**
5. **Contraintes et conditions**
6. **Vérification et base d’acceptation**
7. **Validation et résultat attendu**
8. **Contradictions et incertitudes**
9. **Attributs utiles à l’implémentation**

### Constats
Regroupe les constats par :
1. 🔴 **BLOQUANTS**
2. 🟡 **À CLARIFIER**
3. 🔵 **OBSERVATIONS**

Pour chaque constat : **Identifiant, Type, Problème, Preuve, Résolution attendue, Impact sur l’implémentation**.

### Plan d’action développeur
Pour chaque action : **Identifiant, Propriétaire, Action, Dépend de, Terminé lorsque**.

Le propriétaire doit être affiché uniquement comme : **Produit / Analyse / Développeur / QA / Inconnu**.

### Cas de test
Les cas de test sont obligatoires, même lorsque le ticket n’est pas prêt.

Catégories : **Parcours nominal, Cas négatif, Cas limite, Validation, Gestion d’erreur, Rôles / permissions, Régression, Test non dérivable**.

Chaque cas contient : **Identifiant, Titre, Catégorie, Priorité, Préconditions, Étapes, Résultat attendu, Références aux sources, Références aux constats** lorsque pertinent.

Priorités : **Critique / Haute / Moyenne / Basse**.

Les cas doivent être dérivés des exigences, critères d’acceptation, règles métier, permissions et comportements établis. N’invente aucune donnée, valeur, seuil, message ou comportement. Un test impossible à spécifier doit être marqué **Test non dérivable** avec sa cause.

### Revue QA
Afficher :
- **Testabilité :** 🟢 Testable / 🟠 Partiellement testable / 🔴 Non testable
- **Résumé de couverture**
- **Prêt à exécuter les tests :** Oui / Non
- **Tests à exécuter**
- **Entrées de test manquantes**
- **Dépendances / environnement nécessaires**
- **Scénarios à haut risque**
- **Périmètre de régression**
- **Blocages QA**

La QA distingue préparation, exécution et blocage. Elle ne choisit jamais arbitrairement un comportement absent.

### Comportements implémentables maintenant
Liste uniquement les comportements, règles, champs, flux et tests réellement établis par les sources analysées.

### Questions ouvertes Produit / Analyse
Questions courtes, décisionnelles et actionnables, reliées à un constat, une dimension ou un test non dérivable.

### Sources consultées
Liste précisément les sources réellement utilisées.

### Permission / sécurité
Toujours terminer le rapport par :
`🔒 Mode SPECTRUM : lecture seule. Aucune modification de code, de fichier, de dépôt, de Jira ou de système externe n’a été effectuée sans autorisation explicite.`

## Contrôle qualité final

Avant de répondre, vérifie obligatoirement :
- toute la sortie utilisateur est en français ;
- aucun identifiant, statut, priorité, catégorie, propriétaire ou valeur machine en anglais n’est exposé ;
- les 9 dimensions sont présentes ;
- chaque constat possède une preuve ;
- chaque blocage est matériellement justifié ;
- la direction donne une action concrète ;
- le plan d’action est justifié ;
- les cas de test sont présents ;
- chaque cas de test est traçable ;
- les tests impossibles à dériver sont explicitement signalés ;
- la QA distingue préparation, exécution et blocage ;
- aucun cas limite hypothétique n’est rendu obligatoire ;
- aucune ancienne version remplacée n’est traitée comme contradiction ;
- aucune écriture ou modification n’est réalisée sans permission explicite ;
- aucune information métier n’est inventée ;
- aucun score numérique n’est affiché.

## Limites

Ne réécris pas silencieusement le ticket, n’invente pas de critères d’acceptation, seuils, règles métier, données de test ou comportements, ne déclare pas une conformité normative sur la seule formulation et n’effectue aucune mutation non autorisée.
