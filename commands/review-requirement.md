---
description: Revoir une exigence ou un ticket sous l'angle qualité des exigences, contexte, relations et traçabilité.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Revue d'exigence

Analyse l'entrée fournie comme une revue ciblée des exigences.

## Exécution

Utilise le superviseur SPECTRUM et les Skills autorisés pour cette revue. À la fin de l'analyse, transmets les résultats normalisés au moteur central `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml` et `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`.

Retourne en français : résumé, dimensions concernées, constats avec preuves, ambiguïtés/lacunes/contradictions, impact sur l'implémentation, questions ouvertes et prochaine action.

Ne décide pas d'un score. N'invente aucune exigence. Ne modifie aucun code, fichier, dépôt ou système externe sans autorisation explicite.
