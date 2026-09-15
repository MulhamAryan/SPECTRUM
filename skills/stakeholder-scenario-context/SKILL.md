---
name: stakeholder-scenario-context
description: Établir les parties prenantes et les scénarios opérationnels pertinents à partir des sources autorisées.
type: component
role: contextualization
---

# Stakeholder & Scenario Context

## Purpose
Établir les acteurs pertinents et les scénarios qui donnent un contexte opérationnel vérifiable aux exigences.

## When to use
Activer lorsque la compréhension de l'exigence dépend d'utilisateurs, parties prenantes, acteurs externes, modes opératoires ou séquences d'utilisation.

## Inputs
Required: `ticket`, `available_context`
Optional: `repository_evidence`, `prior_findings`

## Preconditions
- Le contexte disponible est accessible.

## Procedure
1. Extraire les acteurs explicitement mentionnés.
2. Rechercher dans les sources autorisées des rôles associés au système ou à la fonctionnalité.
3. Ne retenir comme partie prenante pertinente que les acteurs soutenus par une relation explicite avec l'exigence ou le système.
4. Déterminer si l'exigence dépend d'un scénario d'utilisation ou d'un contexte opérationnel.
5. Rechercher les scénarios existants, cas d'utilisation, séquences, états ou parcours utiles.
6. Vérifier que les scénarios retenus couvrent le déclencheur, l'acteur, l'action et le résultat lorsqu'ils sont nécessaires à l'analyse.
7. Signaler les scénarios indispensables mais non établis.
8. Conserver la provenance de chaque acteur et scénario.

## Analysis logic
La présence d'un utilisateur dans une phrase ne suffit pas à établir son rôle système. Un scénario n'est requis que s'il affecte réellement l'interprétation ou la validation de l'exigence.

## Decision rules
- `stakeholder_established` lorsque le rôle et sa relation sont sourcés.
- `scenario_established` lorsque les éléments nécessaires du scénario sont disponibles.
- `scenario_needed_missing` lorsque le scénario est nécessaire mais absent.
- `not_required` lorsque le ticket peut être interprété sans scénario supplémentaire.

## Rules
- `ISO29148-R012`
- `ISO29148-R014`

## Output
`stakeholder_context` et `scenario_context` avec `actors`, `relations`, `scenario_elements`, `applicability`, `evidence_refs` et `status`.

## Findings
- `stakeholder_context_gap`
- `operational_scenario_context_gap`
- `stakeholder_role_not_established`

## Evidence
Chaque acteur ou scénario doit avoir au moins une référence de source lorsqu'il est présenté comme fait.

## Handoff
Transmettre le contexte à `validation-analysis` et au workflow.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals
Ne pas inventer de persona, de rôle ou de scénario ; ne pas décider de readiness.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R012`, `ISO29148-R014`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : acteur explicitement sourcé, acteur ambigu, scénario nécessaire, scénario inutile, contexte contradictoire, régression.