# requirement-relationship-traceability — référence

Sections extraites de `SKILL.md` pour alléger le contexte chargé par les agents. Elles servent à l'évaluation et à l'audit, pas à l'exécution.

## References

Primary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, June 2023.

Local controlled representations:

- `knowledge/sources/incose-gtwr-v4-2023/definitions.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/attributes.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

Official source URLs:

- `https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf`
- `https://www.incose.org/docs/default-source/working-groups/requirements-wg/gtwr/incose_rwg_gtwr_v4_040423_final_drafts.pdf`

## Evaluation

Minimum evaluation cases:

- complete_transformation_trace;
- missing_parent_or_source_trace;
- allocation_and_child_relationship;
- dependent_peer_relationship;
- interface_relationship;
- orphan_requirement_with_established_parent_basis;
- incomplete_traceability_artifact;
- contradictory_relationship_sources;
- directionality_error;
- absent_artifact_without_applicability_basis;
- textual_similarity_false_positive;
- correctness_not_inferred_from_link_presence.
