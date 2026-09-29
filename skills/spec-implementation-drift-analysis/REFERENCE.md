# spec-implementation-drift-analysis — référence

Sections extraites de `SKILL.md` pour alléger le contexte chargé par les agents. Elles servent à l'évaluation et à l'audit, pas à l'exécution.

## Critères d'évaluation

Une exécution correcte doit :

- préserver l'identité et la provenance des deux côtés ;
- déclarer la base de comparaison utilisée ;
- conserver les mappings explicites ;
- distinguer absence de preuve et absence démontrée ;
- gérer les mappings un-vers-plusieurs et plusieurs-vers-un ;
- conserver les versions, baselines et temporalités ;
- identifier les écarts observables sans inventer de runtime ;
- produire des findings traçables ;
- être reproductible à entrées et configuration équivalentes ;
- ne produire aucune décision de readiness.
