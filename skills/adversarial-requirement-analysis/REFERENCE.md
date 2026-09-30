# adversarial-requirement-analysis — référence

Sections extraites de `SKILL.md` pour alléger le contexte chargé par les agents. Elles servent à l'évaluation et à l'audit, pas à l'exécution.

## Critères d'évaluation

Une exécution correcte doit :

- couvrir uniquement les catégories déclarées et applicables ;
- conserver les hypothèses comme hypothèses lorsqu'elles ne sont pas établies ;
- distinguer gap, incertitude et contradiction ;
- conserver la temporalité et le périmètre ;
- éviter les faux positifs liés aux cas limites ;
- produire des findings traçables ;
- être reproductible à entrées et configuration équivalentes ;
- ne produire aucune décision de readiness.
