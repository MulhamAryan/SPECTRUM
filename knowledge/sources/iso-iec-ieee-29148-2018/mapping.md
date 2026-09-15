# ISO/IEC/IEEE 29148:2018 → SPECTRUM mapping

## Purpose

This document records the first architectural mapping from the publicly visible structure and terminology of ISO/IEC/IEEE 29148:2018 to SPECTRUM implementation categories.

This is an **architecture mapping**, not a reproduction of the standard and not a claim that ISO defines SPECTRUM's categories.

## Source status

- Source: ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes — Requirements engineering*.
- Authority in SPECTRUM: normative reference.
- Public source used: ISO Online Browsing Platform (OBP).
- The public OBP states that only informative sections of standards are publicly available; the full standard is not reproduced here.

## Mapping principles

1. **Preserve provenance.** Every normative-derived element must remain linked to its ISO section.
2. **Do not turn every concept into a rule.** Definitions belong primarily to knowledge/model layers; only checkable provisions should later become rules.
3. **Do not equate skill with agent.** A skill is an operational capability. An agent is an execution/orchestration mechanism and is a SPECTRUM architectural choice.
4. **Do not treat SPECTRUM decisions as ISO requirements.** Readiness states, scoring, thresholds, prompts and implementation policies are product decisions unless a source explicitly supports them.
5. **Do not infer unpublished detail.** Where the public OBP exposes only a heading and not the underlying normative text, the mapping remains conservative.

## Matrix

| ISO 29148 element visible in OBP | Primary SPECTRUM category | Secondary category | Treatment | Provenance status |
|---|---|---|---|---|
| 1 Scope | Governance / Provenance | Knowledge | Defines applicability boundary of the reference; store as source metadata and applicability information. | ISO-derived |
| 2 Normative references | Governance / Provenance | Knowledge | Record referenced standards because their content can become part of the requirements framework. | ISO-derived |
| 3 Terms, definitions and abbreviated terms | Knowledge | Data Model | Build a controlled vocabulary and canonical terminology layer. | ISO-derived |
| 4 Conformance | Governance / Provenance | Evaluation / Test | Represents the conformance dimension; later supports checks of whether SPECTRUM processes/artifacts follow the selected reference basis. | ISO-derived + SPECTRUM implementation |
| 4.1 Intended usage | Knowledge | Governance / Provenance | Capture intended use and reference scope before applying checks. | ISO-derived |
| 4.2 Full conformance | Governance / Provenance | Evaluation / Test | Keep as a conformance concept; exact implementation must not be invented from the heading alone. | ISO-derived |
| 4.3 Conformance to processes | Workflow / Process | Evaluation / Test | Potential basis for process-level checks once the full normative content is available. | ISO-derived |
| 4.4 Conformance to information item content | Data Model | Evaluation / Test | Potential basis for checking whether required information items contain expected content. | ISO-derived |
| 4.5 Tailored conformance | Governance / Provenance | Configuration / Policy | Explicitly relevant to controlled tailoring; SPECTRUM should model tailoring separately from the base reference. | ISO-derived |
| 5 Concepts | Knowledge | Data Model | Foundational concepts are represented in the knowledge/model layers. | ISO-derived |
| 5.1 General | Knowledge | Data Model | General conceptual basis; no executable rule is created from the heading alone. | ISO-derived |
| 5.2 Requirements fundamentals | Knowledge | Rules | Main candidate source for requirement concepts and later checkable rules. Exact rule extraction requires the accessible normative content. | ISO-derived |
| 5.3 Practical considerations | Knowledge | Rules | Candidate source for implementation guidance and checks; no detailed rules are inferred here. | ISO-derived |
| 5.4 Requirement information items | Data Model | Knowledge | Candidate source for structured requirement-related information entities. | ISO-derived |
| 6 Processes | Workflow / Process | Skills | Main source family for requirements-engineering activities and their lifecycle orchestration. | ISO-derived |
| 6.1 Requirement processes | Workflow / Process | Skills | Candidate root workflow for requirement-engineering activities. | ISO-derived |
| 6.2 Business or mission analysis process | Workflow / Process | Skill | Candidate capability for understanding business/mission context before deriving requirements. | ISO-derived |
| 6.3 Stakeholder needs and requirements definition process | Workflow / Process | Skill | Candidate capability for eliciting and defining stakeholder needs/requirements. | ISO-derived |
| 6.4 System [System/Software] Requirements definition process | Workflow / Process | Skill | Candidate capability for deriving/defining system or software requirements from higher-level needs and context. | ISO-derived |
| 6.5 Requirements engineering activities in other technical processes | Workflow / Process | Skill | Represents RE activities embedded in other technical processes; orchestration must remain context-aware. | ISO-derived |
| 6.6 Requirements management | Workflow / Process | Evidence / Traceability | Candidate basis for identification, documentation, maintenance, communication, traceability and tracking. | ISO-derived |
| 7 Information items | Data Model | Outputs / Artifacts | Main source family for defining the information objects produced by RE processes. | ISO-derived |
| 8 Guidelines for information items | Outputs / Artifacts | Data Model | Candidate basis for artifact structure/format guidance. | ISO-derived |
| 8.1 Requirements information item outlines | Data Model | Outputs / Artifacts | Candidate schemas/outlines for requirement information artifacts. | ISO-derived |
| 8.2 Business requirements specification | Data Model | Outputs / Artifacts | Candidate specification artifact to model; detailed fields must come from the accessible source content. | ISO-derived |

## Terminology candidates from Section 3

The public OBP exposes a set of terms that are directly relevant to SPECTRUM's domain model. They should first be treated as **knowledge**, then mapped to concrete model fields only where the product requires them.

Relevant examples include:

- requirement
- requirements engineering
- requirements elicitation
- requirements management
- requirements traceability
- requirements traceability matrix
- requirements validation
- requirements verification
- stakeholder
- stakeholder requirements specification
- software requirements specification
- system requirements specification
- system-of-interest
- business requirements specification
- operational concept
- operational scenario
- condition
- constraint
- derived requirement
- developer
- user
- verification
- validation
- trade-off
- information item

The public OBP explicitly defines requirements traceability as the upward derivation path and downward allocation/flow-down path of requirements, and identifies the parent/child relationship. This is therefore a strong candidate for SPECTRUM's trace model rather than an individual requirement-quality score.

## What this mapping does **not** establish yet

This matrix intentionally does not define:

- individual requirement-quality rules;
- exact wording patterns or prohibited words;
- acceptance-criteria thresholds;
- readiness scoring or READY/NOT READY states;
- agent prompts;
- model-provider-specific behavior;
- project-specific policies;
- implementation algorithms.

Those require later steps and, where normative claims are made, direct support from the relevant source content.

## Public-source boundary

The ISO OBP page exposes the official table of contents, terminology and selected introductory/conceptual material. It explicitly states that only informative sections are publicly available and that the full content requires access to the standard. Therefore this matrix deliberately avoids fabricating detailed requirements from unavailable normative text.

## Primary official source

ISO Online Browsing Platform:
https://www.iso.org/obp/ui?_escaped_fragment_=iso%3Astd%3Aiso-iec-ieee%3A29148%3Aed-2%3Av1%3Aen

ISO standard record:
https://www.iso.org/standard/72089.html
