# architecture-diagram — référence

## References

Primary:

- ISO/IEC/IEEE 42010:2022 (limite uniquement : la norme ne spécifie pas de notation/outil — le format Mermaid est une décision SPECTRUM).

Local controlled representations:

- `knowledge/sources/iso-iec-ieee-42010-2022/knowledge.yaml`
- `rules/sources/iso-iec-ieee-42010-2022/rules.yaml` (ISO42010-R003)

Aucune source normative ne définit ce Skill au-delà de cette limite — c'est une décision d'implémentation SPECTRUM.

## Evaluation

Minimum evaluation cases:

- diagram_node_maps_exactly_to_existing_architecture_element;
- diagram_edge_maps_exactly_to_existing_relationship;
- no_edge_added_purely_for_visual_completeness;
- isolated_node_remains_isolated_in_diagram;
- inferred_or_unknown_element_visually_distinguished;
- diagram_not_derivable_when_no_model_available;
- diagram_never_used_as_evidence_by_another_skill;
- per_view_diagram_produced_when_views_exist.
