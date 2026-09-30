---
name: multi-source-context
description: Rechercher le contexte pertinent dans les sources autorisées avant de conclure qu'une information manque, en conservant la provenance.
type: component
role: cross_cutting
---

# Multi-Source Context

## Purpose
Établir un contexte consolidé à partir de plusieurs sources autorisées et empêcher qu'une absence du ticket soit confondue avec une absence globale d'information.

## When to use
Activer avant de conclure qu'une information manque lorsque le repository, la documentation, les tickets liés, les tests ou d'autres sources autorisées peuvent contenir cette information.

## Inputs
Required: `ticket`, `authorized_sources`
Optional: `repository`, `documentation`, `related_tickets`, `tests`

## Preconditions
- Les sources autorisées sont connues.
- Les mécanismes d'accès disponibles sont définis.

## Procedure
1. Énumérer les sources autorisées pertinentes au cas.
2. Définir pour chaque source le type d'information recherché.
3. Chercher d'abord les identifiants, noms de composants, fonctionnalités et termes distinctifs du ticket.
4. Examiner les artefacts liés lorsque le premier niveau ne suffit pas.
5. Pour chaque information retrouvée, enregistrer source, localisation, version/révision si disponible et relation avec le ticket.
6. Comparer les sources pour détecter convergence, divergence et contradiction.
7. Classer l'information comme `established`, `partial`, `contradictory` ou `not_found`.
8. Ne conclure à un manque qu'après avoir couvert les sources autorisées pertinentes.
9. Produire un package de contexte réutilisable par les autres Skills.

## Analysis logic
Le Skill ne traite jamais une inférence du modèle comme une source. Une source secondaire ne remplace pas une source plus directement pertinente si la distinction est importante.

## Decision rules
- `found`: information sourcée.
- `found_partial`: information sourcée mais incomplète.
- `contradictory`: plusieurs sources incompatibles.
- `not_found_after_search`: aucune source autorisée pertinente ne l'établit.

## Rules
- `ISO29148-R016`

## Output
`context_package` contient `facts`, `unknowns`, `contradictions`, `source_coverage`, `provenance_records`.

## Findings
- `context_not_sufficiently_established`
- `contradictory_source_context`
- `authorized_source_not_available`

## Evidence
Chaque fait importé doit avoir une référence précise ; conserver également les sources consultées mais infructueuses lorsque cela sert à justifier un gap.

## Handoff
Vers `requirement-context`, puis les Skills spécialisés selon le workflow.

## Exit conditions
- `completed`
- `completed_with_gaps`
- `blocked_on_missing_context`

## Non-goals
Ne pas accéder à une source non autorisée ; ne pas résoudre arbitrairement une contradiction ; ne pas compléter par connaissance générale non sourcée.

## References
- `ISO/IEC/IEEE 29148:2018`
- `ISO29148-R016`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`

## Evaluation
Tester : information trouvée dans ticket, information trouvée dans repository, information multi-source, contradiction, recherche infructueuse, régression.