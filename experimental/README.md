# Expérimental — hors plugin

Ce dossier contient du matériel **non branché** dans le plugin : il n'est ni découvert par Claude Code comme skill, ni référencé par le workflow, le registre ou un agent. Le validateur (`scripts/validate.py`) ignore ce dossier.

## Branche ISO/IEC/IEEE 29148

Six skills et leurs contrats d'évaluation ont été déplacés ici parce que :

1. aucun stage du workflow ni aucun agent ne les invoquait — `/spectrum:analyze-ticket` ne les exécutait jamais ;
2. la base de connaissance ISO (`knowledge/sources/iso-iec-ieee-29148-2018/`) est construite uniquement à partir de la table des matières publique de l'OBP ; l'extraction détaillée des règles suppose l'accès à la norme complète.

| Skill | Note |
|---|---|
| `iso29148-readiness` | Orchestrateur de la branche ISO |
| `conformance-governance` | Gouvernance de conformité |
| `multi-source-context` | Remplacé côté plugin par le stage `multi_source_reasoning` |
| `requirement-context` | Chevauche `requirements-context` (actif) — à fusionner si réactivé |
| `requirements-engineering-context` | Chevauche `requirements-context` (actif) — à fusionner si réactivé |
| `stakeholder-scenario-context` | Contexte parties prenantes / scénarios |

## Réactivation

Condition préalable : les rapports produits sur le jeu de tickets `examples/` montrent un manque que la branche INCOSE ne couvre pas. Alors : fusionner les trois skills de contexte en un seul, créer un agent `standards-context-analyst` branché sur le stage `contextualize`, l'ajouter au registre, et compléter `knowledge/sources/iso-…/` avec les règles détaillées. Ne pas réactiver « parce que c'est là ».

`knowledge/sources/iso-iec-ieee-29148-2018/` et `rules/sources/iso-iec-ieee-29148-2018/` restent à leur place comme référence documentaire.
