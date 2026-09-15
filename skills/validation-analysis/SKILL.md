---
name: validation-analysis
description: Analyser la base permettant d'établir qu'un ensemble de besoins ou d'exigences peut être validé par rapport à l'utilisation prévue, aux objectifs et aux attentes applicables.
type: component
role: validation
---

# Validation Analysis

## Purpose

Déterminer si la base de validation disponible permet d'établir qu'un ensemble de besoins ou d'exigences peut être validé par rapport à l'utilisation prévue, aux objectifs, aux attentes et au contexte de référence applicables.

This is a SPECTRUM analytical capability derived from the official INCOSE Guide to Writing Requirements v4 (GtWR v4) and its associated NRM validation relationships. INCOSE does not define a Skill with this name or this status vocabulary.

The Skill is concerned with set-level validation basis, intended use, stakeholder expectations, lifecycle concepts, needs, higher-level requirements, and validation evidence. Individual wording/context defects remain the responsibility of the Skills whose source-backed scopes cover the relevant characteristics.

## Source boundary

Authoritative source boundary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, especially pages 2–6.
- Official GtWR v4 characteristics and writing-rule definitions.
- Official NRM Concepts and Activities → Characteristics cross-reference matrix.
- INCOSE Guide to Verification and Validation, `INCOSE-TP-2021-004-01`, may be used as supporting guidance when explicitly selected; it does not replace the GtWR/NRM source boundary for the mapping in this Skill.

Local controlled representations:

- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`

The official INCOSE publications remain authoritative.

## Interpretation boundary

Keep these levels distinct:

- `source_fact`: information explicitly represented in the official INCOSE source.
- `spectrum_observation`: an observation produced from source facts and supplied project evidence.
- `business_gap`: a missing project fact, objective, stakeholder expectation, scenario, validation basis, or evidence item.

A validation status, coverage criterion, evidence-quality rule, or recommendation created by SPECTRUM is not an INCOSE rule unless the official source explicitly defines it.

## When to use

Use this Skill when the target is a need set or requirement set and the question is whether the set can be validated against its applicable intended use, objectives, expectations, lifecycle concepts, or higher-level references.

Use it when validation depends on:

- intended use;
- stakeholder expectations or needs;
- lifecycle concepts;
- objectives or goals;
- higher-level needs or requirements;
- approved operational scenarios or conditions of use;
- validation objectives and criteria;
- acceptable-risk or feasibility context where relevant to the validation basis.

Do not use it to invent stakeholder objectives or declare a validation result without supporting evidence.

## Inputs

Required:

- `requirement_set` or another explicitly declared set-level validation target;
- `validation_evidence` or `validation_context`.

Recommended:

- `set_type`: `need_set` or `requirement_set`;
- `intended_use`;
- `system_context`;
- `stakeholder_expectations`;
- `stakeholder_evidence`;
- `lifecycle_concepts`;
- `source_or_parent_reference`;
- `higher_level_needs_or_requirements`;
- `validation_objectives`;
- `validation_criteria`;
- `scenarios_or_operational_concepts`;
- `risk_and_constraint_context`;
- `traceability_evidence`;
- `prior_findings`.

Optional:

- `architecture_model`;
- `interface_definitions`;
- `verification_evidence`;
- `baseline_or_version_reference`.

## Preconditions

1. The validation target is an identifiable set of needs or requirements.
2. The intended system, use, level, or declared validation scope is known or explicitly identified as missing.
3. The validation evidence boundary is known.
4. Stakeholder/source evidence is preserved when it is used to support the validation claim.
5. Validation conclusions are not inferred solely from requirement wording or verification results.

## Procedure

### 1. Preserve the target set

Capture the exact need set or requirement set used for the validation assessment, including stable identifiers and relevant baseline information.

### 2. Identify the validation subject and scope

Determine whether the target is a need set or requirement set and establish the system, system level, lifecycle context, intended use, and declared scope against which validation is being assessed.

### 3. Establish the intended use and objectives

Identify authoritative evidence for:

- intended use;
- operational goals;
- stakeholder objectives;
- lifecycle concepts;
- business or mission objectives when explicitly supplied;
- applicable scenarios or conditions of use.

Do not invent an objective because a requirement appears to imply one.

### 4. Establish the validation reference

Determine what the set is being validated against.

Depending on scope, this may include:

- stakeholder needs or expectations;
- lifecycle concepts;
- system objectives;
- higher-level needs or requirements;
- approved operational scenarios;
- explicit validation criteria.

Preserve reference-to-target relationships where they exist.

### 5. Assess validation criteria

Determine whether the validation basis identifies objective or agreed criteria sufficient to establish the intended-use relationship.

Distinguish:

- criteria absent from the source/context;
- criteria available but not supplied;
- criteria conflicting across authoritative sources;
- criteria not applicable to the declared target.

Do not manufacture acceptance criteria, stakeholder goals, or operational outcomes.

### 6. Assess C14 set-level ability to be validated

Assess `C14 Able to be validated` only at set level.

Evaluate whether the set has an established validation basis through applicable goals, stakeholder expectations, lifecycle concepts, higher-level references, conditions of use, validation objectives, validation criteria, and supporting evidence.

Do not treat C14 as an individual-statement characteristic. Individual validation-related C3, C6, and C8 relationships in the official NRM matrix are outside this Skill's characteristic scope and must not be silently reassigned to C14.

### 7. Correlate with official NRM validation activities

Use the official NRM matrix for activities including:

- `3.2.1.7 System Verification and System Validation`;
- `5.2 Needs Validation`;
- `5.2.2 Perform Needs Validation`;
- `7.2 Design Input Requirements Validation`;
- `7.2.2 Perform Design Input Requirements Validation`;
- `8.5 Design Validation`;
- `14.2.9 Managing System Verification and System Validation`.

The official matrix establishes activity-to-characteristic relationships. It does not define a SPECTRUM validation score or automatic pass/fail formula.

### 8. Separate validation from verification

Do not treat a successful verification result as proof that the set is the right one for intended use.

Do not treat stakeholder agreement as proof that every technical clause is verified.

Validation concerns the relationship to intended use, needs, objectives, and applicable expectations; verification concerns meeting specified requirements.

### 9. Assess coverage

Determine whether the available validation evidence covers the declared set-level validation scope, including where applicable:

- intended uses;
- relevant stakeholder expectations;
- operational scenarios;
- lifecycle concepts;
- higher-level needs or requirements;
- relevant conditions and constraints;
- applicable risk considerations.

Report partial coverage explicitly.

### 10. Detect contradiction or mismatch

Identify cases where:

- the set conflicts with an established stakeholder need or objective;
- the set addresses a different intended use than the declared system purpose;
- the validation evidence refers to the wrong level or system context;
- authoritative sources provide incompatible validation objectives;
- the validation claim exceeds the evidence scope.

### 11. Produce evidence-backed findings

Each finding must identify:

- exact set reference;
- validation reference/objective;
- criteria;
- evidence used;
- coverage;
- relevant INCOSE characteristic/activity reference;
- downstream impact.

## Source-backed scope

The official GtWR v4 Summary Sheet identifies C1–C9 as individual need/requirement characteristics and C10–C15 as set characteristics. This Skill is intentionally scoped to `C14 Able to be validated`, which is a set-level characteristic.

The official NRM matrix associates several validation activities with additional individual and set characteristics. Those source relationships remain in the knowledge corpus, but this Skill does not collapse them into a generic individual validation capability and does not reclassify C14 as individual.

The INCOSE Guide to Verification and Validation is an official supporting guide in the Requirements Working Group product family and may support interpretation when explicitly selected. It does not replace the source relationships recorded from the GtWR/NRM corpus.

## Analysis logic

Use this sequence:

`validation set → intended use/objective → validation reference → criteria → evidence linkage → coverage → C14 status`

The primary question is whether the available evidence supports the set's ability to be validated against the applicable intended use and expectations.

Do not infer validation capability from wording quality, requirement presence, or verification success alone.

## Decision semantics

Use only these Skill-level result semantics:

- `validation_basis_established`: the validation reference, criteria, and supporting evidence are sufficiently established for the declared set-level scope.
- `validation_basis_partial`: the validation basis is materially established but one or more relevant parts remain unsupported.
- `validation_basis_missing`: an essential validation reference, objective, criterion, or evidence basis is not established.
- `validation_evidence_mismatch`: evidence exists but does not correspond reliably to the validation set or intended-use context.
- `validation_contradicted`: authoritative evidence shows an incompatibility between the set and the applicable intended use/objectives/reference.
- `validation_context_missing`: intended use, system context, scope, or other essential validation context cannot be established.
- `not_applicable`: validation is explicitly outside the declared set-level scope.

These are SPECTRUM statuses, not INCOSE certification statuses.

## Findings

Use evidence-backed findings such as:

- `validation_reference_missing`
- `validation_objective_missing`
- `validation_criterion_missing`
- `stakeholder_validation_basis_missing`
- `intended_use_missing`
- `operational_context_missing`
- `validation_evidence_missing`
- `validation_evidence_insufficient`
- `validation_evidence_mismatch`
- `validation_partial_coverage`
- `validation_contradiction`
- `validation_level_mismatch`
- `validation_scope_missing`
- `validation_context_conflict`

A finding must never invent a stakeholder objective, operational outcome, or validation result.

## Evidence

Preserve:

- exact need/requirement set;
- intended-use evidence;
- stakeholder expectations and source evidence;
- lifecycle concepts;
- higher-level needs or requirements;
- validation objectives and criteria;
- scenarios/operational concepts;
- validation records/results when supplied;
- baseline/configuration where relevant;
- official INCOSE characteristic/activity references;
- precise project evidence references.

## Handoff

Results can feed:

- `requirement-set-quality` for set-level completeness, consistency, comprehensibility, feasibility, and correctness questions;
- `requirements-context` for missing intended-use, level, source, condition, or stakeholder context;
- `requirement-relationship-traceability` for source/parent/higher-level relationships;
- `verification-analysis` when the question is actually about meeting specified requirements;
- `elicitation-gap` for missing stakeholder/source information required to establish validation;
- `requirement-statement-quality` only when set analysis reveals a member-level wording defect that obstructs interpretation.

Handoff preserves evidence references and interpretation level.

## Output

Produce a `validation_observation` containing:

- `set_ref`;
- `validation_subject`;
- `intended_use`;
- `validation_reference`;
- `validation_objectives`;
- `validation_criteria`;
- `evidence_refs`;
- `coverage`;
- `status`;
- `characteristics_assessed` (must include only C14 for this Skill);
- `source_activity_refs`;
- `findings`;
- `missing_context`;
- `downstream_impacts`.

Do not output a global implementation-readiness decision.

## Exit conditions

`completed` when the declared set-level validation scope, reference, criteria, and evidence are sufficiently established and assessed.

`completed_with_gaps` when useful validation analysis is possible but one or more evidence elements remain unavailable.

`blocked_on_missing_context` when intended use, validation scope, or essential context cannot be established.

`not_applicable` when validation is explicitly outside the declared scope.

## Non-goals

This Skill does not:

- invent stakeholder objectives, needs, usage scenarios, acceptance criteria, or validation results;
- confuse validation with verification;
- infer validation capability from requirement wording alone;
- treat a verification result as validation evidence by default;
- replace stakeholder elicitation or validation execution;
- create new INCOSE rules or characteristics;
- issue formal INCOSE certification;
- approve or reject implementation readiness;
- silently resolve conflicting authoritative evidence;
- evaluate C14 on an individual statement.

## References

Primary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, June 2023.

Supporting official guide:

- INCOSE Guide to Verification and Validation, `INCOSE-TP-2021-004-01`, May 2022.

Local controlled representations:

- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

Official source URLs:

- `https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf`
- `https://www.incose.org/docs/default-source/working-groups/requirements-wg/gtwr/incose_rwg_gtwr_v4_040423_final_drafts.pdf`
- `https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=GUIDEVERIF`

## Evaluation

Minimum evaluation cases:

- validatable_need_set_with_authoritative_validation_basis;
- validatable_requirement_set_with_authoritative_validation_basis;
- missing_intended_use;
- missing_stakeholder_expectations;
- missing_validation_objective;
- missing_validation_criteria;
- validation_evidence_mismatch;
- validation_level_mismatch;
- contradictory_authoritative_validation_sources;
- partial_validation_coverage;
- verification_success_but_C14_unestablished;
- no_false_positive_from_missing_artifact;
- individual_target_not_misclassified_as_C14;
