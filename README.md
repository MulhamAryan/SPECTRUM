# SPECTRUM

SPECTRUM est un plugin d'ingénierie des exigences et d'analyse de préparation au développement pour les tickets logiciels pilotés par des agents IA.

Le projet sépare les connaissances de référence, les règles exécutables, les compétences, les workflows, les agents, les modèles de données, les preuves, la logique de décision, les rapports, l'évaluation et la gouvernance.

## Installer avec la marketplace Claude Code

```text
/plugin marketplace add MulhamAryan/SPECTRUM
/plugin install spectrum@SPECTRUM
```

## Commandes utilisateur

Analyse complète d'un ticket :

```text
/spectrum:analyze-ticket <chemin-du-ticket-ou-texte>
```

Revue ciblée des exigences :

```text
/spectrum:review-requirement <chemin-du-ticket-ou-texte>
```

Revue des tests et de la testabilité :

```text
/spectrum:review-tests <chemin-du-ticket-ou-texte>
```

Revue de l'implémentation contre la spécification :

```text
/spectrum:review-implementation <entrée-spécification-et-artefacts>
```

Comparaison de deux artefacts :

```text
/spectrum:compare-artifacts <artefact-a> <artefact-b>
```

Explication d'un constat :

```text
/spectrum:explain-finding <identifiant-du-constat>
```

Revue des frontières de sécurité et des permissions :

```text
/spectrum:review-security <chemin-du-ticket-ou-texte>
```

## Fonctionnement

La commande d'analyse complète orchestre les compétences et agents spécialisés disponibles, puis consolide les preuves, constats et éléments de décision dans un rapport utilisateur en français.

Les capacités internes couvrent notamment l'analyse des exigences, la vérification et validation, les règles métier, l'analyse adversariale, la comparaison entre artefacts, l'analyse des écarts entre spécification et implémentation, l'analyse indépendante, le raisonnement multi-sources et la préparation au développement.

## Agents

Les agents spécialisés comprennent notamment :

- analyste des exigences ;
- analyste QA ;
- analyste adversarial ;
- revue de l'implémentation ;
- seconde analyse indépendante ;
- composition du rapport.

Un agent est un mécanisme d'exécution spécialisé ; il ne remplace pas une compétence.

## Intégrations

SPECTRUM définit une couche d'intégration pour Jira et GitHub.

Le mode par défaut est la lecture seule. Les données externes sont normalisées en conservant leur identité, leur version, leur provenance et leur incertitude.

Aucune écriture Jira ou GitHub n'est effectuée automatiquement. Toute écriture doit être explicitement autorisée dans l'interaction courante, cibler précisément l'opération et la cible, puis être vérifiée après exécution.

Les contrats sont disponibles dans `integrations/`.

## Structure du dépôt

- `core/` — fondations d'orchestration
- `knowledge/` — connaissances de référence
- `rules/` — règles et contrôles
- `skills/` — compétences réutilisables
- `workflows/` — workflows d'analyse
- `agents/` — agents spécialisés
- `models/` — modèles de données
- `evidence/` — preuves et traçabilité
- `decisions/` — logique de décision
- `outputs/` — contrats et formats de rapport
- `evaluation/` — évaluations et cas de test
- `governance/` — gouvernance et provenance
- `policies/` — politiques configurables
- `integrations/` — contrats d'intégration externes

## Sécurité

SPECTRUM est conçu pour analyser sans mutation par défaut. L'analyse, un constat, un verdict, un plan d'action, un cas de test ou une revue QA ne constitue jamais une autorisation d'écriture.

## Intégrations d'agents

SPECTRUM reste aussi agnostique que possible vis-à-vis de la plateforme d'agent.

- Claude Code : `.claude-plugin/`
- Interopérabilité Agent Skills : `.agents/`
- Gemini CLI : `gemini-extension.json` et `.gemini/`
