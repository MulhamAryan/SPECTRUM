# cross-artifact-analysis — référence

Sections extraites de `SKILL.md` pour alléger le contexte chargé par les agents. Elles servent à l'évaluation et à l'audit, pas à l'exécution.

## References
- `models/canonical-data-model.yaml`
- `models/finding-model.yaml`
- `models/evidence-model.yaml`
- `models/skill-execution-contract.yaml`
- `models/cross-artifact-analysis.yaml`
- `evaluation/contracts/cross-artifact-analysis.yaml`
- `evaluation/cases/cross-artifact-analysis.yaml`

## Evaluation
Vérifier au minimum :
- cohérence sémantique ;
- correspondance de champs ;
- terminologie et mappings de représentation ;
- alignement des conditions et contraintes ;
- alignement avec les critères d'acceptation ;
- traçabilité ;
- différences de version ;
- différences de temporalité ;
- différences d'applicabilité ;
- relations un-à-plusieurs ;
- champs calculés ;
- faux positifs dus à une absence de match textuel ;
- preuves insuffisantes ;
- contradictions conservées ;
- absence de décision globale générée par le Skill.
