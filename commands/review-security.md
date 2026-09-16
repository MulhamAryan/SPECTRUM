---
description: Vérifier les frontières de sécurité et de permission d'une analyse SPECTRUM sans effectuer de mutation.
argument-hint: [chemin-du-ticket-ou-texte]
---

# SPECTRUM — Revue sécurité et permissions

Vérifie que l'analyse respecte le mode lecture seule et identifie toute action qui nécessiterait une autorisation explicite.

Retourne en français :
- actions autorisées en lecture ;
- actions qui nécessiteraient une permission ;
- cibles concernées ;
- risques de mutation implicite ;
- éléments nécessitant une confirmation avant exécution.

Ne modifie rien et n'appelle aucune opération d'écriture.
