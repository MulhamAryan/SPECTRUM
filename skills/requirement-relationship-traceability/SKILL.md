---
name: requirement-relationship-traceability
description: Analyser les relations de transformation, d'allocation, de traçabilité et de dépendance entre besoins, exigences et artefacts associés à partir de preuves explicites.
type: component
role: relationship_traceability
---

# Requirement Relationship & Traceability

## Purpose

Identifier, qualifier and preserve explicit relationships between needs, requirements, sources, parent requirements, dependent peer requirements, allocations, interfaces, and related artifacts.

This is a SPECTRUM analytical capability derived from the official INCOSE Guide to Writing Requirements v4 (GtWR v4) and its associated NRM activity relationships. INCOSE does not define a Skill with this name or status vocabulary.

## Source boundary

Authoritative source boundary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, June 2023, pages 1–7.
- Official NRM Concepts and Activities → Characteristics matrix.
- Official GtWR v4 attribute inventory and cross-reference information where traceability-related attributes are listed.

Local controlled representations:

- `knowledge/sources/incose-gtwr-v4-2023/definitions.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/attributes.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`

The official INCOSE publication remains authoritative.

## Interpretation boundary

- `source_fact`: information explicitly represented in the INCOSE source.
- `spectrum_observation`: an observation produced from source facts and supplied project evidence.
- `business_gap`: a missing or unresolved project fact, relationship, artifact, agreement, or evidence item.

A missing relation is not automatically a non-conformity. The project scope, lifecycle level, source/parent structure, or applicable process must establish that the relation is relevant before it is reported as missing.

## When to use

Use this Skill when a candidate need or requirement is expected to have explicit relationships to:

- a lifecycle concept or source;
- a need or higher-level requirement;
- a child requirement or allocated requirement;
- a dependent peer requirement;
- an interface or interface definition;
- another artifact needed to understand transformation, allocation, or dependency.

Use it for orphan detection, directionality checks, relationship consistency, and traceability coverage.

Do not use it to invent parents, infer links from textual similarity alone, or declare implementation readiness.

## Inputs

Required:

- `requirements_or_needs`;
- `relationship_evidence`.

Recommended:

- `source_or_parent_set`;
- `allocation_data`;
- `dependent_peer_requirements`;
- `interface_definitions`;
- `traceability_matrix_or_register`;
- `attributes`;
- `architecture_model`;
- `prior_findings`;
- `context_evidence`.

## Preconditions

1. Relationship candidates or target objects are identifiable.
2. The analysis scope and evidence boundary are known.
3. Object identifiers are stable where possible.
4. The evidence boundary distinguishes absence of an artifact from proof that the underlying relation does not exist.
5. The relevant source/parent/peer/interface basis is available when a relation is being assessed.

## Procedure

### 1. Preserve the objects and links

Capture the exact requirements/needs and relationship artifacts used in the run.

Record:

- source object;
- target object;
- relationship type;
- direction;
- source of the relationship claim;
- evidence references;
- version or baseline information when supplied.

### 2. Classify the relationship basis

Determine whether the supplied evidence represents, as applicable:

- transformation from a lifecycle concept or source into a need;
- transformation from a need, source, or higher-level requirement into a requirement;
- flow-down/allocation from a parent to a child requirement;
- dependency between peer requirements;
- relationship to an interface definition;
- another project-defined relationship.

Do not introduce a relationship type merely because it would be convenient.

### 3. Verify object identity

For every asserted relationship:

- confirm the source object exists;
- confirm the target object exists;
- confirm the identifiers are unambiguous;
- confirm the relationship does not point to an obsolete or out-of-scope object when version/scope evidence is available.

### 4. Check transformation traceability

When a need or requirement is represented as transformed from a source, parent, or higher-level object, preserve and assess the supplied linkage.

Relevant source-backed characteristics include:

- C1 Necessary;
- C8 Correct;
- C10 Complete;
- C11 Consistent;
- C14 Able to be validated;
- C15 Correct.

Do not infer C1 or C8 merely from the presence of a link. The link is evidence for analysis; correctness or necessity still requires the appropriate transformation and source context.

### 5. Check allocation and dependent-peer relationships

For design-input requirement structures, inspect supplied evidence for:

- parent-to-child allocation/flow-down;
- child requirements meeting the intent of allocated parents;
- dependent peer relationships;
- consistency of relationship direction.

Where the official NRM matrix explicitly associates these activities with characteristics, preserve those source relationships rather than converting them into a synthetic rule.

### 6. Check interfaces

Where requirements concern interfaces, compare the requirement-side relationship with the supplied interface definition or model.

Do not treat the existence of an interface identifier as proof that the interface requirement is correct or complete.

### 7. Check relationship coverage

Identify:

- established relationships;
- relationships explicitly expected but missing;
- incomplete relationship artifacts;
- contradictory relationship assertions;
- orphan objects where an applicable source, parent, or peer basis has been established.

A missing relationship must be tied to an explicit applicability basis.

### 8. Check directionality and consistency

Verify that the relationship direction matches the semantics established by the project or source model.

Examples:

`source → transformed need`

`higher-level requirement → allocated child requirement`

`peer requirement ↔ dependent peer relationship`

These examples describe SPECTRUM relationship records, not additional INCOSE rules.

### 9. Correlate with official NRM activities

Use the official NRM matrix as contextual source evidence for activities such as:

- `3.2.2.4 Identity and Manage Interdependencies`;
- `6.2.2 Establish Traceability`;
- `6.2.2.1 Establishing Traceability Between Dependent Peer Requirements`;
- `6.2.3.6 Interface Requirements Audit`;
- `6.4.3 Allocation – Flow Down of Requirements`;
- `6.4.4 Defining Child Requirements that Meet the Intent of the Allocated Parents`;
- `6.4.7 Use of Traceability and Allocation to Manage Requirements`;
- `14.2.7 Combine Allocation and Traceability to Manage Requirements`;
- `14.2.8 Managing Interfaces`.

The official matrix establishes activity-to-characteristic relationships. It does not define a SPECTRUM traceability algorithm or score.

### 10. Separate missing evidence from missing relation

Distinguish:

- relation established;
- relation expected but not evidenced;
- relation applicability unresolved;
- artifact absent but relation status not determinable;
- conflicting source evidence.

Do not equate an absent matrix with an absent relationship.

### 11. Produce evidence-backed findings

Each finding must identify:

- affected objects;
- relationship type;
- expected direction;
- source-backed characteristic/activity where relevant;
- project applicability evidence;
- exact evidence references;
- downstream impact.

## Source-backed scope

The official GtWR v4 Summary Sheet defines a requirement expression as a requirement statement plus associated attributes, and defines requirement statements as the result of formal transformation from sources, needs, or higher-level requirements. Source: INCOSE GtWR v4 Summary Sheet, page 1.

The official NRM Concepts and Activities → Characteristics matrix includes the traceability, dependent-peer, interface, allocation, child-requirement, and management activities listed in Procedure 9. Source: INCOSE GtWR v4 Summary Sheet, pages 5–6.

The official characteristics define correctness of an individual requirement in relation to the need, source, or higher-level requirement from which it was transformed, and set-level correctness in relation to the corresponding higher-level sources. Source: INCOSE GtWR v4 Summary Sheet, page 2.

The official attribute inventory includes traceability-relevant attributes such as A2 Trace to Parent, A3 Trace to Source, A32 Trace to Interface Definition, and A33 Trace to Dependent Peer Requirements. Their detailed attribute guidance belongs to the NRM and is not redefined by this Skill. Source: INCOSE GtWR v4 Summary Sheet, page 7 and Appendix E.

## Analysis logic

Use this sequence:

`objects → relationship basis → identity → direction → evidence → applicability → relationship status`

A relationship record is valid only when its endpoints and relationship semantics are evidenced. Textual similarity alone does not establish traceability.

## Decision semantics

Use only these Skill-level result semantics:

- `trace_established`: the relationship is explicitly evidenced with identifiable endpoints and applicable semantics.
- `trace_missing`: a relationship is applicable and expected from explicit project/source context but is not established in the available evidence.
- `trace_incomplete`: a traceability artifact exists but does not cover the applicable scope.
- `trace_contradictory`: supplied authoritative project artifacts assert incompatible relationship information.
- `traceability_context_missing`: applicability or relationship basis cannot be established reliably.
- `not_applicable`: the declared relationship type is outside the analysis scope.

These are SPECTRUM analytical statuses, not INCOSE certification statuses.

## Findings

Use specific findings such as:

- `source_trace_missing`
- `parent_trace_missing`
- `allocation_trace_missing`
- `dependent_peer_trace_missing`
- `interface_trace_missing`
- `orphan_requirement_observed`
- `relationship_endpoint_missing`
- `relationship_direction_inconsistent`
- `incomplete_traceability_artifact`
- `contradictory_traceability`
- `relationship_applicability_unresolved`
- `source_alignment_not_established`
- `transformation_evidence_insufficient`

## Evidence

Preserve:

- exact source and target identifiers;
- relationship type and direction;
- traceability matrix/register entries;
- source/parent/peer/interface artifacts;
- version/baseline information when available;
- official INCOSE source references used for the analysis;
- project evidence establishing applicability.

## Handoff

Results can feed:

- `requirements-context` for missing source or level context;
- `requirement-statement-quality` for member wording analysis;
- `requirement-set-quality` for set-level completeness/consistency/correctness;
- `verification-analysis` where traceability is needed to establish a verification target;
- `validation-analysis` where traceability is needed to establish the validation chain;
- `elicitation-gap` when source, parent, peer, or interface evidence is missing.

Handoffs preserve evidence references and interpretation level.

## Output

Produce a `relationship_traceability_observation` containing:

- `object_refs`;
- `relationship_records`;
- `relationship_status`;
- `source_characteristic_refs`;
- `source_activity_refs`;
- `findings`;
- `missing_context`;
- `evidence_refs`;
- `unassessed_scope`.

Do not output a global implementation-readiness decision.

## Exit conditions

`completed` when all applicable relationship checks are assessed with sufficient evidence.

`completed_with_findings` when one or more evidence-backed relationship issues are observed.

`completed_with_gaps` when the relationship assessment is useful but applicability or evidence remains unresolved.

`blocked_on_missing_context` when the endpoints, relationship basis, or evidence boundary cannot be established.

`not_applicable` when no declared relationship in scope applies.

## Non-goals

This Skill does not:

- invent source, parent, child, peer, or interface relationships;
- infer traceability from textual similarity alone;
- make every traceability matrix universally mandatory;
- infer C1, C8, C10, C11, C14, or C15 solely from link presence;
- create a synthetic INCOSE traceability characteristic or rule;
- replace project requirements management or configuration management;
- approve or reject implementation readiness;
- issue formal INCOSE certification;
- silently resolve conflicting authoritative project artifacts.

## Référence

Critères d'évaluation et sources détaillées : `REFERENCE.md` dans ce dossier (non chargé à l'exécution).
