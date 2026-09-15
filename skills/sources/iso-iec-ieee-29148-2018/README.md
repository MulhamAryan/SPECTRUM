# Step 2.5 — ISO 29148 → SPECTRUM Skills

## Purpose

Cette étape transforme les contrôles SPECTRUM déjà dérivés de l'ISO/IEC/IEEE 29148:2018 en capacités de Skills concrètes. Les Skills ne constituent pas de nouvelles règles normatives : ils exécutent et relient les contrôles déjà présents dans `rules/sources/iso-iec-ieee-29148-2018/rules.yaml`.

## Chaîne de responsabilité

```text
ISO/IEC/IEEE 29148:2018
        ↓
knowledge/sources/iso-iec-ieee-29148-2018/
        ↓
rules/sources/iso-iec-ieee-29148-2018/rules.yaml
        ↓
skills/sources/iso-iec-ieee-29148-2018/skills.yaml
        ↓
findings + evidence
        ↓
décision SPECTRUM
```

## Principes de conception

1. Un Skill possède une responsabilité analytique identifiable.
2. Un Skill peut appliquer plusieurs contrôles lorsqu'ils forment une capacité cohérente.
3. Un même contrôle peut être réutilisé par plusieurs Skills lorsque leurs responsabilités diffèrent.
4. Aucun Skill ne crée silencieusement une obligation qui n'existe pas dans son `rule_refs`.
5. L'absence d'information produit un gap, une incertitude ou un état bloquant ; elle n'est pas complétée par invention.
6. Les sorties destinées à un autre Skill sont structurées et traçables.
7. Les workflows sélectionnent les Skills pertinents selon le contexte ; tous les tickets ne traversent pas nécessairement tous les Skills.
8. Les décisions `READY`, `READY WITH INVESTIGATION` et `NOT READY/BLOCKED` restent des décisions SPECTRUM et non des résultats ISO.

## Familles fonctionnelles

| Skill | Responsabilité | Contrôles ISO principaux |
|---|---|---|
| `requirement-context` | identifier le sujet, le niveau, les besoins, contraintes, conditions et états pertinents | R001, R002, R013, R015 |
| `elicitation-gap` | détecter quand l'analyse nécessite une collecte ou une clarification supplémentaire | R007 |
| `stakeholder-scenario-context` | établir le contexte parties prenantes et scénarios opérationnels pertinents | R012, R014 |
| `requirement-relationship-traceability` | analyser dérivation, allocation et relations de traçabilité disponibles | R004, R005, R006 |
| `verification-analysis` | analyser les affirmations de vérification et leur preuve objective | R009 |
| `validation-analysis` | analyser les affirmations de validation et leur base d'adéquation au système / usage | R008 |
| `requirements-engineering-context` | vérifier que le périmètre d'analyse couvre les activités RE pertinentes et le contexte de gestion | R010, R011 |
| `multi-source-context` | exploiter les sources autorisées avant de conclure à un manque et maintenir leur provenance | R016 |
| `conformance-governance` | contrôler les éventuelles affirmations de conformité à la norme | R017 |

## Typologie SPECTRUM

- `component` : réalise une analyse atomique ou produit un résultat spécialisé.
- `interactive` : réduit une incertitude ou sélectionne l'analyse pertinente lorsque les informations disponibles ne suffisent pas à déterminer automatiquement la voie.
- `workflow` : orchestre plusieurs Skills et leurs handoffs.

Cette typologie est une convention d'architecture SPECTRUM ; elle ne prétend pas provenir comme telle de l'ISO 29148.

## Règle d'instanciation

Les fichiers de Skills concrets devront conserver au minimum :

```text
id
name
type
role
trigger
objective
scope
inputs
required_context
preconditions
operations
rule_refs
outputs
findings
evidence_requirements
dependencies
relations
handoff_contract
exit_conditions
non_goals
evaluation_refs
```

Le détail de cette structure est défini par le contrat fonctionnel associé à Step 2.5, tandis que `skills.yaml` est l'artefact de liaison **contrôle ISO → capacité Skill**.
