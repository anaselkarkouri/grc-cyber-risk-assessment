# Projet 1 - Profil actuel et cible NIST CSF 2.0

**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**

## Périmètre

Ce profil couvre treize sous-catégories sélectionnées pour les risques du cas. Les résumés des résultats attendus sont reformulés. Les mesures et les pièces sont propres à l'exercice.

Les états actuels proviennent de justificatifs simulés. Les états cible sont proposés. Le dossier produit pendant l'étude est distingué de son adoption par la PME : écrire une PSSI ne démontre pas qu'elle est approuvée, diffusée ou appliquée.

## Profil

| Sous-catégorie | Résultat attendu, résumé | État actuel du cas | Pièce | Cible proposée et écart | Action ou vérification |
|---|---|---|---|---|---|
| GV.RR-02 | Responsabilités SSI explicites et exercées | Rôles informels | E10 | Propriétaires, pilotes et autorités validés | Approbation de la gouvernance du document 01 |
| GV.PO-01 | Politique adaptée au contexte et appliquée | Politique approuvée non démontrée | E10 | PSSI approuvée, diffusée et suivie | Document 05, puis preuves de diffusion et d'application |
| GV.RM-06 | Méthode commune d'appréciation des risques | Méthode préalable non fournie | E10 | Méthode définie, validée et utilisée | Document 02 ; revue métier et DG |
| ID.AM-02 | Inventaire des logiciels, services et systèmes | Inventaire initial incomplet | E01 | Services du périmètre couverts et propriétaires identifiés | Validation et maintenance du document 01 |
| ID.RA-05 | Analyse de menaces, faiblesses, vraisemblance et impacts | Analyse initiale non démontrée | E10 | Scénarios documentés avec hypothèses et limites | R01 à R12 ; validation des cotations |
| ID.RA-06 | Traitements choisis et suivis | Pas de suivi initial fourni | E10 | Actions, pilotes, échéances et décisions traçables | M01 à M12 et preuves de clôture |
| PR.AA-03 | Authentification des utilisateurs et services | MFA partiel, comptes existants | E02 | Authentification adaptée, exceptions examinées | M01, T01 |
| PR.AA-05 | Droits nécessaires, gérés et revus | Compte partagé et accès de départ maintenu | E02/E07 | Droits nominatifs et retrait effectif | M01/M07, procédure A |
| PR.DS-11 | Sauvegardes protégées et testées | Jobs déclarés, restaurabilité non démontrée | E04 | Restauration et protection vérifiées | M03, T03 |
| PR.PS-04 | Journaux produits et disponibles pour la surveillance | Événement pilote et couverture limitée | E03 | Sources prioritaires et accès aux journaux examinés | M04, T02 |
| DE.CM-09 | Surveillance des équipements, logiciels et données | Pilote sur une partie des équipements | E03 | Surveillance adaptée, lacunes identifiées et revue réelle | M04 ; suivi de couverture et traitement des alertes |
| RS.MA-01 | Réponse exécutée et coordonnée avec les tiers concernés | Plan et exercice non fournis | E10 | Plan testé dans un exercice et interlocuteurs identifiés | Procédure C ; exercice distinct à réaliser |
| RC.RP-03 | Intégrité des moyens de restauration vérifiée avant usage | Vérification non démontrée | E04 | Copie et moyens de reprise examinés avant restauration | M03 ; T03 limité à son échantillon |

## Interprétation

Les six fonctions Govern, Identify, Protect, Detect, Respond et Recover sont représentées. Leur présence ne signifie pas couverture complète du CSF.

Le profil ne calcule pas de moyenne « Govern 2/5 » ou « Detect 4/5 ». Les Tiers NIST ne sont pas utilisés comme notes par contrôle. La cotation V × I du registre appartient à une autre méthode et ne doit pas être mélangée au profil.

Une cible est satisfaite seulement lorsque son résultat et les preuves attendues sont établis pour le périmètre annoncé. Un document nouvellement écrit peut améliorer la conception sans démontrer le fonctionnement.

## Références

[NIST CSF 2.0, annexe A](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf), [profils organisationnels](https://www.nist.gov/cyberframework/profiles).
