---
name: iso29148-readiness
description: Orchestrer les Skills applicables pour analyser la suffisance d'information d'un ticket avant implémentation.
type: workflow
role: orchestration
---

# ISO 29148 Readiness

## Responsibility

Orchestrer les Skills pertinents pour analyser la suffisance d'information d'un ticket avant implémentation, sans imposer le même parcours à tous les tickets.

## Selection inputs

- `ticket_type`
- `complexity`
- `available_context`
- `identified_risks`
- `prior_findings`
- `active_policy`

## Baseline

- `multi-source-context`
- `requirement-context`

## Conditional Skills

- `elicitation-gap`
- `stakeholder-scenario-context`
- `requirement-expression`
- `requirement-relationship-traceability`
- `verification-analysis`
- `validation-analysis`
- `requirements-engineering-context`
- `conformance-governance`

## Gates

- Le contexte requis est établi ou explicitement déclaré manquant.
- Les findings sont propagés.
- Les liens d'evidence sont conservés.
- Les conditions bloquantes sont explicites.

## Outputs

- `aggregate_findings`
- `evidence_package`
- `decision_inputs`

## Handoffs

Chaque Skill produit des résultats structurés consommables par le workflow. Le workflow agrège les findings et evidence sans redéfinir les contrôles.

## Non-goals

- Ne pas décider directement `READY`, `READY WITH INVESTIGATION` ou `NOT READY/BLOCKED`.
- Ne pas inventer le contexte manquant.
- Ne pas revendiquer une conformité ISO sur la seule base des contrôles exécutés.

## References

- Norme : `ISO/IEC/IEEE 29148:2018`
- Contrôles : `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`
- Architecture : les composants présents sous `skills/`

## Evaluation

Vérifier la sélection conditionnelle, l'ordre des préconditions, la propagation des findings/evidence, les handoffs, les références résolues et la frontière de décision.
