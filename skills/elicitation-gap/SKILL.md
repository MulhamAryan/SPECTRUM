---
name: elicitation-gap
description: Détecter les informations nécessaires à l'analyse qui ne sont pas établies dans les sources disponibles et formuler un gap exploitable.
type: component
role: contextualization
---

# Elicitation Gap

## Purpose
Transformer une absence d'information pertinente en gap explicite et actionnable, sans inventer la réponse manquante.

## When to use
Activer lorsqu'une analyse dépend d'un besoin, d'une règle, d'une décision ou d'un contexte qui n'est pas suffisamment établi dans les sources accessibles.
Ne pas l'utiliser pour décider que toute information non présente dans le ticket est automatiquement manquante.

## Inputs
Required: `requirement_context`, `available_sources`
Optional: `prior_findings`

## Preconditions
- Le contexte analysé existe.
- Les sources déjà consultées sont connues.

## Procedure
1. Lister les informations nécessaires à l'analyse courante.
2. Pour chaque information, rechercher une preuve dans les sources autorisées.
3. Distinguer `absent`, `present_but_incomplete`, `contradictory` et `established`.
4. Vérifier si l'absence empêche une interprétation, une vérification, une validation ou une décision ultérieure.
5. Classer le gap par nature : besoin, contexte, acteur, scénario, contrainte, critère, preuve ou autre.
6. Formuler exactement ce qui doit être clarifié ou collecté.
7. Attacher les preuves montrant pourquoi le gap existe.

## Analysis logic
Un gap est produit seulement lorsque l'information est nécessaire à l'analyse et n'est pas suffisamment établie. Une absence dans un seul artefact n'est pas suffisante si une source autorisée établit déjà l'information ailleurs.

## Decision rules
- `no_gap`: information établie.
- `gap`: information nécessaire non établie.
- `critical_gap`: gap qui empêche une analyse ou une vérification/validation attendue.
- `contradiction_gap`: sources incompatibles nécessitant arbitrage.

## Rules
- `ISO29148-R007`

## Output
`elicitation_gap` contient : `question_or_need`, `why_needed`, `gap_type`, `impact`, `source_scope_checked`, `evidence_refs`, `status`.
Le Skill ne fournit pas la réponse au gap.

## Findings
- `elicitation_gap`
- `critical_elicitation_gap`
- `contradictory_information_gap`

## Evidence
Référencer les sources consultées et, lorsque possible, les passages montrant l'absence, l'incomplétude ou la contradiction.

## Handoff
Transmettre au workflow pour influencer la sélection des analyses et l'évaluation des conditions bloquantes.

## Exit conditions
- `completed`
- `not_applicable`
- `blocked_on_missing_context`

## Non-goals
Ne pas conduire l'entretien d'élicitation, ne pas inventer une réponse, ne pas choisir arbitrairement entre sources contradictoires.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R007`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : gap réellement absent, information trouvée ailleurs, information partielle, contradiction, faux positif d'absence, régression.