---
description: Comparer deux artefacts ou deux versions pour détecter les correspondances, écarts et contradictions traçables.
argument-hint: "[artefact-a] [artefact-b]"
---

# SPECTRUM — Comparaison d'artefacts

Compare uniquement les deux artefacts explicitement fournis.

## Exécution et rendu

Utilise le superviseur SPECTRUM et les Skills autorisés pour cette revue. Transmets ensuite les résultats normalisés au moteur central `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml`.

Retourne en français : périmètre de comparaison, éléments alignés, différences de représentation, écarts ou contradictions avérés, correspondances manquantes, éléments non comparables, preuves, références et actions suivantes.

Ne transforme jamais directement une comparaison en verdict de préparation. Ne réécris pas silencieusement les sources et ne modifie aucun artefact ou système externe sans autorisation explicite.
