# Contribuer à SPECTRUM

## Conventions de langue — une langue par couche

| Couche | Langue | Pourquoi |
|---|---|---|
| Tout ce que le modèle charge à l'exécution : `commands/`, `agents/`, `skills/*/SKILL.md`, `core/` | **Français** | Le rapport est en français par défaut ; un contexte homogène évite les glissements de langue dans la sortie. |
| Modèles, workflow, politiques, registre, contrats : `models/`, `workflows/`, `policies/`, `agents/registry.yaml`, `evaluation/`, `integrations/`, `governance/` | **Anglais** (clés `snake_case` stables) | Ce sont des structures de données lues par des scripts et par le modèle ; les clés ne se traduisent pas. Les champs libres (`purpose`, `note`) restent en anglais. |
| Rapport utilisateur | `report_language` (défaut `fr`) | Paramètre `--lang` des commandes. |
| Messages de commit, CHANGELOG, README technique | Anglais ou français, mais pas les deux dans le même fichier. | |

Ne traduis pas un fichier existant « pour l'homogénéité » : change la langue seulement si le fichier change de couche.

## Où vit quoi

- Le **graphe d'exécution** vit uniquement dans `workflows/ticket-analysis.yaml`. Aucun autre fichier ne définit de phases ou de dépendances.
- La **procédure** d'exécution vit dans `core/orchestration-procedure.md`. Il n'y a pas d'agent superviseur.
- Ce qu'un **agent** doit savoir vit dans `core/agent-brief.md`. Les agents ne chargent pas le registre.
- Un **skill** est atomique : il ne cite pas un autre skill autrement que dans sa section `Handoff`.
- Une **politique** de préparation est versionnée et référencée par un profil du workflow.
- Le matériel non branché vit dans `experimental/`, jamais dans `skills/`.

## Avant tout commit

```bash
pip install pyyaml
python3 scripts/validate.py        # doit sortir 0 error
bash scripts/test-guard.sh         # doit passer
python3 scripts/sync-version.py --check
```

La CI rejoue les trois. Un commit qui casse le validateur n'est pas mergé.

Le garde-fou (`scripts/spectrum-guard.js`) est écrit en Node parce que c'est le seul script exécuté sur le poste de chaque utilisateur du plugin, et Node est la seule dépendance garantie par Claude Code (`python3` absent sur Windows, `python` absent sur macOS).

## Ajouter ou modifier un stage

1. Modifier `workflows/ticket-analysis.yaml` (stage, `agent`, `phase`, `depends_on`, `skills`/`engine`, `produces`, éventuel `when`).
2. Ajouter le stage à `stages:` de l'agent dans `agents/registry.yaml` ; vérifier que les skills du stage sont dans ses `required_skills` ou `optional_skills`.
3. Mettre à jour les profils si le stage doit en faire partie.
4. Lancer `scripts/validate.py`.
5. Ajouter un cas dans `evaluation/cases/ticket-analysis-workflow.yaml` **et** soit un check dans `validate.py` (structurel), soit un ticket dans `examples/` qui l'exerce (comportemental). Voir `evaluation/README.md`.

## Ajouter un skill

1. `skills/<nom>/SKILL.md` avec frontmatter `name` (= nom du dossier) et `description`. Sans frontmatter, Claude Code ne découvre pas le skill — le validateur refuse.
2. L'attribuer à au moins un agent dans le registre **et** à au moins un stage du workflow. Un skill orphelin est refusé par le validateur.
3. Sections lourdes (critères d'évaluation, sources) dans `REFERENCE.md` à côté, pas dans `SKILL.md`.

## Versionner

`python3 scripts/sync-version.py X.Y.Z` puis une entrée dans `CHANGELOG.md`.

## Ce qui n'est pas accepté

- Un invariant dans `evaluation/contracts/` sans vérification exécutable ou ticket qui l'exerce.
- Une modification d'un `examples/expected/*.yaml` pour faire passer un rapport.
- Un agent qui déclare l'outil `Task`.
- Un dossier placeholder (« implementation starts later »).
