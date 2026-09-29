---
description: Revoir la testabilité et dériver les cas de test à partir des exigences établies.
argument-hint: "[chemin-du-ticket-ou-texte]"
---

# SPECTRUM — Revue des tests

Analyse l'entrée pour déterminer ce qui est testable et produire les cas de test directement dérivables.

## Exécution

## Orchestration

Tu es l'orchestrateur (conversation principale). Charge `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md`, `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`, `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` et `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`, puis exécute **uniquement** ce sous-ensemble du graphe, dans l'ordre de ses dépendances :

- Stages : ingest, contextualize, represent_requirements, analyze_verification_validation, analyze_adversarial_requirements, qa, compose_report
- Agents invoqués via `Task` : context-analyst, verification-validation-analyst, adversarial-analyst, qa-analyst, report-composer

Pas de stage `decide_readiness`. Le rapport se concentre sur Cas de test et Revue QA.

Chaque résultat d'agent est vérifié contre `${CLAUDE_PLUGIN_ROOT}/models/agent-execution-result.schema.json`. À la fin, transmets les résultats normalisés au rendu défini par `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml` et `${CLAUDE_PLUGIN_ROOT}/outputs/ticket-analysis-report.yaml`.

Retourne en français : couverture observable, cas de test justifiés, tests non dérivables, préconditions et données établies, dépendances d'environnement, blocages QA et questions ouvertes.

N'invente aucune donnée, valeur, seuil, message ou comportement. Ne lance aucun test ayant un effet persistant sans autorisation explicite.
