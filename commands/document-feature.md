---
description: Produit une documentation technique post-implémentation traçable et prête pour Confluence (architecture, conception, tests, limites, questions ouvertes) à partir d'un ticket déjà implémenté et de ses artefacts.
argument-hint: "[chemin-du-ticket-ou-texte] [--implementation=chemin] [--lang=fr]"
---

# SPECTRUM — Documentation technique de fonctionnalité

Documente une fonctionnalité déjà implémentée : architecture reconstruite et décrite, conception logicielle, documentation des tests réellement présents, et consolidation en documentation technique prête pour Confluence.

## Indépendance vis-à-vis de l'analyse de ticket

Cette commande est **strictement indépendante** de `/spectrum:analyze-ticket` et de ses sous-ensembles (`review-*`). Elle n'exécute jamais `workflows/ticket-analysis.yaml`, ne modifie aucun de ses stages, agents ou skills, et ne produit aucune décision de préparation (`Decision`). Elle réutilise uniquement les fondations partagées : Evidence Model, Canonical Data Model, provenance, traçabilité.

## Tu es l'orchestrateur

Cette commande s'exécute dans la conversation principale, qui est la seule à disposer de `Task`. Il n'y a pas d'agent superviseur. Charge d'abord, dans cet ordre :

1. `${CLAUDE_PLUGIN_ROOT}/core/orchestration-procedure.md` — comment exécuter un graphe (principes réutilisés ; le graphe lui-même vient du fichier ci-dessous)
2. `${CLAUDE_PLUGIN_ROOT}/workflows/feature-documentation.yaml` — le graphe propre à cette commande
3. `${CLAUDE_PLUGIN_ROOT}/agents/registry.yaml` — skills autorisés par agent (entrées `architecture-analyst`, `design-documentation-analyst`, `lifecycle-documentation-analyst`, `test-documentation-analyst`, `documentation-composer`)
4. `${CLAUDE_PLUGIN_ROOT}/governance/spectrum-safety-rules.yaml`
5. `${CLAUDE_PLUGIN_ROOT}/models/documentation-pipeline.yaml`
6. `${CLAUDE_PLUGIN_ROOT}/outputs/technical-documentation-report.yaml`

Puis suis la procédure d'orchestration décrite dans `core/orchestration-procedure.md` en substituant partout `workflows/ticket-analysis.yaml` par `workflows/feature-documentation.yaml` : résolution du profil, ingestion, exécution du graphe via `Task`, vérification de chaque résultat contre le schéma, composition, contrôle final. Il n'y a pas de stage `decide_readiness` dans ce graphe ; ne pas chercher à en simuler un.

## Entrée

`$ARGUMENTS` contient soit un chemin vers un fichier contenant le ticket/la description de fonctionnalité, soit son texte, suivi d'options facultatives :

- `--implementation=<chemin>` — chemin vers les artefacts d'implémentation à analyser (code, migrations, configuration, infrastructure, tests). Sans cette option, les stages `reconstruct_and_describe_architecture` et `document_tests` sont `blocked_on_missing_context` et la commande le dit au lieu d'analyser à vide.
- `--lang=<code>` (défaut : `fr`) — langue du document.

Si c'est un chemin, lis le fichier avant toute analyse.

## Sécurité et permissions — règle absolue

SPECTRUM fonctionne strictement en lecture seule. Le hook `spectrum-guard` bloque mécaniquement toute écriture pendant une analyse SPECTRUM. Si une action a été bloquée, mentionne-le dans la section Permission / sécurité du document ; ne la contourne jamais.

Cette commande ne publie jamais automatiquement vers Confluence ou tout autre système externe ; elle produit un contenu prêt à être collé dans Confluence.

## Règles d'intégrité d'exécution

- Chaque agent est invoqué via `Task` et reçoit uniquement ses entrées amont nécessaires.
- Chaque résultat d'agent est vérifié contre `models/agent-execution-result.schema.json` ; un résultat non conforme est un échec enregistré, jamais complété par toi.
- Un stage conditionnel non applicable est `not_applicable`, pas un échec.
- Un échec reste visible et n'est jamais converti en succès implicite.
- Absence de preuve n'est jamais présentée comme preuve d'absence fonctionnelle.
- Une justification (rationale) non documentée porte explicitement la mention « justification déduite de l'implémentation, aucune justification explicite/ADR trouvée ».

## Sortie obligatoire

Le document est rendu par `documentation-composer` selon `outputs/technical-documentation-report.yaml`, dans la langue `report_language`. C'est une **page de documentation en prose**, pas un rapport de constats : résumé, architecture (racontée, pas tabulée), décisions techniques et points d'attention réels, vérification et tests, limites connues, questions ouvertes — avec, en option, une annexe repliable pour qui veut le catalogue exhaustif.

Aucun identifiant court synthétique (AE-/AV-/AD-/D-/T-/Q-/L-), aucune annexe de traçabilité, aucune section « Sources consultées » ou « Permission et sécurité » dans le corps — ce sont des détails de fonctionnement du pipeline, pas du contenu sur la fonctionnalité. Un élément n'est nommé dans le corps que s'il éclaire une vue, une décision, un point d'attention ou une limite ; le reste va dans l'annexe optionnelle, jamais en remplissage du corps.

Une section sans contenu établi indique explicitement « Aucun changement pertinent détecté » ou « Preuve insuffisante » — jamais un remplissage inventé.

## Contrôle final

Applique la section 8 de la procédure d'orchestration (adaptée : pas de `decide_readiness`) : vérifie tes propres structures d'exécution, pas une auto-attestation. Si un contrôle échoue, corrige l'exécution ou expose l'échec dans le document.

## Limites

Ne réécris pas silencieusement une documentation existante, n'invente pas d'élément d'architecture, de décision, de test ou de justification. Ne transforme pas une hypothèse en fait et n'effectue aucune mutation ni publication automatique.
