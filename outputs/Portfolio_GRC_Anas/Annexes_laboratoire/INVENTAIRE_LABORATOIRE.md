# Inventaire du laboratoire et modifications

**Version 1.1 - opérations réelles du 07/10/2026. Horodatages techniques en UTC.**

Exécution automatisée par Codex sur le poste personnel d’Anas. Les preuves sont réelles ; elles ne décrivent ni Atlas Services ni SupportCloud. Les pièces E/V restent simulées.

## Inventaire initial en lecture seule

Pièce : [inventaire_initial.json](preuves/INVENTAIRE/inventaire_initial.json), relevé 2026-10-07T19:28:39.6728628Z.

- Windows 11 Professionnel, version 10.0.26300 ; processeur 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz, quatre cœurs et huit processeurs logiques.
- Mémoire visible : 19.73 Gio ; libre lors du relevé : 9.28 Gio.
- Volume C libre lors du relevé : 44.17 Gio. La mémoire et l’espace libre varient pendant l’usage.
- Git 2.48.1 ; VirtualBox 7.1.10r169112 ; agent Wazuh 4.14.6 installé, service WazuhSvc actif.
- Quatre VM enregistrées : Kali, Metasploit Ubuntu, Metasploit Windows et Windows 11 Forensic ; aucune VM en cours. Leur fonctionnement et leurs identifiants ne sont pas vérifiés.
- Metasploit Ubuntu est arrêtée, configurée avec 2 Gio, 2 CPU, NAT et réseau interne ; redirection SSH sur 127.0.0.1:2222. Aucun démarrage ni changement n’a été effectué.
- WSL indique qu’il n’est pas installé. Aucune distribution Linux utilisable n’est démontrée.
- Java, Docker et Keycloak n’étaient pas dans PATH ; l’examen des répertoires et des logiciels n’a pas identifié de composant réutilisable pour T01. Cela n’est pas un inventaire exhaustif de tout le disque.
- Inventaire initial non élevé : accès refusés. Inventaire élevé ultérieur réussi : destination Wazuh 192.168.56.10:1514/TCP, canaux et audit relevés, serveur injoignable. [Relevé élevé](preuves/INVENTAIRE/inventaire_eleve.json).
- Adresses privées relevées pour Wi-Fi et interfaces virtuelles ; aucune recherche de cibles de stage ou d’entreprise. La destination est le réseau host-only VirtualBox du laboratoire ; aucun système externe n’est utilisé.

## Modifications effectivement effectuées

| Modification | Périmètre | Trace et réversibilité |
|---|---|---|
| Copie intégrale de référence | 18 Markdown et CV cible | reference_v1_20261007T192733Z ; empreintes REFERENCE_MANIFEST.json ; original CV cible conservé |
| Nouveau dépôt Git | execution_20261007T192733Z/T04_secrets_git | Deux commits, identité Git locale example.invalid ; aucun distant |
| Archive et restauration | execution_20261007T192733Z/T03_sauvegarde_restauration | Trois fichiers artificiels, copie ZIP, restauration distincte ; originaux conservés |
| Keycloak et Java portables | T01_acces_mfa | Keycloak 26.8.0 et Temurin 25.0.4.1+1 ; SHA-256 téléchargements vérifiés ; aucune installation système Java |
| TLS et restriction d’écoute | Keycloak | 127.0.0.1:18443 uniquement ; HTTP arrêté ; certificat local 30 jours, clé privée sous ACL restreintes |
| Identités et politique IAM | Realm grc-lab dédié | LAB-ADMIN, LAB-LECTEUR, TOTP obligatoire à l’inscription ; LAB-RECOVERY master pour mise en place/récupération locale |
| Protection des secrets de laboratoire | Dossier T01 | Héritage ACL retiré ; utilisateur courant, SYSTEM et Administrateurs autorisés ; secrets exclus de la livraison |
| Dépendances de test HTTP | python_deps dédié | requests 2.34.2, beautifulsoup4 4.15.0 ; notice de reproduction |
| Inventaire élevé et événement T02 | PowerShell | UAC initialement annulée puis acceptée ; compte LAB-GRC-EVT créé puis désactivé, échec 4625 enregistré ; configuration/audit Windows préservés |
| Nouvelle VM de gestionnaire | VirtualBox, work/T02 | Ubuntu officiel vérifié, image 20 Gio, 2 Gio RAM ; variantes de CPU/horloge/firmware documentées ; snapshot initial préservé |

## État final T02 et modifications du gestionnaire

Gestionnaire Wazuh 4.14.8-1 actif et agent 001 actif observés ; source, réception et alerte 60122 concordantes. Retest VM réussi avec EFI, HPET actif, 2 CPU, KVM, SATA deux ports. URI des dépôts Ubuntu passées à HTTPS et IPv4/timeout/retry bornés ; archives JSON activées dans le nouveau gestionnaire. Enrôlement automatique de l’agent existant, sans édition manuelle de la destination Windows ni de client.keys ; clé client non exportée. Configuration/droits et paramètres examinés, sans démonstration de 90 jours. Les essais BIOS, l’erreur d’encodage du harnais, la tentative sous verrou dpkg et les retests restent visibles. QEMU n’a pas été installé. Voir T02-P01/P03/P04/P05/P05b/P06 et la fiche.

## Conservation et partage

Les distributions portables, la VM et les secrets restent dans work. La livraison contient seulement scripts sans secrets, preuves sélectionnées, archive de tickets artificiels et documents. Aucun binaire de stage, certificat privé, seed TOTP, jeton ou mot de passe n’est intégré. Les données sont conservées pour la reproduction ; aucun nettoyage destructif n’a été effectué.
