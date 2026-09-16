---
description: Analyser une spécification avec les artefacts GitHub disponibles, en lecture seule.
argument-hint: [dépôt-ou-chemin-ou-demande]
---

# SPECTRUM — Analyse depuis GitHub

Utilise les données GitHub accessibles dans l'environnement pour contextualiser l'analyse lorsque cela est nécessaire : fichiers, branches, commits, demandes de fusion, différences, commentaires et statuts.

Étapes :
1. Identifier précisément le dépôt et la révision utile.
2. Lire uniquement les artefacts nécessaires.
3. Conserver les identités de version et références.
4. Comparer les éléments avec la spécification fournie.
5. Produire le rapport SPECTRUM en français.

Si l'accès GitHub n'est pas disponible, utiliser uniquement les artefacts fournis par l'utilisateur et signaler la limite.

Sécurité : lecture seule. Aucun commit, push, changement de branche, modification de fichier, demande de fusion ou commentaire ne doit être effectué sans autorisation explicite couvrant l'opération et la cible.
