# T01 Habilitations MFA et sessions

**Version 1.1 - opérations réelles du 07/10/2026. Horodatages techniques en UTC.**

Exécution automatisée par Codex sur le poste personnel d’Anas. Les preuves sont réelles ; elles ne décrivent ni Atlas Services ni SupportCloud. Les pièces E/V restent simulées.

**Statut : RÉUSSI dans le périmètre des deux identités du realm grc-lab.**

## Objectif et protocole

R01 / M01 / C01 ; repères 8.2 et 8.5 ; protocole 1.1. Contrôler des autorisations positives et négatives, un MFA imposé et la révocation. Les critères initiaux restent conservés dans la référence 1.0.

## Environnement et prérequis vérifiés

Keycloak 26.8.0, Java Temurin 25.0.4.1+1, Windows du relevé. Service HTTPS local 127.0.0.1:18443, certificat vérifié par le client HTTP. Realm dédié, comptes LAB-ADMIN et LAB-LECTEUR ; aucun compte personnel utilisé. Opérateur : scripts Codex. Les mots de passe, le seed et les tokens ne figurent pas dans les pièces.

## Étapes et résultats

| Sous-critère | Attendu | Observé | Preuve |
| --- | --- | --- | --- |
| Rôles et règle | Droits distincts et enrôlement OTP obligatoire | realm-admin pour administrateur ; query-users/view-users pour lecteur ; CONFIGURE_TOTP enabled/defaultAction | [T01-P01_regles_roles.json](preuves/20261007T193900Z/T01-P01_regles_roles.json) |
| Fonction du lecteur | Lecture autorisée | GET users HTTP 200 | [T01-P02_autorisations.json](preuves/20261007T193900Z/T01-P02_autorisations.json) |
| Administration par lecteur | Refus | PUT realm HTTP 403 | [T01-P02_autorisations.json](preuves/20261007T193900Z/T01-P02_autorisations.json) |
| Administration par administrateur | Modification permise | PUT realm HTTP 204 | [T01-P02_autorisations.json](preuves/20261007T193900Z/T01-P02_autorisations.json) |
| Nouvelle session et mot de passe seul | Challenge OTP ; aucun token | Nouvelle session HTTP ; formulaire OTP atteint, puis arrêt sans fournir de code | [T01-P03_mfa.json](preuves/20261007T193900Z/T01-P03_mfa.json) |
| Mauvais second facteur | Refus | Retour au formulaire OTP ; aucun token délivré | [T01-P03_mfa.json](preuves/20261007T193900Z/T01-P03_mfa.json) |
| Second facteur correct | Connexion valide | Token endpoint HTTP 200 après authentification TOTP et échange de code OIDC avec PKCE | [T01-P03_mfa.json](preuves/20261007T193900Z/T01-P03_mfa.json) |
| Chemins mot de passe alternatifs | Aucun token sans OTP | grc-evidence et admin-cli : HTTP 400 sans access_token | [T01_chemins_alternatifs.json](preuves/20261007T193900Z/T01_chemins_alternatifs.json) |
| Révocation | Session supprimée et réutilisation refusée | 2 sessions avant ; 0 après ; refresh HTTP 400 invalid_grant ; SSO login_required ; ancien access token API HTTP 401 | [T01-P04_revocation_recuperation.json](preuves/20261007T193900Z/T01-P04_revocation_recuperation.json) |
| Récupération et exceptions | Configuration et limites examinées | Pas de mail ni codes de récupération ; master LAB-RECOVERY est une exception locale identifiée ; pas de procédure organisationnelle validée | [T01-P04_revocation_recuperation.json](preuves/20261007T193900Z/T01-P04_revocation_recuperation.json) |


Le reader exerce une fonction de consultation administrative native de Keycloak. Ce n’est pas un test d’un outil de tickets Atlas Services. Les dates exactes, versions et réponses serveur sont dans les exports JSON.

## Anomalies correction et retests

[Diagnostics réels conservés](preuves/INVENTAIRE/T01-D01_diagnostics.txt) : dépendance HTTP absente, cookies Secure incompatibles avec l’essai HTTP, redirections d’action obligatoire et lecture de la clé manuelle. Corrections : dépendances isolées, TLS local, gestion correcte du formulaire et du Base32. Aucun faux indicateur MFA, suppression de cookie Secure ou contournement de l’authentificateur n’a été utilisé.

Les dossiers datés précédents sont conservés ; le retest final est 20261007T193900Z. Ses exports établissent les refus et autorisations attendus. Les corrections du harnais ne prouvent pas une vulnérabilité de Keycloak.

## Conclusion d’audit et limites

Les deux rôles et le MFA TOTP fonctionnent dans le chemin testé ; la session SSO et son renouvellement sont refusés après révocation. L’ancien access token est aussi refusé par l’API native observée. Cela ne démontre pas la révocation immédiate des JWT dans toutes les applications tierces.

TOTP est produit automatiquement à partir du secret réellement délivré par Keycloak. Le mot de passe et ce seed se trouvent sur le même poste de test : aucune séparation matérielle des facteurs, résistance au phishing, récupération par téléphone ou disponibilité d’entreprise n’est démontrée. L’exception master est explicitée, la récupération documentée mais son exercice complet n’est pas réalisé. Le mode start-dev/H2 et le certificat local ne constituent pas une architecture de production.

M01, les risques et les pièces E/V restent dans leur état simulé. Reproduction : prepare_keycloak.py, start_keycloak.py, test_keycloak.py ; voir la notice. Le script crée de nouvelles pièces datées et réutilise le realm dédié uniquement.
