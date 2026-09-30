# Scripts

| Script | Rôle |
|---|---|
| `spectrum-guard.js` | Hook Claude Code : lecture seule mécanique pendant toute commande `/spectrum:` (bloque Write/Edit, Bash à effet d'écriture, outils MCP de mutation). Déclaré dans `hooks/hooks.json`. |
| `test-guard.sh` | Auto-test du garde-fou. |
| `validate.py` | Validation structurelle du plugin : manifestes, frontmatter, registre, graphe du workflow (acyclicité, dépendances, skills autorisés, profils), skills orphelins, politiques, schéma de résultat d'agent, hooks. |
| `sync-version.py` | Vérifie ou aligne la version dans tous les manifestes. |

Aucun de ces scripts n'est chargé par le modèle pendant une analyse ; ils s'exécutent en local ou en CI.

Le garde-fou (`spectrum-guard.js`) est écrit en Node parce que c'est le seul script exécuté sur le poste de chaque utilisateur du plugin, et Node est la seule dépendance garantie par Claude Code (`python3` est absent sur Windows, `python` est absent sur macOS).
