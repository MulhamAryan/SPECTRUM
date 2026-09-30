# ISO/IEC/IEEE 29119-3:2021

This directory records how SPECTRUM uses ISO/IEC/IEEE 29119-3:2021 as a test-documentation reference for `/spectrum:document-feature`.

## Status

- Source: ISO/IEC/IEEE 29119-3:2021, *Software and systems engineering — Software testing — Part 3: Test documentation*.
- Role in SPECTRUM: conceptual reference informing the `test-documentation` skill.
- Evidence basis: a direct fetch of the official ISO catalogue page (`iso.org/standard/79429.html`) returned HTTP 403 in this session. The scope statement in `knowledge.yaml` was corroborated from public search-result snippets (SIS, ANSI, BSI, Wikipedia's ISO/IEC 29119 article).

## Important boundary

- The standard is the normative source; SPECTRUM does not reproduce its text.
- The standard's own named test-documentation templates (test plan, test case specification, incident report, etc.) are **widely cited in public secondary/training material** but were not independently verified against accessible normative text in this session. They are recorded in `knowledge.yaml` under `named_document_templates_pending_verification` with `status: UNVERIFIED` and are **not** used as a basis for any rule.

## What SPECTRUM derives today

Only the confirmed scope: 29119-3 defines test-documentation templates that are an output of the 29119-2 test processes, applicable across SDLC models and testing styles (dynamic, functional/non-functional, manual/automated, scripted/unscripted). SPECTRUM's `test-documentation` skill uses this as a boundary (test documentation describes what was actually tested — never invented) rather than reproducing named templates it has not verified.

## Source and access note

Primary source: ISO standard record, https://www.iso.org/standard/79429.html (direct fetch blocked, HTTP 403, this session). Scope text corroborated via public secondary listings returned by web search.
