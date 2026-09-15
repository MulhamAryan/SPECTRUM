# SPECTRUM Skill Relationships

## Step 2.5 — Lifecycle, routing and composition

Ce document définit comment les Skills SPECTRUM se situent dans le cycle d'analyse et comment ils se composent sans créer de dépendance à un agent ou à une plateforme.

## 1. Lifecycle roles

Le rôle d'un Skill indique sa fonction dans le parcours d'analyse. Il ne constitue pas une séquence rigide imposée à tous les tickets.

```text
CONTEXTUALIZATION
      ↓
REQUIREMENT ANALYSIS
      ↓
QUALITY ANALYSIS
      ↓
RELATIONSHIP / TRACEABILITY
      ↓
VERIFICATION / VALIDATION
      ↓
DECISION PREPARATION
```

Les capacités transverses telles que provenance, evidence, risk et governance peuvent intervenir à plusieurs étapes.

## 2. Phase applicability

Un Skill peut être :

- principalement associé à un rôle ;
- applicable à plusieurs rôles ;
- transversal au cycle.

Il ne faut pas forcer un Skill dans une seule phase si cela déforme sa responsabilité.

## 3. Routing model

Le routage d'un Skill repose sur son contexte et son contrat, pas sur son nom seul.

```text
Available context
      ↓
semantic trigger match
      ↓
precondition check
      ↓
skill activation
```

Les métadonnées de routage doivent permettre de déterminer rapidement si le Skill est pertinent sans charger inutilement toutes ses instructions.

## 4. Relationship vocabulary

Les relations de Skill sont orientées lorsque leur direction a un sens :

| Relation | Sens |
|---|---|
| `requires` | le Skill dépend d'un résultat ou contexte préalable |
| `uses` | le Skill consomme une capacité ou ressource sans en orchestrer l'exécution |
| `invokes` | un Skill demande explicitement l'exécution d'un autre Skill |
| `consumes` | le Skill consomme un résultat structuré |
| `feeds` | le résultat est conçu pour alimenter un autre Skill |
| `validates` | le Skill vérifie un résultat ou un artefact produit ailleurs |
| `triggers` | le résultat ou état peut activer une étape suivante |
| `supersedes` | un contrat ou résultat remplace explicitement une version antérieure |

## 5. Composition graph

Le modèle attendu est un graphe de capacités :

```text
                 ┌───────────────┐
                 │   Workflow    │
                 └───────┬───────┘
                         │ invokes
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Component      Interactive    Component
          │              │              │
          └───────┬──────┴───────┬──────┘
                  ↓               ↓
               Findings       Evidence
                  └───────┬───────┘
                          ↓
                   Decision input
```

Un Workflow agrège et ordonne les capacités ; il ne remplace pas leurs contrats individuels.

## 6. Rule reuse

Une même règle peut alimenter plusieurs Skills.

```text
Rule A ──→ Skill 1
       └─→ Skill 2

Rule B ──→ Skill 2
       └─→ Skill 3
```

Cela permet de conserver une seule définition de contrôle dans `rules/` tout en l'appliquant à plusieurs analyses.

## 7. Findings flow

Les findings ne doivent pas être traités comme de simples phrases finales. Ils doivent constituer des objets consommables :

```text
Skill A
  ↓
Finding package
  ├── subject
  ├── rule refs
  ├── evidence refs
  ├── status
  └── implications
  ↓
Skill B / Workflow / Decision Engine
```

## 8. Handoff flow

Lorsque plusieurs Skills coopèrent, le transfert doit être explicite :

```text
producer
   ↓
validate contract
   ↓
structured payload
   ↓
consumer
   ↓
consumer validation
```

Le producteur et le consommateur doivent connaître la version du contrat et la provenance utile au payload.

## 9. Gates

Un Workflow peut appliquer des gates avant de poursuivre :

```text
Skill completed?
      ↓ yes
Required evidence present?
      ↓ yes
Blocking findings absent?
      ↓ yes
Next skill
```

Un gate doit être basé sur des conditions observables et non sur une appréciation vague de la qualité.

## 10. No forced linearity

SPECTRUM n'impose pas que tous les tickets traversent tous les Skills.

Le Workflow sélectionne les capacités pertinentes selon :

- type et complexité de la demande ;
- contexte disponible ;
- niveau d'exigence ;
- risques identifiés ;
- findings déjà produits ;
- besoin de vérification / validation ;
- politique active.

## 11. Dependency direction

Les dépendances doivent aller de préférence vers des contrats plus fondamentaux :

```text
Knowledge / Rules
        ↓
Component Skills
        ↓
Interactive Skills / Workflows
        ↓
Decision / Outputs
```

Un component ne doit pas dépendre d'un workflow supérieur pour comprendre sa propre responsabilité.

## 12. Evaluation graph

Les relations doivent également être testables :

```text
Input fixture
   ↓
Skill
   ↓
Expected finding / evidence behavior
   ↓
Regression check
```

Lorsqu'un Skill alimente un autre Skill, au moins un test d'intégration doit vérifier que son output respecte le contrat attendu.

## 13. Compatibility boundary

Les relations décrites ici sont fonctionnelles. Les mécanismes d'exécution spécifiques à Claude, Codex, Gemini ou une autre plateforme ne font pas partie du graphe métier SPECTRUM.
