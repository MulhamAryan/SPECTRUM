---
description: Analyse un ticket SPECTRUM de bout en bout avec orchestration réelle d’agents spécialisés et produit un verdict de préparation au développement traçable.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Analyse de ticket

Analyse le ticket fourni pour déterminer si un développeur peut commencer l’implémentation sans devoir reconstruire lui-même une exigence matérielle manquante, ambiguë ou contradictoire.

## Orchestration obligatoire

Charge d'abord :
- `${CLAUDE_PLUGIN_ROOT}/agents/supervisor.md`
- `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/agent-skill-contract.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/agent-orchestration.yaml`
- `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`
- `${CLAUDE_PLUGIN_ROOT}/policies/ticket-readiness-v1.yaml`
- `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/canonical-data-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/evidence-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/finding-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`

Le superviseur doit construire puis exécuter le graphe d'analyse. Il ne doit pas seulement décrire ce graphe.

### Exécution

1. Créer un identifiant d'analyse unique.
2. Identifier les artefacts et sources réellement disponibles.
3. Sélectionner les agents selon le registre et les conditions d'applicabilité.
4. Invoquer les agents sélectionnés avec le mécanisme `Task` de Claude Code.
5. Pour chaque agent, transmettre uniquement les entrées amont nécessaires et demander explicitement le chargement de ses Skills autorisés.
6. Exiger de chaque agent une sortie structurée contenant ses exécutions de Skills, états, preuves, constats, incertitudes, handoffs et limites.
7. Exécuter en parallèle uniquement les agents dont les dépendances sont satisfaites.
8. Attendre les résultats nécessaires avant tout agent dépendant.
9. Continuer les branches indépendantes en cas d'échec d'une branche.
10. Ne jamais remplacer un résultat manquant par une supposition.
11. Transmettre tous les résultats matériels au moteur de consolidation et au compositeur du rapport.

### Graphe minimal d'une analyse complète

```text
Contextualisation
       ↓
┌─────────────────────────────────────────────────────┐
│ Exigences │ Règles métier │ Vérif./Validation │ Cycle│
└─────────────────────────────────────────────────────┘
       ↓
┌───────────────────────────┬─────────────────────────┐
│ Analyse adversariale      │ Cohérence inter-artefacts│
└───────────────────────────┴─────────────────────────┘
       ↓
┌───────────────────────────┬─────────────────────────┐
│ Revue implémentation      │ Seconde analyse          │
└───────────────────────────┴─────────────────────────┘
       ↓
      QA
       ↓
 Consolidation
       ↓
 Décision de préparation
       ↓
 Rapport
```

La revue d'implémentation et la cohérence ne sont exécutées que lorsque leurs artefacts d'entrée existent. La seconde analyse n'est exécutée que lorsqu'elle est demandée ou requise par le workflow/politique.

## Entrée

`$ARGUMENTS` est soit un chemin vers un fichier contenant le ticket, soit le texte du ticket. Si c’est un chemin, lis le fichier avant toute analyse.

## Sécurité et permissions — règle absolue

SPECTRUM fonctionne strictement en lecture seule par défaut. Sans autorisation explicite couvrant l’opération et la cible, il est interdit de modifier du code, des fichiers, le dépôt, les branches, les demandes de fusion, Jira, des systèmes externes ou un environnement persistant.

Une analyse, une recommandation, une direction, un constat, un verdict, un cas de test ou une revue qualité n’autorise jamais automatiquement une écriture.

## Règles d’intégrité d'exécution

- Chaque Skill doit être autorisé par l'agent exécutant.
- Chaque Skill doit être chargé avant son utilisation.
- Les préconditions doivent être vérifiées.
- La procédure du Skill doit être suivie intégralement.
- Le résultat du Skill doit être conservé avec ses références de preuve.
- Chaque handoff doit avoir une raison et des références d'entrée.
- Une analyse indépendante doit rester isolée de l'analyse principale jusqu'à sa propre production.
- Un échec doit rester visible et ne jamais être converti en succès implicite.
- Aucun agent ne décide seul de la préparation globale.

## Langue utilisateur

La sortie finale doit être entièrement en français. Aucun identifiant technique, statut machine, nom de champ interne, priorité machine, catégorie machine ou valeur interne ne doit être exposé.

## Sortie obligatoire

Le rapport doit contenir, dans cet ordre :

### Résultat SPECTRUM
Verdict, qualité des preuves et blocage.

### Résumé exécutif
Situation et conséquence pratique en 2 à 4 phrases.

### Direction
Une seule prochaine action opérationnelle, avec pourquoi, propriétaire suivant et actions immédiates.

### Dimensions
Les neuf dimensions de la politique, chacune avec indicateur visuel, statut français et justification factuelle.

### Constats
🔴 Bloquants, 🟡 À clarifier, 🔵 Observations. Chaque constat doit disposer d’une preuve identifiable.

### Plan d’action développeur
Actions justifiées par les constats ou exigences, avec propriétaire, dépendances et condition de terminaison.

### Cas de test
Cas dérivés des comportements établis, y compris les cas non dérivables lorsque nécessaire.

### Revue QA
Testabilité, couverture, disponibilité pour exécution, entrées manquantes, dépendances, risques, régression et blocages.

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
- une exécution du superviseur a réellement été réalisée ;
- les agents sélectionnés sont justifiés ;
- chaque agent a reçu ses entrées nécessaires ;
- les Skills obligatoires ont été exécutés lorsqu'applicables ;
- les préconditions et états d'exécution sont présents ;
- les handoffs sont explicites ;
- les branches parallèles ne consomment pas de résultats inexistants ;
- les échecs ne sont jamais masqués ;
- tous les constats et preuves sont récupérés ;
- la décision globale vient de la politique de préparation ;
- la sortie utilisateur est entièrement en français ;
- aucune mutation n’a été effectuée sans autorisation explicite.

## Limites

Ne réécris pas silencieusement le ticket, n’invente pas de critères, seuils, règles métier, données, comportements ou preuves. Ne transforme pas une hypothèse en fait et n’effectue aucune mutation non autorisée.
