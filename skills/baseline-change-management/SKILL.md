---
name: baseline-change-management
description: Analyser et préserver la baseline, les changements et les états de besoins/exigences à partir d'informations de cycle de vie explicitement établies, sans inventer de processus de changement.
type: component
role: lifecycle_management
---

# Baseline Change Management

## Purpose

Analyser la maîtrise de l'état courant d'un besoin, d'une exigence ou d'un ensemble lorsqu'une baseline, une proposition de changement, une version, une date, un statut ou une information de gouvernance est fournie.

Ce Skill est une capacité SPECTRUM. INCOSE ne définit pas un Skill portant ce nom ni les statuts SPECTRUM utilisés ici.

## Source boundary

Sources autorisées :

- INCOSE Guide to Writing Requirements v4, `INCOSE-TP-2010-006-04`.
- INCOSE GtWR v4 Summary Sheet, en particulier page 7 pour l'inventaire des attributs.
- NRM uniquement lorsque la définition détaillée d'un attribut ou d'une activité n'est pas exposée dans le Summary Sheet et qu'une source officielle autorisée est disponible.
- Représentations contrôlées locales du corpus INCOSE.

Le Summary Sheet identifie notamment les attributs liés à la gestion du cycle de vie : A15–A25, A26–A40. Les définitions sémantiques détaillées de ces attributs appartiennent au NRM et ne sont pas reconstruites ici.

Les activités NRM explicitement utilisées comme points d'ancrage sont :

- `6.3 Baseline and Manage Design Input Requirements` ;
- `14.2.1 Baseline Needs, Requirements, and Specifications`.

La matrice officielle relie `6.3` et `14.2.1` à plusieurs caractéristiques C1, C3, C4, C6, C8, C10, C11, C12, C13, C14 et C15. Ces relations sont des faits source ; le regroupement en Skill est une décision SPECTRUM.

## When to use

Utiliser lorsque l'analyse doit déterminer si l'état de référence d'un besoin, d'une exigence ou d'un ensemble est identifiable et si les informations fournies permettent de comprendre son évolution ou son statut.

Utiliser notamment lorsque les éléments suivants sont présents ou pertinents : identifiant, auteur, propriétaire, version, dates, proposition de changement, approbation, stabilité, statut, priorité, criticité, risque, ou état d'implémentation.

Ne pas utiliser ce Skill pour inventer une procédure de Change Control, imposer un outil, ou déclarer qu'une organisation doit posséder un Change Board absent des exigences du projet.

## Inputs

Required:

- `target`

Recommended:

- `baseline_reference`
- `attribute_inventory`
- `change_record`
- `version_history`
- `approval_evidence`
- `project_change_policy`
- `owner_and_authority_evidence`
- `status_evidence`
- `impact_analysis`
- `traceability_evidence`
- `requirement_set`
- `prior_findings`

## Preconditions

1. La cible et son identifiant sont connus ou explicitement absents.
2. La frontière d'évidence est connue.
3. Toute obligation de gouvernance projet est distinguée de l'inventaire INCOSE.
4. Un état ou une version ne doit pas être déclaré incohérent sans une seconde preuve comparable.
5. Une absence d'attribut ne devient pas une non-conformité sans base d'applicabilité.

## Procedure

### 1. Preserve the target record

Conserver la cible, son identifiant, sa version et la référence de baseline lorsqu'elles sont fournies.

### 2. Identify the baseline

Déterminer si une baseline explicite, une version approuvée, une référence de configuration ou un autre état de référence est fourni.

Si aucune baseline n'est identifiable, ne pas en inventer une.

### 3. Identify lifecycle attributes

Rechercher, lorsqu'ils sont applicables, les attributs suivants depuis l'inventaire officiel :

- A15 Unique Identifier ;
- A16 Unique Name ;
- A17 Originator/Author ;
- A18 Date Requirement Entered ;
- A19 Owner ;
- A20 Stakeholders ;
- A21 Change Board ;
- A22 Change Proposed ;
- A23 Version Number ;
- A24 Approval Date ;
- A25 Date of Last Change ;
- A26 Stability/Volatility ;
- A27 Responsible Person ;
- A28 Need or Requirement Verification Status ;
- A29 Need or Requirement Validation Status ;
- A30 Status of the Need or Requirement ;
- A31 Status (of Implementation) ;
- A34 Priority ;
- A35 Criticality or Essentiality ;
- A36 Risk (of Implementation) ;
- A37 Risk (Mitigation) ;
- A38 Key Driving Need or Requirement ;
- A39 Additional Comments ;
- A40 Type/Category.

Ces noms sont des éléments de l'inventaire officiel. Leur présence dans un projet, leur valeur et leur obligation sont des sujets séparés.

### 4. Establish change identity

Lorsqu'un changement est signalé, établir avec les preuves disponibles :

`target → current baseline/version → proposed change → authority/evidence → resulting state`

Ne pas créer de transition d'état qui n'est pas fournie ou supportée par le projet.

### 5. Compare versions and states

Comparer uniquement des versions, dates ou états qui sont objectivement reliés.

Détecter notamment :

- version incohérente avec l'historique fourni ;
- date de changement antérieure à l'entrée de l'exigence lorsque les deux données sont comparables ;
- statut incompatible avec une preuve d'approbation ou de retrait ;
- changement annoncé mais sans cible identifiable ;
- état d'implémentation confondu avec statut de l'exigence ;
- propriétaire/auteur/responsable incohérent avec la politique projet explicite.

### 6. Assess approval and authority evidence

Lorsque le projet définit une autorité d'approbation ou de changement, vérifier que la preuve fournie correspond à cette autorité.

Ne pas déduire qu'une approbation existe parce qu'une date ou un statut apparaît.

### 7. Preserve change impact

Lorsqu'un changement est établi, conserver les références vers son impact sur :

- contenu du besoin/exigence ;
- relations de traçabilité ;
- vérification ;
- validation ;
- risque ;
- sets affectés.

L'analyse détaillée de ces effets reste dans les Skills spécialisés.

### 8. Correlate with official baseline activities

Utiliser les activités NRM suivantes comme ancrages source :

- `6.3 Baseline and Manage Design Input Requirements` ;
- `14.2.1 Baseline Needs, Requirements, and Specifications`.

La matrice officielle associe ces activités à des caractéristiques de qualité, mais ne définit pas le workflow SPECTRUM de Change Control.

### 9. Preserve uncertainty

Retourner une incertitude lorsque la baseline, l'historique, l'autorité ou la politique applicable ne peut pas être établie.

## Analysis logic

Séquence :

`target → baseline → lifecycle attributes → change evidence → authority/status → version/state consistency → downstream impacts`

La question est : « l'état et l'évolution déclarés de cet objet sont-ils suffisamment établis pour être interprétés de façon fiable ? »

Ce Skill ne prétend pas que le Summary Sheet définit à lui seul un processus organisationnel complet de gestion des changements.

## Decision semantics

- `baseline_state_established`: baseline et informations d'état applicables suffisamment établies.
- `baseline_state_partial`: une partie de l'état est établie, mais des éléments importants restent non supportés.
- `baseline_state_missing`: la référence d'état essentielle n'est pas établie.
- `change_state_conflicting`: des versions, états, dates ou autorités se contredisent.
- `change_context_missing`: l'applicabilité, l'autorité ou la politique nécessaire ne peut pas être établie.
- `not_applicable`: aucune analyse de baseline/changement n'est applicable au périmètre déclaré.

Ces statuts sont des statuts analytiques SPECTRUM.

## Findings

- `baseline_reference_missing`
- `baseline_identity_missing`
- `version_history_inconsistent`
- `change_target_missing`
- `change_authority_missing`
- `approval_evidence_missing`
- `approval_authority_mismatch`
- `change_proposal_missing`
- `change_date_inconsistent`
- `requirement_status_inconsistent`
- `implementation_status_confusion`
- `owner_authority_inconsistent`
- `baseline_evidence_partial`
- `change_impact_untraced`
- `change_context_missing`

## Evidence

Conserver :

- objet exact ;
- baseline/version ;
- historique lorsqu'il existe ;
- proposition de changement ;
- autorité et preuve d'approbation ;
- statut et état d'implémentation séparément ;
- politique projet applicable ;
- impacts et liens de traçabilité ;
- référence INCOSE utilisée.

## Handoff

- `requirements-attribute-management` pour l'inventaire et la provenance des attributs ;
- `requirement-relationship-traceability` pour les impacts et relations affectés ;
- `requirement-statement-quality` pour les changements de formulation ;
- `verification-analysis` pour les effets sur la vérification ;
- `validation-analysis` pour les effets sur la validation ;
- futur Workflow de décision et gouvernance pour l'application opérationnelle du Change Control.

## Output

Produire `baseline_change_observation` contenant au minimum :

- `target_ref`
- `baseline_ref`
- `current_version`
- `change_ref`
- `lifecycle_attributes`
- `state_observation`
- `authority_evidence`
- `evidence_refs`
- `findings`
- `downstream_impacts`
- `status`

## Exit conditions

- `completed`
- `completed_with_findings`
- `completed_with_gaps`
- `blocked_on_change_context`
- `not_applicable`

## Non-goals

- ne pas inventer un workflow de Change Control ;
- ne pas rendre A15–A49 universellement obligatoires ;
- ne pas confondre statut d'une exigence et statut de son implémentation ;
- ne pas inférer une approbation ;
- ne pas inventer une version ou une baseline ;
- ne pas conclure READY/NOT READY ;
- ne pas déclarer une certification INCOSE ;
- ne pas remplacer les analyses de traçabilité, vérification ou validation ;
- ne pas reconstruire les définitions détaillées du NRM sans source officielle autorisée.

## Référence

Critères d'évaluation et sources détaillées : `REFERENCE.md` dans ce dossier (non chargé à l'exécution).
