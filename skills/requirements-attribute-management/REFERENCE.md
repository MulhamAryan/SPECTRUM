# requirements-attribute-management — référence

Sections extraites de `SKILL.md` pour alléger le contexte chargé par les agents. Elles servent à l'évaluation et à l'audit, pas à l'exécution.

## References

Primary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, June 2023.

Local controlled sources:

- `knowledge/sources/incose-gtwr-v4-2023/attributes.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

## Evaluation

Minimum evaluation cases:

- applicable_rationale_attribute_present;
- trace_to_source_attribute_present;
- trace_attribute_missing_with_established_applicability;
- optional_attribute_not_marked_as_failure;
- conflicting_attribute_values;
- missing_attribute_source;
- attribute_value_mismatch_with_authoritative_source;
- owner_or_status_inconsistency;
- lifecycle_attribute_without_project_policy_is_inconclusive;
- traceability_attribute_handoff;
- verification_attribute_handoff;
- validation_attribute_handoff;
- no_false_positive_from_unmapped_attribute;
- no_false_positive_from_absent_optional_attribute.
