---
name: architecture-diagram
description: Dériver une représentation diagrammatique (Mermaid ou équivalent) strictement à partir du modèle d'architecture validé et des références de preuve, sans inventer de relation pour l'esthétique.
type: component
role: architecture_diagram
---

# Architecture Diagram

## Purpose

Dériver une représentation visuelle (diagramme) strictement à partir des `ArchitectureElement`, `ArchitectureView` et `Relationship` déjà établis par `architecture-description`/`architecture-reconstruction`/`software-design-description` — jamais une source de vérité indépendante.

Aucune norme ne prescrit Mermaid, PlantUML ou un autre format : le choix de format est une décision d'implémentation SPECTRUM (ISO42010-R003), pas une exigence de l'ISO/IEC/IEEE 42010:2022.

## Source boundary

- `knowledge/sources/iso-iec-ieee-42010-2022/knowledge.yaml` (limite : la norme ne spécifie ni notation ni outil).
- Aucune source normative supplémentaire : ce Skill est une décision d'implémentation SPECTRUM.

## Interpretation boundary

Un diagramme est toujours `derived` par construction (jamais `observed` directement) : il reflète des `ArchitectureElement`/`Relationship` déjà qualifiés en amont, avec leurs propres statuts (`observed`/`derived`/`inferred`/`unknown`) préservés par annotation, pas effacés par le rendu.

## When to use

Utiliser en dernière étape de la branche architecture, une fois que `architecture-description`, `architecture-reconstruction` et, le cas échéant, `software-design-description` ont produit un modèle d'éléments et de relations validé.

Ne pas l'utiliser pour découvrir de nouveaux éléments ou relations — ce Skill ne fait aucune analyse de code ou de preuve, uniquement du rendu dérivé.

## Inputs

Required:

- `architecture_element_refs` et `relationship_refs` déjà établis (pas de code source brut).

Recommended:

- `architecture_view_refs` pour organiser le diagramme par vue/viewpoint plutôt qu'en un graphe plat.

## Preconditions

1. Au moins un `ArchitectureElement` avec au moins une `Relationship` évaluée est disponible.
2. Aucune relation supplémentaire n'est requise ou inventée pour produire un diagramme visuellement complet.

## Procedure

### 1. Sélectionner le périmètre du diagramme

Un diagramme par `ArchitectureView` quand des vues existent ; un diagramme global uniquement si aucune vue n'a été établie et que le périmètre reste raisonnable à représenter sans perte de lisibilité.

### 2. Transposer les éléments

Chaque nœud du diagramme correspond à exactement un `ArchitectureElement` existant, avec son identifiant technique conservé en commentaire ou en annexe pour la traçabilité.

### 3. Transposer les relations

Chaque arête correspond à exactement une `Relationship` existante (`depends_on`, `interfaces_with`, `allocated_to`, `parent_of`). Ne jamais ajouter une arête pour relier des nœuds visuellement isolés si aucune relation evidence-backed ne le justifie — un nœud isolé reste isolé dans le diagramme.

### 4. Annoter l'incertitude

Un élément ou une relation `inferred` ou `unknown` est visuellement distingué (ex. style en pointillés, libellé explicite) plutôt que rendu identique à un élément `observed`.

### 5. Ne jamais dériver de conclusion du diagramme

Le diagramme ne devient jamais lui-même une preuve pour un autre Skill ; toute analyse ultérieure doit revenir au modèle d'architecture sous-jacent, pas au rendu.

## Analysis logic

`éléments/relations validés → sélection du périmètre (vue ou global) → transposition nœuds/arêtes → annotation d'incertitude`

Aucune étape d'analyse de preuve : ce Skill est un renderer, au même titre que `documentation-composer` l'est pour le document final.

## Decision semantics

- `diagram_derived`: rendu produit, toutes les relations tracées vers le modèle source.
- `diagram_not_derivable`: aucun élément/relation suffisant pour un rendu utile.

## Findings

- `diagram_element_without_model_basis` (ne doit jamais se produire — signale une violation si détectée)
- `diagram_relationship_without_model_basis` (idem)
- `uncertainty_not_visually_distinguished`

## Evidence

Ce Skill ne produit pas de nouvelle `Evidence` ; chaque nœud/arête référence l'`ArchitectureElement`/`Relationship` source.

## Handoff

- Retour vers `architecture-description`/`architecture-reconstruction` si un élément semble manquant — ce Skill ne comble jamais lui-même ce manque.
- `lifecycle-documentation` pour l'intégration du ou des diagrammes dans `TechnicalDocumentation.diagram_artifact_refs`.

## Output

Produire un ou plusieurs `Artifact` (`artifact_kind: diagram`) référençant leur contenu Mermaid (ou équivalent) et la liste exacte des `architecture_element_refs`/`relationship_refs` représentés.

## Exit conditions

`completed` (diagramme produit), `not_applicable` (aucun élément/relation suffisant).

## Non-goals

Ce Skill ne fait pas :

- analyser le code ou découvrir de nouveaux éléments/relations ;
- ajouter une relation pour l'esthétique du diagramme ;
- présenter Mermaid ou tout autre format comme prescrit par une norme ;
- devenir une source de vérité indépendante du modèle d'architecture.

## Référence

`REFERENCE.md` dans ce dossier (non chargé à l'exécution).
