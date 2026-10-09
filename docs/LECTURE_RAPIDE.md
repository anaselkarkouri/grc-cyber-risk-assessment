# Lire le projet SSI en dix minutes

Ce projet relie une analyse de risques, une revue documentaire de contrôles et des tests techniques. Il porte sur Atlas Services, une PME fictive. Les pièces de l'entreprise sont simulées ; les tests du laboratoire personnel ont leurs propres exports et ne valident pas les contrôles de cette PME.

## La question étudiée

Quels risques faut-il traiter en priorité, sur quelles observations s'appuyer et quelles preuves demander avant de considérer une action comme terminée ?

Le dossier comprend dix actifs, douze scénarios de risque et douze actions proposées. La cotation vraisemblance × impact sert à prioriser le cas. Elle exprime un jugement pédagogique, pas une probabilité mesurée ou une exigence chiffrée d'ISO.

## Le parcours de lecture

1. [Contexte, périmètre et actifs](../outputs/Portfolio_GRC_Anas/Projet_1_SSI/01_contexte_perimetre_actifs.md) : comprendre ce qui est évalué et les responsabilités.
2. [Méthode et registre des risques](../outputs/Portfolio_GRC_Anas/Projet_1_SSI/02_methode_registre_risques.md) : suivre les scénarios, les cotations, leurs hypothèses et leurs propriétaires.
3. [Traitement et extrait de SoA](../outputs/Portfolio_GRC_Anas/Projet_1_SSI/03_traitement_controles_SoA.md) : relier les mesures proposées aux risques et aux critères de clôture.
4. [Matrice des preuves du laboratoire](../outputs/Portfolio_GRC_Anas/Annexes_laboratoire/MATRICE_PREUVES.md) : examiner les observations techniques sans les confondre avec les pièces fictives.
5. [Synthèse direction](../outputs/Portfolio_GRC_Anas/Projet_1_SSI/08_synthese_direction.md) : lire les priorités et les décisions proposées.

## Exemple de raisonnement : accès privilégiés

Dans le scénario, la pièce E02 conduit au constat C01, au risque R01 et au traitement M01. Il faut expliquer le risque pour le service, les responsabilités et les preuves nécessaires pour valider le traitement.

Le test T01 est une illustration technique distincte : deux comptes de laboratoire, des rôles, le MFA TOTP et la révocation des accès sont examinés avec Keycloak. Sa réussite dans ce périmètre n'établit ni la couverture des comptes de la PME fictive ni la conformité globale d'un SMSI.

## Ce que les tests démontrent

| Test | Résultat conservé | Limite à connaître |
| --- | --- | --- |
| T01 - Keycloak | Habilitations, MFA et révocation vérifiés sur les comptes du laboratoire | Pas d'audit d'un IAM d'entreprise ni de couverture de tous les scénarios |
| T02 - Windows/Wazuh | Un même événement 4625 rapproché entre source Windows, réception et alerte Wazuh | Test partiel ; conservation de 90 jours et couverture globale non démontrées |
| T03 - Restauration | Trois fichiers restaurés, contenus et SHA-256 identiques | Pas de validation de la reprise d'un service complet ni d'un RTO/RPO en production |
| T04 - Historique Git | Un marqueur retiré du fichier courant reste visible dans un ancien commit | Aucun secret réel ni rotation de clé, aucune recherche exhaustive de secrets |

## Livrables et conclusion

Une PSSI, des procédures, un extrait de déclaration d'applicabilité et un profil actuel/cible NIST CSF 2.0 complètent le registre. Le profil couvre treize sous-catégories ; l'extrait de SoA couvre vingt mesures. Ils restent partiels.

Les douze actions du cas sont proposées et aucune n'est déclarée clôturée. Les scores à l'état cible sont conditionnels. Le laboratoire illustre la vérification de certaines mesures ; il ne transforme pas ces objectifs en résultats obtenus.

La préparation a bénéficié d'outils IA et de Codex. Les étapes à comprendre et à reprendre sont indiquées dans le [guide d'appropriation](../outputs/Portfolio_GRC_Anas/GUIDE_APPROPRIATION.md). Ce dépôt montre un travail d'apprentissage documenté, sans revendication de certification ISO ou de maîtrise complète des référentiels.

## À pouvoir expliquer en entretien

- Partir d'un actif et d'un scénario, puis justifier vraisemblance, impact et priorité.
- Expliquer pourquoi un contrôle est pertinent et quelle preuve permettrait de le vérifier.
- Distinguer absence de justificatif, écart explicite et efficacité réellement testée.
- Relier une action à son responsable et à un critère de clôture.
- Expliquer les limites de T02 et pourquoi les tests personnels ne clôturent pas les actions de la PME fictive.
