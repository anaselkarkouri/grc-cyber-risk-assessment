# Projet 1 - PSSI et procédures proposées

**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**  
**Statut : propositions pour la PME fictive, non approuvées et non déployées.**

## PSSI proposée

### 1. Objet et responsabilité

La politique protège les informations et services du périmètre défini dans le document 01. La DG porte la décision et les ressources. Le RSSI coordonne la politique. Chaque responsable métier porte les risques et les informations de son domaine.

La politique est revue au moins annuellement, après un incident important, un changement de périmètre ou un changement fournisseur significatif. Une revue laisse une décision, une date, une version et un responsable.

### 2. Classification et usage des données

Trois niveaux sont retenus pour ce cas : public, interne et confidentiel. Les informations clients, le code non public, les journaux sensibles et les sauvegardes sont au minimum confidentiels.

Les tickets contiennent uniquement les données nécessaires au support. Les mots de passe, clés privées, documents d'identité et données de santé ne doivent pas y être déposés. Un exemple d'interdiction doit être montré lors de la sensibilisation.

Les exports ont un propriétaire, un usage, des destinataires limités et une durée justifiée. Pour l'exercice, un export de travail est supprimé après trente jours, sauf justification formalisée. Ce délai est un choix local à valider et non une règle légale générale.

### 3. Identités et habilitations

Les comptes humains sont nominatifs. Les droits suivent le besoin et le moindre privilège. Les fonctions d'administration sont séparées des usages ordinaires. Les comptes techniques ont un propriétaire et un usage explicites.

Le MFA est imposé pour les accès privilégiés et les accès distants retenus dans le périmètre. L'enregistrement d'un second facteur ne suffit pas : l'obligation et la récupération doivent être examinées.

Un accès de secours fait l'objet d'une justification, d'un stockage protégé, d'une traçabilité et d'une revue. Une exception ne doit pas être invisible dans l'inventaire.

Les droits sensibles sont revus trimestriellement et après une mobilité. Au départ d'une personne, l'accès est retiré à la date et à l'heure prévues. Une situation urgente impose une coordination RH, métier et infrastructure.

### 4. Secrets et code

Les secrets utilisables sont stockés dans un moyen adapté, hors du dépôt et des tickets. Leur accès est limité. La revue de code et la revue des droits du dépôt participent au contrôle.

En cas d'exposition, le secret est invalidé et remplacé. La dernière version et l'historique sont examinés. La suppression du texte ne remplace pas l'invalidation.

Les revues manuelles de l'exercice sont limitées au périmètre annoncé. Une recherche automatique exhaustive serait une extension technique distincte.

### 5. Postes et vulnérabilités

Les postes contenant des informations clients sont inventoriés, protégés, mis à jour et chiffrés selon le besoin. Les moyens de récupération du chiffrement sont conservés sous contrôle et testés sans exposer les clés.

Les vulnérabilités ont un propriétaire, une criticité et un délai de traitement. Dans le cas pédagogique, un défaut permettant l'accès non autorisé aux données clients bloque la mise en production du service concerné. Un délai générique ne remplace pas l'analyse de risque.

Les tests sont réalisés uniquement sur des environnements autorisés et des données artificielles.

### 6. Journaux et surveillance

Les sources prioritaires sont inventoriées. Pour chaque source, définir événements utiles, collecte, accès, protection, conservation, alertes et responsabilité de revue.

Le cas retient un objectif de disponibilité de 90 jours pour les journaux utiles du serveur de tickets et des accès privilégiés. La durée et les données collectées doivent être validées avec le besoin opérationnel et les obligations applicables.

Un événement visible prouve seulement le parcours testé. La couverture, les lacunes de collecte et les exceptions sont enregistrées.

### 7. Sauvegarde et continuité

L'application de tickets est sauvegardée quotidiennement. Le stockage et les comptes sont séparés des accès ordinaires. La restauration est exercée dans un environnement isolé.

Les objectifs proposés sont RTO huit heures et RPO 24 heures pour le service de tickets. Leur validation métier précède une acceptation du risque.

Le test vérifie les données restaurées, les dépendances et le service, pas seulement la présence de fichiers. Les échecs et limites sont conservés.

### 8. Fournisseurs

Un fournisseur critique est évalué avant production. Les preuves attendues portent sur le service, la formule et les engagements réellement achetés.

Le contrat précise responsabilités, protection des données, accès support, incidents, sous-traitance, journaux, réversibilité et fin de contrat. Un certificat hors périmètre ne clôture pas l'évaluation.

La validation de sécurité et l'examen des obligations relatives aux données personnelles sont enregistrés séparément. Le RSSI ne remplace pas la fonction juridique compétente.

### 9. Changements

Un changement sensible dispose d'un responsable, d'un risque examiné, d'une approbation, d'une vérification et d'un retour arrière. L'approbation indépendante est recherchée lorsque le même développeur prépare le changement.

Un changement d'urgence conserve sa justification et fait l'objet d'une revue ultérieure. « Urgent » ne signifie pas absence de dossier.

### 10. Exceptions et indicateurs

Chaque exception comporte son périmètre, sa justification, son risque, ses mesures compensatoires, son approbateur, sa date d'expiration et sa condition de réexamen.

Les indicateurs proposés dans la synthèse sont suivis après validation des populations et des sources. Aucun pourcentage global de conformité ISO n'est calculé.

## Procédure A - Gestion des habilitations

**Pilote : RI. Approbateur métier : propriétaire de l'information. Vérificateur : RSSI.**

| Étape | Action | Pièce attendue |
|---|---|---|
| 1. Demande | Identifier personne ou service, rôle, systèmes, durée et droits demandés | Ticket d'accès et identité de test |
| 2. Approbation | Le propriétaire vérifie nécessité et séparation des fonctions | Décision explicite avec date |
| 3. Mise en place | Créer compte nominatif, limiter droits, imposer MFA si applicable | Relevé de droits et configuration |
| 4. Vérification | Vérifier accès autorisé et refus d'un accès non nécessaire | Résultat positif et négatif |
| 5. Revue | Examiner les droits sensibles et exceptions à l'échéance | Liste de population et décision |
| 6. Mobilité/départ | Retirer accès, sessions, jetons et comptes associés à l'heure prévue | Checklist de retrait et contrôle de refus |
| 7. Archivage | Conserver décision et résultat avec accès limité | Dossier d'accès traçable |

**Exemple rempli dans le scénario E07 :** départ du 30 septembre, contrôle du 7 octobre, accès encore actif. Action conservatoire M07 proposée. Aucun retrait réel n'est déclaré.

**Point de contrôle :** si l'application possède un compte local qui n'utilise pas l'annuaire, sa suppression doit être vérifiée séparément.

## Procédure B - Sauvegarde et restauration

**Pilote : RI. Validation fonctionnelle : RS.**

1. Définir les données et dépendances à sauvegarder avec le métier.
2. Planifier le job, les droits, la protection et le stockage séparé.
3. Examiner les résultats des jobs et traiter les erreurs.
4. Sélectionner une sauvegarde pour un test isolé et enregistrer l'heure de départ.
5. Restaurer vers un emplacement de test, jamais sur une donnée originale non sauvegardée.
6. Vérifier trois enregistrements artificiels connus, leurs champs et l'usage de l'application ou du fichier de test.
7. Enregistrer l'heure de fin, l'âge de la copie et les limites.
8. Comparer le résultat aux objectifs applicables. Ouvrir une action si l'objectif n'est pas atteint ou n'est pas démontré.
9. Faire valider le résultat par une autre personne, puis nettoyer les copies de test.

Une restauration de trois fichiers démontre ce périmètre seulement. Elle ne démontre pas la reprise complète du serveur, ni une sauvegarde résistante à toutes les attaques.

## Procédure C - Signalement et coordination d'incident

**Pilote : RSSI. Coordination métier : RS.**

| Phase | Action et limite |
|---|---|
| Signalement | Enregistrer date, source, système, observation et interlocuteur ; ne pas transmettre de secret dans le ticket |
| Qualification | Distinguer événement, alerte, faux positif et incident confirmé |
| Décision | Définir priorité, responsable et nécessité de confinement |
| Conservation | Préserver les pièces disponibles et leur provenance ; éviter les modifications non nécessaires |
| Coordination | Inclure les fournisseurs concernés et informer la DG selon la gravité |
| Reprise | Vérifier les dépendances et l'intégrité avant retour au service |
| Clôture | Confirmer critères de clôture, limites et actions d'amélioration |

Un exercice sur papier peut vérifier les rôles et la circulation de l'information. Il ne démontre pas l'efficacité d'un confinement technique.

## Gestion documentaire proposée

Documenter titre, version, auteur, relecteur, approbateur, date d'effet et historique. Pour cette version, l'approbation et la date d'effet sont **non réalisées**. Aucun paraphe ou accord de direction n'est simulé comme authentique.
