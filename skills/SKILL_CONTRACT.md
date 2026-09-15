# SPECTRUM Skill Contract

This document defines the contract for Skills that operationalize validated SPECTRUM controls.

## Relation to the SPECTRUM chain

```text
ISO/IEC/IEEE 29148 knowledge
        ↓
SPECTRUM derived controls
        ↓
SPECTRUM Skills
        ↓
Findings + Evidence
        ↓
Decision / Output
```

A Skill is an implementation unit for one or more existing SPECTRUM controls. It MUST keep explicit references to those controls and MUST NOT silently redefine them.

## Required contract

Each concrete Skill declares:

- `id`
- `name`
- `type`: `component`, `interactive`, or `workflow`
- `role`
- `trigger`
- `objective`
- `scope`
- `inputs`
- `required_context`
- `preconditions`
- `rule_refs`
- `operations`
- `outputs`
- `finding_types`
- `evidence_requirements`
- `relations`
- `handoff`
- `exit_conditions`
- `non_goals`
- `evaluation_refs`

## Rule-to-Skill constraint

Every ISO-derived Skill MUST reference at least one existing rule from `rules/`. Every referenced rule MUST remain traceable to its source knowledge. A Skill may combine several rules when they form one coherent analytical responsibility.

## Execution boundary

A Skill observes and analyses evidence. It does not invent missing facts, approve requirements, make implementation decisions, or claim formal ISO conformance unless an explicit governance control supports such a claim.

## Output boundary

A Skill should emit structured findings and evidence references that can be consumed by another Skill or a Workflow. Free-form explanation may accompany them but is not the sole machine-consumable result.
