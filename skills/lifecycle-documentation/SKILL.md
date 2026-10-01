---
name: lifecycle-documentation
description: Définir le modèle documentaire canonique nécessaire à une documentation technique de cycle de vie, sans imposer de gabarit Confluence arbitraire, selon ISO/IEC/IEEE 15289.
type: component
role: lifecycle_documentation
---

# Lifecycle Documentation

## Purpose

Structurer les informations nécessaires à une documentation technique de cycle de vie complète pour une fonctionnalité déjà implémentée : rattacher chaque section établie (périmètre, exigences, architecture, décisions, vérification, limites, questions ouvertes) à l'objet canonique `TechnicalDocumentation`, sans dicter un gabarit Confluence figé.

Dérivé de la portée publique de l'ISO/IEC/IEEE 15289:2019.

## Source boundary

- `knowledge/sources/iso-iec-ieee-15289-2019/knowledge.yaml`
- `rules/sources/iso-iec-ieee-15289-2019/rules.yaml`

Seul le vocabulaire de 7 types génériques de document (description, plan, policy, procedure, report, request, specification) est confirmé publiquement. Le contenu normatif détaillé par type n'est pas vérifié dans cette session.

## Interpretation boundary

Ce Skill ne produit pas lui-même de nouvelles preuves : il consolide celles déjà produites par `architecture-description`, `architecture-reconstruction`, `software-design-description`, `test-documentation`, et le stage de découverte d'implémentation, dans la structure `TechnicalDocumentation`.

## When to use

Utiliser en fin de pipeline `/spectrum:document-feature`, une fois les analyses spécialisées terminées, pour assembler leurs résultats en un modèle documentaire canonique cohérent — jamais pour réanalyser le code ou réinterpréter leurs constats.

## Inputs

Required:

- `architecture_description_observation`, `architecture_reconstruction_observation` (quand disponibles).
- `software_design_description_observation` (quand disponible).
- `test_documentation_observation` (quand disponible).
- `feature_ref` (ticket ou périmètre documenté).

Recommended:

- `requirement_refs` établis par les sources disponibles (ticket, spécification).
- `known_limitations`, `open_questions` déjà identifiés en amont.

## Preconditions

1. Au moins une analyse spécialisée amont a produit un résultat (même partiel).
2. Le `feature_ref` est identifiable.

## Procedure

### 1. Rattacher chaque information à un type générique

Pour chaque section candidate de `TechnicalDocumentation`, identifier si son contenu relève d'une `description` (état observé), d'une `specification` (exigence), d'un `report` (constat, limite), ou d'un autre type générique — de façon informative, jamais comme obligation vérifiée par la norme.

### 2. Consolider sans réanalyser

Ne jamais recalculer un constat déjà produit par un Skill amont ; ce Skill assemble des références (`*_refs`), il ne recrée pas les objets sous-jacents.

### 3. Représenter l'absence explicitement

Une section sans contenu établi porte la mention explicite « Aucun changement pertinent détecté » ou « Preuve insuffisante », jamais un remplissage plausible.

### 4. Préserver les contradictions

Si deux sources amont se contredisent (ex. documentation existante vs. code observé), préserver la contradiction dans `known_limitations`/`open_questions` — ne jamais la résoudre silencieusement en faveur de l'une.

### 5. Distinguer ce qui mérite le corps du document de ce qui relève du catalogue

Pour chaque `ArchitectureElement`/relation consolidé, déterminer s'il est référencé par une `ArchitectureView`, une `ArchitectureDecisionRecord`, un `Finding`, ou une limite connue. Marquer ceux qui le sont comme `narrative_relevant: true` ; les autres restent disponibles pour l'annexe de catalogue mais ne sont pas remontés comme contenu central. Ce marquage guide `documentation-composer` ; il ne supprime aucune donnée, il hiérarchise sa présentation.

### 6. Ne jamais figer une structure Confluence rigide

La combinaison ou la subdivision des sections reste possible selon le contexte du projet (ISO15289-R002) ; la structure de `outputs/technical-documentation-report.yaml` est une convention de rendu SPECTRUM, pas une exigence normative.

## Analysis logic

`résultats amont → rattachement au type générique → consolidation par référence → absence explicite → contradictions préservées`

## Decision semantics

- `documentation_complete`: toutes les sections applicables ont un contenu établi ou une absence explicite.
- `documentation_partial`: une ou plusieurs analyses amont manquent ou ont échoué.
- `documentation_blocked`: aucune analyse amont exploitable n'est disponible.

## Findings

- `section_without_upstream_basis`
- `contradiction_silently_resolved` (jamais permis — signalé s'il est détecté dans un résultat amont)
- `upstream_analysis_missing_or_failed`

## Evidence

Ce Skill ne crée pas de nouvelle `Evidence` ; il propage les `evidence_refs` des objets qu'il consolide.

## Handoff

- `documentation-composer` (agent de rendu) pour la production du document final.
- Retour vers le Skill amont concerné si une section manque une référence attendue.

## Output

Produire un objet `TechnicalDocumentation` (entité canonique) avec tous ses champs `*_refs` renseignés par référence, `status`, `provenance`, et le marquage `narrative_relevant` par élément (étape 5).

## Exit conditions

`completed`, `completed_with_gaps` (sections partielles), `blocked` (aucune entrée amont exploitable).

## Non-goals

Ce Skill ne fait pas :

- réanalyser le code, les tests, ou l'architecture ;
- inventer une section pour satisfaire un gabarit ;
- imposer une structure Confluence comme normative ;
- produire une décision de préparation ou un score.

## Référence

`REFERENCE.md` dans ce dossier (non chargé à l'exécution).
