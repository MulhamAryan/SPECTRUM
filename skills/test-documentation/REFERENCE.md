# test-documentation — référence

## References

Primary:

- ISO/IEC/IEEE 29119-3:2021, *Software and systems engineering — Software testing — Part 3: Test documentation*.

Local controlled representations:

- `knowledge/sources/iso-iec-ieee-29119-3-2021/knowledge.yaml`
- `knowledge/sources/iso-iec-ieee-29119-3-2021/README.md`
- `rules/sources/iso-iec-ieee-29119-3-2021/rules.yaml`
- `models/canonical-data-model.yaml` — `Scenario.scenario_kind: test_case` (extension additive)

Official source URL:

- `https://www.iso.org/standard/79429.html` (fetch returned HTTP 403 in the session that built this Skill)

## Evaluation

Minimum evaluation cases:

- test_case_established_from_real_test_file;
- test_case_not_invented_when_no_test_found;
- absence_of_test_not_qualified_as_defect;
- traceability_chain_requirement_to_implementation_to_test_complete;
- traceability_chain_partial_when_test_link_missing;
- test_declared_in_repo_vs_execution_unverified_distinguished;
- test_type_classification_from_observed_structure_not_assumed;
- no_conformance_claim_to_29119_3_emitted;
- no_invented_coverage_percentage.
