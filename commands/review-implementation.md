---
description: Comparer un ticket ou une spécification avec les artefacts d'implémentation fournis et détecter les écarts traçables.
argument-hint: [chemin-du-ticket-et-des-artefacts]
---

# SPECTRUM — Revue de l'implémentation

Analyse la spécification et les artefacts d'implémentation explicitement fournis.

## Exécution et rendu

Utilise le superviseur SPECTRUM et les Skills autorisés pour cette revue. Transmets ensuite les résultats normalisés au moteur central `${CLAUDE_PLUGIN_ROOT}/reporting/report-renderer.md`.

Le rapport utilisateur doit respecter `${CLAUDE_PLUGIN_ROOT}/models/reporting-pipeline.yaml`.

Retourne en français : périmètre comparé, correspondances, écarts avérés, éléments non vérifiables, preuves et références, impact potentiel et actions recommandées.

Une absence de résultat n'est pas une preuve d'absence fonctionnelle. Ne simule pas un comportement d'exécution qui n'a pas été fourni. Ne modifie aucun code, fichier, dépôt ou système externe sans autorisation explicite.
