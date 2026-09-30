---
name: architecture-description
description: Décrire l'architecture observée d'une implémentation (éléments, vues, parties prenantes, préoccupations, décisions et justification) à partir de preuves explicites, selon ISO/IEC/IEEE 42010.
type: component
role: architecture_description
---

# Architecture Description

## Purpose

Produire une description d'architecture (AD) traçable des éléments, vues, parties prenantes, préoccupations et décisions réellement établis par les preuves disponibles pour un ticket ou une fonctionnalité déjà implémentée.

Cette capacité SPECTRUM est dérivée de la portée publique de l'ISO/IEC/IEEE 42010:2022. La norme ne définit ni ce Skill, ni son vocabulaire de statut, ni un format de rendu.

## Source boundary

Référence autoritaire :

- ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*.
- Base de preuve : énoncé de portée public uniquement (le fetch direct de la page ISO a échoué dans cette session ; voir `knowledge/sources/iso-iec-ieee-42010-2022/README.md`).

Représentations locales contrôlées :

- `knowledge/sources/iso-iec-ieee-42010-2022/knowledge.yaml`
- `rules/sources/iso-iec-ieee-42010-2022/rules.yaml`

La norme elle-même reste autoritaire sur son propre périmètre ; ce Skill ne prétend pas en couvrir le texte intégral.

## Interpretation boundary

- `observed`: un élément, une vue ou une relation directement visible dans le code, la configuration, l'infrastructure ou un artefact fourni.
- `derived`: une conclusion construite à partir de plusieurs observations combinées (ex. un ensemble de modules qui communiquent via un même contrat forme un élément de service).
- `inferred`: une conclusion qui dépend d'une hypothèse non entièrement démontrée par la preuve disponible (ex. supposer un rôle architectural à partir du seul nom d'un dossier).
- `unknown`: l'information n'est ni observée, ni dérivable, ni raisonnablement inférable des preuves fournies.

Ces quatre statuts se représentent avec le vocabulaire canonique existant — jamais un nouveau champ parallèle :

- `observed`/`derived` → `Observation.status` (`observed`, `partially_observed`) avec `evidence_refs` vers une `Evidence` de `evidence_kind: project_artifact` ou `derived_observation`.
- `inferred` → `Evidence.provenance.method: inference` et un `rationale` obligatoire sur l'objet produit (`ArchitectureElement.rationale`, `ArchitectureDecisionRecord.rationale`).
- `unknown` → `Observation.status: not_observed` ou `inconclusive`, ou `Evidence.evidence_kind: absence`.

## When to use

Utiliser ce Skill quand une documentation technique post-implémentation doit établir : quels éléments d'architecture existent, quelles vues et préoccupations de parties prenantes sont pertinentes, et quelles décisions d'architecture sont documentées ou seulement déductibles.

Ne pas l'utiliser pour évaluer la préparation au développement (`analyze-ticket`), ni pour juger la qualité d'une architecture, ni pour produire un score.

## Inputs

Required:

- `implementation_artifacts` (code, structure de projet réellement fournie).
- `evidence_refs` déjà établis par les stages amont (`discover_implementation`).

Recommended:

- `api_contracts`, `database_schema`, `configuration`, `infrastructure_descriptors`.
- `existing_documentation` (ADR existants, README d'architecture).
- `stakeholder_hints` (rôles mentionnés explicitement dans le ticket ou la documentation).

## Preconditions

1. Au moins un artefact d'implémentation est réellement fourni (pas de scope vide).
2. L'évidence disponible permet de distinguer un élément observé d'un élément supposé.
3. Le périmètre de l'analyse (quel sous-ensemble du dépôt) est explicite.

## Procedure

### 1. Identifier les parties prenantes et préoccupations

Établir `Concern` uniquement quand une préoccupation de partie prenante est explicitement documentée (ticket, README, commentaire de code attribuable) — ne jamais inventer un stakeholder ou une préoccupation absente des preuves.

### 2. Identifier les éléments d'architecture

Pour chaque élément candidat (composant, module, service, interface, magasin de données, système externe) :

- confirmer son existence par un artefact réel (fichier, définition de service, entrée de configuration) ;
- classer `element_kind` et `granularity: architecture` ;
- préserver `observation_refs` et `evidence_refs`.

### 3. Établir les relations

Utiliser le vocabulaire `Relationship.relation_type` déjà existant (`depends_on`, `interfaces_with`, `allocated_to`, `parent_of`) — ne jamais introduire un type de relation uniquement pour enrichir le rendu.

### 4. Construire les vues

Une `ArchitectureView` n'existe que si un `viewpoint` explicite et un ensemble d'éléments/préoccupations associés sont identifiables. Ne pas produire une vue générique sans préoccupation associée.

### 5. Documenter les décisions d'architecture

Pour chaque `ArchitectureDecisionRecord` :

- si une justification explicite existe (commentaire, ADR, PR, ticket) → `rationale_status: explicitly_documented`, avec la citation exacte ;
- si la décision est seulement déductible du code → `rationale_status: inferred_from_implementation`, avec `rationale: "Rationale inferred from implementation. No explicit rationale/ADR found."` ;
- sinon → `rationale_status: unknown`.

Ne jamais fabriquer une justification plausible.

### 6. Séparer absence de preuve et absence de fonctionnalité

Une architecture élément non trouvé dans le périmètre fourni est `not_observed`, jamais une preuve que l'élément n'existe pas ailleurs dans le système.

## Analysis logic

`préoccupations → éléments → relations → vues → décisions`

Un élément n'est retenu que si son existence est evidence-backed. Une vue n'est retenue que si son viewpoint et ses préoccupations associées sont explicites.

## Decision semantics

- `element_established`: existence et rôle confirmés par preuve directe.
- `element_derived`: existence établie par combinaison cohérente de plusieurs preuves.
- `element_inferred`: existence probable mais dépendant d'une hypothèse non pleinement démontrée — toujours accompagné d'un `rationale`.
- `element_unknown`: ni observable ni raisonnablement inférable.
- `view_established` / `view_not_derivable`.
- `decision_documented` / `decision_inferred` / `decision_rationale_unknown`.

Ces statuts sont des statuts analytiques SPECTRUM, pas une certification ISO 42010.

## Findings

- `architecture_element_unsupported`
- `concern_without_stakeholder_basis`
- `view_without_viewpoint_basis`
- `relationship_endpoint_missing`
- `architecture_decision_without_rationale`
- `architecture_description_contradicts_existing_documentation`

## Evidence

Préserver : fichier/chemin exact, extrait de configuration, définition de contrat, commentaire attribué, PR ou ADR cité, avec `evidence_kind` correct (`project_artifact` pour le code lui-même, `derived_observation` pour une conclusion combinée).

## Handoff

- `architecture-reconstruction` quand une reconstruction plus large depuis le code brut est nécessaire.
- `software-design-description` pour la granularité conception (modules/interfaces internes).
- `architecture-diagram` pour la représentation dérivée.
- `lifecycle-documentation` pour la structuration documentaire finale.

## Output

Produire un `architecture_description_observation` contenant :

- `concern_refs`, `architecture_element_refs`, `architecture_view_refs`, `architecture_decision_record_refs`
- `relationship_refs`
- `findings`, `evidence_refs`, `unassessed_scope`

Ne jamais produire de verdict de préparation globale ni de score de qualité d'architecture.

## Exit conditions

`completed` quand tous les éléments candidats du périmètre déclaré sont assessés avec preuve suffisante.

`completed_with_findings` quand un ou plusieurs éléments/décisions posent un problème evidence-backed.

`completed_with_gaps` quand l'analyse est utile mais une partie du périmètre reste non résolue.

`blocked_on_missing_context` quand aucun artefact d'implémentation n'est fourni.

`not_applicable` quand le ticket ne concerne aucun changement architectural observable.

## Non-goals

Ce Skill ne fait pas :

- inventer un stakeholder, une préoccupation, un élément ou une décision ;
- attribuer une qualité (« bonne » ou « mauvaise » architecture) ;
- remplacer une revue de sécurité ou de performance ;
- décider de la préparation au développement ;
- prescrire un format ou un outil de modélisation comme imposé par la norme.

## Référence

Sources détaillées et cas d'évaluation : `REFERENCE.md` dans ce dossier (non chargé à l'exécution).
