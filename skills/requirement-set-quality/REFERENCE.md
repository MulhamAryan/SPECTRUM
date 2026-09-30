# requirement-set-quality — référence

Sections extraites de `SKILL.md` pour alléger le contexte chargé par les agents. Elles servent à l'évaluation et à l'audit, pas à l'exécution.

## References

Primary:

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`, July 2023.
- INCOSE Guide to Writing Requirements v4 – Summary Sheet, June 2023, especially pp. 2–6.

Supporting source representations in SPECTRUM:

- `knowledge/sources/incose-gtwr-v4-2023/characteristics.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/rules.yaml`
- `knowledge/sources/incose-gtwr-v4-2023/matrices.yaml`
- `models/skill-relationships/incose-gtwr-v4.yaml`

Official source URLs:

- https://www.incose.org/docs/default-source/working-groups/requirements-wg/gtwr/incose_rwg_gtwr_v4_040423_final_drafts.pdf
- https://www.incose.org/docs/default-source/working-groups/requirements-wg/guidetowritingrequirements/incose_rwg_gtwr_v4_summary_sheet.pdf

## Evaluation

The Skill should be evaluated with cases covering at least:

- complete, internally consistent requirement set;
- duplicate expressions violating uniqueness;
- explicit contradiction between two members;
- overlap that requires scope analysis rather than lexical comparison;
- inconsistent terminology against a glossary or data dictionary;
- inconsistent units or measurement systems;
- acronym inconsistency;
- abbreviation issues;
- inconsistent decimal format;
- missing required grouping/structure when a project template exists;
- unrelated requirements correctly kept separate;
- incomplete set with explicit source evidence for the missing coverage;
- feasibility assessment with sufficient constraints and risk evidence;
- feasibility assessment blocked by missing constraints;
- validation assessment with explicit goals and stakeholder basis;
- correctness assessment with parent/source traceability;
- correctness assessment blocked by missing transformation evidence;
- set comprehensibility issue caused by unresolved relationships;
- no-false-positive case where generic best-practice expectations are not treated as INCOSE findings;
- official source discrepancy handling, including R14 labeling;
- individual-versus-set characteristic separation;
- regression verifying that R29/R41/R42 are assessed at set level rather than treated as individual wording rules.
