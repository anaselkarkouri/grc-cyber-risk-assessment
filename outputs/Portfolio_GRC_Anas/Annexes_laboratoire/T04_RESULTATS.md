# T04 Marqueur Git historique et accès locaux

**Version 1.1 - opérations réelles du 07/10/2026. Horodatages techniques en UTC.**

Exécution automatisée par Codex sur le poste personnel d’Anas. Les preuves sont réelles ; elles ne décrivent ni Atlas Services ni SupportCloud. Les pièces E/V restent simulées.

**Statut : RÉUSSI pour un fichier dans un nouveau dépôt Git local et deux commits.**

## Objectif et protocole

R06 / M06 / C04 ; repères 5.17 et 8.4 ; protocole 1.1. Démontrer qu’une suppression courante ne retire pas le contenu de l’historique. Examiner les ACL locales et expliquer la réaction à une vraie exposition.

## Environnement et étapes

Git 2.48.1, Windows, dépôt créé exclusivement sous execution_20261007T192733Z/T04_secrets_git/depot_demo. Identité Git LAB-GRC et adresse example.invalid configurées localement ; aucun dépôt existant modifié, aucun remote. Le compte exécutant est l’utilisateur Windows courant.

1. configuration.txt contient uniquement des données artificielles et SECRET-DEMO-NON-UTILISABLE.
2. Commit initial réel : 456c91950b48e1401cd872f1b5369d67da1f5d05.
3. Marqueur retiré dans le fichier courant et commit réel : 9b7dd80636c691bda4dfb6661cc2016490fcb215.
4. git show et git grep exécutés sur HEAD et sur l’ancien commit ; git log, status et remote relevés.
5. icacls exécuté sur le dépôt et .git.

| Sous-critère | Attendu | Observé | Preuve |
| --- | --- | --- | --- |
| Marqueur initial | Présent avant retrait | Présent dans le premier commit | [T04-P02_premier_commit.json](preuves/20261007T192733Z/T04-P02_premier_commit.json) |
| Version courante | Marqueur absent | git grep HEAD code 1 ; git show sans marqueur | [T04-P03_historique.json](preuves/20261007T192733Z/T04-P03_historique.json) |
| Historique | Marqueur toujours lisible | git grep ancien commit code 0 ; contenu retrouvé | [T04-P03_historique.json](preuves/20261007T192733Z/T04-P03_historique.json) |
| Périmètre des accès | ACL locales examinées | icacls dépôt et .git ; pas de distant | [T04-P01_perimetre_droits.json](preuves/20261007T192733Z/T04-P01_perimetre_droits.json) |
| Vraie exposition | Procédure justifiée et limites | Invalidation/rotation requises ; non exécutées avec ce marqueur | [T04-P04_conclusion.json](preuves/20261007T192733Z/T04-P04_conclusion.json) |


## Constat recommandation et procédure applicable

Le retrait de la dernière version conserve le contenu accessible aux lecteurs de l’ancien commit. Un dépôt local n’a pas de rôles GitHub vérifiés ; ses ACL ne démontrent pas l’absence de clones ou de copies déjà accessibles ailleurs.

Pour une vraie clé : identifier sa portée et préserver la preuve ; révoquer/invalider immédiatement l’ancien secret auprès du service ; créer une valeur de remplacement stockée hors du dépôt ; tester l’inefficacité de l’ancien et l’usage attendu du nouveau sans les afficher ; examiner les journaux et les lecteurs ; traiter l’historique, références, tags et copies en coordination avec les utilisateurs autorisés ; revoir les habilitations et la prévention ; documenter la clôture et les limites. Réécrire un historique ne remplace pas l’invalidation et impose un plan de conservation et de synchronisation des copies.

## Anomalies limites et reproductibilité

Aucune anomalie du mécanisme Git attendu. La persistance historique est l’observation recherchée, pas un secret réel à corriger. Le dossier conserve ce dépôt comme preuve ; aucune réécriture de son historique.

Un marqueur inoffensif, un fichier et deux commits : pas de rotation réelle, pas de recherche exhaustive de secrets, pas de preuve de rôles de plateforme distante, ni de constat d’exposition de données d’entreprise. M06 reste proposée dans le cas. Reproduction : tests_locaux.py ; chaque exécution crée un dépôt distinct.
