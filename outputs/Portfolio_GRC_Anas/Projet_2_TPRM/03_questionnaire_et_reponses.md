# Projet 2 - Questionnaire, réponses et examen

**Vingt questions renseignées - cas simulé - version 1.0 - 7 octobre 2026**

Les réponses ci-dessous appartiennent au fournisseur fictif. L'évaluation porte sur la formule Standard et l'usage cible. « Documenté » ne signifie pas vérification opérationnelle exhaustive.

## Questionnaire évalué

| ID | Question et preuve attendue | Réponse fictive et pièce reçue | Appréciation de l'évaluateur |
|---|---|---|---|
| Q01 | Quel service et quelle formule sont couverts ? Fiche et périmètre contractuel | Service de tickets, formule Standard ; V01 | Documenté pour le cadrage. Ne pas retenir les fonctions Enterprise |
| Q02 | Quelles données sont traitées, et quelles limites de contenu ? Cartographie et règles | Noms, courriels, textes et pièces ; pas de filtrage garantissant l'absence de secrets ; V01 | Partiel : le client doit maîtriser ce qu'il envoie |
| Q03 | Où sont hébergement, sauvegardes et accès support ? Cartographie complète | « Europe uniquement » ; V01 mentionne Irlande/France et support Maroc/Portugal | Partiel : distinguer stockage et accès distant ; partenaire externe encore inconnu |
| Q04 | Qui sont les sous-traitants et comment les changements sont-ils notifiés ? Liste et procédure | Liste V07, partenaire support incomplet ; délai contractuel imprécis | Non démontré pour la liste complète et les modalités de changement |
| Q05 | Quels rôles client limitent les accès ? Matrice de rôles et test de refus | Rôles lecteur/administrateur décrits ; V03 | Conception documentée ; fonctionnement sur un tenant à vérifier |
| Q06 | Le MFA peut-il être imposé aux administrateurs client dans la formule achetée ? Paramétrage et test | MFA disponible mais facultatif en Standard ; V03 | Écart au besoin du cas : activation possible ne démontre pas obligation |
| Q07 | Tous les accès privilégiés fournisseur sont-ils nominatifs et protégés ? Population et exceptions | « Tous protégés » ; V03 décrit SUPPORT-PARTAGE sans MFA imposé | Écart confirmé dans le dossier simulé |
| Q08 | Comment arrivées, départs et revues de droits sont-ils tracés ? Échantillon et compte rendu | Revue trimestrielle annoncée ; compte rendu non fourni ; V03 | Non démontré. Ne pas conclure que la revue n'existe pas |
| Q09 | Comment les données sont-elles chiffrées et les clés gérées ? Architecture et configuration | TLS et chiffrement stocké décrits ; V02 | Documenté pour la conception ; configuration et opérations non démontrées |
| Q10 | Quels journaux sont disponibles et pendant combien de temps ? Échantillon et politique | Trente jours en Standard ; export partiel annoncé ; V04 | Écart au besoin de 90 jours, solution compensatoire non validée |
| Q11 | Qui peut modifier les logs et comment sont-ils protégés ? Droits et protection | Aucun relevé précis fourni ; V04 | Non démontré, information complémentaire nécessaire |
| Q12 | Les vulnérabilités importantes sont-elles corrigées et retestées ? Registre et retest | Correctif inter-clients annoncé ; constat ouvert ; V06 | Écart confirmé, blocage de production |
| Q13 | Quels tests couvrent le service acheté ? Rapport daté, périmètre et limites | Résumé portail/API du 12 septembre ; intégrations exclues ; V06 | Partiel : rapport utile, pas assurance exhaustive ni preuve de retest |
| Q14 | Quel RTO/RPO est démontré pour le service complet ? Rapport de restauration | « Huit heures démontrées » ; V05 ne couvre que des fichiers restaurés en six heures | Non démontré pour le service complet et le RPO |
| Q15 | Peut-on récupérer toutes les données à la sortie ? Export de test et fenêtre contractuelle | CSV annoncé, pièces non démontrées, accès 48 heures ; V08 | Partiel, avec écart à la fenêtre proposée de trente jours |
| Q16 | Quels délais et preuves de suppression couvrent actif et sauvegardes ? Engagement et attestation | Trente jours actif, 90 jours sauvegardes, exceptions non détaillées ; V08 | Partiel : engagements et preuve de fin de traitement à préciser |
| Q17 | Quelle certification ou autre assurance couvre ce service aujourd'hui ? Certificat, portée, dates | Allégation commerciale et fiche ancienne hors portée démontrée ; V09 | Certification du service non démontrée ; ne pas la déclarer inexistante |
| Q18 | Quel délai de notification client est engagé ? Politique et clause | 72 heures après confirmation ; contrat renvoie à la politique ; V02/V08 | Écart au besoin contractuel de 24 heures ; ce besoin n'est pas présenté comme légal |
| Q19 | Le contrat fixe-t-il responsabilités, contrôle et modifications ? Projet complet et validation | Projet non signé, modalités partielles ; V08 | Partiel ; examen et négociation nécessaires |
| Q20 | Comment client et fournisseur coordonnent-ils incident et reprise ? Contacts et exercice | Plan fournisseur annoncé, aucun exercice client fourni ; V02 | Coordination opérationnelle non démontrée |

## Relances à adresser dans le scénario

1. Fournir la population complète des accès privilégiés, leurs règles MFA et les exceptions, pour la formule Standard.
2. Fournir le retest du défaut inter-clients, avec service, version, résultat et limites.
3. Démontrer une reprise du service complet, pas uniquement des fichiers.
4. Clarifier journalisation, protection et conservation pour la formule retenue.
5. Fournir la liste complète des sous-traitants et des accès aux données.
6. Proposer les clauses d'incident, sortie, suppression et changement fournisseur.
7. Clarifier la portée de l'allégation ISO avec une pièce actuelle, ou documenter les assurances alternatives.

Aucune relance n'a été envoyée à une entreprise réelle.

## Principes de décision

Un « oui » au questionnaire ne clôture pas une question lorsque la preuve contredit la réponse, concerne une autre formule ou ne couvre qu'un sous-ensemble.

Les réponses ne sont pas additionnées pour produire un pourcentage de conformité. Une seule faiblesse bloquante peut empêcher la production même si de nombreuses autres réponses sont documentées.
