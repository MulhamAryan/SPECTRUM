---
name: requirements-context
description: Establish and assess the contextual evidence needed to understand, transform, and evaluate an individual need or requirement without inventing missing project facts.
type: component
role: requirements_context
---

# Requirements Context

## Purpose

Establish whether the contextual information surrounding a need or requirement is sufficient to interpret and assess it reliably.

This is a SPECTRUM analytical capability derived from the official INCOSE Guide to Writing Requirements v4 (GtWR v4), its Summary Sheet, and the cited NRM/GtNR relationship information. The Skill does not create an additional INCOSE characteristic or rule.

The Skill is concerned with the evidence needed to understand the entity, level, source/transformation context, conditions, constraints, and terminology of the candidate need or requirement. It does not decide implementation readiness.

## Source boundary

Authoritative source boundary:

- INCOSE Guide to Writing Requirements v4, INCOSE-TP-2010-006-04.
- INCOSE GtWR v4 Summary Sheet, especially pages 1–7.
- Official GtWR v4 characteristics and rule definitions.
- Official GtWR v4 NRM Concepts and Activities to Characteristics cross-reference matrix.
- Official GtWR v4 attribute inventory, noting that the Summary Sheet identifies these attributes as defined in the NRM.

Local structured source files are controlled representations of the official publications:

- `knowledge/sources/incose-gtwr-v4-2023/definitions.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/rules.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/attributes.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`

The official INCOSE publication remains authoritative. Local files do not become an independent normative source.

## Interpretation boundary

Keep these levels distinct:

- `source_fact`: information explicitly represented in the official INCOSE publication.
- `spectrum_observation`: a SPECTRUM assessment of supplied project evidence against the source-backed analysis scope.
- `business_gap`: a project-specific missing fact, decision, artifact, agreement, or evidence item.

The concept of a `requirements_context` Skill is a SPECTRUM architecture decision. INCOSE does not thereby define this Skill or its status vocabulary.

## When to use

Use this Skill before or alongside requirement statement/set analysis when interpretation depends on contextual information that is not contained in the statement alone.

Use it particularly when it is necessary to establish:

- the entity to which the need or requirement applies;
- the applicable abstraction, organizational, or architecture level;
- the lifecycle concept, source, need, or higher-level requirement from which the statement was transformed;
- conditions of use, states, or modes relevant to interpretation;
- constraints and acceptable-risk context relevant to feasibility;
- terms and concepts referenced by the statement;
- the evidence boundary for judging necessity, correctness, feasibility, or completeness.

Do not use it to invent the missing context. Report the gap instead.

## Inputs

Required:

- `requirement_expression` or `requirement_set`;
- `available_context_evidence`.

Recommended:

- `entity_definition`;
- `abstraction_or_architecture_level`;
- `source_or_parent_reference`;
- `lifecycle_concept_reference`;
- `project_glossary`;
- `project_data_dictionary`;
- `architecture_model`;
- `conditions_of_use`;
- `states_and_modes`;
- `constraints_and_risk`;
- `stakeholder_evidence`;
- `traceability_evidence`;
- `prior_findings`.

Optional:

- `style_guide`;
- `interface_definitions`;
- `allocation_data`;
- `validation_basis`;
- `verification_basis`.

## Preconditions

1. The candidate need or requirement is identifiable.
2. The analysis scope and evidence boundary are known.
3. A canonical GtWR v4 source reference is available.
4. Supplied project artifacts can be distinguished from absence of artifacts; absence alone is not proof that the underlying information does not exist.
5. Any source used to establish project facts is retained as evidence.

## Procedure

### 1. Preserve the candidate

Record the exact supplied need/requirement expression or set without rewriting it.

Record stable identifiers, source references, and linked artifacts.

### 2. Identify the entity and level

Determine the entity to which the need or requirement applies and the applicable level of abstraction, organization, or system architecture.

Use authoritative project evidence such as an architecture model, system definition, organizational boundary, or approved source document.

For C2 Appropriate, do not infer that the amount of detail is appropriate merely because the statement is grammatically sound.

### 3. Establish the transformation source

Determine whether the candidate was transformed from:

- a lifecycle concept;
- an external or internal source;
- a need;
- a higher-level requirement;
- another explicitly identified authoritative basis.

Preserve source-to-candidate references where they exist.

This contextual basis is relevant to C1 Necessary and C8 Correct because the official characteristics explicitly define these in relation to the source, lifecycle concept, need, or higher-level requirement.

### 4. Establish conditions and operating context

Identify explicit conditions, states, modes, and conditions of use that materially affect interpretation or applicability.

Compare the candidate with available attributes and supporting artifacts such as states and modes or conditions of use.

Do not add a condition merely because one would be customary in a similar system.

### 5. Establish constraint and risk context

Identify explicit constraints applicable to the entity or obligation, including where supplied:

- cost;
- schedule;
- technical constraints;
- legal or regulatory constraints;
- ethical constraints;
- safety constraints;
- other relevant entity constraints;
- acceptable-risk basis.

C6 Feasible must be treated as context-dependent. Missing feasibility evidence is an evidence gap, not automatic proof of infeasibility.

### 6. Establish terminology context

Resolve terms used in the candidate against authoritative project vocabulary when available:

- project glossary;
- data dictionary;
- architecture model;
- approved ontology or equivalent project vocabulary.

Do not manufacture definitions for undefined project terms and present those definitions as source facts.

### 7. Establish stakeholder and agreement context

Where the evidence permits, identify the applicable stakeholders, approving authority, or agreement basis relevant to the statement or set.

The purpose is to identify evidence needed for interpretation and assessment, not to invent stakeholder approval.

### 8. Identify contextual evidence dependencies

Map each conclusion that depends on context to the specific evidence needed to support it.

Examples:

- C1 → transformation/source or lifecycle-concept evidence;
- C2 → entity/level/abstraction evidence;
- C3/C4 → contextual terms, conditions, constraints, and applicable scope;
- C6 → entity constraints and risk evidence;
- C8 → source/parent/transformation evidence;
- C9 → approved pattern/style or governing convention;
- applicable rule analysis → associated glossary/data dictionary, project conventions, or other source evidence when explicitly relevant.

These are evidence dependencies for SPECTRUM analysis, not new INCOSE requirements.

### 9. Analyze unknowns explicitly

Identify unknowns that prevent reliable interpretation or assessment.

Distinguish:

- unknown because the evidence was not supplied;
- unknown because the project source is ambiguous or conflicting;
- unknown because the scope itself is not established.

Do not convert unknowns into non-conformities without sufficient evidence.

### 10. Produce contextual findings

Each finding must state:

- the affected requirement/set;
- the contextual element;
- the evidence expected or used;
- the source-backed characteristic or activity to which it relates;
- the impact on downstream analysis;
- evidence references.

## Source-backed scope

The official GtWR v4 Summary Sheet defines an entity and situates needs and requirements in relation to lifecycle concepts, sources, needs, higher-level requirements, constraints, and acceptable risk. It defines C1 Necessary, C2 Appropriate, C4 Complete, C6 Feasible, C8 Correct, and C9 Conforming in ways that depend on contextual or transformation information rather than wording alone.

The same source states that the underlying analysis from which a need or requirement was derived is as important as how well the statement is formed. The NRM Concepts and Activities → Characteristics matrix links activities such as analysis from which needs and requirements are derived, managing unknowns, appropriate-to-level analysis, feasibility/risk, stakeholder agreement, and baseline/manage activities to relevant characteristics.

The official attribute inventory includes A1 Rationale, A2 Trace to Parent, A3 Trace to Source, A4 States and Modes, A12 Condition of Use, and other contextual or management attributes. The Summary Sheet identifies these attributes as defined in the NRM; SPECTRUM does not redefine them here.

## Analysis logic

Use this sequence:

`candidate → entity/level → transformation source → conditions/constraints → terminology → stakeholder/agreement context → unknowns → evidence sufficiency`

The Skill answers whether the context required for reliable analysis is established. It does not answer whether the project should implement the requirement.

For a context-dependent characteristic, absence of a required evidence item produces an inconclusive result unless an applicable project or process rule establishes that the evidence must exist.

## Decision semantics

Use only these Skill-level result semantics:

- `context_established`: the relevant contextual basis is sufficiently established for the declared analysis scope.
- `context_partially_established`: important context is available but one or more downstream conclusions remain limited.
- `context_missing`: essential contextual evidence is not available in the analysis boundary.
- `context_conflicting`: supplied authoritative project sources conflict in a way that blocks reliable interpretation.
- `not_applicable`: the requested context element is explicitly outside the declared scope.

These statuses are SPECTRUM analytical statuses, not INCOSE certification statuses.

## Findings

Use evidence-backed findings such as:

- `entity_not_established`
- `abstraction_level_not_established`
- `source_or_parent_not_established`
- `lifecycle_concept_not_established`
- `condition_of_use_missing`
- `state_or_mode_context_missing`
- `constraint_context_missing`
- `risk_basis_missing`
- `stakeholder_context_missing`
- `term_definition_missing`
- `context_source_conflict`
- `analysis_blocked_by_context_gap`
- `source_alignment_not_established`
- `necessary_context_not_established`

A finding must identify evidence; it must not imply a missing business fact that was not established by the project evidence boundary.

## Evidence

Preserve:

- exact candidate expression/set;
- entity and level evidence;
- source/parent/lifecycle-concept evidence;
- condition/state/mode evidence;
- constraint and risk evidence;
- glossary/data-dictionary/architecture evidence;
- stakeholder or agreement evidence when used;
- applicable official INCOSE source references;
- precise project evidence references.

## Handoff

Results can feed:

- `requirement-statement-quality` for wording analysis;
- `requirement-set-quality` for set-level analysis;
- `requirement-relationship-traceability` for source/parent/allocation relationships;
- `verification-analysis` for verification basis;
- `validation-analysis` for validation basis;
- `elicitation-gap` when missing source or stakeholder information requires further elicitation.

The handoff must preserve evidence references and interpretation level.

## Output

Produce a `requirements_context_observation` containing:

- `requirement_ref` or `set_ref`;
- `context_scope`;
- `context_elements`;
- `context_status`;
- `characteristics_affected`;
- `source_activity_refs`;
- `missing_context`;
- `conflicting_context`;
- `evidence_refs`;
- `downstream_impacts`.

Do not output a global implementation-readiness decision.

## Exit conditions

`completed` when the declared contextual scope is sufficiently established.

`completed_with_gaps` when the context assessment is useful but one or more relevant elements remain unavailable.

`blocked_on_missing_context` when an essential entity, source, scope, or evidence boundary cannot be established.

`not_applicable` when the target is outside this Skill's declared context scope.

## Non-goals

This Skill does not:

- invent project facts, business values, stakeholder decisions, constraints, or requirements;
- redefine INCOSE characteristics or rules;
- claim that every possible context artifact is mandatory;
- declare feasibility, correctness, necessity, or validation success solely from context presence;
- create a synthetic traceability characteristic;
- replace requirements verification, validation, elicitation, or management processes;
- approve or reject implementation readiness;
- issue formal INCOSE certification;
- silently resolve conflicts between authoritative project sources.

## Référence

Critères d'évaluation et sources détaillées : `REFERENCE.md` dans ce dossier (non chargé à l'exécution).
