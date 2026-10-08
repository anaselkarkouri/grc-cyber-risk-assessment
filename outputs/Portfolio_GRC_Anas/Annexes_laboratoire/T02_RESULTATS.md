# T02 Événement collecte et SIEM

**Version 1.1 — opérations réelles du 7 octobre 2026 ; dates techniques UTC. Opérateur : scripts Codex sur le poste personnel.**

**Statut : PARTIEL. Source → réception Wazuh → alerte prouvées ; configuration/droits examinés ; conservation opérationnelle et fonctionnement sur 90 jours non démontrés.**

## Objectif et périmètre

R04 / M04 / C02, repères 8.15 et 8.16, protocole 1.1. Suivre un échec de connexion contrôlé depuis Windows jusqu’au gestionnaire et à sa règle ; examiner les sources, accès et conservation. Atlas Services et SupportCloud demeurent fictifs et leurs actions ouvertes.

Source : Windows 11 Professionnel DESKTOP-3SQ1K5Q, agent Wazuh 4.14.6 ; compte artificiel LAB-GRC-EVT. Gestionnaire : nouvelle VM GRC-Wazuh-T02-20261007, Ubuntu 24.04.5 LTS, noyau 6.8.0-142-generic, paquet wazuh-manager 4.14.8-1. Deux CPU, 2 Gio, disque 20 Gio, NAT et host-only 192.168.56.10. Accès SSH à clé par 127.0.0.1:22022 ; pas d’indexer, Filebeat ou dashboard installés.

L’alias historique de l’agent est TMED-POC-HOST (ID 001), mais l’événement vient du poste personnel DESKTOP-3SQ1K5Q. Cet alias ne désigne pas une cible de production Tanger Med. L’adresse agent 192.168.56.1 est celle du host-only Windows. Le réseau et les quatre VM préexistantes ont été inventoriés ; aucune VM initiale n’a été lancée ou modifiée.

## Prérequis et étapes réelles

1. Inventaire initial en lecture seule, refus d’accès non élevé et UAC initialement annulée ; diagnostics conservés, puis UAC acceptée pour lecture Security/configuration et compte de test.
2. Agent initial actif mais serveur inaccessible. Destination Windows 192.168.56.10:1514/TCP conservée ; canaux Application/Security/System et deux sources déjà configurées identifiés. Audit de connexion succès/échecs déjà actif ; aucun changement d’audit.
3. LAB-GRC-EVT créé avec mot de passe aléatoire non affiché. Un LogonUser avec mot de passe incorrect : false/Win32 1326. Source Security 4625 recherchée sur le compte et la période ; compte désactivé en finally.
4. Gestionnaire minimal préparé à partir d’une image Ubuntu officielle datée du 26 septembre, SHA-256 attendu/observé identiques. Snapshot avant les corrections, clés SSH privées et images conservés sous ACL dans work.
5. Les variantes BIOS ont montré des pertes SSH, retard d’horloge et kernel panic IO-APIC/timer. Le retest EFI avec HPET actif, 2 CPU, KVM et SATA limité à deux ports a permis un démarrage stable, puis l’installation du gestionnaire.
6. Dépôts Ubuntu HTTP injoignables, HTTPS testé 200 ; URI passées en HTTPS et IPv4/timeout/retry bornés dans la VM dédiée. Dépôt Wazuh signé accessible ; paquet installé par cloud-init. Un essai manuel concurrent a rencontré le verrou dpkg et n’a pas été forcé. L’installation existante a été laissée se terminer.
7. Archives JSON activées dans le gestionnaire (<logall_json>yes). Service actif et agent ID 001 actif. L’agent personnel s’est enrôlé auprès du nouveau serveur ; aucune édition manuelle de ossec.conf ou client.keys Windows. L’empreinte de la clé client n’a pas été relevée ni publiée.
8. Recherche dans archives.json et alerts.json sur LAB-GRC-EVT et 4625. Sept champs source/gestionnaire rapprochés exactement ; alerte retrouvée sur le même record. Revue POSIX et paramètres de conservation, sans suppression de traces ni injection de règle artificielle.

## Attendu et observé

| Sous-critère | Attendu | Observé | Preuve |
|---|---|---|---|
| Source/règles de collecte | Hôte, version, canaux, audit et destination identifiés | Source et configuration relevées ; audit existant, canal Security comprend cet événement | [T02-P01 source](preuves/20261007T195320Z/T02-P01_source.json) |
| Échec contrôlé | Tentative refusée sur compte dédié | LAB-GRC-EVT, API false, erreur 1326, 4625 | [T02-P02](preuves/20261007T195320Z/T02-P02_evenement_local.json) |
| Événement local | Compte, hôte, ID, record et UTC identifiés | Record 2204782, 2026-10-07T19:53:20.9715351Z, statut 0xc000006d/0xc000006a | T02-P02 |
| Gestionnaire/agent | Service et agent réellement connectés | 4.14.8-1 actif, agent 001 actif | [T02-P01 gestionnaire](preuves/20261007T202438Z/T02-P01_gestionnaire.json) |
| Réception | Même événement et équipement | Archives JSON ; sept champs source/gestionnaire identiques | [T02-P03](preuves/20261007T202438Z/T02-P03_reception.json), [T02-P06](preuves/20261007T202438Z/T02-P06_rapprochement.json) |
| Alerte | Règle applicable observée | Règle native 60122, niveau 5, « Logon Failure - Unknown user or bad password », même record | [T02-P04](preuves/20261007T202438Z/T02-P04_alerte.json) |
| Accès | Droits et protection examinés | Dossiers 750, fichiers 640, groupe wazuh ; lecture labgrc sans sudo refusée ; sudo permet accès et modification | [T02-P05](preuves/20261007T202438Z/T02-P05_droits_conservation.json), [P05b](preuves/20261007T202438Z/T02-P05b_parametres_retention.json) |
| Conservation | Paramètres et durée réellement vérifiés | Fichiers du jour, JSON/rotation/compression relevés ; aucune récupérabilité à 90 jours démontrée | T02-P05/P05b ; non démontré pour la durée |

## Chronologie et portée de la réception

Événement source : 2026-10-07T19:53:20.9715351Z. Réception/alerte Wazuh : 2026-10-07T20:23:19.944+0000. Écart des horodatages : 1798.972465 secondes, environ 29 min 59. L’événement avait été créé avant la disponibilité du gestionnaire puis retrouvé après connexion. Ce résultat ne mesure pas le délai habituel d’alerte, n’atteste pas la synchronisation des horloges pendant toute la préparation et ne prouve pas qu’aucun autre événement n’a été perdu.

## Conservation protection et couverture

jsonout_output=yes, alerts_log=yes, logall=no, logall_json=yes, log_alert_level=3. Le relevé montre les fichiers archives/alertes courants et datés du jour. Rotation et compression sont activées. monitord.keep_log_days=31 porte sur les **journaux internes tournés**, d’après la [documentation officielle](https://documentation.wazuh.com/current/user-manual/reference/internal-options.html#monitord) ; ce paramètre n’établit pas à lui seul la durée des archives d’événements. Aucune politique opérationnelle complète de 90 jours n’est validée. Le besoin de 90 jours reste une exigence locale du cas, pas une prescription légale.

Les droits empêchent la lecture du fichier par labgrc sans sudo ; l’opérateur sudo/root reste capable de modifier les traces. Pas de stockage immuable, séparation complète des fonctions, restauration à 90 jours ou preuve de rotation sur plusieurs jours. Une seule source Security et un événement sont démontrés ; les autres canaux configurés et le parc entier ne sont pas validés.

## Anomalies corrections et retests

Captures réelles et extraits VBox conservés dans le dossier 20261007T195320Z. Le firmware/HPET et le réseau des paquets ont été corrigés uniquement dans la VM dédiée, puis démarrage, installation et collecte ont été vérifiés. Aucune modification globale de Windows, BIOS hôte ou paramètres de sécurité n’a été réalisée ; l’alternative QEMU envisagée n’a pas été installée.

Une première lecture globale UTF-8 du journal a échoué sur un octet 0xe9 d’une autre ligne. Le harnais lit désormais chaque ligne en binaire, tente UTF-8 puis CP1252 en secours, et sélectionne seulement les champs autorisés du compte de test. La ligne de cet événement est bien UTF-8 ; sept champs restent identiques à la source. [Diagnostic export](preuves/20261007T202438Z/T02-D05_diagnostic_export.txt), [diagnostic réseau](preuves/20261007T202438Z/T02-D06_diagnostic_reseau.txt), [tentative sous verrou](preuves/20261007T202438Z/T02-D06_diagnostic_installer.txt). Les journaux bruts et autres comptes restent privés dans la VM, sans export au portfolio.

## Conclusion et reproductibilité

Le parcours Windows → agent → gestionnaire → alerte fonctionne pour cet événement après rétablissement du serveur. Les droits et paramètres sont examinés, mais la conservation longue durée et la couverture restent non démontrées : **T02 partiel**, sans modification du critère pour annoncer une réussite complète. Les tags MITRE et de conformité joints à la règle sont des métadonnées du produit ; ils ne prouvent ni une attaque réelle T1531 ni une conformité réglementaire.

Reproduction : preparer_wazuh.py, inventaire_eleve.ps1, t02_source_windows.ps1 avec compte inexistant LAB-GRC-EVT2 et les deux commutateurs explicites, puis relever_wazuh.py et completer_retention.py. Vérifier la disponibilité avant un nouvel événement ; une lecture Security élevée nécessite UAC. Les nouvelles pièces sont datées et ne remplacent pas les précédentes. Aucun nouveau clic n’a été nécessaire pour retrouver l’événement initial.
