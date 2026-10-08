# Projet 2 - Remédiation, conditions de production et suivi

**Cas simulé - version 1.0 - 7 octobre 2026**  
**Toutes les actions sont proposées et ouvertes. Aucun engagement fournisseur n'est réellement obtenu.**

## 1. Principes de traitement

RS reste propriétaire du risque cyber du service. RI vérifie les fonctions du tenant, RSSI examine l'assurance et RJ examine les clauses et obligations applicables. SupportCloud réalise les changements sur son service. DG autorise éventuellement la production.

J correspond au 7 octobre. Les délais sont des **objectifs du client dans le scénario**, en jours calendaires. Ils ne constituent pas des promesses du fournisseur. Si une échéance ne peut pas être tenue, le service reste hors production et le client réexamine la solution.

## 2. Plan de remédiation renseigné

| Action | Risque et constat | Traitement demandé | Pilote client / intervenant fournisseur | Cible proposée | Preuve attendue et vérification | État |
|---|---|---|---|---|---|---|
| VM01 | S01/F01 | Comptes administrateurs individuels, MFA imposé pour la formule retenue, récupération et sessions maîtrisées | RI / responsable IAM fournisseur | J+15, 22 octobre ; avant production | Matrice complète des administrateurs, règles effectives et essais d'authentification positive/négative sur tenant d'essai. Une fiche Enterprise seule est rejetée | Ouverte |
| VM02 | S02/F02 | Retirer SUPPORT-PARTAGE, encadrer accès support temporaires, revue et journalisation nominative | RSSI / responsable opérations fournisseur | J+15, 22 octobre ; avant production | Liste de population privilégiée, retrait du compte partagé, MFA et revue avec décideur. RSSI examine les exceptions et les accès d'urgence | Ouverte |
| VM03 | S03/F03 | Couvrir les événements utiles sur 90 jours, protéger les traces et limiter les droits ; préciser la solution Standard ou une autre formule | RI / responsable service et logs fournisseur | J+30, 6 novembre ; avant production | Échantillon représentatif, conservation configurée, accès/protection et récupération d'événements vérifiés. L'export manuel partiel ne clôture pas l'action | Ouverte |
| VM04 | S04/F04 | Démontrer reprise du service complet et point de reprise, puis une voie de récupération client exploitable | RI et RS / responsable continuité fournisseur | J+30, 6 novembre ; avant production | Rapport avec début/fin, composants, données restaurées, contrôles d'intégrité, dépendances, RTO/RPO observés et limites. RS confirme les objectifs métier | Ouverte |
| VM05 | S05/F05 | Compléter tiers/localisations/accès, responsabilités, exigences de sécurité et modalités de changement | RJ et RSSI / responsable données et contrats fournisseur | J+15, 22 octobre ; avant production | Cartographie et liste complètes, restrictions d'accès, contrat pertinent et revue compétente documentée. Aucun avis juridique favorable n'est présumé | Ouverte |
| VM06 | S06/F06 | Négocier fenêtre de récupération, export complet, restitution, suppression et exceptions de sauvegarde | RS et RJ / responsable service fournisseur | J+30, 6 novembre ; avant production | Export de tickets ET pièces testé, réutilisation démontrée, clause de fenêtre suffisante et délais distincts de suppression. Assurance adaptée de fin de traitement prévue | Ouverte |
| VM07 | S07/F07 | Convenir notification initiale sous 24 heures après confirmation d'un incident affectant le client ; contacts, escalade et exercice commun | RSSI et RJ / responsable incidents fournisseur | Clause J+15 ; exercice J+30, 6 novembre ; avant production | Clause acceptée, contacts et scénario de table avec chronologie, décisions et écarts. Pas de notification réelle ni d'attaque dans l'exercice | Ouverte |
| VM08 | S08/F08 | Corriger le défaut d'autorisation inter-clients et faire retester le périmètre affecté | RSSI / responsable développement et test fournisseur | Plan J+2, 9 octobre ; correction et retest visés J+10, 17 octobre ; avant production | Preuve du correctif, version, tests de refus entre tenants, vérification des voies concernées et limites du retest. Aucun test intrusif client non autorisé | Ouverte |

L'estimation de coût et la faisabilité restent à recueillir. Changer de formule ou de fournisseur impose de réexaminer périmètre, pièces, contrat et risques ; aucune fonction supplémentaire n'est considérée acquise.

### Clarification complémentaire de Q17

Demander une pièce d'assurance actuelle avec portée et dates, ou une explication documentée de l'allégation commerciale. La traiter comme assurance complémentaire. Ne pas remplacer les preuves VM01 à VM08 par un certificat, et ne pas inventer de certificat pour remplir le dossier.

## 3. Six conditions bloquantes avant production

| Condition | Vérifications nécessaires | État au 7 octobre |
|---|---|---|
| G1 - Isolation des clients | VM08 : défaut corrigé et retest pertinent, aucun défaut équivalent ouvert dans le périmètre retenu | NON SATISFAITE |
| G2 - Accès privilégiés | VM01/VM02 : comptes nominatifs, MFA imposé et récupération encadrée, tenant et support couverts | NON SATISFAITE |
| G3 - Reprise et récupération | VM04 : objectifs métier validés, service complet repris et données récupérables avec mesures observées | NON DÉMONTRÉE |
| G4 - Investigation et incident | VM03/VM07 : traces utiles et protégées, conservation retenue, clause et coordination d'incident | NON SATISFAITE |
| G5 - Données et tiers | VM05 : cartographie, sécurité des accès, engagements et revue compétente avant production | NON DÉMONTRÉE |
| G6 - Sortie et suppression | VM06 : export exploitable, fenêtre adaptée et engagements de suppression vérifiés au niveau pertinent | NON SATISFAITE |

Une condition n'est satisfaite qu'après examen de **tous** ses éléments. Une réponse « oui » à une question du formulaire ne suffit pas. La clarification de l'allégation ISO complète l'assurance mais ne remplace aucune de ces conditions.

Le niveau de preuve de suppression avant production peut être une procédure démontrée, une assurance de contrôle pertinente et un engagement contractuel précis. La preuve de suppression de **nos propres données** sera collectée après une sortie effective ; on ne peut pas l'exiger comme un fait déjà réalisé avant la première utilisation.

## 4. Extraits de clauses à négocier

Ces propositions sont des exigences client pédagogiques à faire examiner par RJ. Elles ne sont pas des clauses juridiquement validées ni un contrat prêt à signer.

### Authentification et responsabilité

Le périmètre contractuel identifie la formule et les fonctions de sécurité disponibles. Les administrateurs client et les opérateurs fournisseur accédant aux données disposent d'identités individuelles et d'une authentification renforcée obligatoire. Les accès d'urgence font l'objet de règles d'activation, durée, traçabilité et revue. Les responsabilités de paramétrage du tenant et d'exploitation fournisseur sont explicites.

### Incident

Le besoin du client est une première information sous 24 heures après confirmation d'un incident affectant ses données ou le service convenu. Cette première information contient les éléments connus, l'état des incertitudes, un contact et le prochain point de suivi. Les parties définissent aussi le signalement rapide d'une suspicion pertinente, sans attendre artificiellement une certitude totale. Aucune obligation légale n'est déduite de cette durée contractuelle locale.

### Reprise et journaux

Les objectifs RTO/RPO et les composants couverts sont fixés après validation métier. Les preuves d'exercice indiquent mesure, périmètre et limites. Les événements utiles, accès aux traces, durée de disponibilité, protection et moyens d'investigation sont définis pour la formule souscrite.

### Données, tiers et sortie

Les lieux de stockage et d'accès, les catégories de tiers et leurs responsabilités sont documentés. Les changements donnent lieu à une information permettant une réévaluation et à des modalités d'objection ou de sortie convenues.

Le retour porte sur tickets, commentaires, pièces et métadonnées nécessaires à une reprise. La fenêtre de trente jours est une proposition à valider contre les besoins et moyens du client. Le contrat distingue suppression des données actives, expiration des sauvegardes, restrictions pendant cette période, exceptions motivées et preuve de fin de traitement.

## 5. Registre de suivi des conditions

Ce tableau est une photographie du dossier. Les champs non remplis sont réellement non obtenus, pas implicitement favorables.

| Étape | Situation documentée |
|---|---|
| Relance des pièces | Liste de demandes rédigée ; aucun envoi réel |
| Accord du fournisseur | Aucun engagement réel |
| Réception de nouvelles preuves | Aucune nouvelle pièce réelle |
| Examen technique | Non réalisé sur un service réel |
| Réévaluation des scores | Cibles estimées ; résiduels non réévalués après traitement effectif |
| Approbation de production | Non accordée dans la décision proposée |
| Acceptation signée | Aucune |

Une clôture doit enregistrer identifiant VM, pièce et version, vérificateur, date, population testée, résultat, limites, nouvelle cotation et approbateur. Si une pièce est rejetée, inscrire la raison et la prochaine demande. Conserver la version précédente.

## 6. Suivi si le fournisseur devient admissible

Le calendrier proposé dépend de sa criticité :

- Revue des accès et des exceptions du client chaque trimestre ; assurance fournisseur pertinente demandée à la même cadence.
- Suivi trimestriel des incidents, vulnérabilités ouvertes importantes, changements de tiers et conditions contractuelles.
- Réévaluation complète au moins annuelle dans le scénario, et avant renouvellement majeur.
- Réévaluation immédiate après incident affectant le client, nouveau défaut important, nouveau sous-traitant, changement de lieu, modification de formule, perte d'une fonction de sécurité ou assurance devenue périmée.
- Revue de sortie avant résiliation, avec export de contrôle et plan de conservation/suppression.

Ces fréquences sont des choix locaux. Elles ne sont pas des obligations universelles fixées par NIST.

### Indicateurs proposés

| Indicateur | État actuel du dossier | Cible |
|---|---|---|
| Conditions G1 à G6 satisfaites | 0 sur 6 | 6 sur 6 avant production |
| Actions VM clôturées avec preuve | 0 sur 8 | 8 sur 8, puis surveillance |
| Défauts ouverts donnant accès inter-clients | 1 dans le résumé simulé | 0 dans le périmètre retenu et retesté |
| Reprise du service complet démontrée | Non | Objectifs convenus atteints et limites acceptées |
| Liste complète des tiers et accès | Non démontrée | Pièce actuelle examinée |

Ne pas convertir ces indicateurs en un pourcentage de « conformité ISO » ou de sécurité du fournisseur.

## 7. Repères NIST CSF 2.0 - GV.SC

Sélection pédagogique de huit sous-catégories, avec thèmes reformulés et applications propres au cas. Ce tableau n'est pas une évaluation de toute la catégorie GV.SC.

| Repère | Thème de travail | Trace dans ce projet |
|---|---|---|
| GV.SC-01 | Organisation de la démarche fournisseur | Cadrage, méthode, conditions et calendrier proposés |
| GV.SC-02 | Responsabilités internes et externes | RS, RSSI, RI, RJ, DG et interlocuteurs fournisseur |
| GV.SC-04 | Identification et priorisation des fournisseurs | Criticité de l'usage support cible |
| GV.SC-05 | Exigences intégrées aux accords | Critères client et clauses à négocier |
| GV.SC-06 | Examen avant engagement | Questionnaire et recoupement des pièces avant production |
| GV.SC-07 | Risques fournisseur suivis au cours de la relation | Registre S01 à S08, actions et événements de réévaluation |
| GV.SC-08 | Coordination des incidents avec les fournisseurs | VM07, contacts et exercice de table proposés |
| GV.SC-10 | Fin de relation préparée | VM06, retour et suppression des données |

Le [NIST SP 1305](https://csrc.nist.gov/pubs/sp/1305/final) guide l'utilisation du CSF pour les risques de la chaîne d'approvisionnement. Les identifiants sont issus du [CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf). Les documents créés ici décrivent un exercice et des cibles ; ils ne prouvent pas l'exécution d'un programme fournisseur réel.
