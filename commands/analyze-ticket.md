---
description: Analyse un ticket SPECTRUM de bout en bout avec orchestration d’agents spécialisés et produit un verdict de préparation au développement traçable.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Analyse de ticket

Analyse le ticket fourni pour déterminer si un développeur peut commencer l’implémentation sans devoir reconstruire lui-même une exigence matérielle manquante, ambiguë ou contradictoire.

## Orchestration obligatoire

Commence par charger :
- `${CLAUDE_PLUGIN_ROOT}/agents/supervisor.md`
- `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/agent-skill-contract.yaml`
- `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`
- `${CLAUDE_PLUGIN_ROOT}/policies/ticket-readiness-v1.yaml`
- `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/canonical-data-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/evidence-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/finding-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`

Le superviseur doit construire le plan d’exécution avant l’analyse détaillée. Chaque Skill exécuté doit être sélectionné par le registre, autorisé par l’agent concerné, chargé dans son intégralité, contrôlé sur ses préconditions et tracé jusqu’à ses sorties.

## Entrée

`$ARGUMENTS` est soit un chemin vers un fichier contenant le ticket, soit le texte du ticket. Si c’est un chemin, lis le fichier avant toute analyse.

## Sécurité et permissions — règle absolue

SPECTRUM fonctionne strictement en lecture seule par défaut. Sans autorisation explicite couvrant l’opération et la cible, il est interdit de modifier du code, des fichiers, le dépôt, les branches, les demandes de fusion, Jira, des systèmes externes ou un environnement persistant.

Une analyse, une recommandation, une direction, un constat, un verdict, un cas de test ou une revue qualité n’autorise jamais automatiquement une écriture.

## Principes d’analyse

Ne confonds jamais problème détecté et blocage, information absente et information prouvée nécessaire, ancienne formulation et contradiction actuelle, cas limite imaginable et cas requis, gravité d’un constat et décision de préparation.

Aucun agent ne décide seul de la préparation globale. Aucun accord entre agents ne constitue une preuve de vérité.

## Langue utilisateur

La sortie finale doit être entièrement en français. Aucun identifiant technique, statut machine, nom de champ interne, priorité machine, catégorie machine ou valeur interne ne doit être exposé.

Utilise les statuts visuels SPECTRUM :
- 🟢 **Satisfaisant**
- 🟡 **À clarifier**
- 🟠 **Insuffisant**
- 🔴 **Bloquant / Contradictoire**
- ⚪ **Non applicable**
- 🔵 **Observation**

Verdicts globaux :
- 🟢 **Prêt pour le développement**
- 🔴 **Pas prêt pour le développement**
- 🟠 **Évaluation inconclusive**

Qualité des preuves : **Élevée / Moyenne / Faible**.

## Sortie obligatoire

Le rapport doit contenir, dans cet ordre :

### Résultat SPECTRUM
Verdict, qualité des preuves et blocage.

### Résumé exécutif
Situation et conséquence pratique en 2 à 4 phrases.

### Direction
Une seule prochaine action opérationnelle, avec pourquoi, propriétaire suivant et actions immédiates.

### Dimensions
Les neuf dimensions de la politique, chacune avec indicateur visuel, statut français et justification factuelle :
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
🔴 Bloquants, 🟡 À clarifier, 🔵 Observations. Chaque constat doit disposer d’une preuve identifiable.

### Plan d’action développeur
Actions justifiées par les constats ou exigences, avec propriétaire, dépendances et condition de terminaison.

### Cas de test
Cas dérivés des comportements établis, avec parcours nominaux, cas négatifs, cas limites justifiés, validation, gestion d’erreur, rôles/permissions, régression et tests non dérivables lorsque nécessaire.

### Revue QA
Testabilité, couverture, disponibilité pour exécution, cas à exécuter, entrées manquantes, dépendances/environnement, risques, régression et blocages QA.

### Comportements implémentables maintenant
Uniquement les comportements réellement établis par les sources.

### Questions ouvertes Produit / Analyse
Questions courtes, décisionnelles et traçables.

### Sources consultées
Sources réellement utilisées et éléments de provenance utiles.

### Permission / sécurité
`🔒 Mode SPECTRUM : lecture seule. Aucune modification de code, de fichier, de dépôt, de Jira ou de système externe n’a été effectuée sans autorisation explicite.`

## Contrôle qualité final

Avant de répondre, vérifie :
- le plan d’orchestration identifie les agents et Skills exécutés ;
- chaque Skill est autorisé par son agent et respecte ses préconditions ;
- chaque exécution produit un état et des références de preuve ;
- les handoffs sont explicites et traçables ;
- aucune sortie d’agent n’est silencieusement ignorée ;
- la décision globale vient de la politique de préparation ;
- la sortie utilisateur est entièrement en français ;
- aucune mutation n’est effectuée sans autorisation explicite.

## Limites

Ne réécris pas silencieusement le ticket, n’invente pas de critères, seuils, règles métier, données, comportements ou preuves. Ne transforme pas une hypothèse en fait et n’effectue aucune mutation non autorisée.
