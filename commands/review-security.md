---
description: Vérifier les frontières de sécurité et de permission d'une analyse SPECTRUM sans effectuer de mutation.
argument-hint: "[chemin-du-ticket-ou-texte]"
---

# SPECTRUM — Revue sécurité et permissions

Vérifie que l'analyse respecte le mode lecture seule et identifie toute action qui nécessiterait une autorisation explicite.

## Exécution et rendu

## Orchestration

Tu es l'orchestrateur (conversation principale). Charge `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md`, `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`, `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` et `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`, puis exécute **uniquement** ce sous-ensemble du graphe, dans l'ordre de ses dépendances :

- Stages : ingest, contextualize, represent_requirements, analyze_business_rules, analyze_adversarial_requirements (catégories `authorization_boundary`, `actor_misuse`, `adversarial_actor`, `dependency_failure` activées explicitement), consolidate_findings, consolidate, compose_report
- Agents invoqués via `Task` : context-analyst, business-rule-analyst, adversarial-analyst, report-composer

Pas de stage `decide_readiness`. Le rapport se concentre sur les frontières de sécurité, permissions et rôles établis ou manquants.

Chaque résultat d'agent est vérifié contre `${CLAUDE_PLUGIN_ROOT}/models/agent-execution-result.schema.json`. À la fin, transmets les résultats normalisés au rendu défini par `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml` (langue : `report_language`, français par défaut).

Retourne : actions autorisées en lecture, actions nécessitant une permission, cibles concernées, risques de mutation implicite et éléments nécessitant une confirmation.

Ne modifie rien et n'appelle aucune opération d'écriture.
