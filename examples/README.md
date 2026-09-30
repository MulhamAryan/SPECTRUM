# Jeu de tickets de référence

C'est ici que se mesure la valeur réelle de SPECTRUM. Sans ce jeu, les invariants comportementaux du dossier `evaluation/` sont des intentions.

## Ce qu'il faut mettre ici

- `tickets/<id>.md` — 8 à 10 tickets **réels, anonymisés**, gradués du très bon au très mauvais. Les trois tickets `synth-*` fournis sont **synthétiques** : ils servent à vérifier que la chaîne tourne, pas à calibrer la politique. Remplace-les.
- `expected/<id>.yaml` — pour chaque ticket, le verdict attendu et les constats bloquants attendus, décidés par un humain (dev senior ou analyste) **avant** de lancer l'outil.
- `reports/<id>.md` — le rapport produit par `/spectrum:analyze-ticket examples/tickets/<id>.md`, copié tel quel.
- `runs.md` — journal : date, ticket, profil, durée, coût (`/cost` dans Claude Code), verdict obtenu.

## Boucle

```bash
# 1. lancer dans Claude Code, par ticket
/spectrum:analyze-ticket examples/tickets/synth-01-good.md --profile=standard
# 2. coller le rapport dans examples/reports/synth-01-good.md
# 3. scorer
python3 scripts/score-examples.py
```

Le score compare le verdict obtenu au verdict attendu et vérifie que chaque constat bloquant attendu apparaît dans la section 🔴 Bloquants (par mots-clés). Il affiche aussi le taux d'« Évaluation inconclusive ».

## Ce que les chiffres doivent déclencher

| Observation | Action |
|---|---|
| Inconclusif > 30 % des tickets | Une dimension exige du contexte que les tickets n'ont jamais : passer son `applicability` à `not_applicable` par défaut dans la politique (ou utiliser `ticket-readiness-agile-v1`). |
| Faux bloquant (🔴 non attendu) | Lire le constat : si c'est une règle INCOSE appliquée mécaniquement, ajouter l'exception dans le Skill concerné (« faux positifs à éviter »). |
| Bloquant attendu manqué | Identifier le Skill qui aurait dû le voir ; vérifier qu'il a bien été exécuté (section Exécution du rapport) avant de toucher sa procédure. |
| Coût > budget | Utiliser `--profile=quick` pour le tri, `standard` pour l'analyse. |

Ne modifie **jamais** un `expected/` pour faire passer un rapport.
