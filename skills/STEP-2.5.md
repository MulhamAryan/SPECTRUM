# Step 2.5 — ISO Controls to SPECTRUM Skills

## Objective

Transform the validated controls from Step 2.4 into executable, composable SPECTRUM capabilities without changing the meaning of the underlying controls.

## Source chain

```text
knowledge/sources/iso-iec-ieee-29148-2018/knowledge.yaml
        ↓
rules/sources/iso-iec-ieee-29148-2018/rules.yaml
        ↓
skills/SKILL_CONTRACT.md
        ↓
skills/SKILLS.md
```

## Control coverage matrix

| Control | Skill | Reason |
|---|---|---|
| R001 | SP-SK-001, SP-SK-002 | Context establishes the item of interest; identification analyses the requirement against it |
| R002 | SP-SK-001, SP-SK-002 | Context distinguishes need/constraint/condition; identification preserves those distinctions |
| R003 | SP-SK-003 | Direct expression-quality responsibility |
| R004 | SP-SK-004 | Derived requirement relationship |
| R005 | SP-SK-004 | Upward/downward traceability |
| R006 | SP-SK-004 | Traceability-matrix artifact when applicable |
| R007 | SP-SK-001 | Context gap / elicitation gap detection |
| R008 | SP-SK-006 | Validation basis and evidence |
| R009 | SP-SK-005 | Verification basis and evidence |
| R010 | SP-SK-007 | Coverage of RE activities relevant to the analysis |
| R011 | SP-SK-007 | Requirements-management context when applicable |
| R012 | SP-SK-001 | Operational scenario context when relevant |
| R013 | SP-SK-001 | Condition / constraint / state context |
| R014 | SP-SK-001 | Stakeholder context |
| R015 | SP-SK-001, SP-SK-002 | Requirement level must be established and respected |
| R016 | SP-SK-001 | Multi-source context establishment |
| R017 | SP-SK-008 | Governance of any formal conformance claim |

## Coverage rule

All 17 controls are assigned to at least one Skill. Shared assignment is intentional where a control is needed both to establish context and to perform the downstream analytical responsibility.

## Important boundary

These Skills do not create a new requirements-engineering standard. They operationalize the existing SPECTRUM derived controls. Detailed quality criteria from other references, such as INCOSE, remain separate until their own validated rule set is introduced.

## Execution model

```text
1. Establish context from authorized sources.
2. Identify and classify requirements and their level.
3. Analyse requirement expression.
4. Analyse relationships and traceability.
5. Analyse verification basis.
6. Analyse validation basis.
7. Assess broader RE / management coverage where applicable.
8. Review conformance claims separately under governance control.
9. Aggregate findings and evidence into decision inputs.
```

The order above describes the default analytical dependency. A workflow may omit non-applicable Skills or execute independent Skills in parallel when their prerequisites are satisfied.
