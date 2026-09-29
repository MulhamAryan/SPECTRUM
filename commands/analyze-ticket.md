---
description: Analyse un ticket SPECTRUM de bout en bout en orchestrant les agents spécialisés depuis la conversation principale et produit un verdict de préparation au développement traçable.
argument-hint: [chemin-du-ticket-ou-texte] [--profile=quick|standard|full] [--lang=fr]
---

# SPECTRUM — Analyse de ticket

Analyse le ticket fourni pour déterminer si un développeur peut commencer l'implémentation sans devoir reconstruire lui-même une exigence matérielle manquante, ambiguë ou contradictoire.

## Tu es l'orchestrateur

Cette commande s'exécute dans la conversation principale, qui est la seule à disposer de `Task`. Il n'y a pas d'agent superviseur. Charge d'abord, dans cet ordre :

1. `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md` — comment exécuter le graphe
2. `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml` — le graphe, les profils, les conditions
3. `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` — skills autorisés par agent
4. `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`
5. La politique de préparation référencée par le profil (`policies/…`)
6. `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`

Les modèles de moteurs (`models/multi-source-reasoning.yaml`, `models/finding-engine.yaml`, `models/analysis-engine.yaml`, `models/ticket-readiness-engine.yaml`) sont chargés au moment où leur stage s'exécute, pas avant.

Puis suis la procédure d'orchestration **intégralement** : résolution du profil, ingestion, exécution du graphe via `Task`, vérification de chaque résultat contre le schéma, décision, QA, rapport, contrôle final.

## Entrée

`$ARGUMENTS` contient soit un chemin vers un fichier contenant le ticket, soit le texte du ticket, suivi d'options facultatives :

- `--profile=quick|standard|full` (défaut : `standard`) — voir `profiles` dans le workflow.
- `--lang=<code>` (défaut : `fr`) — langue du rapport utilisateur.

Si c'est un chemin, lis le fichier avant toute analyse.

## Sécurité et permissions — règle absolue

SPECTRUM fonctionne strictement en lecture seule. Le hook `spectrum-guard` bloque mécaniquement toute écriture pendant une analyse SPECTRUM. Si une action a été bloquée, mentionne-le dans la section Permission / sécurité du rapport ; ne la contourne jamais.

Une analyse, une recommandation, une direction, un constat, un verdict, un cas de test ou une revue qualité n'autorise jamais automatiquement une écriture.

## Règles d'intégrité d'exécution

- Chaque agent est invoqué via `Task` et reçoit uniquement ses entrées amont nécessaires.
- Chaque résultat d'agent est vérifié contre `models/agent-execution-result.schema.json` ; un résultat non conforme est un échec enregistré, jamais complété par toi.
- Un stage conditionnel non applicable est `not_applicable`, pas un échec.
- L'analyse indépendante ne reçoit aucune conclusion des autres agents.
- Un échec reste visible et n'est jamais converti en succès implicite.
- Aucun agent ne décide seul de la préparation globale ; la décision vient de la politique, appliquée par toi au stage `decide_readiness`.

## Sortie obligatoire

Le rapport est rendu par `report-composer` selon `outputs/ticket-analysis-report.yaml`, dans la langue `report_language`, avec dans cet ordre :

1. Résultat SPECTRUM — verdict, qualité des preuves, blocage.
2. Résumé exécutif — 2 à 4 phrases.
3. Direction — une seule prochaine action, pourquoi, propriétaire suivant, actions immédiates.
4. Dimensions — les dimensions de la politique appliquée, avec indicateur visuel, statut et justification factuelle.
5. Constats — 🔴 Bloquants, 🟡 À clarifier, 🔵 Observations, chacun avec un identifiant court lisible (C-01…) et sa preuve.
6. Plan d'action développeur.
7. Cas de test.
8. Revue QA.
9. Comportements implémentables maintenant.
10. Questions ouvertes Produit / Analyse.
11. Sources consultées.
12. Exécution — profil, agents invoqués, stages non applicables, échecs.
13. Permission / sécurité.
14. Annexe Traçabilité — correspondance entre identifiants courts du rapport et références techniques (`FND-`, `EV-`, `execution_id`).

## Contrôle final

Applique la section 8 de la procédure d'orchestration : vérifie tes propres structures d'exécution, pas une auto-attestation. Si un contrôle échoue, corrige l'exécution ou expose l'échec dans le rapport ; ne réponds pas avec un rapport qui prétend une exécution qui n'a pas eu lieu.

## Limites

Ne réécris pas silencieusement le ticket, n'invente pas de critères, seuils, règles métier, données, comportements ou preuves. Ne transforme pas une hypothèse en fait et n'effectue aucune mutation.
