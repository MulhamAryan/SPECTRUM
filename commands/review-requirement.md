---
description: Revoir une exigence ou un ticket sous l'angle qualité des exigences, contexte, relations et traçabilité.
argument-hint: "[chemin-du-ticket-ou-texte]"
---

# SPECTRUM — Revue d'exigence

Analyse l'entrée fournie comme une revue ciblée des exigences.

## Exécution

## Orchestration

Tu es l'orchestrateur (conversation principale). Charge `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md`, `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`, `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` et `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`, puis exécute **uniquement** ce sous-ensemble du graphe, dans l'ordre de ses dépendances :

- Stages : ingest, contextualize, represent_requirements, analyze_requirements, analyze_business_rules, consolidate_findings, consolidate, compose_report
- Agents invoqués via `Task` : context-analyst, requirement-analyst, business-rule-analyst, report-composer

Pas de stage `decide_readiness` : cette revue ne rend pas de verdict de préparation, seulement des constats sur les exigences.

Chaque résultat d'agent est vérifié contre `${CLAUDE_PLUGIN_ROOT}/models/agent-execution-result.schema.json`. À la fin, transmets les résultats normalisés au rendu défini par `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml` et `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`.

Retourne en français : résumé, dimensions concernées, constats avec preuves, ambiguïtés/lacunes/contradictions, impact sur l'implémentation, questions ouvertes et prochaine action.

Ne décide pas d'un score. N'invente aucune exigence. Ne modifie aucun code, fichier, dépôt ou système externe sans autorisation explicite.
