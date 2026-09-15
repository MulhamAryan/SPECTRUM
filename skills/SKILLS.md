# SPECTRUM Skills — Step 2.5

## Purpose

This catalogue defines the first Skill architecture derived from the validated ISO/IEC/IEEE 29148:2018 controls in `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`.

The Skills are SPECTRUM implementation constructs. They are not ISO vocabulary.

## Skill families

| ID | Skill | Type | Primary role | ISO control refs |
|---|---|---|---|---|
| SP-SK-001 | Context Establishment | component | contextualization | R001, R002, R007, R012, R013, R014, R015, R016 |
| SP-SK-002 | Requirement Identification | component | requirement analysis | R001, R002, R015 |
| SP-SK-003 | Requirement Expression Analysis | component | quality analysis | R003 |
| SP-SK-004 | Requirement Relationship & Traceability Analysis | component | relationship / traceability | R004, R005, R006 |
| SP-SK-005 | Verification Readiness Analysis | component | verification / validation | R009 |
| SP-SK-006 | Validation Readiness Analysis | component | verification / validation | R008 |
| SP-SK-007 | Requirements Engineering Coverage Analysis | workflow | decision preparation | R010, R011 |
| SP-SK-008 | Conformance Claim Review | component | governance | R017 |

## Why these boundaries exist

The boundaries are based on analytical responsibility, not one-rule-per-Skill mechanics. A Skill can implement several controls when those controls require the same context and produce a coherent result.

For example, contextualization groups the controls needed to establish whether a ticket is sufficiently grounded before downstream analysis. Traceability groups controls concerning upward/downward relationships and traceability artifacts. Verification and validation remain separate because their purposes and evidence are different in the source model.

## Lifecycle / phase mapping

```text
CONTEXTUALIZATION
    SP-SK-001
        ↓
REQUIREMENT ANALYSIS
    SP-SK-002
        ↓
QUALITY ANALYSIS
    SP-SK-003
        ↓
RELATIONSHIP / TRACEABILITY
    SP-SK-004
        ↓
VERIFICATION + VALIDATION
    SP-SK-005 ─── SP-SK-006
        ↓
DECISION PREPARATION
    SP-SK-007

CROSS-CUTTING GOVERNANCE
    SP-SK-008
```

This is an applicability model, not a mandatory linear sequence. A Workflow selects the Skills relevant to the ticket and the available evidence.

## Composition

```text
SP-SK-001 Context Establishment
   ├── feeds → SP-SK-002 Requirement Identification
   ├── feeds → SP-SK-004 Traceability Analysis
   └── feeds → SP-SK-007 Coverage Analysis

SP-SK-002 Requirement Identification
   ├── feeds → SP-SK-003 Expression Analysis
   ├── feeds → SP-SK-004 Traceability Analysis
   └── feeds → SP-SK-005 Verification Readiness

SP-SK-003 Expression Analysis
   └── feeds → SP-SK-005 Verification Readiness

SP-SK-004 Traceability Analysis
   └── feeds → SP-SK-007 Coverage Analysis

SP-SK-005 Verification Readiness
   └── feeds → SP-SK-007 Coverage Analysis

SP-SK-006 Validation Readiness
   └── feeds → SP-SK-007 Coverage Analysis

SP-SK-008 Conformance Claim Review
   └── governance check on claims produced anywhere in the system
```

## Catalogue rule

No concrete Skill should be added to this catalogue without:

1. at least one `rule_ref`;
2. a bounded responsibility;
3. explicit inputs and outputs;
4. an evidence model;
5. observable exit conditions;
6. evaluation cases.
