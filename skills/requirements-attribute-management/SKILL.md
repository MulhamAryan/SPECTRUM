---
name: requirements-attribute-management
description: Structurer, analyser et préserver les attributs de besoins et d'exigences utiles à leur gestion et à leur qualité, sans rendre obligatoires les attributs qui ne le sont pas par la source ou le projet.
type: component
role: requirements_management
---

# Requirements Attribute Management

## Purpose

Structurer et analyser les attributs associés aux besoins et exigences lorsque ces attributs sont nécessaires pour interpréter, tracer, vérifier, valider ou gérer leur cycle de vie.

Ce Skill est une capacité SPECTRUM dérivée du corpus officiel INCOSE GtWR v4 et de ses relations avec les attributs. Le nom du Skill, son schéma et ses statuts sont des décisions SPECTRUM et ne constituent pas une nomenclature INCOSE.

## Source boundary

Sources autorisées :

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, notamment page 7 pour l'inventaire et les relations Attributs → Caractéristiques.
- NRM lorsqu'une définition détaillée d'un attribut est nécessaire.
- Représentations contrôlées locales dans `knowledge/sources/incose-gtwr-v4-2023/`.

La source officielle reste l'autorité. Une interprétation produite par SPECTRUM n'est jamais une définition INCOSE.

## When to use

Utiliser lorsque l'analyse exige de savoir quels attributs sont présents, absents, contradictoires, non attribués ou insuffisamment sourcés, notamment pour la traçabilité, la vérification, la validation et la gestion du cycle de vie.

Ne pas utiliser ce Skill pour décider que tous les attributs de l'inventaire A1–A49 sont obligatoires dans tous les projets.

## Inputs

Required:

- `requirement_or_need`

Recommended:

- `attributes`
- `requirement_set`
- `source_or_parent_evidence`
- `traceability_evidence`
- `verification_validation_evidence`
- `baseline_context`
- `project_attribute_policy`
- `project_glossary`
- `prior_findings`

## Preconditions

1. La cible est identifiable.
2. Les attributs fournis sont distingués du texte normatif de l'exigence.
3. La politique ou le contexte de projet applicable est connu lorsqu'il est utilisé pour déterminer l'obligation d'un attribut.
4. Une absence d'attribut n'est pas interprétée comme une non-conformité sans preuve d'applicabilité.

## Procedure

### 1. Preserve the requirement record

Conserver le besoin/exigence et ses identifiants comme evidence immuable.

### 2. Inventory supplied attributes

Identifier les attributs présents, leurs valeurs, leurs sources, leur auteur/origine lorsqu'ils sont fournis et leur statut de confiance.

### 3. Distinguish source inventory from project obligation

Comparer les attributs fournis avec l'inventaire officiel A1–A49, puis déterminer séparément si chaque attribut est :

- `required_by_project` ;
- `required_by_process` ;
- `supported_but_optional` ;
- `not_applicable` ;
- `applicability_unknown`.

L'inventaire GtWR ne devient pas automatiquement une politique projet.

### 4. Assess source-backed relationships

Utiliser la matrice officielle Attributes → Characteristics pour identifier les caractéristiques susceptibles d'être soutenues par un attribut.

Relations particulièrement pertinentes dans le corpus actuel :

- A1 → C1, C3, C12 ;
- A2 → C1, C9 ;
- A3 → C1 ;
- A4 → C9 ;
- A6 → C3, C4, C6, C7, C8 ;
- A8 → C3, C4, C6, C7, C8 ;
- A12 → C4, C8 ;
- A26 → C6, C12 ;
- A31 → C10 ;
- A32 → C1, C4, C7, C11 ;
- A33 → C1, C11 ;
- A34 → C1 ;
- A35 → C1 ;
- A36 → C6, C12 ;
- A38 → C6, C12 ;
- A39 → C3 ;
- A40 → C10.

Ces relations sont des transcriptions de la matrice source ; aucune relation supplémentaire ne doit être déduite du nom de l'attribut.

### 5. Assess attribute evidence

Pour chaque attribut applicable, déterminer :

- valeur présente ou absente ;
- source de la valeur ;
- attribution de la valeur ;
- cohérence avec le contexte ;
- conflit éventuel avec d'autres sources ;
- effet sur les analyses downstream.

### 6. Assess lifecycle-management information

Lorsque le contexte le justifie, examiner les attributs de gouvernance et d'évolution, par exemple identifiant, auteur, propriétaire, version, dates, stabilité, statut, changement, priorité et criticité.

Ne pas prétendre que leur définition détaillée provient du Summary Sheet lorsque celle-ci se trouve dans le NRM.

### 7. Assess traceability attributes

Examiner les attributs de traçabilité tels que trace to parent, trace to source, trace to interface definition et trace to dependent peer requirements lorsqu'ils sont applicables.

La présence d'un lien ou d'un identifiant ne prouve pas à elle seule la correction de la relation ; les Skills de traçabilité restent responsables de l'analyse relationnelle.

### 8. Detect contradictions and provenance gaps

Produire un finding lorsqu'un attribut :

- possède plusieurs valeurs incompatibles ;
- n'a pas de source identifiable alors qu'une source est requise ;
- est attribué à un mauvais objet ;
- est incompatible avec une source autorisée ;
- est annoncé comme obligatoire sans base de politique identifiable.

### 9. Preserve uncertainty

Une valeur absente ou inconnue produit un état d'incertitude lorsque l'applicabilité est établie, pas un faux défaut lorsque l'applicabilité elle-même est inconnue.

### 10. Handoff

Transmettre les conséquences aux Skills concernés avec les références d'évidence intactes.

## Analysis logic

Séquence canonique :

`target → attribute inventory → applicability basis → attribute value/source → characteristic relationship → finding/evidence status`

Le Skill ne transforme jamais un inventaire documentaire en obligation universelle.

## Decision semantics

- `attributes_sufficient`: les attributs applicables sont présents avec une base d'évidence suffisante pour le périmètre déclaré.
- `attributes_partial`: une partie des attributs applicables est établie, une autre reste incomplète.
- `attributes_missing`: un ou plusieurs attributs applicables nécessaires au périmètre sont absents.
- `attributes_conflicting`: des valeurs ou sources d'attributs se contredisent.
- `attribute_applicability_unknown`: l'obligation ou l'applicabilité ne peut pas être déterminée.
- `not_applicable`: aucun attribut relevant de ce Skill n'est applicable au périmètre déclaré.

Ces statuts sont des statuts analytiques SPECTRUM.

## Findings

- `attribute_missing`
- `attribute_value_missing`
- `attribute_source_missing`
- `attribute_provenance_missing`
- `attribute_conflict`
- `attribute_owner_missing`
- `attribute_status_inconsistent`
- `attribute_version_inconsistent`
- `attribute_traceability_missing`
- `attribute_policy_basis_missing`
- `attribute_applicability_unknown`
- `attribute_source_mismatch`

## Evidence

Conserver :

- cible exacte ;
- attribut et valeur ;
- source de valeur ;
- base d'applicabilité ;
- characteristic(s) associée(s) lorsqu'applicable ;
- politique projet ou processus applicable ;
- références de traçabilité ;
- source INCOSE correspondante.

## Handoff

- `requirement-relationship-traceability` pour les relations parent/source/interface/dépendances ;
- `verification-analysis` pour les attributs liés à la base de vérification ;
- `validation-analysis` pour les attributs nécessaires à la base de validation ;
- `requirements-context` pour les attributs qui servent à établir contexte, état ou condition ;
- futur Workflow de baseline/change management pour les attributs de cycle de vie.

## Output

Produire `requirements_attribute_observation` contenant au minimum :

- `target_ref`
- `attributes_assessed`
- `applicability`
- `attribute_observations`
- `characteristic_relationships`
- `findings`
- `evidence_refs`
- `status`
- `downstream_impacts`

## Exit conditions

- `completed`
- `completed_with_findings`
- `completed_with_gaps`
- `blocked_on_attribute_applicability`
- `not_applicable`

## Non-goals

- ne pas rendre A1–A49 universellement obligatoires ;
- ne pas inventer une valeur d'attribut ;
- ne pas inventer une définition détaillée du NRM ;
- ne pas conclure à la conformité INCOSE ;
- ne pas décider READY/NOT READY ;
- ne pas remplacer la traçabilité relationnelle ;
- ne pas silently normaliser une contradiction de source.

## References

Primary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, June 2023.

Local controlled sources:

- `knowledge/sources/incose-gtwr-v4-2023/attributes.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

## Evaluation

Minimum evaluation cases:

- applicable_rationale_attribute_present;
- trace_to_source_attribute_present;
- trace_attribute_missing_with_established_applicability;
- optional_attribute_not_marked_as_failure;
- conflicting_attribute_values;
- missing_attribute_source;
- attribute_value_mismatch_with_authoritative_source;
- owner_or_status_inconsistency;
- lifecycle_attribute_without_project_policy_is_inconclusive;
- traceability_attribute_handoff;
- verification_attribute_handoff;
- validation_attribute_handoff;
- no_false_positive_from_unmapped_attribute;
- no_false_positive_from_absent_optional_attribute.
