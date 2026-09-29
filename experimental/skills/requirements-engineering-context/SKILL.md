---
name: requirements-engineering-context
description: Vérifier que le périmètre d'analyse couvre les activités de Requirements Engineering pertinentes et le contexte de gestion dans le temps lorsqu'applicable.
type: component
role: cross_cutting
---

# Requirements Engineering Context

## Purpose
Vérifier que l'analyse traite les activités de Requirements Engineering pertinentes au ticket et qu'aucun besoin de gestion du cycle de vie n'est ignoré lorsqu'il s'applique.

## When to use
Activer pour les changements significatifs, tickets modifiant des exigences existantes, activités où plusieurs pratiques RE sont nécessaires, ou lorsque la gestion dans le temps fait partie du contexte.

## Inputs
Required: `ticket`, `available_context`
Optional: `workflow_state`, `requirement_history`

## Preconditions
- Le ticket est disponible.
- Le contexte de processus connu est accessible.

## Procedure
1. Classer le ticket selon les activités RE potentiellement pertinentes.
2. Examiner l'évidence disponible pour les activités de découverte/élicitation, développement, analyse, vérification, validation, communication, documentation et management selon le contexte.
3. Ne retenir que les activités justifiées par la nature du ticket.
4. Pour une exigence déjà gérée dans le temps, rechercher son identification, historique, maintenance, communication, traçabilité et suivi lorsqu'ils sont applicables.
5. Identifier les activités attendues mais non couvertes par les sources disponibles.
6. Distinguer "non applicable" de "non démontré".
7. Produire une vue de couverture exploitable par le workflow.

## Analysis logic
Toutes les activités RE ne sont pas obligatoires pour chaque ticket. Le Skill évalue la pertinence et la couverture démontrable, pas l'existence d'un processus universel identique.

## Decision rules
- `covered`: activité pertinente et suffisamment établie.
- `not_demonstrated`: activité pertinente mais evidence insuffisante.
- `not_applicable`: activité non pertinente pour le cas analysé.
- `lifecycle_gap`: gestion attendue dans le temps non établie.

## Rules
- `ISO29148-R010`
- `ISO29148-R011`

## Output
`re_context_assessment` contient `relevant_activities`, `coverage_by_activity`, `lifecycle_observations`, `evidence_refs`, `status`.

## Findings
- `requirements_engineering_coverage_gap`
- `requirements_management_context_gap`

## Evidence
Pour chaque activité jugée couverte, conserver la justification et les sources ; pour chaque gap, conserver les éléments montrant pourquoi l'activité est pertinente.

## Handoff
Vers `iso29148-readiness` pour l'agrégation et l'évaluation globale.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `not_applicable`

## Non-goals
Ne pas imposer toutes les activités à tous les tickets ; ne pas imposer un cycle de vie unique.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R010`, `ISO29148-R011`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : ticket simple, changement d'exigence existante, activité pertinente non démontrée, gestion lifecycle applicable, non-applicable, régression.