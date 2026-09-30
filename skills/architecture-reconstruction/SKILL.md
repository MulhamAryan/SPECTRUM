---
name: architecture-reconstruction
description: Reconstruire l'architecture technique d'une implémentation existante à partir du code, de la structure du projet, des dépendances, contrats API, schéma de base de données, configuration, infrastructure, tests et historique Git, en distinguant observé/dérivé/inféré/inconnu.
type: component
role: architecture_reconstruction
---

# Architecture Reconstruction

## Purpose

Reconstruire — jamais deviner — l'architecture technique réelle d'une fonctionnalité ou d'un ticket déjà implémenté, à partir exclusivement des artefacts fournis. Ce Skill alimente `architecture-description` avec les `ArchitectureElement` et `Relationship` que celui-ci qualifie ensuite en vues et décisions.

Dérivé de la portée publique de l'ISO/IEC/IEEE 42010:2022 et du résumé public de l'IEEE 1016-2009 (norme Inactive-Reserved, utilisée ici uniquement comme référence conceptuelle sur la reconstruction de conception depuis une implémentation existante — jamais comme conformité).

## Source boundary

- `knowledge/sources/iso-iec-ieee-42010-2022/knowledge.yaml`
- `knowledge/sources/ieee-1016-2009/knowledge.yaml` (IEEE1016-R001 : une description reconstruite doit être marquée comme telle, jamais présentée comme conception d'origine)
- `${CLAUDE_PLUGIN_ROOT}/models/evidence-model.yaml` et `${CLAUDE_PLUGIN_ROOT}/models/canonical-data-model.yaml` restent la source canonique de statut d'evidence ; ce Skill n'introduit aucun vocabulaire parallèle.

## Interpretation boundary

Identique à `architecture-description` : `observed` (Evidence project_artifact directe), `derived` (Observation combinée), `inferred` (Evidence.provenance.method: inference + rationale obligatoire), `unknown` (absence ou inconclusive). Voir ce Skill pour le détail du mapping.

## When to use

Utiliser quand aucune architecture documentée fiable n'existe et qu'elle doit être reconstruite depuis l'implémentation réelle — structure du dépôt, dépendances déclarées, contrats API, schéma de base de données, migrations, configuration, descripteurs d'infrastructure, tests, historique Git, PR, documentation existante.

Ne pas l'utiliser pour évaluer si l'architecture est correcte ou suffisante ; ce Skill décrit ce qui existe, il ne le juge pas.

## Inputs

Required:

- `source_code_or_repository_structure`.

Recommended:

- `dependency_manifests` (package.json, csproj, requirements.txt, etc.) ;
- `api_contracts` (OpenAPI, contrôleurs, définitions de routes) ;
- `database_schema_or_migrations` ;
- `configuration_files` ;
- `infrastructure_descriptors` (Dockerfile, docker-compose, manifests Kubernetes/Helm, IaC) ;
- `tests` ;
- `git_history_and_pull_requests` ;
- `existing_documentation`.

## Preconditions

1. Au moins un artefact d'implémentation réel est fourni — sans quoi le Skill est `blocked_on_missing_context`, jamais complété par supposition.
2. Le périmètre exact analysé (fichiers, dossiers, services) est explicite et conservé dans la sortie.

## Procedure

### 1. Inventorier le périmètre réellement fourni

Lister précisément ce qui a été lu (fichiers, dossiers). Un élément hors de ce périmètre est `unassessed_scope`, pas `absent`.

### 2. Identifier les éléments candidats

Pour chaque signal structurel (dossier de service, module, classe de contrôleur, définition de conteneur, déclaration de table, entrée de configuration) : établir un `ArchitectureElement` candidat avec `element_kind` et `granularity: architecture`, en citant l'artefact exact.

### 3. Établir les dépendances et interfaces

À partir des imports, des appels réseau déclarés, des contrats d'API et des définitions de schéma : établir des `Relationship` (`depends_on`, `interfaces_with`) uniquement quand le lien est observable dans le code ou la configuration, jamais par similarité de nom seule.

### 4. Séparer preuve de dépôt et preuve d'exécution

Une dépendance déclarée dans le code (ex. un appel HTTP vers un service nommé) est une preuve de **conception**, pas une preuve que ce service tourne réellement en environnement — ne jamais transformer l'une en l'autre.

### 5. Comparer avec la documentation existante

Quand une documentation d'architecture préexistante est fournie, comparer sans la réécrire silencieusement : préserver toute contradiction entre la documentation et le code observé comme un `Finding`, jamais résolue automatiquement en faveur de l'un ou l'autre.

### 6. Reconstruire la conception (granularité design)

Quand la reconstruction descend au niveau composant/module interne (pas seulement service/architecture), produire des `ArchitectureElement` avec `granularity: design` — ceux-ci alimentent `software-design-description`, qui applique la discipline IEEE 1016 de marquage « reconstruit ».

### 7. Historique Git comme preuve de provenance, pas de comportement

Un commit ou une PR peut établir *qu'un* changement a eu lieu et *où*, mais n'établit jamais seul le comportement runtime réel — combiner avec le code/tests pour toute affirmation de comportement.

## Analysis logic

`périmètre → éléments candidats → dépendances/interfaces → comparaison documentation → granularité design`

## Decision semantics

Identique à `architecture-description` : `element_established`, `element_derived`, `element_inferred`, `element_unknown`. S'y ajoute :

- `reconstruction_complete`: le périmètre déclaré a été intégralement couvert.
- `reconstruction_partial`: une partie du périmètre reste non analysée (préciser pourquoi : volume, artefact illisible, hors périmètre).

## Findings

- `architecture_element_unsupported`
- `dependency_inferred_from_naming_only`
- `repository_evidence_conflated_with_runtime_behavior`
- `documentation_code_contradiction`
- `reconstruction_scope_incomplete`

## Evidence

Préserver : chemin de fichier exact, ligne/section, extrait, SHA de commit quand cité, version de dépendance déclarée.

## Handoff

- `architecture-description` pour la qualification en vues/préoccupations/décisions.
- `software-design-description` pour les éléments de granularité design.
- `architecture-diagram` pour la représentation dérivée.
- `spec-implementation-drift-analysis` (existant) quand une spécification fournie doit être comparée à l'implémentation reconstruite — ce Skill ne rejoue pas cette analyse, il la réutilise.

## Output

Produire un `architecture_reconstruction_observation` contenant :

- `architecture_element_refs`, `relationship_refs`
- `reconstruction_status`, `unassessed_scope`
- `findings`, `evidence_refs`

## Exit conditions

`completed`, `completed_with_findings`, `completed_with_gaps`, `blocked_on_missing_context`, `not_applicable` — sémantique identique à `architecture-description`.

## Non-goals

Ce Skill ne fait pas :

- inventer un élément ou une dépendance non observable ;
- déduire un comportement d'exécution non fourni ;
- transformer l'absence d'un fichier trouvé en preuve d'absence fonctionnelle ;
- juger la qualité de l'architecture reconstruite ;
- affirmer une conformité IEEE 1016 (norme Inactive-Reserved, référence conceptuelle uniquement).

## Référence

`REFERENCE.md` dans ce dossier (non chargé à l'exécution).
