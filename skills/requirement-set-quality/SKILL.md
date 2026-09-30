---
name: requirement-set-quality
description: Analyser la qualité d'un ensemble de besoins ou d'exigences contre les caractéristiques d'ensemble C10–C15 et les règles GtWR v4 de niveau ensemble (R29, R41, R42) explicitement reliées.
type: component
role: analysis
---

# Skill: requirement-set-quality

## Purpose

Analyze the quality of a set of needs or requirements against the set-level characteristics and the writing rules of the INCOSE Guide to Writing Requirements v4 (GtWR v4) that are explicitly related to set characteristics.

This is a SPECTRUM analytical capability derived from the official INCOSE source corpus. The Skill does not add, redefine, or claim authority for INCOSE rules.

## Source boundary

Authoritative source boundary:

- INCOSE Guide to Writing Requirements v4, INCOSE-TP-2010-006-04.
- INCOSE GtWR v4 Summary Sheet, especially pages 2–6.
- INCOSE GtWR v4 set-level rule-to-characteristic relationships in the official cross-reference matrix.
- INCOSE GtWR v4 NRM Concepts and Activities to Characteristics matrix on pages 5–6 when contextual analysis is required.

Local structured source files are controlled representations of those publications:

- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/rules.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`

The official source remains authoritative. Local files must not be treated as an independent normative source.

## Interpretation boundary

The following are distinct and must remain distinct:

- `source_fact`: a fact explicitly represented in the official INCOSE publication.
- `spectrum_observation`: an analytical observation produced by this Skill using the source facts and the supplied project evidence.
- `business_gap`: a project-specific missing fact, decision, agreement, or evidence item.

A SPECTRUM observation, finding, status, heuristic, threshold, or recommendation is not an INCOSE rule unless the official source explicitly states it.

## When to use

Use this Skill when the analysis target is a collection of related need statements or requirement statements and the question concerns whether the set itself is complete, consistent, feasible, comprehensible, validatable, or correct.

Use it after individual-statement analysis when set-level relationships, coverage, overlap, contradiction, uniformity, structure, or aggregate evidence must be examined.

Do not use it as a substitute for source elicitation, detailed verification/validation planning, or project approval decisions.

## Inputs

Required:

- `requirement_set`: the complete available set of need expressions or requirement expressions for the analysis scope.

Recommended:

- `set_type`: `need_set` or `requirement_set`.
- `entity_context`: entity, level, architecture scope, system-of-interest, process, or other applicable context.
- `parent_set` or `source_set`: the higher-level set against which transformation accuracy may be evaluated.
- `project_glossary` and `data_dictionary`.
- `architecture_model` or other authoritative models relevant to terminology and scope.
- `verification_and_validation_basis`.
- `risk_constraints` including cost, schedule, technical, legal, regulatory, safety, security, or other applicable constraints.
- `prior_findings` from individual statement analysis and related Skills.
- `traceability_evidence`.

Optional:

- `style_guide`.
- `classification_scheme`.
- `interface_definitions`.
- `allocation_data`.
- `stakeholder_expectations`.
- `lifecycle_concepts`.

## Preconditions

Before analysis:

1. The target set and its intended scope must be identified.
2. The analyst must have a canonical GtWR v4 source reference.
3. Individual expressions must retain stable identifiers or evidence references where possible.
4. The evidence boundary must be known: do not assume that an absent artifact is proof that the artifact does not exist.
5. Set-level conclusions must be based on the supplied set and supporting project evidence, not on invented completeness assumptions.

## Procedure

### 1. Preserve the target set

Capture the input set as immutable evidence for the analysis run.

Record:

- set identifier;
- set type;
- entity and abstraction level;
- source or parent set, when supplied;
- membership of individual need/requirement expressions;
- associated attributes and supporting artifacts;
- evidence identifiers.

### 2. Establish the set boundary

Determine what the set is intended to cover and what is explicitly outside scope.

Do not enlarge the set because a category appears to be commonly expected elsewhere. Missing coverage is a finding only when the applicable source, scope, stakeholder evidence, model, or project baseline establishes that the item belongs in the set.

### 3. Load the official characteristic scope

Use the official GtWR v4 cross-reference matrix to distinguish set-level characteristics from individual-statement characteristics.

This Skill assesses:

- C10 Complete
- C11 Consistent
- C12 Feasible
- C13 Comprehensible
- C14 Able to be validated
- C15 Correct

Do not reinterpret C1–C9 as set characteristics. Individual and set characteristic columns remain separate.

### 4. Load the applicable rule relationships

Read rule-to-characteristic relationships from the controlled `matrices.yaml` representation and verify them against the official Summary Sheet page 4 or the corresponding official GtWR matrix.

For this Skill, the rule scope is limited to rules for which the official matrix contains at least one marked C10–C15 cell:

- R3 Appropriate Subject-Verb → C10, C14
- R4 Defined Terms → C11, C13, C14, C15
- R26 Absolutes → C12
- R29 Classification → C10, C11
- R30 Unique Expression → C11
- R33 Range of Values → C11
- R34 Measurable Performance → C12
- R36 Consistent Terms and Units → C11, C13, C14, C15
- R37 Acronyms → C11, C13, C14, C15
- R38 Abbreviations → C11, C13, C14, C15
- R39 Style Guide → C11, C13, C14, C15
- R40 Decimal Format → C11
- R41 Related Needs and Requirements → C10, C11, C13, C15
- R42 Structured Sets → C10, C12, C13, C14, C15

This list is a transcription of the official matrix relationship, not a statement that these rules are generally “set rules”. For example, R3 and R4 also have individual-characteristic cells and are assessed here only for their marked set cells.

Never infer a set relationship merely because a rule sounds relevant.

### 5. Test set completeness and coverage

For C10, inspect whether the supplied set stands alone at its applicable level of abstraction and sufficiently describes the necessary scope supported by authoritative project evidence.

Examine, as applicable:

- capabilities and characteristics;
- functionality and performance;
- drivers and constraints;
- conditions and interactions;
- standards and regulations;
- safety, security, resilience, and quality factors;
- relevant interfaces and externally visible behavior;
- expected scope supported by lifecycle concepts or higher-level sources.

Do not infer missing content solely from a generic checklist. A missing element becomes a supported finding when the project scope, source, model, stakeholder evidence, parent set, or governing constraint establishes that the item belongs in the set.

### 6. Test consistency and uniqueness

For C11:

- detect duplicate or materially repeated expressions;
- identify conflicts between statements;
- identify overlapping obligations that create inconsistent or redundant coverage;
- compare terminology across the set;
- compare units and measurement systems;
- compare use of terms against the project glossary, ontology, architecture model, and data dictionary;
- examine acronym and abbreviation consistency;
- inspect number and decimal formatting when applicable.

R29 addresses classification at set level, R30 addresses unique expression, and R36–R40 address uniformity of terms, units, acronyms, abbreviations, style, and decimal format where their official matrix cells map to C11.

A suspected conflict or duplicate must include evidence references to the affected members. Do not mark a contradiction merely because two expressions appear different; determine whether their scopes, conditions, entities, measures, or states actually overlap.

### 7. Test feasibility at set level

For C12, evaluate the set against explicit entity constraints and risk evidence.

Use available:

- cost constraints;
- schedule constraints;
- technical constraints;
- legal and regulatory constraints;
- safety and security constraints;
- architecture and allocation evidence;
- implementation or technology maturity evidence;
- risk analysis.

The official matrix links C12 to R26, R34 and R42. Apply those relationships only in their stated source meaning.

Do not infer feasibility from wording quality. If feasibility cannot be demonstrated from supplied evidence, return an inconclusive or evidence-missing result rather than a failure asserted as fact.

### 8. Test comprehensibility

For C13, assess whether the set communicates what is expected of the entity and its relationship to the macro system in a way that intended readers can understand without reconstructing essential meaning from unrelated material.

Consider:

- structure and grouping;
- terminology;
- dependency visibility;
- relationship between related requirements;
- supporting diagrams/models where needed;
- level of detail and abstraction;
- classification and organization;
- avoidance of unexplained local vocabulary.

Do not treat formatting preference as a non-conformity unless it conflicts with an explicit project style guide, source rule, or other authoritative project convention.

### 9. Test ability to be validated

For C14, assess whether the set can be validated against its applicable goals, objectives, stakeholder expectations, lifecycle concepts, constraints, and acceptable-risk basis for a need set, or against the applicable needs and higher-level requirements for a requirement set.

Use supplied validation objectives, success criteria, stakeholder evidence, source traceability, models, and validation planning information.

Do not claim that a set is valid merely because every individual statement appears well-written.

### 10. Test correctness of transformation

For C15, determine whether the set accurately represents the supplied lifecycle concepts, sources, needs, or higher-level requirements from which it was transformed.

Required evidence can include:

- parent or source set;
- traceability links;
- transformation rationale;
- approved source material;
- stakeholder agreement;
- architecture/model evidence.

Do not infer correctness from wording alone.

### 11. Analyze structured organization

Apply R41 and R42 using project-defined organization evidence.

Check whether related needs and requirements are grouped in a way supported by their relationships, and whether the set conforms to a defined structure or template where one has been established.

Apply R29 when a classification scheme or relevant organizing dimensions are supplied or established by the project context.

Do not invent a taxonomy and then report absence of that invented taxonomy as an INCOSE non-conformity.

### 12. Analyze cross-statement language consistency

Apply only the set-level matrix cells of R36–R40.

Compare:

- terms;
- units;
- acronyms;
- abbreviations;
- style conventions;
- decimal representation.

Use the project glossary, ontology, data dictionary, and style guide when present.

### 13. Correlate with NRM activities

Where set-level assessment requires underlying analysis, use the official NRM Concepts and Activities → Characteristics matrix as contextual evidence.

Relevant activities may include:

- Managing Sets of Needs and Requirements;
- Analysis from Which Needs and Requirements are Derived;
- Completeness;
- Consistency;
- Identity and Manage Interdependencies;
- Get Stakeholder Agreement;
- Organizing the Integrated Set of Needs;
- Completeness of the Integrated Set of Needs;
- Needs Feasibility and Risk;
- Establish Traceability;
- Organizing Sets of Design Input Requirements;
- Requirements Feasibility and Risk;
- Baseline and Manage Design Input Requirements.

The matrix establishes source relationships to characteristics; it does not prescribe a SPECTRUM scoring model.

### 14. Separate observations from missing evidence

For every assessed characteristic or rule:

- identify supporting evidence;
- identify observed non-conformity, if present;
- identify missing evidence when a reliable conclusion cannot be reached;
- identify source conflict when official source materials disagree.

Do not convert uncertainty into failure.

### 15. Produce findings with traceability

Each finding must identify:

- affected set/member references;
- characteristic or rule;
- observed evidence;
- source or project evidence reference;
- impact on analysis;
- whether remediation is evidence acquisition, clarification, correction, or restructuring.

## Analysis logic

The GtWR v4 Summary Sheet states that set characteristics result from both the writing rules and the activities associated with the Needs and Requirements Manual / Guide to Needs and Requirements, and that underlying analysis is as important as the wording of the need or requirement. Therefore this Skill is not limited to lexical inspection of the set.

Set-level reasoning must follow this sequence:

`set boundary → source/context evidence → official rule/characteristic relationship → cross-member analysis → finding/evidence status`

The absence of evidence is not itself proof of non-conformity unless the applicable process or project baseline requires that evidence to exist.

## Decision semantics

Use only these Skill-level result semantics:

- `conformant_observed`: the available evidence supports conformity for the assessed scope.
- `non_conformant_observed`: the available evidence shows an observed violation or contradiction for the assessed scope.
- `inconclusive_missing_context`: the evidence is insufficient to determine the result.
- `inconclusive_source_conflict`: relevant source evidence conflicts and the conflict prevents a reliable conclusion.
- `not_applicable`: the characteristic/rule does not apply to the supplied set scope based on explicit scope evidence.

These statuses are SPECTRUM analytical statuses, not INCOSE conformance certifications.

## Findings

Use findings that are specific and evidence-backed, such as:

- `set_incomplete_observed`
- `set_conflict_observed`
- `duplicate_requirement_observed`
- `overlap_observed`
- `terminology_inconsistency_observed`
- `unit_inconsistency_observed`
- `acronym_inconsistency_observed`
- `abbreviation_issue_observed`
- `decimal_format_inconsistency_observed`
- `classification_missing_or_unsupported`
- `related_requirements_grouping_issue`
- `structured_set_conformance_issue`
- `feasibility_evidence_missing`
- `validation_basis_missing`
- `source_alignment_not_established`
- `set_comprehension_blocked_by_missing_context`
- `missing_scope_evidence`
- `analysis_blocked_by_missing_context`

A finding must never imply a business fact that is not present in the evidence.

## Evidence

Evidence must preserve:

- the exact set membership used for the assessment;
- affected requirement/need identifiers;
- exact relevant passages or structural relationships;
- the official INCOSE rule or characteristic reference;
- project evidence references used to establish scope or correctness;
- glossary/model/data-dictionary evidence where terminology is assessed;
- parent/source traceability evidence when correctness is assessed;
- feasibility and risk evidence when C12 is assessed;
- validation evidence when C14 is assessed.

When official source materials contain a discrepancy, preserve the discrepancy rather than silently replacing one source expression with another.

## Handoff

This Skill can hand findings to:

- `requirement-statement-quality` for member-level wording analysis;
- `requirement-relationship-traceability` for relationship and transformation evidence;
- `verification-analysis` for verification-oriented evidence gaps;
- `validation-analysis` for validation-oriented evidence gaps;
- `elicitation-gap` when missing stakeholder/source context blocks analysis;
- future set-structure or requirements-management Skills.

Handoff must preserve evidence references and must not change a finding's interpretation level.

## Output

Produce a `requirement_set_quality_observation` containing:

- `set_ref`;
- `set_type`;
- `status`;
- `characteristics_assessed`;
- `applicable_rules`;
- `member_comparisons`;
- `characteristic_observations`;
- `findings`;
- `missing_context`;
- `evidence_refs`;
- `source_refs`;
- `unassessed_scope`.

Do not output a global implementation readiness decision from this Skill.

## Exit conditions

`completed` when all applicable set-level checks were assessed with sufficient evidence for the declared scope.

`completed_with_findings` when analysis is complete and one or more evidence-backed non-conformities or structural issues were observed.

`completed_with_gaps` when analysis is useful but one or more conclusions remain inconclusive because context or evidence is missing.

`blocked_on_missing_context` when the set boundary, source basis, or other essential evidence cannot be established.

`not_applicable` when the supplied target is not a set of needs or requirements or the declared set-level scope is explicitly inapplicable.

## Non-goals

This Skill does not:

- invent missing requirements, stakeholder needs, business values, constraints, or priorities;
- define an INCOSE rule not present in the official source;
- create a synthetic C16 or another new INCOSE characteristic;
- infer set feasibility, necessity, or correctness solely from wording;
- replace project-specific requirements engineering activities;
- approve or reject implementation readiness;
- issue a formal INCOSE certification or compliance claim;
- silently rewrite or normalize official source discrepancies;
- treat a missing artifact as proof of non-conformity without an applicable evidence basis;
- replace the source corpus with secondary summaries.

## Référence

Critères d'évaluation et sources détaillées : `REFERENCE.md` dans ce dossier (non chargé à l'exécution).
