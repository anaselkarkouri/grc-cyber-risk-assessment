# Projet 1 - Traitement, mesures et extrait de SoA

**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**

## 1. Plan de traitement proposé

J correspond au 7 octobre 2026. Les délais sont des jours calendaires et des objectifs locaux. Toutes les actions sont **proposées, non réalisées**. Le coût n'est pas inventé : les pilotes doivent l'estimer avant arbitrage.

| Action | Risque | Mesure proposée | Pilote | Délai cible | Critère de clôture |
|---|---|---|---|---|---|
| M01 | R01 | Retirer l'accès partagé, limiter les droits, imposer le MFA privilégié et contrôler la récupération | RI | J+2, 9 octobre | Export de tous les comptes privilégiés, exceptions approuvées, essais positifs/négatifs et retrait des sessions |
| M02 | R02 | Compléter protection des accès et de la messagerie, sensibilisation adaptée au phishing | RI et RS | J+30, 6 novembre | Configurations et exercice documentés, accès revus, canal d'alerte connu |
| M03 | R03 | Protéger les sauvegardes, séparer les accès et réaliser une restauration de contrôle | RI | Mesure conservatoire J+2 ; preuve complète J+15, 22 octobre | Test isolé, intégrité, RTO/RPO validés et procédure répétable |
| M04 | R04 | Étendre les sources prioritaires, définir alerte, revue, conservation et protection des journaux | RI | J+30, 6 novembre | Inventaire des sources, réception et alerte testées, revue et contrôle des accès |
| M05 | R05 | Réduire l'exposition de la fonction vulnérable, corriger et faire valider le correctif | RD | Restriction J+2 ; correction J+10, 17 octobre | Preuve de correction et retest autorisé, sans vulnérabilité ouverte équivalente |
| M06 | R06 | Invalider le secret exposé dans le scénario, effectuer la rotation et contrôler le dépôt et son historique | RD | J+1, 8 octobre | Ancien secret inutilisable, nouveau secret stocké hors dépôt, revue documentée des chemins concernés |
| M07 | R07 | Désactiver l'accès de départ et formaliser le retrait de comptes, sessions et jetons | RI et RH | Cas ouvert J+1 ; processus J+15 | Preuve de retrait de l'accès et fiche de sortie complète |
| M08 | R08 | Maintenir le SaaS hors production et exiger la clôture du défaut inter-clients et des blocages fournisseur | RS | Avant toute donnée réelle | Décision fondée sur preuves et critères du projet 2, sans acceptation par simple courriel commercial |
| M09 | R09 | Limiter exports et accès, fixer une durée justifiée et une suppression contrôlée | RS | J+30, 6 novembre | Inventaire des exports, habilitations et exemple de suppression |
| M10 | R10 | Désigner un suppléant et exercer une procédure de reprise documentaire | RI | J+60, 6 décembre | Exercice effectué par le suppléant et limites relevées |
| M11 | R11 | Chiffrer le poste concerné, conserver la récupération en lieu contrôlé et examiner les autres postes | RI | Poste ouvert J+2 ; inventaire J+15 | État du volume et récupération contrôlée, couverture documentée |
| M12 | R12 | Mettre en place approbation, vérification et retour arrière pour les changements sensibles | RD | J+30, 6 novembre | Dossier d'un changement complet, approbation indépendante et vérification du retour arrière |

La suppression d'un secret dans la dernière version d'un fichier ne clôture pas M06 si le secret reste utilisable ou présent dans l'historique. La réussite d'un job ne clôture pas M03. La simple activation d'un agent ne clôture pas M04.

## 2. Sélection des mesures

Les mesures répondent aux risques identifiés, aux critères métier et aux besoins de gouvernance. ISO/IEC 27002 sert de guide. D'autres mesures peuvent être nécessaires dans un SMSI complet.

| Groupe | Risques principaux | Repères ISO/IEC 27001 annexe A / ISO/IEC 27002 | Application concrète retenue |
|---|---|---|---|
| Gouvernance | Tous | 5.1, 5.2, 5.9 | PSSI, rôles, actifs et décisions |
| Identités et secrets | R01, R06, R07 | 5.17, 5.18, 8.2, 8.4, 8.5 | Comptes nominatifs, MFA, droits, secret hors dépôt et retrait des accès |
| Fournisseur et cloud | R08 | 5.19, 5.20, 5.22, 5.23 | Diligence, contrat, décision, suivi et sortie |
| Sensibilisation et incident | R02, R04, R10 | 6.3, 5.24 | Consignes, signalement, responsabilités et exercice |
| Robustesse technique | R03, R05, R11, R12 | 8.8, 8.13, 8.24, 8.32 | Correctifs, restauration, chiffrement et changements |
| Visibilité | R04 | 8.15, 8.16 | Collecte, protection, revue et réponse aux signaux |

## 3. Extrait de déclaration d'applicabilité

**SoA signifie Statement of Applicability, ou déclaration d'applicabilité.**

L'extrait comporte vingt repères sélectionnés. Les thèmes sont reformulés pour le cas et ne reproduisent pas les libellés normatifs. « Retenue » signifie sélectionnée pour le traitement et la gouvernance du cas. « Partielle » décrit la mise en œuvre déclarée dans les documents simulés, pas une conformité à la norme.

Le travail complet doit comparer les mesures nécessaires avec l'ensemble de l'annexe A pour vérifier qu'aucune mesure nécessaire n'a été oubliée. La SoA doit documenter les mesures retenues, leur justification, leur état de mise en œuvre et les justifications d'exclusion des mesures de référence ; des mesures supplémentaires peuvent être nécessaires. **Aucune exclusion de l'annexe A n'est prononcée dans cet extrait.**

| Repère | Thème adapté au cas | Retenue et justification | État actuel du cas | Pièce ou action | Responsable |
|---|---|---|---|---|---|
| 5.1 | Politique SSI | Oui : règles et arbitrages communs | Non démontré, document approuvé absent du dossier | E10, PSSI proposée | DG |
| 5.2 | Attribution des responsabilités | Oui : propriétaires et validation | Partielle, rôles informels | E10, contexte et revue | DG |
| 5.9 | Inventaire et propriétaires des actifs | Oui : dépendances et criticité | Partiel | E01, inventaire proposé | RI |
| 5.17 | Protection des informations d'authentification | Oui : R01/R06 | Insuffisante dans le scénario de secret | E05, M06 | RD |
| 5.18 | Cycle de vie des habilitations | Oui : R01/R07 | Partiel, retrait de départ défaillant | E02/E07, M01/M07 | RI |
| 5.19 | Risques liés aux fournisseurs | Oui : R08 | Diligence préparée, décision encore ouverte | Projet 2, M08 | RS |
| 5.20 | Exigences de sécurité contractuelles | Oui : incident, données et sortie | Non démontré pour le contrat final | V08, projet 2 | RS et RJ |
| 5.22 | Revue de la sécurité fournisseur | Oui : changements et engagements | À organiser | Projet 2, calendrier de suivi | RS |
| 5.23 | Usage et sortie du cloud | Oui : A08 et dépendance | Pilote seulement | V01/V08, projet 2 | RS |
| 5.24 | Préparation de réponse aux incidents | Oui : escalade et coordination | Non démontrée | E10, procédure proposée | RSSI |
| 6.3 | Sensibilisation et apprentissage SSI | Oui : R02 | Ponctuelle | E10, M02 | RS |
| 8.2 | Accès privilégiés | Oui : R01 | Partiel, compte partagé | E02, M01 | RI |
| 8.4 | Accès au code | Oui : R06/R12 | Dépôt privé déclaré, revue des droits non démontrée | E05, M06/M12 | RD |
| 8.5 | Authentification sûre | Oui : R01/R02 | MFA incomplet | E02, M01 | RI |
| 8.8 | Gestion des faiblesses techniques | Oui : R05 | Faiblesse ouverte | E09, M05 | RD |
| 8.13 | Sauvegardes et restaurabilité | Oui : R03 | Jobs présents, restauration non démontrée | E04, M03 | RI |
| 8.15 | Production et protection des journaux | Oui : R04 | Partielle | E03, M04 | RI |
| 8.16 | Surveillance et examen des signaux | Oui : R04 | Signal pilote, examen régulier non démontré | E03, M04 | RI |
| 8.24 | Chiffrement adapté aux données | Oui : R11 et confidentialité | Partiel sur l'échantillon | E06, M11 | RI |
| 8.32 | Maîtrise des changements | Oui : R12 | Écart explicite dans le cas | E08, M12 | RD |

## 4. Exemple de décision de traitement

**R01 - décision proposée**

La direction fictive reçoit un risque actuel estimé à 20. Le traitement M01 est prioritaire. Tant que le MFA n'est pas imposé et vérifié, un score cible de 5 ne peut pas être repris comme score actuel.

Si un accès de secours est maintenu, le dossier doit justifier sa nécessité, son stockage, les accès autorisés, la surveillance, les conditions d'utilisation et la revue. « MFA sur tous les comptes sauf le compte de secours » ne constitue pas une exception suffisamment examinée.

## 5. Validation et preuve

Le pilote fournit le justificatif. Le RSSI vérifie sa pertinence, la population, la date, le périmètre et le résultat. Le propriétaire réévalue le risque. L'autorité prévue approuve le traitement ou l'acceptation.

Statuts possibles : proposée, planifiée, en cours, preuve reçue, vérifiée, acceptation approuvée, close. Une action ne passe pas directement de proposée à close.

## Références

[ISO/IEC 27001](https://www.iso.org/standard/27001), [ISO/IEC 27002](https://www.iso.org/standard/75652.html). Les mesures et critères de clôture sont adaptés au cas pédagogique.
