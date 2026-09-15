# SPECTRUM Skill Evaluation

## Step 2.5 — Evaluation and completeness model

Les Skills SPECTRUM sont des composants exécutables : leur qualité doit donc être testable indépendamment de la seule lecture du texte du Skill.

## 1. Evaluation contract

Chaque Skill concret devra déclarer ou référencer une stratégie d'évaluation qui permet de vérifier :

- activation correcte ;
- respect de son périmètre ;
- application des règles référencées ;
- exploitation correcte du contexte ;
- non-invention face aux informations manquantes ;
- production de findings structurés ;
- rattachement des conclusions à l'evidence disponible ;
- respect des conditions de sortie ;
- respect des contrats de handoff ;
- stabilité lors des régressions.

## 2. Test classes

Chaque Skill doit être évalué, lorsque pertinent, sur les classes suivantes :

### Nominal

Le contexte satisfait les préconditions et le Skill doit produire le résultat attendu.

### Missing context

Une information nécessaire manque. Le Skill doit signaler le manque ou son état bloquant au lieu d'inventer une valeur.

### Contradictory context

Deux sources ou deux éléments pertinents sont incompatibles. Le Skill doit conserver le conflit comme finding ou état prévu par son contrat.

### Not applicable

Le contexte ne justifie pas l'activation du Skill. Le résultat doit pouvoir être distingué d'un échec d'analyse.

### Evidence insufficient

Une conclusion potentielle ne peut pas être suffisamment étayée. Le Skill doit représenter l'insuffisance d'evidence explicitement.

### Regression

Un cas précédemment validé est rejoué après modification afin de détecter une régression de comportement.

## 3. Evaluation layers

```text
Skill metadata
    ↓
Routing evaluation
    ↓
Contract evaluation
    ↓
Rule application evaluation
    ↓
Finding / evidence evaluation
    ↓
Handoff evaluation
    ↓
Integration evaluation
```

## 4. Expected behavior

Un test doit préciser au minimum :

```text
fixture / input
context
expected activation
expected relevant rules
expected findings
expected evidence links
expected output shape
expected exit state
```

Les tests ne doivent pas uniquement vérifier qu'une réponse contient des mots-clés ; lorsque c'est possible, ils doivent vérifier la structure et les relations entre objets.

## 5. Skill-level checks

Avant qu'un Skill soit considéré comme valide, vérifier :

- son identifiant est stable ;
- son type est correct ;
- son routage est suffisamment discriminant ;
- son objectif est cohérent avec sa responsabilité ;
- ses entrées et préconditions sont explicites ;
- ses opérations sont bornées ;
- ses Rule refs sont valides ;
- ses outputs sont consommables ;
- ses findings sont structurés ;
- son evidence model est défini ;
- ses dépendances sont explicites ;
- ses handoffs sont versionnables lorsqu'ils existent ;
- ses exit conditions sont observables ;
- ses non-goals sont présents ;
- sa stratégie d'évaluation est présente.

## 6. Workflow-level checks

Un Workflow doit en plus être évalué sur :

- ordre ou conditions d'invocation ;
- sélection des Skills pertinents ;
- propagation des findings ;
- propagation de l'evidence ;
- validation des handoffs ;
- gestion des erreurs / états bloquants ;
- respect des gates ;
- absence de duplication des responsabilités ;
- résultat agrégé cohérent.

## 7. Cross-skill integration checks

Lorsqu'un Skill A alimente un Skill B :

```text
A output
   ↓ schema validation
B input
   ↓ execution
B result
```

Un test d'intégration doit vérifier que le contrat de A est réellement accepté et interprété correctement par B.

## 8. Completeness gates for Step 2.5

Avant de considérer le modèle Skill complet, effectuer plusieurs passages de vérification.

### Check 1 — Contract completeness

Confirmer que toutes les dimensions nécessaires d'un Skill sont représentées dans le contrat.

### Check 2 — Architecture completeness

Confirmer que type, phase, routing, composition et dépendances sont représentables sans ambiguïté.

### Check 3 — Evidence completeness

Confirmer qu'un finding important peut être relié à une source, une règle et une evidence, ou signaler explicitement leur absence.

### Check 4 — Execution completeness

Confirmer que préconditions, opérations, états et conditions de sortie sont représentables.

### Check 5 — Interoperability completeness

Confirmer que les handoffs et outputs peuvent être consommés par d'autres Skills sans dépendre d'un prompt ou d'une plateforme particulière.

### Check 6 — Evaluation completeness

Confirmer que les Skills peuvent être testés sur des cas nominaux, absences, conflits, non-applicabilité et régressions.

### Check 7 — SPECTRUM layer alignment

Confirmer l'alignement avec :

```text
knowledge/
rules/
skills/
workflows/
agents/
evidence/
decisions/
outputs/
evaluation/
governance/
policies/
```

### Check 8 — ISO linkage

Confirmer qu'aucun Skill dérivé des règles ISO ne perd son `rule_ref` et qu'aucune règle n'est silencieusement transformée en obligation différente.

## 9. Definition of done for a concrete Skill

Un Skill concret n'est pas considéré terminé tant que :

```text
Contract defined
AND
Routing defined
AND
Rules linked
AND
Inputs / Preconditions defined
AND
Operations bounded
AND
Outputs defined
AND
Findings / Evidence defined
AND
Dependencies / Relations defined
AND
Exit conditions defined
AND
Non-goals defined
AND
Evaluation cases defined
```

## 10. Important boundary

L'évaluation d'un Skill vérifie le comportement du Skill et la conformité à son contrat SPECTRUM. Elle ne constitue pas à elle seule une affirmation de conformité formelle à une norme externe.
