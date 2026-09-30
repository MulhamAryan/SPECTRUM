# Changelog

Format : [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/). Versions : SemVer.

## [0.5.1] — 2026-09-30

### Corrigé
- `scripts/spectrum-guard.py` → `scripts/spectrum-guard.js` : le hook read-only échouait sur Windows (`python3` = stub Microsoft Store). Node est la seule dépendance garantie par Claude Code, portage à comportement identique. `hooks/hooks.json`, `scripts/test-guard.sh` et la CI mis à jour en conséquence.

## [0.5.0] — 2026-09-30

Hardening release issue de l'audit du 30/09/2026 (branche `fix/hardening-plan`).

### Corrigé
- **Orchestration inexécutable** : le superviseur était un sous-agent censé lancer d'autres sous-agents via `Task`, ce qu'un sous-agent ne peut pas faire (et son frontmatter ne déclarait pas `Task`). La commande slash est désormais l'orchestrateur ; `agents/supervisor.md` supprimé au profit de `core/orchestration-procedure.md`.
- **Deux graphes contradictoires** (`workflows/ticket-analysis.yaml` vs `models/agent-orchestration.yaml`) : le workflow (v8) est l'unique source de vérité, avec `agent` et `phase` par stage ; l'orchestration (v2) ne garde que principes, routage et politique d'échec. Décision : l'analyse indépendante tourne en parallèle du drift et n'en dépend pas.
- **5 skills sans frontmatter**, donc jamais découverts par Claude Code : `adversarial-requirement-analysis`, `business-rule-analysis`, `independent-analysis`, `requirement-set-quality`, `spec-implementation-drift-analysis`.
- **YAML invalide** dans le frontmatter des 9 commandes (`argument-hint` avec crochets non quotés).
- **Tension identifiants cachés / traçabilité** dans le rapport : identifiants courts lisibles dans le corps, annexe Traçabilité obligatoire pour les références techniques.
- Les 5 commandes de revue invoquaient « le superviseur » sans rien charger ; elles exécutent maintenant un sous-ensemble explicite du graphe.

### Ajouté
- `hooks/hooks.json` + `scripts/spectrum-guard.js` : lecture seule **mécanique** pendant toute commande `/spectrum:` (Write/Edit, Bash à effet d'écriture, outils MCP de mutation bloqués). Auto-test `scripts/test-guard.sh`. Garde-fou en Node : c'est le seul script exécuté sur le poste de chaque utilisateur du plugin, et Node est la seule dépendance garantie par Claude Code (`python3` absent sur Windows, `python` absent sur macOS).
- `scripts/validate.py` : invariants structurels exécutables (manifestes, frontmatter, registre ↔ workflow, DAG, skills autorisés, ordre des stages, isolation, groupes parallèles, profils, orphelins, politiques, schéma, hooks). CI `.github/workflows/validate.yml`.
- `models/agent-execution-result.schema.json` : format de retour obligatoire de chaque agent, vérifié par l'orchestrateur.
- `core/agent-brief.md` : remplace le chargement registre + contrat dans chaque agent.
- `agents/context-analyst.md` : `requirement-analyst` ne tourne plus deux fois ; `qa-analyst` consomme les sorties V&V au lieu de rejouer leurs skills.
- Profils `quick` / `standard` / `full` (`--profile`) et `--lang`.
- `policies/ticket-readiness-agile-v1.yaml` (profil quick, non calibrée).
- `examples/` : jeu de tickets de référence (3 synthétiques à remplacer), attentes humaines, journal des runs ; `scripts/score-examples.py`.
- Section **Exécution** obligatoire dans le rapport (profil, agents, stages non applicables, échecs, actions bloquées).
- `CONTRIBUTING.md` (une langue par couche, règles d'ajout), `NOTICE`, `scripts/sync-version.py`.

### Déplacé
- Branche ISO/IEC/IEEE 29148 (6 skills jamais invoqués + contrats d'évaluation) → `experimental/`. Résout aussi le triplon `requirement-context` / `requirements-context` / `requirements-engineering-context` : seul `requirements-context` reste actif.
- Sections `Evaluation` / `References` de chaque `SKILL.md` → `REFERENCE.md` (non chargé à l'exécution).

### Supprimé
- Coquilles vides : `.agents/`, `.gemini/`, `gemini-extension.json`, `core/README.md` placeholder. Le README ne revendique plus le multi-plateformes.

### Non fait (volontairement)
- Condensation de fond des skills vers 120–150 lignes : réécriture manuelle à relire.
- Calibration de la politique : impossible sans rapports sur des tickets réels (voir `examples/README.md`).
- Rapport d'exemple réel dans `outputs/` : ne pas commiter un rapport fabriqué.

## [0.4.3]

État initial audité.
