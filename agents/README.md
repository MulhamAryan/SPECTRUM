# Agents

Définitions des agents spécialisés SPECTRUM, invoqués par l'orchestrateur (la commande slash, dans la conversation principale) via `Task`.

Il n'y a **pas** d'agent superviseur : un sous-agent Claude Code ne peut pas en lancer d'autres. La procédure d'orchestration est dans `core/orchestration-procedure.md` et le graphe dans `workflows/ticket-analysis.yaml`.

Chaque agent charge `core/agent-brief.md` (règles + format de retour) puis ses Skills autorisés, et retourne un bloc YAML conforme à `models/agent-execution-result.schema.json`.

Un agent est un mécanisme d'exécution ; il ne remplace pas un Skill.

| Agent | Stages | Rôle |
|---|---|---|
| context-analyst | contextualize, represent_requirements | Contexte, entités, contraintes, représentation des exigences |
| requirement-analyst | analyze_requirements | Qualité des exigences individuelles et d'ensemble |
| verification-validation-analyst | analyze_verification_validation | Base de vérification et de validation |
| lifecycle-change-analyst | analyze_lifecycle_change | Baselines, changements, attributs de cycle de vie |
| business-rule-analyst | analyze_business_rules | Règles métier explicites |
| adversarial-analyst | analyze_adversarial_requirements | Défis, cas limites, échecs |
| consistency-analyst | analyze_cross_artifacts | Cohérence inter-artefacts (conditionnel) |
| implementation-reviewer | analyze_spec_implementation_drift | Écarts spec/implémentation (conditionnel) |
| independent-reviewer | analyze_independent | Seconde analyse isolée (profil full) |
| qa-analyst | qa | Testabilité et cas de test à partir des résultats amont |
| report-composer | compose_report | Rendu du rapport utilisateur |
