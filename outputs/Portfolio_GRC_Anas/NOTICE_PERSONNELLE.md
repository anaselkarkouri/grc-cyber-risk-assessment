# Relancer les tests et présenter le portfolio

**Anas El Karkouri - 07/10/2026.**

## Ce que je peux dire

« J’ai préparé deux études de cas simulées avec assistance : douze risques SSI et huit risques fournisseur, avec preuves attendues, constats et traitements. Le laboratoire a vérifié les rôles, le MFA TOTP et les sessions sur Keycloak, la restauration de trois fichiers avec SHA-256, et la persistance d’un marqueur Git dans un ancien commit. Le parcours Windows vers Wazuh et une alerte native sont prouvés ; la conservation longue durée et la couverture du parc restent non démontrées. Je débute dans les référentiels et je sais préciser la portée de chaque preuve. »

La chaîne Tanger Med était un travail collectif sur ordinateurs personnels et VM. Deux essais bénins et des faux positifs sont documentés, sans taux de détection ni déploiement en production. Le CV final conserve cette portée et les deux certificats de participation ; aucune certification ISO acquise n’est ajoutée.

## Reproduction locale

Les scripts sont dans scripts_laboratoire de la livraison et dans work/grc_laboratoire/scripts de la mission. Les chemins ROOT de leurs versions sources désignent la racine originale ; les copies livrées ont une notice d’adaptation. Utiliser Python, Git et PowerShell ; pour les tests HTTP, installer requests et beautifulsoup4 dans python_deps dédié. Aucun secret ne doit être copié dans outputs.

1. tests_locaux.py : crée un dossier daté nouveau ; exécute T04 puis T03 ; sauvegarde la référence et les preuves. Il n’efface ni dépôt existant ni données originales.
2. prepare_keycloak.py : télécharge une distribution officielle et un JDK portable dans T01, vérifie SHA-256 et limite les ACL ; crée des mots de passe aléatoires locaux. Les scripts de préparation livrés épinglent désormais les versions et les empreintes observées 26.8.0/25.0.4.1+1 ; cette modification de reproductibilité ne prétend pas être un nouveau test.
3. start_keycloak.py : démarre le service uniquement en HTTPS 127.0.0.1:18443. Vérifier la disponibilité ; ne pas lancer une seconde instance sur la même base. Le certificat local expire après 30 jours ; renouveler uniquement les fichiers dédiés et conserver la trace si nécessaire.
4. test_keycloak.py : utilise les secrets sous ACL dans work, crée/réutilise exclusivement grc-lab, vérifie les réponses serveur et produit un dossier de preuves daté. Il révoque les sessions de LAB-ADMIN en fin de test. Un mot de passe ou seed manquant nécessite réenrôlement local propre, jamais un résultat inventé.
5. T02 : préparer/réutiliser uniquement GRC-Wazuh-T02-20261007. Le script livré choisit désormais EFI/HPET/SATA deux ports ; modifications de reproductibilité non présentées comme une nouvelle installation. Garder les deux NIC et les MAC correspondantes à cloud-init. Vérifier Wazuh/agent actifs via inspecter_wazuh.py avant de produire un nouveau 4625. inventaire_eleve.ps1 et t02_source_windows.ps1 nécessitent PowerShell administrateur ; -Compte LAB-GRC-EVT2 doit désigner un compte inexistant. Utiliser -Evenement -GestionnaireLaboratoireConfirme uniquement sur ce laboratoire. relever_wazuh.py filtre les comptes de test et completer_retention.py relève les paramètres. Le premier SSH accepte la clé hôte par TOFU puis les exports la vérifient ; contrôler l’empreinte console avant usage sur une autre installation. Les problèmes de dépôts peuvent être examinés par depanner_wazuh.py ; ne jamais contourner un verrou dpkg. Ne pas relancer une préparation sur une VM existante sans en vérifier le nom, l’état et la conservation des données. La réception d’un événement ne valide pas 90 jours de conservation.
6. Conserver chaque résultat initial, erreur, correction et retest. Refaire MANIFEST_FINAL après toute modification et actualiser fiche, protocole, README, VERIFICATION et CV si le statut change.

## Arrêt et conservation

Le service Keycloak est un processus portable. Pour l’arrêter, identifier seulement java.exe dont le chemin absolu commence par le dossier T01 du laboratoire, puis arrêter ce PID. Ne pas arrêter toutes les JVM du poste. Les quatre VM initiales n’ont pas été lancées ; la nouvelle VM de test possède les preuves et données privées. Pour l’arrêter proprement : connexion SSH au seul gestionnaire, sudo shutdown -h now, puis vérifier son état VirtualBox. Pour le redémarrer : VBoxManage startvm GRC-Wazuh-T02-20261007 --type headless, attendre le service et l’agent actifs. Les données et distributions sont conservées ; avant tout nettoyage, vérifier que chaque cible résolue reste sous work/grc_laboratoire et garder les pièces nécessaires.

## Expliquer une décision en entretien

Choisir R03 : sept jobs annoncés ne prouvent pas une restauration ; trois fichiers locaux prouvent leur récupération uniquement. Choisir S08 : correctif annoncé sans retest maintient le risque 16 et bloque la production ; R08 est le même scénario. Choisir Q17 : certificat non fourni signifie certification non démontrée, pas inexistante. Expliquer que 24 h/90 jours/30 jours sont des besoins locaux à négocier, puis nommer les preuves nécessaires avant une nouvelle décision.

## Registres éditables

Le XLSX reprend la référence fictive. V/I sont modifiables et scores/niveaux se recalculent ; les cibles restent conditionnelles. Les actions disposent de champs de pièce reçue, date de vérification et suivi. Remplir une pièce seule ne valide pas automatiquement une action ni une condition. Toute nouvelle cotation exige justification et répercussion dans les Markdown/synthèses ; le tableur ne les modifie pas automatiquement.
