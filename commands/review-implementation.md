---
description: Comparer un ticket ou une spécification avec les artefacts d'implémentation fournis et détecter les écarts traçables.
argument-hint: "[chemin-du-ticket-et-des-artefacts]"
---

# SPECTRUM — Revue de l'implémentation

Analyse la spécification et les artefacts d'implémentation explicitement fournis.

## Exécution et rendu

## Orchestration

Tu es l'orchestrateur (conversation principale). Charge `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md`, `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`, `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` et `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`, puis exécute **uniquement** ce sous-ensemble du graphe, dans l'ordre de ses dépendances :

- Stages : ingest, contextualize, represent_requirements, analyze_business_rules, analyze_cross_artifacts, analyze_spec_implementation_drift, consolidate_findings, consolidate, compose_report
- Agents invoqués via `Task` : context-analyst, business-rule-analyst, consistency-analyst, implementation-reviewer, report-composer

Les artefacts d'implémentation sont obligatoires : sans eux, `analyze_spec_implementation_drift` est bloqué et la commande le dit au lieu d'analyser à vide.

Chaque résultat d'agent est vérifié contre `${CLAUDE_PLUGIN_ROOT}/models/agent-execution-result.schema.json`. À la fin, transmets les résultats normalisés au rendu défini par `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml`.

Retourne en français : périmètre comparé, correspondances, écarts avérés, éléments non vérifiables, preuves et références, impact potentiel et actions recommandées.

Une absence de résultat n'est pas une preuve d'absence fonctionnelle. Ne simule pas un comportement d'exécution qui n'a pas été fourni. Ne modifie aucun code, fichier, dépôt ou système externe sans autorisation explicite.
