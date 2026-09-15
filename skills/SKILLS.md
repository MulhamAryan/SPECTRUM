# SPECTRUM Skills — Step 2.5

## Purpose

This file is the human-readable catalogue for the canonical Skill definitions in `skills/sources/iso-iec-ieee-29148-2018/skills.yaml`.

The Skills are SPECTRUM implementation constructs. They are not ISO vocabulary and this file is not a second source of normative rules.

## Canonical source

The machine-readable Skill definitions and workflow are canonical. This catalogue is a readable index and must remain consistent with them.

## Skill families

| ID | Skill | Type | Primary role | ISO control refs |
|---|---|---|---|---|
| SPECTRUM-SK-REQ-CONTEXT | Requirement Context | component | requirement analysis | R001, R002, R013, R015 |
| SPECTRUM-SK-ELICITATION-GAP | Elicitation Gap | component | contextualization | R007 |
| SPECTRUM-SK-STK-SCENARIO | Stakeholder & Scenario Context | component | contextualization | R012, R014 |
| SPECTRUM-SK-REQUIREMENT-EXPRESSION | Requirement Expression Analysis | component | quality analysis | R003 |
| SPECTRUM-SK-RELATIONSHIP-TRACEABILITY | Requirement Relationship & Traceability | component | relationship / traceability | R004, R005, R006 |
| SPECTRUM-SK-VERIFICATION | Verification Analysis | component | verification | R009 |
| SPECTRUM-SK-VALIDATION | Validation Analysis | component | validation | R008 |
| SPECTRUM-SK-RE-COVERAGE | Requirements Engineering Coverage | component | cross-cutting | R010, R011 |
| SPECTRUM-SK-MULTI-SOURCE | Multi-Source Context | component | cross-cutting | R016 |
| SPECTRUM-SK-CONFORMANCE | Conformance Governance | component | governance | R017 |
| SPECTRUM-WF-ISO29148-READINESS | ISO 29148 Ticket Readiness Analysis | workflow | orchestration | — |

## Lifecycle / applicability model

```text
CONTEXTUALIZATION
    SPECTRUM-SK-MULTI-SOURCE
            ↓
    SPECTRUM-SK-REQ-CONTEXT
            ↓
    ┌───────────────┬────────────────────────┐
    ↓               ↓                        ↓
ELICITATION   STAKEHOLDER /           REQUIREMENT
GAP            SCENARIO                EXPRESSION
    │               │                        │
    └───────────────┴──────────────┬─────────┘
                                   ↓
                 RELATIONSHIP / TRACEABILITY
                                   ↓
                     VERIFICATION / VALIDATION
                                   ↓
                  RE ENGINEERING COVERAGE

CONFORMANCE GOVERNANCE
    cross-cutting validation of conformance claims

ISO 29148 READINESS WORKFLOW
    selects and orchestrates the applicable Skills above
```

This is an applicability model, not a mandatory linear sequence. The Workflow selects the Skills relevant to the ticket and the available evidence.

## Composition

```text
MULTI-SOURCE CONTEXT
   └── feeds → REQUIREMENT CONTEXT

REQUIREMENT CONTEXT
   ├── feeds → ELICITATION GAP
   ├── feeds → REQUIREMENT EXPRESSION
   ├── feeds → RELATIONSHIP & TRACEABILITY
   ├── feeds → VERIFICATION
   └── feeds → VALIDATION

STAKEHOLDER & SCENARIO CONTEXT
   └── feeds → VALIDATION

REQUIREMENT EXPRESSION
   └── feeds → VERIFICATION

RELATIONSHIP & TRACEABILITY
   ├── feeds → VERIFICATION
   └── feeds → VALIDATION

ELICITATION GAP ───────────────┐
STAKEHOLDER & SCENARIO ────────┤
REQUIREMENT EXPRESSION ────────┤
RELATIONSHIP & TRACEABILITY ───┤
VERIFICATION ──────────────────┤
VALIDATION ────────────────────┤
RE COVERAGE ───────────────────┤
                               ↓
                    ISO 29148 READINESS WORKFLOW

CONFORMANCE GOVERNANCE
   └── validates → ISO 29148 READINESS WORKFLOW
```

## Catalogue rule

No concrete Skill should be added without:

1. at least one `rule_ref`;
2. a bounded responsibility;
3. explicit inputs and outputs;
4. an evidence model;
5. observable exit conditions;
6. evaluation cases;
7. explicit relationships or an explicit declaration that it has none.
