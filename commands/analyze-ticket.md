---
description: Analyse un ticket SPECTRUM de bout en bout et produit un verdict de readiness traçable.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Analyse de ticket

Exécute une analyse SPECTRUM complète du ticket fourni. Le but est de déterminer si les informations disponibles sont suffisantes pour qu’un développeur commence l’implémentation sans devoir reconstruire lui-même les exigences.

## Entrée

`$ARGUMENTS` est soit :
- un chemin vers un fichier contenant le ticket ;
- soit le texte du ticket.

S’il s’agit d’un chemin, lis le fichier avant toute analyse.

Charge comme références normatives du moteur :
- `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`
- `${CLAUDE_PLUGIN_ROOT}/policies/ticket-readiness-v1.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/canonical-data-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/evidence-model.yaml`
- `${CLAUDE_PLUGIN_ROOT}/models/finding-model.yaml`

## Règle d’exécution MVP

Exécute le workflow dans son ordre de dépendance, mais sans prétendre disposer d’un moteur externe. Le modèle joue le rôle d’orchestrateur d’exécution et applique les Skills SPECTRUM présents dans `skills/`.

Pour chaque étape :
1. conserve le contenu source du ticket ;
2. distingue faits source, observations analytiques, findings et décision ;
3. ne fabrique aucune information métier absente ;
4. conserve les incertitudes et contradictions ;
5. cite les éléments du ticket ou des fichiers de projet utilisés comme preuve.

Pour le premier passage, couvre au minimum les analyses suivantes lorsqu’elles sont applicables :
- contexte et périmètre ;
- qualité des exigences ;
- vérification / validation ;
- règles métier ;
- analyse adversariale ;
- cohérence entre artefacts disponibles ;
- dérive spécification ↔ implémentation lorsque du code ou des artefacts d’implémentation sont fournis ;
- seconde opinion indépendante lorsque suffisamment de matière est disponible.

Puis consolide les findings et applique `ticket-readiness-v1`.

## Recherche de contexte projet

Ne cherche pas partout aveuglément. Commence par les fichiers explicitement référencés par le ticket. Si le ticket contient des identifiants, noms de fichiers, endpoints, tables, composants, règles ou liens, utilise-les pour retrouver le contexte dans le dépôt.

Ne considère jamais « non trouvé dans le dépôt » comme preuve d’inexistence du besoin ou de l’artefact.

## Décision

Le résultat final doit être exactement l’un des états prévus par la policy :
- `ready_for_implementation`
- `not_ready_for_implementation`
- `assessment_inconclusive`

La décision doit être dérivée des dimensions de readiness de la policy. N’utilise aucun score numérique inventé.

## Sortie

Retourne un rapport compact avec cette structure :

### SPECTRUM RESULT
- **Outcome:** `ready_for_implementation` | `not_ready_for_implementation` | `assessment_inconclusive`
- **Confidence:** factuelle, sous forme de niveau de preuve (`high` | `medium` | `low`), jamais comme probabilité
- **Blocking:** oui/non

### Dimensions
Pour chacune des 9 dimensions de la policy :
`status` (`satisfied` | `insufficient` | `contradictory` | `not_applicable`) + justification factuelle en une phrase.

### Findings bloquants
Pour chaque finding bloquant :
- identifiant local SPECTRUM ;
- problème ;
- preuve ;
- information attendue ;
- impact sur l’implémentation.

### Contradictions / incertitudes
Lister uniquement celles qui influencent l’interprétation ou la décision.

### Ce que le développeur peut réellement implémenter
Décrire les éléments suffisamment établis, sans compléter les trous par des hypothèses.

### Sources utilisées
Lister les fichiers / fragments réellement consultés.

## Limites

Ne pas :
- réécrire silencieusement le ticket ;
- présenter une hypothèse comme un fait ;
- transformer un finding de qualité en décision sans passer par la policy ;
- inventer des critères d’acceptation, seuils, règles métier ou comportements ;
- déclarer la conformité à une norme sur la seule base d’une formulation ;
- donner un score global de qualité.
