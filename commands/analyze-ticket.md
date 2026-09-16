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

Exemple : « OTP 5 chiffres » dans une contrainte projet toujours applicable contre « OTP 6 chiffres » dans l’exigence active = blocage potentiel. Une ancienne formulation remplacée par une nouvelle sans conflit encore actif ≠ contradiction.

### Libellés / wording
Un changement de libellé (`Chauffeur` → `Livreur`, par exemple) devient `blocking` seulement si ce libellé change réellement le comportement, le rôle métier, les permissions ou une condition d’acceptation. Un wording ancien dans un commentaire n’est pas bloquant à lui seul si la formulation actuelle est explicite.

### Dépendances
Une dépendance est bloquante uniquement lorsque l’implémentation dépend de sa valeur, de son contrat ou de sa disponibilité et que cette information reste indéterminée. La simple mention « à confirmer » doit être analysée selon son impact matériel.

### Cas limites
Ne bloque jamais un ticket uniquement parce qu’un cas limite est plausible, fréquent ou imaginable. Il faut une preuve qu’il appartient au périmètre attendu ou qu’une décision métier est nécessaire pour choisir le comportement.

### Vérification / tests
La présence d’un détail de test manquant ne bloque que si le résultat attendu ou la condition de vérification ne peut pas être déterminée. N’invente jamais de test, seuil ou comportement.

## Décision

Applique ensuite strictement `ticket-readiness-v1`.

Les seuls outcomes autorisés sont :
- `ready_for_implementation`
- `not_ready_for_implementation`
- `assessment_inconclusive`

N’utilise aucun score numérique.

## Sortie

Retourne exactement les sections suivantes, sans texte inutile :

### SPECTRUM RESULT
- **Outcome:** ...
- **Evidence quality:** `high` | `medium` | `low` — qualité de la preuve disponible, pas probabilité de vérité.
- **Blocking:** `yes` | `no`

### Executive summary
2 à 4 phrases maximum expliquant pourquoi le ticket est ou n’est pas implémentable.

### Dimensions
Les **9 dimensions**, dans l’ordre exact de la policy. Pour chacune :
`status` parmi `satisfied | insufficient | contradictory | not_applicable` + justification factuelle courte.

Ne jamais remplacer ces statuts par `gap`, `ambiguous`, `blocked` ou d’autres variantes.

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

### Contradictions / incertitudes
Uniquement les éléments non résolus qui affectent l’interprétation ou la décision.

### Implementable now
Liste uniquement les comportements, règles, champs, flux et tests réellement établis par les sources analysées. Ne complète aucune information manquante.

### Sources consulted
Liste précise des sources réellement utilisées.

## Contrôle qualité final

Avant de répondre, vérifie :
- les 9 dimensions sont présentes ;
- chaque finding possède une preuve ;
- chaque blocage est matériellement justifié ;
- aucun cas limite hypothétique n’est promu en blocage ;
- aucune ancienne version n’est traitée comme contradiction si elle a été explicitement remplacée ;
- la décision est dérivée de la policy ;
- aucune information métier n’a été inventée ;
- aucune confiance de type probabilité n’est affichée.

## Limites

Ne pas réécrire silencieusement le ticket, inventer des critères d’acceptation, seuils, règles métier ou comportements, déclarer une conformité normative sur la seule formulation, ni produire un score global de qualité.