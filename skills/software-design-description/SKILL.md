---
name: software-design-description
description: Produire une description de conception logicielle (composants, interfaces, données, dépendances, interactions, contraintes, décisions de conception) récupérée depuis une implémentation existante, selon IEEE 1016 (référence conceptuelle, norme Inactive-Reserved).
type: component
role: software_design_description
---

# Software Design Description

## Purpose

Décrire la conception logicielle au niveau composant/module (granularité plus fine que `architecture-description`) à partir des `ArchitectureElement` de granularité `design` produits par `architecture-reconstruction`.

Dérivé du résumé public de l'IEEE 1016-2009. **IEEE liste cette norme Inactive-Reserved** : elle sert de référence conceptuelle sur le contenu d'une Software Design Description (SDD), jamais de cible de conformité.

## Source boundary

- `knowledge/sources/ieee-1016-2009/knowledge.yaml`
- `rules/sources/ieee-1016-2009/rules.yaml`

Seul le résumé public fetché directement depuis `standards.ieee.org` est confirmé (voir README de la source) : une SDD couvre la documentation de conception y compris en contexte de rétro-ingénierie, quel que soit le type d'application, sans restriction de taille. Le modèle de contenu détaillé (entité, attribut, vue, décision/relation de conception) est largement connu publiquement mais **non vérifié** dans cette session — il n'est donc pas imposé comme structure obligatoire ici ; ce Skill s'appuie à la place sur les entités canoniques SPECTRUM déjà définies.

## Interpretation boundary

Identique à `architecture-description`/`architecture-reconstruction` : `observed`/`derived`/`inferred`/`unknown`, représentés via `Observation.status`, `Evidence.evidence_kind`, `Evidence.provenance.method` et `rationale`. Toute conception reconstruite (et non rédigée a priori) doit porter la mention explicite de reconstruction (IEEE1016-R001).

## When to use

Utiliser quand la documentation technique doit descendre au niveau des composants internes, de leurs interfaces, de leurs données échangées, de leurs dépendances et interactions, et des décisions de conception associées — au-delà de la vue architecture de service déjà couverte par `architecture-description`.

Ne pas l'utiliser pour documenter des éléments de granularité `architecture` déjà couverts ailleurs — éviter la duplication de contenu entre les deux granularités.

## Inputs

Required:

- `architecture_element_refs` (granularité `design`, produits par `architecture-reconstruction`).

Recommended:

- `interface_definitions`, `data_contracts`, `internal_api_signatures`.
- `design_constraints` (ex. contraintes de performance, de sécurité, de compatibilité explicitement documentées).
- `existing_design_documentation`.

## Preconditions

1. Au moins un `ArchitectureElement` de granularité `design` est disponible.
2. Le périmètre de conception analysé est explicite.

## Procedure

### 0. Ne pas redécrire ce qu'architecture-description a déjà établi

Ce Skill n'énumère **jamais** à nouveau la liste des éléments déjà produite par `architecture-reconstruction`/`architecture-description`. Pour chaque élément de granularité `design`, vérifier d'abord s'il apporte une information **nouvelle** (signature exacte d'interface, type de donnée échangé, contrainte, décision) par rapport à ce qui est déjà couvert au niveau architecture. Si un élément n'apporte rien de nouveau à ce niveau de détail, ne pas produire d'entrée de conception pour lui — la duplication entre les deux niveaux est un défaut à éviter, pas une preuve de rigueur.

### 1. Confirmer les composants et modules qui apportent une information nouvelle

Pour chaque élément retenu à l'étape 0 : préserver son identité, son rôle observé, et les interfaces qu'il expose ou consomme (`element_kind: interface` comme élément séparé, relié par `interfaces_with`).

### 2. Documenter les données échangées

Décrire la structure des données uniquement à partir de contrats/schémas réellement observés (DTO, schéma JSON, définition de table utilisée par le module). Ne jamais inventer un champ ou un type non présent dans la preuve.

### 3. Documenter les dépendances et interactions

Réutiliser les `Relationship` déjà établis par `architecture-reconstruction` ; ne pas dupliquer l'analyse de dépendance, uniquement la qualifier au niveau conception (ex. ordre d'appel observé dans le code).

### 4. Documenter les contraintes de conception

N'enregistrer une contrainte (`Constraint`, entité déjà existante) que si elle est explicitement exprimée (commentaire, configuration, règle métier documentée) — jamais déduite de la seule structure du code.

### 5. Documenter les décisions de conception

Utiliser `ArchitectureDecisionRecord` avec `rationale_status` selon la même discipline que `architecture-description` : documentée, inférée, ou inconnue.

### 6. Marquer la reconstruction

Toute description de conception construite depuis une implémentation existante (et non depuis une documentation de conception a priori) porte `provenance.method: reverse_engineering` — jamais présentée comme la conception d'origine telle que l'auteur l'avait prévue.

## Analysis logic

`éléments de conception → interfaces/données → dépendances/interactions → contraintes → décisions`

## Decision semantics

Identique à `architecture-description` (`element_established`, `element_derived`, `element_inferred`, `element_unknown`), avec :

- `design_reconstructed`: la description provient de rétro-ingénierie, marquage explicite requis.
- `design_documented_a_priori`: une documentation de conception antérieure existe et a été utilisée comme source (rare en post-implémentation, mais possible).

## Findings

- `design_element_unsupported`
- `interface_data_contract_not_established`
- `design_constraint_without_explicit_source`
- `design_decision_without_rationale`
- `reconstruction_marker_missing`

## Evidence

Préserver : signature d'interface exacte, schéma de données cité, contrainte citée avec sa source, fichier/ligne.

## Handoff

- `architecture-reconstruction` si un élément de conception nécessite une preuve supplémentaire au niveau architecture.
- `architecture-diagram` pour la représentation dérivée au niveau composant.
- `lifecycle-documentation` pour l'intégration dans la structure documentaire finale.

## Output

Produire un `software_design_description_observation` contenant :

- `architecture_element_refs` (design), `technical_decision_refs`, `constraint_refs`
- `findings`, `evidence_refs`, `unassessed_scope`

## Exit conditions

`completed`, `completed_with_findings`, `completed_with_gaps`, `blocked_on_missing_context` (aucun élément design disponible), `not_applicable`.

## Non-goals

Ce Skill ne fait pas :

- inventer un champ, une interface ou une contrainte non observée ;
- affirmer une conformité IEEE 1016 ;
- dupliquer l'analyse de dépendance déjà faite par `architecture-reconstruction` ;
- redécrire un élément déjà couvert au niveau architecture sans information nouvelle ;
- juger la qualité de la conception.

## Référence

`REFERENCE.md` dans ce dossier (non chargé à l'exécution).
