# Procédure d'orchestration SPECTRUM

Ce document est chargé par les commandes SPECTRUM (`analyze-ticket`, `review-*`) et exécuté **par la commande elle-même, dans la conversation principale**. Il n'existe pas d'agent superviseur : un sous-agent Claude Code ne peut pas lancer d'autres sous-agents, donc seule la conversation principale dispose du mécanisme `Task` nécessaire.

Le graphe d'exécution est défini **uniquement** dans `${CLAUDE_PLUGIN_ROOT}/workflows/ticket-analysis.yaml`. Ce document décrit comment l'exécuter ; il ne redéfinit pas le graphe.

## 1. Résolution du profil

1. Lire `$ARGUMENTS`. Si un argument `--profile=<quick|standard|full>` est présent, l'extraire ; sinon utiliser `profiles.default` du workflow.
2. Charger le workflow et ne conserver que les stages du profil (`stages: all`, `all_except` + `excluded_stages`, ou liste explicite).
3. Prendre `readiness_policy_ref` du profil, sauf si l'utilisateur en a fourni une autre.
4. Si `--lang=<code>` est présent, l'utiliser comme `report_language` ; sinon `fr`.

## 2. Ingestion

1. Créer un `analysis_id` unique (`SPX-<date>-<4 caractères>`).
2. Si `$ARGUMENTS` (hors options) est un chemin, lire le fichier ; sinon traiter le texte comme le ticket.
3. Inventorier les sources et artefacts réellement disponibles : ticket, commentaires, artefacts projet, artefacts d'implémentation. Ne rien supposer.
4. Évaluer les conditions `when` de chaque stage conditionnel à partir de cet inventaire. Un stage dont la condition n'est pas satisfaite reçoit le statut `not_applicable` et n'est pas invoqué.

## 3. Exécution du graphe

Pour chaque stage dont toutes les dépendances sont `completed*` ou `not_applicable` :

- **stage `agent: orchestrator`** : exécuter le moteur ou l'opération décrite dans le modèle correspondant (`models/multi-source-reasoning.yaml`, `models/finding-engine.yaml`, `models/analysis-engine.yaml`, `models/ticket-readiness-engine.yaml`) dans la conversation principale.
- **stage avec un agent spécialisé** : invoquer l'agent via `Task` avec le prompt décrit en §4. Les stages du même groupe parallélisable dont les dépendances sont satisfaites sont lancés dans le même tour.

Règles :
- Ne jamais lancer un stage dont une dépendance est `running`, `blocked` ou `failed` (sauf dépendance `not_applicable`).
- Un stage déjà exécuté n'est jamais rejoué.
- Deux stages attribués au même agent et à la même phase (`contextualize` + `represent_requirements`) sont exécutés dans une seule invocation.

## 4. Prompt d'invocation d'un agent

Chaque `Task` reçoit, dans cet ordre :

1. `analysis_id`, `profile`, `stage_id(s)` à exécuter.
2. Le contenu du ticket et les références des sources disponibles.
3. Les **résultats amont nécessaires uniquement** (ceux listés par `depends_on` et `consumes_outputs_of`), jamais l'intégralité des résultats.
4. L'instruction de charger `${CLAUDE_PLUGIN_ROOT}/core/agent-brief.md` puis chaque `SKILL.md` de ses skills autorisés pour le stage, avant toute analyse.
5. L'instruction de retourner **un seul bloc YAML** conforme à `${CLAUDE_PLUGIN_ROOT}/models/agent-execution-result.schema.json`.
6. Le rappel : lecture seule, aucune invention, aucune décision de préparation globale.

Pour `independent-reviewer` : ne transmettre **aucune** conclusion des autres agents, seulement le ticket, les sources et le périmètre déclaré. La comparaison avec l'analyse principale est faite par l'orchestrateur après réception du résultat.

## 5. Vérification de chaque résultat d'agent

À réception d'un `Task`, vérifier mécaniquement :

- le bloc YAML existe et se parse ;
- les champs obligatoires du schéma sont présents : `execution_id`, `agent_id`, `stage_ids`, `status`, `skill_executions`, `findings`, `evidence_refs`, `handoffs`, `limitations`, `provenance` ;
- `status` est une valeur autorisée ;
- chaque skill obligatoire du stage apparaît dans `skill_executions` avec un `status` ;
- chaque finding a au moins une `evidence_ref`.

Si une vérification échoue : le stage est marqué `failed`, la sortie brute est conservée dans `failures`, et **l'orchestrateur ne complète jamais le résultat lui-même**.

## 6. Gestion des échecs

- Conserver chaque échec dans le plan.
- Continuer les branches indépendantes.
- Bloquer uniquement les stages dont la dépendance manquante est matérielle.
- Ne jamais fabriquer une sortie de remplacement.
- Remettre explicitement les échecs à la consolidation et au rapport.

## 7. Décision et rapport

1. `decide_readiness` applique la politique du profil au `AnalysisResult`. Aucun agent ne participe à cette étape.
2. `qa` reçoit les sorties de `verification-validation-analyst`, `adversarial-analyst` et `business-rule-analyst` ; il ne rejoue pas leurs skills.
3. `compose_report` reçoit `AnalysisResult`, `DecisionEvaluation`, `Decision`, le résultat QA, la liste des échecs et `report_language`. Il rend le rapport selon `outputs/ticket-analysis-report.yaml`.

## 8. Contrôle final par l'orchestrateur

Avant de répondre, l'orchestrateur vérifie sur ses propres structures (pas par auto-attestation) :

- chaque stage du profil a un statut final (`completed`, `completed_with_findings`, `completed_with_gaps`, `blocked`, `failed`, `not_applicable`) ;
- chaque agent sélectionné a un résultat conforme ou un échec enregistré ;
- aucun stage n'a consommé un résultat inexistant ;
- la décision provient de `decide_readiness` et de la politique référencée ;
- la liste des échecs est reportée dans le rapport ;
- aucune mutation n'a été effectuée (le hook `spectrum-guard` l'empêche ; s'il a bloqué une action, le rapport le mentionne).

## 9. Sortie d'orchestration

Produire un `analysis_execution_plan` conservé avec le rapport :

```yaml
plan_id: <analysis_id>
profile: <quick|standard|full>
readiness_policy_ref: <chemin>
stages:
  - id: <stage>
    agent: <agent>
    status: <statut>
    execution_id: <id ou null>
failures: []
handoffs: []
```
