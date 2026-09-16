---
description: Vérifier les frontières de sécurité et de permission d'une analyse SPECTRUM sans effectuer de mutation.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Revue sécurité et permissions

Vérifie que l'analyse respecte le mode lecture seule et identifie toute action qui nécessiterait une autorisation explicite.

## Exécution et rendu

Utilise le superviseur SPECTRUM et les Skills autorisés pour cette revue. Transmets ensuite les résultats normalisés au moteur central `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml` et rester entièrement en français.

Retourne : actions autorisées en lecture, actions nécessitant une permission, cibles concernées, risques de mutation implicite et éléments nécessitant une confirmation.

Ne modifie rien et n'appelle aucune opération d'écriture.
