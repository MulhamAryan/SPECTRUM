---
description: Revoir la testabilité et dériver les cas de test à partir des exigences établies.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Revue des tests

Analyse l'entrée pour déterminer ce qui est testable et produire les cas de test directement dérivables.

## Exécution

Utilise le superviseur SPECTRUM et les Skills autorisés pour cette revue. À la fin de l'analyse, transmets les résultats normalisés au moteur central `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml` et `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`.

Retourne en français : couverture observable, cas de test justifiés, tests non dérivables, préconditions et données établies, dépendances d'environnement, blocages QA et questions ouvertes.

N'invente aucune donnée, valeur, seuil, message ou comportement. Ne lance aucun test ayant un effet persistant sans autorisation explicite.
