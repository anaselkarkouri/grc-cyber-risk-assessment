# Projet 1 - Justificatifs et constats documentaires

**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**

## 1. Règles d'examen

Tous les éléments E01 à E10 ci-dessous sont **SIMULÉS**. Leurs dates appartiennent au scénario, pas à une exécution réelle par Anas.

Chaque conclusion distingue :

- **conception** : le contrôle prévu répond-il au risque et au besoin ?
- **mise en œuvre documentée** : un paramétrage ou une opération est-il décrit ?
- **fonctionnement dans la durée** : une période et des preuves suffisantes existent-elles ?

Les catégories de conclusion sont : satisfait pour la pièce et le périmètre examinés, partiellement satisfait, écart au critère de l'atelier, ou non démontré. Elles ne signifient pas « certifié ISO ».

## 2. Dossier d'entreprise simulé

### E01 - Inventaire initial, 30 septembre 2026

Provenance fictive : fichier du service infrastructure, version initiale. Six lignes décrivent annuaire, serveur de tickets, dépôt Git, sauvegardes, SIEM et documentation. Deux lignes n'ont pas de propriétaire ; les portables, exports, messagerie et SaaS candidat ne figurent pas dans cette version.

Conclusion : inventaire partiel par comparaison avec le périmètre déclaré. L'inventaire proposé de dix actifs est une correction documentaire préparée, encore à valider.

### E02 - État des accès privilégiés, 6 octobre 2026

Provenance fictive : export de configuration de l'annuaire. Population du cas : trois comptes privilégiés pour deux administrateurs.

| Compte fictif | Type | Actif | MFA imposé | Responsable identifié |
|---|---|---|---|---|
| ADM01 | Nominatif | Oui | Oui | Administrateur 1 |
| ADM02 | Nominatif | Oui | Non | Administrateur 2 |
| ADMIN-PARTAGE | Partagé | Oui | Non | Deux utilisateurs, responsabilité ambiguë |

L'export permet de conclure que la configuration simulée ne satisfait pas l'objectif du cas. Il ne démontre pas, pour ADM01, un fonctionnement effectif ou une récupération sûre.

### E03 - Journalisation pilote, 5 octobre 2026

Provenance fictive : fiche de couverture et relevé du tableau de bord Wazuh. Deux sources actives sur six sources déclarées prioritaires. Un échec de connexion est visible pour LAB-WIN-01 à 10 h 02. Une alerte associée est affichée à 10 h 03.

Pas de relevé de conservation, de protection des journaux, d'accès au tableau de bord ou de revue quotidienne.

Conclusion : présence d'un signal dans le relevé simulé. Couverture incomplète et efficacité durable non démontrée. Le temps d'une minute ne constitue pas une mesure de performance de production.

### E04 - Sauvegardes, semaine du 28 septembre au 4 octobre 2026

Provenance fictive : relevé de sept jobs quotidiens du serveur de tickets, chacun marqué réussi. Dernier job annoncé : 4 octobre à 23 h.

Le dossier de restauration contient un état « aucun compte rendu fourni ». Les droits du compte de sauvegarde et l'isolement du stockage ne sont pas documentés.

Conclusion : exécution déclarée de sauvegardes pendant la période. Restaurabilité et objectifs de reprise non démontrés. Ne pas conclure à l'absence de sauvegarde.

### E05 - Revue du dépôt, 6 octobre 2026

Provenance fictive : fiche de revue d'un dépôt privé. La fiche signale un marqueur « SECRET-DEMO-NON-UTILISABLE » dans un fichier de configuration et dans une ancienne version.

L'énoncé stipule qu'un secret exploitable aurait été actif dans ce scénario. Le marqueur représente cette exposition ; **ce n'est pas une vraie clé**. Aucune rotation ou invalidation n'est consignée.

Conclusion : écart du scénario de protection des secrets. La confidentialité d'un dépôt ne protège pas un secret contre tous ses lecteurs ou contre une future divulgation.

### E06 - Chiffrement de postes, 6 octobre 2026

Provenance fictive : trois fiches de configuration prises dans un parc de 40 postes.

| Poste | Chiffrement déclaré | Récupération documentée |
|---|---|---|
| PC01 | Activé | Non fournie |
| PC02 | Activé | Non fournie |
| PC03 | Désactivé | Sans objet à ce stade |

Conclusion : écart explicite sur PC03. Le statut des 37 autres postes et la récupérabilité de PC01/PC02 ne sont pas démontrés.

### E07 - Départ et accès, 7 octobre 2026

Provenance fictive : départ RH effectif le 30 septembre ; compte utilisateur TST-DEPART encore actif le 7 octobre et accès au serveur de tickets conservé.

Conclusion : écart de retrait d'accès dans le cas. La revue ne prétend pas avoir examiné tous les départs historiques.

### E08 - Changement applicatif, 1er octobre 2026

Provenance fictive : fiche de déploiement sur le serveur local de tickets. Champs renseignés : approbation avant production « non », vérification après changement « partielle », retour arrière documenté « non ».

Conclusion : écart explicite du cas. Un ticket sans signature aurait seulement justifié une demande complémentaire ; ici l'énoncé indique directement l'absence d'approbation.

### E09 - Vulnérabilité locale, relevé du 12 septembre 2026

Provenance fictive : fiche de vulnérabilité élevée sur la fonction de recherche de tickets, accès réservé aux utilisateurs authentifiés. Correctif non installé et retest non réalisé au 7 octobre.

Aucune cible réelle ni charge d'exploitation n'est fournie. L'accès restreint est une mesure existante, mais ne supprime pas le risque d'exploitation par un compte compromis.

### E10 - Entretien de contexte, 7 octobre 2026

Provenance fictive : notes du responsable infrastructure et du responsable support.

- Rôles SSI connus oralement ; PSSI approuvée non fournie.
- Méthode préalable, registre de risques et suivi de traitement non fournis.
- Sensibilisation ponctuelle réalisée dans le scénario ; aucune mesure récente de son efficacité.
- Filtrage de base de la messagerie déclaré, non testé.
- Exports de tickets présents ; règles de durée et de partage non formalisées.
- Procédures d'exploitation principalement détenues par un administrateur.
- Procédure de réponse aux incidents et compte rendu d'exercice non fournis.

Conclusion : déclarations utiles au cadrage, avec assurance limitée. Les absences documentaires sont conservées comme informations non démontrées.

## 3. Matrice de constats

| Constat | Critère de l'atelier | Justificatif et examen | Conclusion documentée | Risque et action |
|---|---|---|---|---|
| C01 | Accès privilégiés nominatifs, nécessaires et protégés | E02, lecture des trois comptes | Écart de conception et configuration sur deux comptes ; fonctionnement d'ADM01 non testé | R01, M01, T01 |
| C02 | Sources prioritaires surveillées et journaux exploitables | E03, couverture deux sur six et un relevé | Partiel pour la couverture ; conservation/protection/revue non démontrées | R04, M04, T02 |
| C03 | Sauvegardes restaurables selon les besoins métier | E04, sept jobs, aucun rapport de restauration | Existence déclarée des jobs ; restaurabilité non démontrée | R03, M03, T03 |
| C04 | Secret utilisable absent du dépôt et invalidé après exposition | E05, fiche de revue et historique fictifs | Écart explicite dans le scénario ; aucune clé réelle exposée | R06, M06, T04 |
| C05 | Fin des accès au départ effectif | E07, comparaison date de départ et accès | Écart constaté pour le compte examiné | R07, M07 |
| C06 | Postes transportant des données clients protégés | E06, trois fiches | Écart PC03 ; conclusion limitée à l'échantillon | R11, M11 |
| C07 | Vulnérabilité identifiée suivie et traitée | E09, état de la fiche | Faiblesse ouverte ; aucune validation de correction | R05, M05 |
| C08 | Changement sensible approuvé et retour arrière préparé | E08, fiche explicitement renseignée | Écart sur le changement examiné | R12, M12 |

C03 est une illustration importante : **une preuve de restauration absente ne démontre pas que la sauvegarde n'existe pas ou que la restauration échouera.** Elle empêche d'affirmer la restaurabilité.

## 4. Examen limité des exigences du SMSI

Il s'agit d'une gap analysis pédagogique ciblée, pas d'une évaluation exhaustive des clauses.

| Sujet et repère | Situation du cas | Document proposé | Limite restante |
|---|---|---|---|
| Contexte, parties intéressées et périmètre - 4 | Informations dispersées, inventaire partiel | Document 01 | Validation du métier et interfaces manquantes |
| Politique et responsabilités - 5 | Rôles informels, PSSI approuvée non fournie | PSSI et gouvernance | Approbation et diffusion non réalisées |
| Appréciation et traitement - 6.1.2/6.1.3 | Méthode initiale non fournie | Registre, plan et extrait de SoA | Texte normatif complet à relire ; acceptations non signées |
| Objectifs SSI - 6.2 | Besoins de reprise proposés | Indicateurs de la synthèse | Besoins et ressources à valider |
| Compétences et documents - 7 | Sensibilisation ponctuelle, documentation partielle | Procédures et guide | Historique et gestion documentaire à organiser |
| Exécution du traitement - 8 | Actions encore proposées | Plan M01 à M12 | Preuves d'exécution absentes |
| Évaluation - 9 | Pas de revue exhaustive ni d'audit interne effectué | Matrice et revue proposée | Cette étude ne remplace pas un audit interne indépendant |
| Amélioration - 10 | Pas de suivi formalisé fourni | Suivi et critères de clôture | Actions correctives et efficacité à vérifier |

## 5. Conservation des nouvelles preuves

Pour une preuve réelle, enregistrer : identifiant, date et fuseau, système, propriétaire, origine, périmètre, opérateur, méthode, résultat, limites et lien vers la pièce.

Les captures doivent masquer identifiants sensibles, secrets, données clients et informations privées de tiers. Une pièce masquée doit conserver les informations nécessaires au raisonnement.

Les nouvelles pièces réelles seront nommées T01-P01, T02-P01, etc. Elles ne remplaceront jamais silencieusement les justificatifs E simulés.

## Références

[ISO/IEC 27001](https://www.iso.org/standard/27001), [ISO/IEC 27002](https://www.iso.org/standard/75652.html). Les critères et conclusions sont ceux de l'atelier.
