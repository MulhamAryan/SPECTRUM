# ISO/IEC/IEEE 15289:2019

This directory records how SPECTRUM uses ISO/IEC/IEEE 15289:2019 as a life-cycle documentation reference for `/spectrum:document-feature`.

## Status

- Source: ISO/IEC/IEEE 15289:2019, *Systems and software engineering — Content of life-cycle information items (documentation)*.
- Role in SPECTRUM: conceptual reference informing the `lifecycle-documentation` skill.
- Evidence basis: a direct fetch of the official ISO catalogue page (`iso.org/standard/74909.html`) returned HTTP 403 in this session. The scope statement in `knowledge.yaml` was corroborated from public search-result snippets (IEEE Xplore, IEEE SA, ANSI/ITeh listings).

## Important boundary

- The standard is the normative source; SPECTRUM does not reproduce its text.
- The 7 generic document types (description, plan, policy, procedure, report, request, specification) were present verbatim in the publicly indexed scope text and are recorded as confirmed.
- The standard's actual per-document-type required-content rules — its real normative payload, and the reason the standard exists — were **not accessible** in this session and are explicitly not fabricated.

## What SPECTRUM derives today

Only the confirmed generic document-type vocabulary and the fact that 15289 maps ISO/IEC/IEEE 12207:2017 and 15288:2015 process clauses to information items. SPECTRUM's own 22-section `TechnicalDocumentation` structure (see `outputs/technical-documentation-report.yaml`) is a product decision informed by this vocabulary, not a reproduction of a 15289-defined template — no such per-section template was verified this session.

## Source and access note

Primary source: ISO standard record, https://www.iso.org/standard/74909.html (direct fetch blocked, HTTP 403, this session). Scope text corroborated via public secondary listings returned by web search.
