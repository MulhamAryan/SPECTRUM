---
name: test-documentation
description: Documenter les preuves de test réellement présentes dans le dépôt (unitaires, intégration, API, E2E, régression) et leur traçabilité vers les exigences et l'implémentation, selon ISO/IEC/IEEE 29119-3.
type: component
role: test_documentation
---

# Test Documentation

## Purpose

Documenter les tests **réellement présents** dans le dépôt pour une fonctionnalité déjà implémentée, et leur traçabilité vers l'exigence/le comportement établi et l'implémentation — jamais des cas de test synthétisés pour combler une section.

Dérivé de la portée publique de l'ISO/IEC/IEEE 29119-3:2021.

## Source boundary

- `knowledge/sources/iso-iec-ieee-29119-3-2021/knowledge.yaml`
- `rules/sources/iso-iec-ieee-29119-3-2021/rules.yaml`

Seule la portée publique (les templates de documentation de test sont un output des processus 29119-2, applicables à tous les modèles de cycle de vie et styles de test) est confirmée. Les noms de templates spécifiques largement cités publiquement ne sont pas vérifiés dans cette session (voir exclusions).

## Interpretation boundary

Réutilise le champ `Scenario.scenario_kind: test_case` (extension additive du modèle canonique) et `Scenario.evidence_refs` — pas de nouvelle entité. `observed` = test trouvé et lisible dans le dépôt ; `unknown` = aucun test identifié pour le comportement concerné, jamais transformé en « comportement non testé par négligence » sans preuve.

## When to use

Utiliser pour documenter, à partir des tests unitaires, d'intégration, API, E2E et de régression réellement présents, ce qui est effectivement couvert — et pour signaler explicitement l'absence de test quand elle est constatée.

Ne pas l'utiliser pour exécuter des tests, générer de nouveaux cas de test, ou juger la suffisance globale de la couverture (ce n'est pas un score de couverture).

## Inputs

Required:

- `test_files_or_test_artifacts` réellement fournis.

Recommended:

- `requirement_refs` ou comportement établi à relier aux tests.
- `implementation_artifacts` pour la relation test → implémentation.
- `ci_configuration` si elle précise quels tests s'exécutent réellement.

## Preconditions

1. Le périmètre de test analysé (quels répertoires/fichiers) est explicite.
2. Absence de test découverte est distinguée d'absence de périmètre fourni.

## Procedure

### 1. Inventorier les tests réellement présents

Lister chaque fichier/cas de test trouvé, son type apparent (unitaire, intégration, API, E2E, régression) d'après sa structure ou sa configuration — sans reclasser arbitrairement un test ambigu.

### 2. Établir la relation exigence → implémentation → test

Réutiliser `requirement-relationship-traceability` (Skill existant, non dupliqué) pour la chaîne amont exigence/implémentation ; ce Skill ajoute le dernier maillon `implementation → test` en citant le test exact qui exerce le comportement.

### 3. Représenter chaque test comme `Scenario`

`scenario_kind: test_case`, `actors_refs`/`conditions`/`expected_outcomes` tirés **uniquement** du contenu réel du test (nom de test, assertions, fixtures), jamais complétés par une attente plausible.

### 4. Signaler l'absence sans la qualifier de défaut

Un comportement établi sans test identifié est rapporté comme `test_evidence_absent`, jamais reformulé en « bug » ou « couverture insuffisante » — la qualification revient à une analyse de qualité distincte, hors périmètre de ce Skill.

### 5. Distinguer test déclaré et test exécuté en CI

Un test présent dans le dépôt n'est pas automatiquement un test qui s'exécute réellement en intégration continue ; si la configuration CI est fournie et l'exclut, le signaler explicitement.

## Analysis logic

`inventaire des tests → classification par type observé → chaîne exigence→implémentation→test → absence signalée sans qualification`

## Decision semantics

- `test_evidence_established`: un test réel couvre le comportement concerné, avec référence exacte.
- `test_evidence_partial`: un test existe mais ne couvre qu'une partie du comportement établi.
- `test_evidence_absent`: aucun test identifié pour un comportement établi.
- `test_execution_status_unknown`: présence dans le dépôt confirmée, exécution réelle (CI/environnement) non observable.

## Findings

- `test_case_without_requirement_or_behavior_basis`
- `test_evidence_absent_for_established_behavior`
- `test_declared_but_execution_unverified`
- `test_type_misclassified`

## Evidence

Préserver : chemin du fichier de test, nom du test/cas, extrait d'assertion, configuration CI citée si disponible.

## Handoff

- `requirement-relationship-traceability` pour la partie amont exigence/implémentation de la chaîne.
- `verification-analysis` / `validation-analysis` (Skills existants) quand la base de vérification/validation doit être réexaminée plutôt que rejouée ici.
- `lifecycle-documentation` pour l'intégration dans la documentation finale.

## Output

Produire un `test_documentation_observation` contenant :

- `test_scenario_refs` (`Scenario` avec `scenario_kind: test_case`)
- `traceability_chain_refs` (exigence → implémentation → test)
- `findings`, `evidence_refs`, `unassessed_scope`

## Exit conditions

`completed`, `completed_with_findings`, `completed_with_gaps`, `blocked_on_missing_context` (aucun test fourni ni périmètre défini), `not_applicable`.

## Non-goals

Ce Skill ne fait pas :

- inventer un cas de test, un résultat attendu, ou une donnée de couverture ;
- exécuter des tests ou modifier l'environnement ;
- qualifier une absence de test de défaut sans analyse dédiée ;
- affirmer une conformité ISO/IEC/IEEE 29119-3.

## Référence

`REFERENCE.md` dans ce dossier (non chargé à l'exécution).
