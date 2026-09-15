---
name: verification-analysis
description: Analyser la base de vérification d'un besoin ou d'une exigence et déterminer si des preuves objectives permettent d'établir une vérification exploitable.
type: component
role: verification
---

# Verification Analysis

## Purpose

Déterminer si un besoin ou une exigence dispose d'une base de vérification objectivement exploitable et si les preuves disponibles soutiennent réellement la vérification visée.

This is a SPECTRUM analytical capability derived from the official INCOSE Guide to Writing Requirements v4 (GtWR v4) and its associated NRM verification relationships. INCOSE does not define a Skill with this name or this status vocabulary.

The Skill is concerned with the verification basis and evidence. It does not replace requirement expression analysis, validation analysis, test execution, or implementation approval.

## Source boundary

Authoritative source boundary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, especially pages 2–6.
- Official GtWR v4 characteristics and writing-rule definitions.
- Official NRM Concepts and Activities → Characteristics cross-reference matrix.

Local controlled representations:

- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/rules.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`

The official INCOSE publication remains authoritative.

## Interpretation boundary

Keep these levels distinct:

- `source_fact`: information explicitly represented in the INCOSE source.
- `spectrum_observation`: an observation produced from source facts and supplied project evidence.
- `business_gap`: a missing project fact, verification basis, artifact, result, or decision.

A verification status, evidence-quality criterion, coverage criterion, or finding created by SPECTRUM is not an INCOSE rule unless the source explicitly defines it.

## When to use

Use this Skill when an identified need or requirement must be assessed for verifiability or when a verification method, criterion, test, inspection, analysis, demonstration, measurement, record, or other objective evidence is expected.

Use it after context and statement analysis when the analyst needs to establish whether the verification claim is objectively testable and whether available evidence supports it.

Use it for both individual requirements and set-level verification evidence when the target scope is explicit.

Do not use it as a substitute for validation. Verification asks whether the requirement can be checked against objective evidence; validation concerns whether the need, requirement, or set is appropriate to its intended purpose and stakeholders.

## Inputs

Required:

- `requirement_or_need` or `requirement_set`;
- `verification_evidence`.

Recommended:

- `verification_method`;
- `verification_criteria`;
- `acceptance_or_success_criteria`;
- `test_or_analysis_procedure`;
- `test_results`;
- `inspection_records`;
- `demonstration_records`;
- `measurement_data`;
- `simulation_or_analysis_results`;
- `requirement_context`;
- `source_or_parent_reference`;
- `traceability_evidence`;
- `baseline_or_version_reference`;
- `prior_findings`.

Optional:

- `architecture_model`;
- `interface_definitions`;
- `risk_constraints`;
- `configuration_data`;
- `tool_outputs`.

## Preconditions

1. The verification target is identifiable.
2. The requirement or need under verification is preserved as evidence.
3. The applicable scope and evidence boundary are known.
4. The analyst can distinguish a planned verification method from an executed verification result.
5. A claimed verification result is linked to an identifiable artifact or record when such a result is asserted.

## Procedure

### 1. Preserve the target

Capture the exact requirement or need expression, including its stable identifier and relevant version/baseline information.

If the target is a set, preserve the exact set membership used for the verification assessment.

### 2. Identify the verification target

Determine exactly what property, behavior, performance, condition, interface behavior, or constraint is intended to be verified.

A target must be observable enough to support an objective verification activity. Do not invent a measurable property that the requirement does not establish.

### 3. Identify the verification basis

Determine whether the supplied project evidence establishes a verification method or basis, such as:

- test;
- inspection;
- analysis;
- demonstration;
- measurement;
- review of objective records;
- another explicitly defined project verification method.

The method vocabulary above is a SPECTRUM organizational representation. It is not a new INCOSE rule.

### 4. Identify objective criteria

Determine what result, condition, threshold, range, state, observation, or other criterion would establish that the verification target has been met.

When criteria are absent, distinguish:

- criterion truly absent from the requirement/context;
- criterion exists elsewhere but was not supplied;
- criterion applicability unresolved.

Do not manufacture a threshold, tolerance, test value, or acceptance limit.

### 5. Check linkage between target, method, and evidence

For each verification claim, verify the chain:

`requirement/need → verification target → method/basis → criterion → evidence/result`

Check that:

- the evidence concerns the correct target;
- the evidence was generated under the relevant configuration/baseline where such information exists;
- the evidence is attributable to the requirement or need being assessed;
- the evidence is objective rather than a bare assertion;
- the evidence covers the relevant conditions and scope.

### 6. Assess verifiability at individual level

Use the official individual characteristic `C7 Verifiable` as the primary source-backed characteristic for individual verification assessment.

A statement may be well written and still lack an objectively usable verification basis. Conversely, a verification record does not repair a requirement whose target remains undefined.

Use the official writing-rule relationships and prior statement analysis when they materially affect the ability to verify, but do not duplicate member-level wording analysis already performed by `requirement-statement-quality`.

### 7. Assess set-level verification evidence

When the target is a set, keep verification distinct from the set-level characteristic `C14 Able to be validated`.

C14 is not reinterpreted as a generic verification characteristic. When a source-backed NRM activity links verification and validation work to C14, preserve that source relationship and hand validation-specific questions to `validation-analysis`.

### 8. Correlate with official NRM verification activities

Use the official NRM matrix for activities including:

- `3.2.1.7 System Verification and System Validation`;
- `5.1.2 Perform Needs Verification`;
- `6.2.5 Plan for System Verification`;
- `7.1.2 Perform Design Input Requirements Verification`;
- `8.4 Design Verification`;
- `14.2.9 Managing System Verification and System Validation`.

The official matrix establishes activity-to-characteristic relationships. It does not define a SPECTRUM scoring algorithm, evidence threshold, or pass/fail formula.

### 9. Distinguish verification plan from verification result

A planned verification method is not evidence that verification succeeded.

A test procedure is not a test result.

A statement such as “tested successfully” is not sufficient evidence without an attributable result artifact when the result is being asserted.

### 10. Assess coverage

Determine whether the available evidence covers:

- all relevant clauses or obligations;
- applicable conditions and modes;
- required performance or ranges;
- relevant interfaces;
- the correct product/system configuration;
- the declared verification scope.

Report partial coverage explicitly rather than collapsing it into success.

### 11. Detect evidence mismatch

Identify cases where:

- the evidence concerns another requirement;
- the measurement does not correspond to the required property;
- the baseline/configuration is incompatible;
- the evidence is too weak to support the claim;
- the result cannot be attributed to the target.

### 12. Produce evidence-backed findings

Each finding must identify:

- the exact requirement/need or set reference;
- verification target;
- method/basis;
- criterion;
- evidence/result reference;
- coverage status;
- relevant INCOSE characteristic/activity reference;
- downstream impact.

## Source-backed scope

The GtWR v4 Summary Sheet defines `C7 Verifiable` as an individual need/requirement characteristic and distinguishes set-level `C14 Able to be validated`. The official Concepts and Activities → Characteristics matrix identifies verification-related activities and their characteristic relationships.

The official NRM matrix includes `5.1.2 Perform Needs Verification`, `6.2.5 Plan for System Verification`, `7.1.2 Perform Design Input Requirements Verification`, `8.4 Design Verification`, and `14.2.9 Managing System Verification and System Validation`. These source relationships constrain the Skill but do not define a SPECTRUM evidence score or automatic pass/fail threshold.

## Analysis logic

Use this sequence:

`target → observable verification basis → criterion → method/evidence linkage → coverage → evidence status`

The primary question is whether the verification claim is objectively supportable from the declared evidence boundary.

Do not infer verification success from requirement wording alone. Do not infer verification failure merely because an artifact was not supplied unless the evidence boundary or applicable project process establishes that the artifact should be present.

## Decision semantics

Use only these Skill-level result semantics:

- `verification_basis_established`: target, basis, and applicable objective evidence are sufficiently established for the declared scope.
- `verification_basis_partial`: some verification coverage exists but one or more relevant portions remain unsupported.
- `verification_basis_missing`: an essential verification basis or criterion is not established.
- `verification_evidence_mismatch`: evidence exists but does not reliably correspond to the verification target.
- `verification_context_missing`: the target, scope, or applicable verification context cannot be established reliably.
- `not_applicable`: verification is explicitly outside the declared scope.

These are SPECTRUM statuses, not INCOSE certification statuses.

## Findings

Use evidence-backed findings such as:

- `verification_target_not_observable`
- `verification_method_missing`
- `verification_criterion_missing`
- `verification_evidence_missing`
- `verification_evidence_insufficient`
- `verification_evidence_mismatch`
- `verification_partial_coverage`
- `verification_baseline_mismatch`
- `verification_result_unattributed`
- `verification_plan_without_result`
- `verification_scope_missing`
- `verification_context_missing`

A finding must never invent a test result, measurement, threshold, or business acceptance criterion.

## Evidence

Preserve:

- exact target expression/set;
- verification target description as supplied or directly derived from the target;
- verification method/basis;
- objective criterion;
- test/procedure/inspection/analysis/demonstration record;
- result artifact and baseline/configuration when supplied;
- source-backed characteristic/activity references;
- precise project evidence references.

## Handoff

Results can feed:

- `requirement-statement-quality` for wording defects that obstruct verification;
- `requirements-context` for missing conditions, levels, constraints, or source context;
- `requirement-relationship-traceability` for requirement-to-verification or source relationships where explicitly modeled;
- `validation-analysis` for validation-specific analysis;
- `elicitation-gap` for missing information required to establish a verification basis.

Handoff preserves evidence references and interpretation level.

## Output

Produce a `verification_observation` containing:

- `requirement_ref` or `set_ref`;
- `verification_target`;
- `verification_method_or_basis`;
- `verification_criteria`;
- `evidence_refs`;
- `coverage`;
- `context_status`;
- `status`;
- `characteristics_assessed`;
- `source_activity_refs`;
- `findings`;
- `missing_evidence`;
- `downstream_impacts`.

Do not output a global implementation-readiness decision.

## Exit conditions

`completed` when the declared verification scope is sufficiently established and assessed.

`completed_with_gaps` when useful verification analysis is possible but one or more evidence elements remain unavailable.

`blocked_on_missing_context` when the verification target, scope, or essential context cannot be established.

`not_applicable` when verification is explicitly outside the declared scope.

## Non-goals

This Skill does not:

- invent thresholds, tests, measurements, acceptance criteria, or results;
- confuse a verification plan with a verification result;
- infer verification success from wording quality alone;
- replace validation analysis;
- replace project verification execution or test management;
- create new INCOSE rules or characteristics;
- issue formal INCOSE certification;
- approve or reject implementation readiness;
- silently resolve conflicting evidence.

## References

Primary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, June 2023.

Local controlled representations:

- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

Official source URLs:

- `https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf`
- `https://www.incose.org/docs/default-source/working-groups/requirements-wg/gtwr/incose_rwg_gtwr_v4_040423_final_drafts.pdf`

## Evaluation

Minimum evaluation cases:

- verifiable_requirement_with_objective_evidence;
- verification_basis_missing;
- criterion_missing;
- verification_plan_without_result;
- evidence_mismatch;
- baseline_mismatch;
- partial_coverage;
- unobservable_target;
- set_level_verification_scope;
- missing_verification_context;
- no_false_positive_from_missing_artifact;
- wording_defect_handed_to_statement_quality.
