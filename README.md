# Évaluation des risques cyber et des contrôles SSI

**Étude de cas GRC cyber : PME fictive et tests dans un laboratoire personnel.**

Le dossier relie actifs, scénarios, constats, risques, mesures de sécurité et preuves attendues. Il prépare une décision argumentée : quels risques traiter en priorité, qui en est responsable et comment vérifier la clôture d'une action ?

[Guide de lecture en dix minutes](docs/LECTURE_RAPIDE.md) · [English overview](docs/OVERVIEW_EN.md)

## Résultats et livrables

- **10 actifs et 12 risques**, avec cotations, hypothèses et propriétaires.
- **12 actions de traitement proposées**, responsabilités et critères de clôture.
- Cadrage du SMSI, PSSI, procédures et synthèse direction.
- Extrait de déclaration d'applicabilité (**20 mesures**) et profils actuel/cible **NIST CSF 2.0 sur 13 sous-catégories**.
- Registre Excel avec validations, formules protégées et tableau de bord.
- Tests de laboratoire : Keycloak/habilitations/MFA, rapprochement Windows/Wazuh, restauration et historique Git.

## Parcours de lecture

1. [Contexte, périmètre et actifs](outputs/Portfolio_GRC_Anas/Projet_1_SSI/01_contexte_perimetre_actifs.md).
2. [Méthode et registre des risques](outputs/Portfolio_GRC_Anas/Projet_1_SSI/02_methode_registre_risques.md).
3. [Traitement, contrôles et extrait de SoA](outputs/Portfolio_GRC_Anas/Projet_1_SSI/03_traitement_controles_SoA.md).
4. [Synthèse direction](outputs/Portfolio_GRC_Anas/Projet_1_SSI/08_synthese_direction.md).

[Rapport final PDF](outputs/Projet_1_SSI_rapport_final.pdf) · [Rapport Markdown](outputs/Projet_1_SSI_rapport_final.md) · [Registres Excel](outputs/Registres_GRC_Anas.xlsx)

## Vérifications documentées

| Test | Observation | Portée |
| --- | --- | --- |
| T01 — Keycloak | Habilitations, MFA TOTP et révocation vérifiés | Comptes du laboratoire |
| T02 — Windows/Wazuh | Même événement 4625 rapproché entre source, réception et alerte | Partiel : conservation sur 90 jours non démontrée |
| T03 — Restauration | Trois fichiers restaurés, contenus et SHA-256 identiques | Fichiers testés ; reprise d'un service complet non validée |
| T04 — Historique Git | Marqueur retiré du présent, conservé dans un ancien commit | Marqueur de test, sans secret réel |

[Matrice des preuves](outputs/Portfolio_GRC_Anas/Annexes_laboratoire/MATRICE_PREUVES.md) · [Fiches et exports](outputs/Portfolio_GRC_Anas/Annexes_laboratoire) · [Instructions de reproduction](outputs/scripts_laboratoire/README_REPRODUCTION.md)

La révision du tableur a conservé **28 essais de recalcul et 120 résultats numériques concordants**. La CI contrôle l'intégrité des fichiers ; elle ne rejoue pas les tests techniques.

## Périmètre et limites

Atlas Services et ses pièces E01–E10 sont fictifs. Les tests personnels illustrent la vérification de certaines mesures ; ils ne valident pas les contrôles de cette entreprise simulée. Les actions restent proposées et les cotations cibles sont conditionnelles.

L'extrait de SoA et les profils NIST sont partiels. Les références ISO/IEC 27001, 27002 et 27005 (2022) servent de repères d'apprentissage ; ce cas ne représente pas un SMSI certifié ni un audit professionnel complet. [Sources et portée](outputs/Portfolio_GRC_Anas/SOURCES.md).

**Auteur : Anas El Karkouri.** Dossier préparé avec assistance d'outils IA ; [guide d'appropriation](outputs/Portfolio_GRC_Anas/GUIDE_APPROPRIATION.md).

[Cas complémentaire : risque fournisseur SaaS](https://github.com/anaselkarkouri/grc-saas-vendor-risk-assessment). Les documents communs sont conservés dans les deux dépôts pour maintenir les références croisées.
