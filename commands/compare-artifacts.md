---
description: Comparer deux artefacts ou deux versions pour détecter les correspondances, écarts et contradictions traçables.
argument-hint: "[artefact-a] [artefact-b]"
---

# SPECTRUM — Comparaison d'artefacts

Compare uniquement les deux artefacts explicitement fournis.

## Exécution et rendu

## Orchestration

Tu es l'orchestrateur (conversation principale). Charge `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md`, `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`, `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` et `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`, puis exécute **uniquement** ce sous-ensemble du graphe, dans l'ordre de ses dépendances :

- Stages : ingest (les deux artefacts), contextualize, represent_requirements, analyze_cross_artifacts, consolidate_findings, consolidate, compose_report
- Agents invoqués via `Task` : context-analyst, consistency-analyst, report-composer

Les deux artefacts sont obligatoires ; `analyze_cross_artifacts` est le cœur de la commande.

Chaque résultat d'agent est vérifié contre `${CLAUDE_PLUGIN_ROOT}/models/agent-execution-result.schema.json`. À la fin, transmets les résultats normalisés au rendu défini par `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml`.

Retourne en français : périmètre de comparaison, éléments alignés, différences de représentation, écarts ou contradictions avérés, correspondances manquantes, éléments non comparables, preuves, références et actions suivantes.

Ne transforme jamais directement une comparaison en verdict de préparation. Ne réécris pas silencieusement les sources et ne modifie aucun artefact ou système externe sans autorisation explicite.
