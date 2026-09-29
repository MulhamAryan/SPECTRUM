---
name: iso29148-readiness
description: Orchestrer les Skills applicables pour analyser la suffisance d'information d'un ticket avant implémentation.
type: workflow
role: orchestration
---

# ISO 29148 Readiness

## Purpose
Orchestrer une analyse adaptative de ticket en sélectionnant les Skills pertinents, en garantissant leurs préconditions, puis en consolidant les findings, evidence et gaps pour une décision externe.

## When to use
Activer pour une analyse globale de ticket avant implémentation ou pour une réévaluation d'un ticket après changement de contexte.

## Inputs
- `ticket`
- `ticket_type`
- `complexity`
- `available_context`
- `authorized_sources`
- `identified_risks`
- `prior_findings`
- `active_policy`

## Preconditions
1. Le ticket est identifiable.
2. Les sources autorisées sont connues.
3. Les règles applicables sont disponibles.

## Execution model
1. Charger les métadonnées des Skills candidats sans supposer qu'ils doivent tous être exécutés.
2. Exécuter `multi-source-context` lorsque des sources externes au ticket peuvent contenir du contexte pertinent.
3. Exécuter `requirement-context` sur le résultat consolidé.
4. À partir de son résultat et du type de ticket, sélectionner conditionnellement : `elicitation-gap`, `stakeholder-scenario-context`, `requirement-expression`, `requirement-relationship-traceability`, `verification-analysis`, `validation-analysis` et `requirements-engineering-context`.
5. Si une revendication de conformité existe, exécuter `conformance-governance`.
6. Respecter les préconditions de chaque Skill ; si une condition manque, produire un état explicite plutôt que contourner la précondition.
7. Propager les findings et evidence entre les Skills selon les relations définies dans `models/skill-relationships/iso-iec-ieee-29148.yaml`.
8. Agréger les résultats sans fusionner leurs responsabilités.
9. Construire `decision_inputs` à partir des gaps, findings, contradictions, evidence et limites.
10. Transmettre les `decision_inputs` à la couche de décision externe.

## Selection logic
- Toujours partir du contexte et de l'applicabilité, pas d'une séquence fixe.
- `requirement-expression` est prioritaire lorsque des formulations d'exigence sont identifiées.
- `verification-analysis` devient pertinent lorsque des critères observables, des tests ou des claims de vérification existent.
- `validation-analysis` devient pertinent lorsque l'adéquation au système, à l'usage, au besoin ou aux parties prenantes doit être établie.
- `requirement-relationship-traceability` devient pertinent dès qu'une relation hiérarchique ou de traçabilité est explicitement utilisée ou attendue.
- `requirements-engineering-context` devient pertinent lorsque plusieurs activités RE ou la gestion du cycle de vie sont impliquées.
- `conformance-governance` ne s'active que pour les claims de conformité.

## Gates
- Aucun Skill ne peut être exécuté avec une précondition manquante sans produire un état explicite.
- Les gaps critiques et contradictions doivent rester visibles dans `decision_inputs`.
- Toute evidence importée conserve sa provenance.
- Le workflow ne transforme pas un finding en fait ni une absence en succès.

## Outputs
`aggregate_findings`, `evidence_package`, `decision_inputs`, `executed_skills`, `skipped_skills_with_reason`, `unresolved_gaps`, `scope_and_limitations`.

## Handoffs
Les component Skills consomment le contexte et produisent des résultats structurés. Le workflow agrège et transmet à la couche de décision ; il ne décide pas lui-même le statut final.

## Failure handling
- Source inaccessible : l'indiquer et réduire explicitement le périmètre.
- Skill bloqué : conserver son état et poursuivre seulement les branches indépendantes.
- Contradiction : conserver les deux références et produire un gap/risque explicite.
- Résultat partiel : propager le statut partiel, jamais le convertir en succès complet.

## Non-goals
Ne pas décider `READY`, `READY WITH INVESTIGATION` ou `NOT READY/BLOCKED` ; ne pas inventer le contexte ; ne pas revendiquer une conformité ISO sur la seule base des contrôles exécutés.

## References
- `ISO/IEC/IEEE 29148:2018`
- `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`
- `models/skill-relationships/iso-iec-ieee-29148.yaml`
- `evaluation/skills/iso-iec-ieee-29148.yaml`

## Evaluation
Vérifier la sélection conditionnelle, les préconditions, les handoffs, la propagation des findings/evidence, la gestion des erreurs, la traçabilité des Skills exécutés et la préservation de la frontière de décision.