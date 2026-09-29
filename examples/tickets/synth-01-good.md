<!-- SYNTHÉTIQUE — exemple de ticket bien spécifié. À remplacer par un ticket réel anonymisé. -->
# PROJ-101 — Export CSV de la liste des factures filtrée

## Contexte
Les comptables exportent aujourd'hui la liste des factures manuellement depuis l'écran « Factures » (copier-coller). Le module Factures existe (v2.3) et la liste supporte déjà les filtres statut, client et période.

## Exigence
L'écran « Factures » doit proposer un bouton « Exporter en CSV » qui exporte **les lignes actuellement affichées après application des filtres actifs**, dans un fichier `factures_<AAAA-MM-JJ>.csv` encodé UTF-8 avec séparateur `;`.

## Colonnes exportées (dans cet ordre)
Numéro, Date d'émission, Client (raison sociale), Montant HT, TVA, Montant TTC, Statut, Date d'échéance.

## Règles
- Les montants sont exportés avec deux décimales et le séparateur décimal `,` (convention comptable belge).
- Une liste vide produit un fichier contenant uniquement l'en-tête.
- Le bouton est visible uniquement pour les rôles `comptable` et `admin` (rôles existants, voir module Auth).
- Limite : 10 000 lignes par export ; au-delà, message « Affinez vos filtres (max. 10 000 lignes) » et pas de fichier.

## Hors périmètre
Export Excel, planification d'exports récurrents, export des lignes de détail des factures.

## Critères d'acceptation
1. Avec filtre statut = « Payée » et période = mars 2026, le fichier contient exactement les lignes affichées et l'en-tête.
2. Un utilisateur avec le rôle `vendeur` ne voit pas le bouton.
3. Un export de 10 001 lignes affiche le message et ne télécharge rien.
4. Le fichier s'ouvre correctement dans Excel FR sans corruption des accents.

## Dépendances
Aucune nouvelle. Utilise le service `InvoiceQueryService` existant.
