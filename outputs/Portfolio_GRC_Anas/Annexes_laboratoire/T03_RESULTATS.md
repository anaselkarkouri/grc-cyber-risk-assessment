# T03 Sauvegarde et restauration de fichiers

**Version 1.1 - opérations réelles du 07/10/2026. Horodatages techniques en UTC.**

Exécution automatisée par Codex sur le poste personnel d’Anas. Les preuves sont réelles ; elles ne décrivent ni Atlas Services ni SupportCloud. Les pièces E/V restent simulées.

**Statut : RÉUSSI pour trois fichiers artificiels sauvegardés en ZIP et restaurés séparément.**

## Objectif et environnement

R03 / M03 / C03 ; repère 8.13 ; protocole 1.1. Windows et Python 3.12 du runtime, module standard zipfile, compression ZIP_DEFLATED. Données LAB-001, LAB-002 et LAB-003 ; exécutant automatisé, utilisateur Windows courant. Aucun compte de sauvegarde séparé n’est utilisé.

## Prérequis et étapes exécutées

Répertoire dédié créé avec échec si le nom daté existe ; trois objets JSON aux contenus connus ; source et restauration distinctes. Contenus, tailles et SHA-256 consignés avant sauvegarde. Archive créée à 2026-10-07T19:27:35.004494+00:00, empreinte 8070450a97c21799443f873b91558d33acb95bc6f0c4f28f670c8ce7df7afd21. Les chemins d’extraction ont été vérifiés pour rester sous la destination résolue. Les originaux n’ont pas été modifiés.

| Sous-critère | Attendu | Observé | Preuve |
| --- | --- | --- | --- |
| Jeu attendu | Trois contenus connus et empreintes | LAB-001/LAB-002/LAB-003 consignés avant copie | [T03-P01_attendus.json](preuves/20261007T192733Z/T03-P01_attendus.json) |
| Copie identifiée | Date, périmètre et mécanisme réel | ZIP local, trois entrées, date/empreinte/taille enregistrées | [T03-P02_copie.json](preuves/20261007T192733Z/T03-P02_copie.json) |
| Restauration distincte | Ne pas écraser la source | Dossier restaure séparé, source conservée | [T03-P03_comparaison.json](preuves/20261007T192733Z/T03-P03_comparaison.json) |
| Intégrité | Contenus, tailles et empreintes identiques | 3 sur 3 pour les trois comparaisons | [T03-P03_comparaison.json](preuves/20261007T192733Z/T03-P03_comparaison.json) |
| Durée et âge | Mesures réellement obtenues | Restauration 0.003680 s ; copie âgée de 0.032541 s au départ | [T03-P04_chronologie.json](preuves/20261007T192733Z/T03-P04_chronologie.json) |
| Droits accessibles | ACL source, archive et restauration | Sorties icacls conservées ; même utilisateur et même volume | [T03-P03_comparaison.json](preuves/20261007T192733Z/T03-P03_comparaison.json) |


## Comparaison détaillée

| Fichier | Octets source et restaurés | SHA-256 identique | Contenu identique |
| --- | --- | --- | --- |
| LAB-001.json | 118 / 118 | 070047713cb0a4b279542ca2aa7c3d373a82f7635a7b87ae77d676aaf07a949a | Oui |
| LAB-002.json | 165 / 165 | bebc71c8caf652a294b96af87010ebd630a97b075a95d42e27b8535f896d7048 | Oui |
| LAB-003.json | 144 / 144 | 5555992300f17092c607695eb15d2303b7565d010909975a11953d37e4e78ebc | Oui |


## Anomalies et conclusion

Aucune divergence de données, de taille ou d’empreinte observée. Aucun retest correctif de restauration nécessaire. La copie artificielle est fournie comme pièce ZIP ; aucun fichier original ni restauration n’a été supprimé.

La copie permet de récupérer ces trois fichiers uniquement. Même volume et même utilisateur : absence de séparation des privilèges et du support, pas de stockage immuable ni de copie hors site. Cette faiblesse de résilience demeure explicitement hors du critère de récupération locale ; elle empêche toute conclusion de sauvegarde d’entreprise. Ni SaaS, base de tickets, index ou authentification ne sont restaurés. Durée de quelques millisecondes et copie récente ne prouvent pas RTO huit heures/RPO 24 heures. M03 reste proposée dans le cas.

Reproduction : tests_locaux.py crée une nouvelle source, copie et restauration datées, contrôle la destination ZIP, puis compare les trois critères.
