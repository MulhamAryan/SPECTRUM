# architecture-reconstruction — référence

## References

Primary:

- ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*.
- IEEE 1016-2009, *Software Design Descriptions* (Inactive-Reserved — conceptual reference only).

Local controlled representations:

- `knowledge/sources/iso-iec-ieee-42010-2022/knowledge.yaml`
- `knowledge/sources/ieee-1016-2009/knowledge.yaml`
- `rules/sources/ieee-1016-2009/rules.yaml` (IEEE1016-R001)

Official source URLs:

- `https://www.iso.org/standard/74393.html` (fetch returned HTTP 403 in the session that built this Skill)
- `https://standards.ieee.org/ieee/1016/4502/` (fetched directly)

## Evaluation

Minimum evaluation cases:

- element_established_from_direct_code_evidence;
- dependency_established_from_observable_import_or_api_call;
- dependency_inferred_from_naming_only_rejected;
- repository_evidence_not_conflated_with_runtime_behavior;
- documentation_code_contradiction_preserved;
- reconstruction_partial_with_explicit_unassessed_scope;
- design_granularity_element_marked_as_reconstructed;
- git_history_used_as_provenance_not_behavior_proof;
- no_conformance_claim_to_ieee_1016_emitted;
- absent_artifact_not_treated_as_functional_absence.
