# Évaluation des risques cyber et des contrôles SSI

Portfolio GRC cyber — étude de cas documentaire et laboratoire technique.

Dix actifs, douze risques évalués et douze mesures de traitement proposées. Le dossier relie contexte, justificatifs, constats, risques, contrôles et actions pour préparer une décision de sécurité argumentée.

## Livrables

- Cadrage du SMSI et inventaire des actifs.
- Méthode de cotation vraisemblance × impact, registre des risques et priorisation.
- Évaluation documentaire de contrôles, extrait de déclaration d’applicabilité et plan de traitement.
- PSSI, procédures et synthèse destinée à la direction.
- Profil actuel/cible NIST CSF 2.0 sur treize sous-catégories.
- Registre Excel avec validation des saisies, formules protégées et tableau de bord.
- Annexes techniques : Keycloak/MFA, collecte et alerte Wazuh, restauration et historique Git.

## Lire le dossier

- [Guide de lecture en dix minutes : démarche, résultats, limites et entretien](docs/LECTURE_RAPIDE.md)
- [Rapport final — 51 pages](outputs/Projet_1_SSI_rapport_final.pdf)
- [Rapport Markdown](outputs/Projet_1_SSI_rapport_final.md)
- [Synthèse direction](outputs/Portfolio_GRC_Anas/Projet_1_SSI/08_synthese_direction.md)
- [Dossier SSI détaillé](outputs/Portfolio_GRC_Anas/Projet_1_SSI)

## Références et vérifications

Repères ISO/IEC 27001, 27002 et 27005 (2022), NIST CSF 2.0 et gestion du risque fournisseur. [Sources et portée](outputs/Portfolio_GRC_Anas/SOURCES.md).

Le tableur courant a passé 28 essais de recalcul, avec 120 résultats numériques concordants lors de la révision. Les essais du laboratoire sont séparés des conclusions documentaires : T01 Keycloak/MFA, T03 restauration et T04 historique Git réussis dans leur périmètre ; T02 établit un événement Windows 4625, sa réception et son alerte Wazuh.

- [Registres Excel des deux cas](outputs/Registres_GRC_Anas.xlsx)
- [Matrice des preuves](outputs/Portfolio_GRC_Anas/Annexes_laboratoire/MATRICE_PREUVES.md)
- [Fiches de tests et exports](outputs/Portfolio_GRC_Anas/Annexes_laboratoire)
- [Scripts et instructions de reproduction Windows](outputs/scripts_laboratoire/README_REPRODUCTION.md)

Les organisations « Atlas Services » et « SupportCloud », ainsi que leurs pièces E/V, sont des scénarios pédagogiques fictifs. Les tests techniques concernent un laboratoire personnel ; les objectifs cibles sont conditionnels. Le portfolio est une étude de cas, sans attribution de certification ISO. Les rapports et les pièces publiques sont fournis dans leur version documentaire révisée ; les secrets, le CV, les machines virtuelles et les exports privés ne font pas partie du dépôt.

Auteur du portfolio : **Anas El Karkouri**. Analyse et préparation réalisées avec assistance d’outils IA, revue et appropriation du dossier à suivre selon le [guide](outputs/Portfolio_GRC_Anas/GUIDE_APPROPRIATION.md).

[Projet complémentaire](https://github.com/anaselkarkouri/grc-saas-vendor-risk-assessment). Les documents communs sont conservés dans les deux dépôts pour maintenir leurs références croisées.
