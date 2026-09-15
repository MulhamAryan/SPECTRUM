# SPECTRUM Skill Contract

## Step 2.5 — Contract of a Skill

Ce document définit le contrat fonctionnel commun des Skills SPECTRUM. Il sert de référence de conception avant la création des Skills concrets.

## 1. Identité

Chaque Skill possède un identifiant stable et un nom lisible.

Le nom doit exprimer la capacité couverte, sans incorporer le nom d'un agent, d'un fournisseur ou d'une plateforme.

## 2. Type

Chaque Skill est de type :

- `component` — capacité spécialisée et réutilisable.
- `interactive` — capacité qui réduit une incertitude ou sélectionne une voie d'analyse.
- `workflow` — capacité qui orchestre d'autres Skills et leurs transitions.

Le type est un attribut architectural SPECTRUM ; il ne provient pas d'ISO/IEC/IEEE 29148 comme vocabulaire normatif de Skills.

## 3. Rôle dans le cycle

Un Skill déclare son rôle dans le cycle d'analyse SPECTRUM. Le rôle indique où la capacité est utile ; il ne définit pas nécessairement une séquence obligatoire.

Les rôles doivent permettre de distinguer au minimum :

- contextualisation et découverte
- analyse des exigences
- analyse de qualité
- analyse des relations et niveaux
- vérification / validation
- evidence / traçabilité
- préparation à la décision
- capacités transverses

Ces catégories pourront être raffinées lors de l'instanciation des Skills sans remettre en cause le contrat commun.

## 4. Routage

Le frontmatter doit permettre à un orchestrateur de déterminer rapidement quand activer un Skill.

Champs conceptuels :

```yaml
name: stable-skill-id
description: use-when description
intent: detailed purpose
type: component|interactive|workflow
role: lifecycle-role
triggers:
  - semantic trigger
best_for:
  - primary scenario
```

Le routage doit rester indépendant de la plateforme d'agent.

## 5. Objectif et responsabilité

Le Skill doit définir :

- son objectif ;
- sa responsabilité principale ;
- ce qui est explicitement hors périmètre.

Un Skill ne doit pas silencieusement absorber la responsabilité d'un autre Skill.

## 6. Entrées

Chaque Skill déclare les entrées nécessaires et distingue :

- données obligatoires ;
- données optionnelles ;
- contexte recherché ;
- contexte absent mais tolérable.

Exemples d'entrées :

```text
Ticket
Requirements
Source references
Project context
Repository evidence
Prior findings
Prior decisions
```

## 7. Contexte requis

Le Skill doit indiquer quelles informations doivent être établies avant son exécution et quelles sources sont autorisées pour les obtenir.

Il ne doit pas considérer une information comme fiable uniquement parce qu'elle apparaît dans une source non corroborée lorsque le contexte exige une confirmation.

## 8. Préconditions

Une exécution peut être refusée ou différée lorsque des préconditions essentielles ne sont pas satisfaites.

Exemples :

```text
required input exists
required source is accessible
requirement has an identifiable target
prior analysis package is valid
```

Une précondition échouée doit produire un résultat structuré, pas une complétion silencieuse.

## 9. Opérations

Le Skill décrit les opérations qu'il est responsable d'effectuer.

Une opération doit être suffisamment délimitée pour être vérifiable et pour que son résultat puisse être identifié séparément.

Forme recommandée :

```text
Operation
  input
  condition
  analysis
  result
```

Les opérations complexes peuvent être réparties en plusieurs component Skills et orchestrées par un workflow.

## 10. Règles utilisées

Chaque Skill concret doit déclarer ses références vers les règles de `rules/` :

```yaml
rule_refs:
  - ISO29148-Rxxx
```

Le Skill applique la règle ; il ne la redéfinit pas.

Une règle peut être utilisée par plusieurs Skills.

## 11. Sorties

Les sorties doivent être structurées et nommables.

Un Skill peut produire :

- findings ;
- evidence links ;
- requirement attributes ;
- gaps ;
- relationship records ;
- verification / validation observations ;
- structured handoff ;
- workflow state ;
- decision inputs.

Le texte explicatif peut accompagner ces objets, mais ne doit pas être l'unique représentation d'un résultat qui sera consommé par un autre composant.

## 12. Findings

Un finding doit identifier au minimum :

```text
finding_id
subject
rule_ref(s)
status
observation
impact or implication
required evidence or missing context
```

Le finding décrit ce qui est observé ; il ne doit pas masquer une hypothèse comme un fait.

## 13. Evidence

Quand un Skill avance une conclusion vérifiable, il doit pouvoir pointer vers les éléments de preuve disponibles.

Une evidence doit conserver au minimum :

```text
source
location / reference
supporting excerpt or observation
retrieval / revision information when available
```

L'absence d'evidence ne doit pas être comblée par invention.

## 14. Relations et dépendances

Un Skill peut déclarer :

```text
requires
uses
invokes
consumes
feeds
validates
triggers
supersedes
```

Les relations doivent être orientées et explicites lorsque leur direction importe.

## 15. Handoffs

Lorsqu'un résultat est destiné à un autre Skill ou à un Workflow, il doit utiliser un contrat de handoff explicite.

Un handoff doit pouvoir identifier :

```text
kind
schema/version
producer
payload
source references
rule references
provenance
validation state
```

Le consommateur reste responsable de valider le payload selon son contrat ; il ne doit pas considérer un handoff comme fiable uniquement parce qu'il a été produit par un autre Skill.

## 16. Conditions de sortie

Un Skill doit définir ses conditions de sortie.

Exemples :

```text
completed
completed_with_gaps
blocked_on_missing_context
not_applicable
requires_follow_up
```

Ces états sont des états d'exécution du Skill. Ils ne constituent pas directement les décisions produit finales telles que `READY` ou `NOT READY`.

## 17. Non-objectifs

Chaque Skill doit préciser ce qu'il ne fait pas.

Exemples :

```text
does not invent missing requirements
does not approve requirements
does not make implementation decisions
does not claim formal standards conformance
```

## 18. Références et chargement contextuel

Les références spécialisées ne doivent pas être dupliquées intégralement dans chaque Skill.

Un Skill peut référencer :

```text
shared knowledge
specific source knowledge
rule definitions
examples
templates
schemas
```

Le chargement détaillé doit être contextuel lorsque cela réduit le bruit et évite de rendre chaque Skill monolithique.

## 19. Évaluation

Tout Skill concret doit avoir une stratégie d'évaluation couvrant au minimum :

- cas nominal ;
- cas de manque de contexte ;
- cas contradictoire lorsque pertinent ;
- cas de non-applicabilité ;
- respect des règles ;
- qualité des findings ;
- traçabilité vers evidence ;
- respect des conditions de sortie.

Les tests de régression doivent être réexécutables lorsque le Skill évolue.

## 20. Compatibilité multi-agent

Le contrat doit être portable entre mécanismes d'exécution.

Les conventions d'interface utilisateur propres à un agent doivent rester hors du contrat métier lorsque possible.

## 21. Invariant de non-invention

Un Skill ne doit jamais transformer une inconnue en valeur factuelle sans evidence suffisante.

La réponse attendue face à une lacune est une observation structurée : gap, blocked state, uncertainty, request for context, ou équivalent défini par le contrat.
