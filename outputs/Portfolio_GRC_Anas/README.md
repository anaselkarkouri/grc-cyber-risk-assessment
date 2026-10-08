# Portfolio GRC cyber, audit SSI et risques cyber

**Destinataire : Anas El Karkouri**  
**Version : 1.1 - 07/10/2026**  
**Nature : deux études de cas documentaires simulées et annexes de laboratoire réel distinctes.**

## Les deux projets

1. **Évaluation des risques cyber et des contrôles SSI** : cadrage d'un SMSI, actifs, méthode, douze risques, traitement, évaluation documentaire de contrôles, PSSI, procédures, extrait de déclaration d'applicabilité et profil NIST CSF 2.0.
2. **Évaluation du risque cyber d'un fournisseur SaaS** : criticité, vingt questions et réponses, dossier fournisseur simulé, huit risques, remédiation, décision d'homologation proposée et synthèse en anglais.

L'entreprise « Atlas Services - cas pédagogique » et le fournisseur « SupportCloud - cas pédagogique » sont inventés. Aucun résultat ne concerne une entreprise portant éventuellement un nom similaire. Aucun audit de Tanger Med ou d'Amendis n'est présenté dans ces projets.

## Ce qui est réalisé dans cette version

Les dossiers contiennent des analyses renseignées, des scénarios évalués, des constats motivés et des décisions proposées. Ce ne sont pas uniquement des listes de tâches ou des formulaires vides.

Les documents d'entreprise et de fournisseur utilisés comme justificatifs sont créés pour l'exercice et signalés **SIMULÉS**. Les sources ISO, NIST et CNDP sont réelles. Une annexe examine séparément les éléments techniques décrits dans le rapport de stage Tanger Med fourni par Anas.

**Quatre tests exécutés : T01 Keycloak, T03 restauration de fichiers et T04 historique Git réussis dans leur périmètre ; T02 PARTIEL : source, réception Wazuh et alerte prouvées ; conservation longue durée non démontrée.** Les [annexes réelles](Annexes_laboratoire/MATRICE_PREUVES.md) conservent preuves, diagnostics et retests. H01 reste une observation historique distincte. Aucun test personnel ne clôture un contrôle fictif.

Les PSSI, procédures, décisions et mesures proposées ne sont pas approuvées par une direction réelle. Les niveaux de risque cible restent des estimations conditionnelles. Ce portfolio ne constitue pas un SMSI certifié, un audit de certification ou un certificat professionnel.

## Lecture recommandée

Commencer par les deux synthèses :

- [Synthèse du projet 1](Projet_1_SSI/08_synthese_direction.md)
- [Synthèse du projet 2](Projet_2_TPRM/06_decision_et_synthese_EN.md)

Puis suivre le chemin de preuve :

**Projet 1**

- [Contexte, périmètre et actifs](Projet_1_SSI/01_contexte_perimetre_actifs.md)
- [Méthode et registre des risques](Projet_1_SSI/02_methode_registre_risques.md)
- [Traitement, contrôles et extrait de SoA](Projet_1_SSI/03_traitement_controles_SoA.md)
- [Justificatifs simulés et constats](Projet_1_SSI/04_preuves_et_constats.md)
- [PSSI et procédures](Projet_1_SSI/05_PSSI_procedures.md)
- [Quatre tests manuels et preuve historique](Projet_1_SSI/06_tests_manuels.md)
- [Profil actuel/cible NIST CSF 2.0](Projet_1_SSI/07_profil_NIST_CSF_2.md)

**Projet 2**

- [Périmètre et criticité du fournisseur](Projet_2_TPRM/01_cadrage_criticite.md)
- [Dossier fournisseur simulé](Projet_2_TPRM/02_dossier_fournisseur_simule.md)
- [Questionnaire, réponses et appréciation](Projet_2_TPRM/03_questionnaire_et_reponses.md)
- [Constats et registre des risques fournisseur](Projet_2_TPRM/04_constats_registre_risques.md)
- [Remédiation et suivi du fournisseur](Projet_2_TPRM/05_remediation_suivi.md)

Le [registre des sources](SOURCES.md) précise ce qui a été vérifié et les limites d'accès aux normes. Le [guide d'appropriation](GUIDE_APPROPRIATION.md) décrit le travail personnel nécessaire pour défendre le portfolio en entretien. Le [compte rendu de vérification](VERIFICATION.md) rassemble les contrôles de cohérence et les limites restantes.

## Convention de traçabilité

| Préfixe | Signification |
|---|---|
| A01 à A10 | Actifs de la PME |
| R01 à R12 | Risques du projet 1 |
| M01 à M12 | Actions de traitement du projet 1 |
| E01 à E10 | Justificatifs d'entreprise simulés |
| C01 à C08 | Constats documentaires du projet 1 |
| T01 à T04 | Tests techniques avec résultats réels séparés |
| H01 | Observation documentaire historique du rapport de stage |
| V01 à V09 | Justificatifs fournisseur simulés |
| Q01 à Q20 | Questions fournisseur |
| S01 à S08 | Risques fournisseur |
| F01 à F08 | Constats fournisseur |
| VM01 à VM08 | Actions fournisseur |

Un identifiant reste stable lorsqu'un document est modifié. Chaque modification de vraisemblance, impact, preuve ou décision doit être enregistrée dans l'historique du document concerné.

## Utilisation dans le CV

Cette version permet de décrire **des études de cas documentaires simulées réalisées avec assistance**, une fois le contenu compris et vérifié par Anas.

Le CV final décrit les deux études simulées et les opérations réellement vérifiées : rôles/MFA/sessions Keycloak, événement Windows reçu et alerté dans Wazuh, restauration avec SHA-256 et persistance d’un marqueur Git historique. Il ne revendique pas de conservation prouvée sur 90 jours. Les référentiels restent présentés comme des bases en cours d’apprentissage.

Une formulation immédiatement fidèle au dossier est : « Étude de cas simulée : cadrage SSI, registre de douze risques, plan de traitement, évaluation documentaire de contrôles, extrait de SoA et profil actuel/cible NIST CSF 2.0. »

## Livraison finale et historique

- [Inventaire et modifications](Annexes_laboratoire/INVENTAIRE_LABORATOIRE.md)
- [Fiches T01](Annexes_laboratoire/T01_RESULTATS.md), [T02](Annexes_laboratoire/T02_RESULTATS.md), [T03](Annexes_laboratoire/T03_RESULTATS.md), [T04](Annexes_laboratoire/T04_RESULTATS.md)
- [Matrice des preuves](Annexes_laboratoire/MATRICE_PREUVES.md) et manifestes SHA-256
- [Revue fournisseur finale](Projet_2_TPRM/07_revue_documentaire.md)
- [Notice personnelle et reproduction](NOTICE_PERSONNELLE.md)

Rapports consolidés PDF avec sources Markdown éditables et registre XLSX des risques/suivis livrés à côté du portfolio. Les scripts utiles sont fournis sans les secrets ni les distributions portables. La version documentaire 1.0 a été copiée avant tout changement dans reference_v1_20261007T192733Z. Le CV cible original est préservé.

| Version | Date | Objet |
|---|---|---|
| 1.0 | 7 octobre 2026 | Deux études documentaires ; aucun nouveau test exécuté |
| 1.1 | 07/10/2026 | Trois tests réels validés, T02 partiel, relecture de cohérence, rapports et CV fidèles |
