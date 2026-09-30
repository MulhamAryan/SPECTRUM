# Évaluation

Les fichiers de `contracts/` et `cases/` décrivent des invariants et des cas attendus. Ils ne sont **pas exécutables tels quels** ; ce dossier explique comment ils sont réellement vérifiés.

## Deux familles d'invariants

**Structurels** — vérifiables sur les fichiers du dépôt sans exécuter d'analyse (graphe acyclique, dépendances existantes, skills déclarés, décision produite au bon stage, politique versionnée, ordre des stages…). Ils sont implémentés dans `scripts/validate.py`, qui affiche la liste des identifiants couverts à chaque exécution (`TAW-001`, `TAW-002`, `TAW-003`, …). Tout invariant structurel non encore couvert par le script est une dette à résorber, pas une garantie.

**Comportementaux** — vérifiables uniquement en exécutant une analyse sur un ticket (« une hypothèse n'est pas promue en fait », « un échec n'est pas masqué », « l'indépendante ne lit pas les conclusions principales »). Ils sont vérifiés par le jeu de tickets de référence dans `examples/` : chaque ticket a un verdict et des constats attendus, et chaque rapport produit est comparé à cette attente. Sans ce jeu, un invariant comportemental est une intention, pas une preuve.

## Règle

Un nouvel invariant ajouté dans `contracts/` doit soit être implémenté dans `validate.py` (structurel), soit avoir au moins un ticket dans `examples/` qui l'exerce (comportemental). Sinon il n'est pas ajouté.

## Exécuter

```bash
pip install pyyaml
python3 scripts/validate.py      # structurel
bash scripts/test-guard.sh       # garde-fou lecture seule
python3 scripts/sync-version.py --check
```

La CI (`.github/workflows/validate.yml`) lance les trois à chaque push.
