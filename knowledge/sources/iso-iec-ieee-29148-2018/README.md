# ISO/IEC/IEEE 29148:2018

This directory records how SPECTRUM will use ISO/IEC/IEEE 29148:2018 as a requirements-engineering reference.

## Status

- Source: ISO/IEC/IEEE 29148:2018
- Edition: 2nd edition, 2018
- Role in SPECTRUM: normative reference
- Current work item: Step 2.1 — identify the official structure and classify what SPECTRUM may derive from it
- Mapping status: structural inventory completed from the publicly available ISO Online Browsing Platform (OBP); detailed rule extraction is a later step.

## Important boundary

SPECTRUM must distinguish the source standard from its own implementation.

- The standard is the normative source.
- `knowledge/` stores derived knowledge representations and source metadata.
- `rules/` will contain SPECTRUM's machine-actionable interpretations only after their normative source has been identified.
- `skills/`, `workflows/`, `agents/`, `models/`, and the other system layers are SPECTRUM implementation decisions; they are not presented as terminology defined by ISO/IEC/IEEE 29148:2018.
- The repository does not reproduce the copyrighted full text of the standard.

## Official top-level structure

The ISO OBP table of contents exposes these top-level sections:

1. Scope
2. Normative references
3. Terms, definitions and abbreviated terms
4. Conformance
5. Concepts
6. Processes
7. Information items
8. Guidelines for information items

The public table of contents further identifies these major subsections:

### Section 3 — Terms, definitions and abbreviated terms

- 3.1 Terms and definitions
- 3.2 Abbreviated terms

The public OBP lists terminology covering, among other concepts, acquirer, attribute, baseline, business requirements specification, concept of operations, condition, constraint, context of use, customer, derived requirement, developer, document, human systems integration, information item, level of abstraction, operational concept, operational scenario, operator, requirement, requirements elicitation, requirements engineering, requirements management, requirements traceability, requirements traceability matrix, requirements validation, requirements verification, software requirements specification, stakeholder, stakeholder requirements specification, state, supplier, system-of-interest, system requirements specification, trade-off, user, validation, and verification.

### Section 4 — Conformance

- 4.1 Intended usage
- 4.2 Full conformance
- 4.3 Conformance to processes
- 4.4 Conformance to information item content
- 4.5 Tailored conformance

### Section 5 — Concepts

- 5.1 General
- 5.2 Requirements fundamentals
- 5.3 Practical considerations
- 5.4 Requirement information items

### Section 6 — Processes

- 6.1 Requirement processes
- 6.2 Business or mission analysis process
- 6.3 Stakeholder needs and requirements definition process
- 6.4 System [System/Software] Requirements definition process
- 6.5 Requirements engineering activities in other technical processes
- 6.6 Requirements management

### Section 7 — Information items

- 7. Information items

The public table of contents does not expose the complete internal list of information items in the accessible OBP excerpt. This repository therefore does not invent or fill in missing item names.

### Section 8 — Guidelines for information items

- 8.1 Requirements information item outlines
- 8.2 Business requirements specification

The public OBP excerpt available to SPECTRUM does not expose every detailed guideline subsection. Missing subsection names are intentionally not fabricated.

## Sections 1–4: classification basis

The following classification is an architectural interpretation for SPECTRUM, not ISO terminology.

| ISO section | What SPECTRUM can derive | Primary SPECTRUM layer | Status |
|---|---|---|---|
| 1 Scope | applicability boundary and source metadata | `governance/`, `knowledge/` | source-basis |
| 2 Normative references | dependency/reference graph between standards | `governance/`, `knowledge/` | source-basis |
| 3.1 Terms and definitions | controlled vocabulary and concept relationships | `knowledge/`, `models/` | source-basis |
| 3.2 Abbreviated terms | controlled abbreviations | `knowledge/` | source-basis |
| 4 Conformance | conformance concepts and evaluation metadata | `governance/`, `evaluation/` | source-basis |

## Sections 5–8: classification basis

| ISO section | What SPECTRUM can potentially derive | Primary SPECTRUM layer | Status |
|---|---|---|---|
| 5 Concepts | requirements-engineering concepts and analytical context | `knowledge/`, `models/` | to be mapped at detail level |
| 5.1 General | conceptual foundation | `knowledge/` | to be mapped |
| 5.2 Requirements fundamentals | requirement concepts, structure, relationships and attributes exposed by the source | `knowledge/`, `models/`, later `rules/` | to be mapped |
| 5.3 Practical considerations | contextual analytical considerations | `knowledge/`, later `skills/` | to be mapped |
| 5.4 Requirement information items | information-item concepts and relationships | `knowledge/`, `models/` | to be mapped |
| 6 Processes | lifecycle/process knowledge and candidate workflows | `knowledge/`, `workflows/`, later `skills/` | to be mapped |
| 6.1 Requirement processes | overall requirements-process orchestration | `workflows/` | to be mapped |
| 6.2 Business or mission analysis process | business/mission analysis capability | `skills/`, `workflows/` | to be mapped |
| 6.3 Stakeholder needs and requirements definition process | stakeholder-needs elicitation/definition capability | `skills/`, `workflows/` | to be mapped |
| 6.4 System [System/Software] Requirements definition process | system/software requirement definition capability | `skills/`, `workflows/` | to be mapped |
| 6.5 Requirements engineering activities in other technical processes | integration points with other engineering activities | `workflows/`, `governance/` | to be mapped |
| 6.6 Requirements management | lifecycle management, tracking and change-related capabilities | `skills/`, `workflows/`, `models/` | to be mapped |
| 7 Information items | structured artifacts exchanged/produced by requirements processes | `models/`, `outputs/` | to be mapped |
| 8 Guidelines for information items | format/content guidance for derived artifacts | `outputs/`, later `rules/` | to be mapped |
| 8.1 Requirements information item outlines | artifact structure metadata | `models/`, `outputs/` | to be mapped |
| 8.2 Business requirements specification | business-requirement artifact model | `models/`, `outputs/` | to be mapped |

## Official vocabulary relevant to SPECTRUM

The public definitions show that the standard distinguishes concepts that are directly relevant to a developer-readiness analysis, including:

- `requirement`
- `requirements elicitation`
- `requirements engineering`
- `requirements management`
- `requirements traceability`
- `requirements traceability matrix`
- `requirements validation`
- `requirements verification`
- `derived requirement`
- `constraint`
- `condition`
- `stakeholder`
- `user`
- `developer`
- `system-of-interest`
- `operational scenario`
- `system requirements specification`
- `software requirements specification`

These terms should become controlled concepts in SPECTRUM rather than ad-hoc terminology. The public source defines, for example, requirements engineering as including discovering, eliciting, developing, analysing, verifying, validating, communicating, documenting and managing requirements; it separately defines requirements management and requirements traceability. These distinctions matter for later skill boundaries.

## Initial architectural interpretation

For SPECTRUM, the 29148 source can feed the architecture through several different mechanisms:

```text
ISO/IEC/IEEE 29148:2018
        |
        +--> Knowledge
        |      concepts, definitions, vocabulary, relationships
        |
        +--> Rules
        |      checkable requirements-engineering provisions
        |
        +--> Skills
        |      operational capabilities derived from processes
        |
        +--> Workflows / Processes
        |      sequencing and orchestration derived from process structure
        |
        +--> Data Model
        |      requirement and information-item structures
        |
        +--> Evidence / Traceability
        |      source relationships and requirement derivation/flow-down concepts
        |
        +--> Evaluation / Test
        |      conformance/evaluation concepts
        |
        +--> Governance / Provenance
               source version, normative status, references, tailoring
```

This diagram is a SPECTRUM architecture decision. It is not a claim that ISO/IEC/IEEE 29148 defines these software folders or components.

## Normative references identified by 29148

The official OBP identifies these as normative references:

- ISO/IEC/IEEE 15288:2015 — Systems and software engineering — System life cycle processes
- ISO/IEC/IEEE 12207:2017 — Systems and software engineering — Software life cycle processes

These references are important for later analysis because SPECTRUM must not silently treat 29148 as an isolated body of requirements-engineering guidance.

## Provenance rules for implementation

Every future SPECTRUM rule derived from this source should carry at least:

- `source_id`: `iso-iec-ieee-29148-2018`
- `source_section`: exact section/subsection when known
- `source_type`: `standard`
- `normative_status`: normative / informative / implementation adaptation, as applicable
- `interpretation_level`: direct / derived / product-specific
- `version`: `2018`

A rule must not be presented as an ISO requirement when it is only a SPECTRUM interpretation.

## What remains deliberately outside Step 2.1

Step 2.1 does **not** yet define:

- individual machine-checkable rules;
- LLM prompts;
- agent roles;
- `READY` / `NOT READY` product statuses;
- thresholds or scores;
- INCOSE GtWR C1–C14 checks;
- VNVSpec implementation details.

Those belong to later steps and must retain their own provenance.

## Source and access note

The ISO Online Browsing Platform exposes the table of contents and selected informative/publicly viewable material, while the full standard is not freely reproduced there. SPECTRUM therefore records the public structural inventory and source metadata without copying the full copyrighted standard.

Primary source: ISO Online Browsing Platform, ISO/IEC/IEEE 29148:2018.
