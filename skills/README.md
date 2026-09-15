# SPECTRUM Skills

## Step 2.5 — Skill architecture

Cette section définit le modèle de conception des Skills SPECTRUM avant leur instanciation à partir des contrôles validés.

### Objectif

Un Skill SPECTRUM est une capacité explicite, composable et évaluable qui transforme un contexte d'entrée en résultats structurés, traçables et vérifiables.

Un Skill n'est pas un Agent et n'est pas une règle. Un Workflow est un type de Skill ; il se distingue d'un component ou d'un interactive par sa responsabilité d'orchestration.

### Chaîne de conception

```text
Knowledge
   ↓
Rules
   ↓
Skill definition
   ↓
Skill execution
   ↓
Findings + Evidence + structured outputs
   ↓
Workflow / Decision / Output
```

### Dimensions obligatoires

Chaque Skill SPECTRUM doit être définissable selon les dimensions suivantes :

- identité et identifiant stable
- type de Skill
- rôle dans le cycle SPECTRUM
- déclencheur / routage sémantique
- objectif
- périmètre
- responsabilité unique ou responsabilité explicitement bornée
- entrées
- contexte requis
- opérations
- règles utilisées
- sorties
- findings produits
- evidence attendues
- préconditions
- conditions de sortie
- dépendances
- relations avec les autres Skills
- handoffs entrants et sortants lorsqu'ils existent
- non-objectifs / limites
- références
- stratégie d'évaluation

### Typologie

SPECTRUM distingue trois types fonctionnels :

#### component

Capacité spécialisée exécutant une analyse ou une transformation bien délimitée.

Un component doit être réutilisable indépendamment d'un Workflow.

#### interactive

Capacité destinée à réduire une incertitude ou à orienter le choix d'une analyse, d'une source, d'une méthode ou d'une prochaine étape.

Un interactive peut demander des informations complémentaires lorsque celles-ci sont nécessaires à une décision responsable.

#### workflow

Capacité d'orchestration qui enchaîne plusieurs Skills, applique des conditions de passage et agrège leurs résultats.

Un workflow ne doit pas dupliquer inutilement les responsabilités métier des component Skills qu'il orchestre.

### Principe de composition

```text
Workflow
   ├── invokes → component
   ├── invokes → interactive
   ├── consumes → findings / evidence
   ├── enforces → gates
   └── produces → structured handoff / package
```

### Principe de chargement

Les métadonnées courtes du Skill doivent permettre son routage sans charger toute son instruction. Le contenu détaillé, les références et les exemples sont chargés à l'exécution selon le besoin et le contexte.

Le Skill doit donc séparer :

```text
Metadata
   ↓
Routing
   ↓
Detailed instructions
   ↓
Contextual references
```

### Principe de responsabilité

Chaque Skill doit répondre clairement à la question :

> « Quel résultat précis ce Skill est-il responsable de produire ou de vérifier ? »

Lorsqu'une capacité devient trop large, elle doit être divisée en composantes cohérentes puis éventuellement recomposée par un Workflow.

### Principe evidence-first

Un Skill SPECTRUM ne doit pas transformer une absence d'information en fait inventé.

Lorsqu'un résultat dépend d'une information non établie, le Skill doit produire un finding, un gap ou une demande de contexte selon son contrat, au lieu de compléter silencieusement par hypothèse.

### Principe de traçabilité

Tout résultat significatif doit pouvoir être relié à :

```text
source / context
      ↓
requirement or analyzed object
      ↓
rule
      ↓
skill
      ↓
finding / evidence / decision input
```

### Relation avec Step 2.4

Les contrôles de `rules/` constituent la base normative/produit utilisée par les Skills. Les Skills ne redéfinissent pas les règles ; ils décrivent comment les appliquer dans une analyse observable.

Chaque Skill concret devra déclarer explicitement les règles qu'il utilise.

### Relation avec Step 2.3

Les éléments de `knowledge/` fournissent le vocabulaire, les concepts, les niveaux, les relations et les limites de provenance nécessaires à l'exécution des Skills.

### Relation avec les autres couches

- `workflows/` orchestre les Skills lorsque le Workflow est porté par une couche distincte.
- `agents/` fournit le mécanisme d'exécution.
- `evidence/` porte les éléments probants.
- `decisions/` porte les décisions et leurs justifications.
- `outputs/` porte les artefacts destinés aux consommateurs.
- `evaluation/` vérifie la qualité et le comportement des Skills.
- `governance/` et `policies/` contraignent l'exécution et les claims.

### État de Step 2.5

Cette section définit le modèle de Skills et leur architecture de composition. Elle ne constitue pas encore le catalogue final des Skills dérivés des 17 contrôles ISO.

Avant toute instanciation, le modèle doit être validé contre :

1. couverture des responsabilités
2. composabilité
3. traçabilité Rule → Skill
4. evidence et provenance
5. préconditions / conditions de sortie
6. handoffs
7. évaluation et régression
8. compatibilité multi-agent / multi-plateforme
9. absence de dépendance à une plateforme particulière
10. cohérence avec les artefacts déjà présents dans SPECTRUM
