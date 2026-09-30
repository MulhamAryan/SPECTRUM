# IEEE 1016-2009

This directory records how SPECTRUM uses IEEE 1016-2009 as a software-design-description reference for `/spectrum:document-feature`.

## Status

- Source: IEEE 1016-2009, *IEEE Standard for Information Technology — Systems Design — Software Design Descriptions*.
- **Current IEEE status: Inactive-Reserved.** SPECTRUM never claims conformance to this standard, in any skill, agent, or rendered document. It is used strictly as a conceptual reference.
- Role in SPECTRUM: conceptual reference informing the `software-design-description` skill and the `granularity: design` value of the `ArchitectureElement` canonical entity.
- Evidence basis: directly fetched from `standards.ieee.org/ieee/1016/4502/` in this session (the only one of the four new standards successfully fetched directly rather than corroborated via search snippets).

## Important boundary

- The standard is the normative source; SPECTRUM does not reproduce its text.
- Only the publicly fetched abstract is recorded as confirmed: it establishes the information content and organization of a Software Design Description (SDD), explicitly covering reverse engineering and traditional development, across commercial/scientific/military contexts, independent of size or complexity, with format/language flexibility.
- The standard's detailed content model (design entity, attribute, view, decision/rationale, relationship) is widely documented in public secondary literature but was **not** independently verified against accessible normative clause text in this session, and is not used as a rule basis.

## What SPECTRUM derives today

The abstract's explicit inclusion of reverse engineering is directly relevant: SPECTRUM's `architecture-reconstruction` and `software-design-description` skills recover a design description from an existing implementation rather than author one from scratch, which is exactly the scenario this standard's scope anticipates.

## Source and access note

Primary source: IEEE Standards Association, https://standards.ieee.org/ieee/1016/4502/ (fetched directly, this session).
