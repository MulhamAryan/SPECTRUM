# Intégrations SPECTRUM

SPECTRUM peut consommer des données provenant de systèmes externes, notamment Jira et GitHub.

## Principe

Les intégrations servent d'abord à **lire et contextualiser** les données nécessaires à l'analyse.

Le flux standard est :

```text
Système externe
      ↓
 Lecture / collecte
      ↓
 Normalisation SPECTRUM
      ↓
 Preuves + sources
      ↓
 Analyse
      ↓
 Rapport
```

Toute écriture est séparée de l'analyse :

```text
Analyse
  ↓
Action proposée
  ↓
Permission explicite de l'utilisateur
  ↓
Opération ciblée
  ↓
Résultat vérifié
```

## Jira

Le connecteur Jira peut fournir le ticket, les commentaires, les pièces jointes accessibles, l'historique utile et les références liées lorsque ces informations sont disponibles.

Aucune création, modification, commentaire, transition ou modification de champ Jira n'est autorisée par défaut.

## GitHub

Le connecteur GitHub peut fournir les fichiers, commits, branches, demandes de fusion, commentaires, statuts et différences nécessaires à une analyse de cohérence ou d'écart lorsque ces informations sont accessibles.

Aucun commit, push, création de branche, modification de demande de fusion ou écriture de commentaire n'est autorisé par défaut.

## Permissions

La permission doit couvrir l'opération et la cible concrètes. Une autorisation générale ou ancienne ne doit pas être réutilisée implicitement.
