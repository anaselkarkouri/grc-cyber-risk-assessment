# Protocoles des tests et observation historique

**Version 1.1 - 07/10/2026. Quatre tests exécutés : trois réussites bornées ; T02 partiel.**

La version 1.0 des protocoles est conservée dans la copie initiale. La mission actuelle autorise explicitement code et configurations utiles. Les critères sont conservés ; les étapes peuvent être automatisées si elles produisent une preuve réelle. Aucun système de stage, compte principal ou service fictif n’est ciblé.

## T01 Accès MFA et sessions

R01/M01/C01. Service standard réel avec rôles, MFA imposé et révocation ; LAB-ADMIN et LAB-LECTEUR. Relever versions/règles ; accès lecteur permis et administration refusée ; administration permise ; nouvelle session mot de passe seul insuffisante ; mauvais OTP refusé et bon OTP accepté ; révocation suivie de refus ou réauthentification ; récupération et exceptions examinées. Pièces T01-P01 à P04. [Résultats et limites](../Annexes_laboratoire/T01_RESULTATS.md). **RÉUSSI** dans le realm Keycloak dédié ; récupération examinée mais exercice complet non démontré.

## T02 Événement collecte et SIEM

R04/M04/C02. Source Windows, compte artificiel, agent et Wazuh personnel accessibles. Identifier horloges et canaux ; produire un échec contrôlé ; relever localement l’événement puis retrouver même hôte/compte/ID/période dans Wazuh ; examiner alerte selon règle, sources, droits, conservation et protection. Conserver les résultats initiaux et documenter toute modification de collecte/règle avant retest. Pièces T02-P01 à P05. **PARTIEL** : [source, réception et alerte prouvées ; limites de conservation](../Annexes_laboratoire/T02_RESULTATS.md). Le relevé d’un service actif ne remplace pas la réception.

## T03 Sauvegarde restauration

R03/M03/C03. Au moins trois données artificielles connues, contenus/tailles/SHA-256 avant copie ; sauvegarde réelle identifiée et datée ; restauration séparée ; comparaison de chaque élément ; durée et âge de copie ; revue des droits. Vérifier tous les chemins avant modification/suppression, préserver l’échec éventuel puis corriger et retester. Pièces T03-P01 à P04. **RÉUSSI** : [résultats ZIP de trois fichiers](../Annexes_laboratoire/T03_RESULTATS.md). RTO/RPO du service non démontrés.

## T04 Secrets Git

R06/M06/C04. Nouveau dépôt local exclusivement dédié ; seul marqueur SECRET-DEMO-NON-UTILISABLE ; commit initial, retrait et nouveau commit ; constater absence courante et présence ancienne par Git réel ; revoir ACL locales ; écrire procédure de vraie exposition. Pièces T04-P01 à P04. **RÉUSSI** : [résultats et historique](../Annexes_laboratoire/T04_RESULTATS.md). Aucune vraie clé, rotation ou revue GitHub démontrée.

## Fiche et traçabilité

Chaque fiche en annexe contient objectif, date/versions/comptes, prérequis, étapes, attendu/observé, pièces, statut, diagnostics/retests, conclusion bornée et reproduction. L’opérateur est l’automatisation Codex ; l’appropriation personnelle reste à réaliser. Le cas E/V, les scores et les actions ne sont pas automatiquement modifiés par les tests. Les cibles demeurent conditionnelles.

## 7. H01 - Observation historique du stage Tanger Med

**Nature : lecture d'un document utilisateur réel, pas reproduction du test.**

Le rapport de stage fourni décrit une chaîne ClamAV/YARA/CAPEv2/Wazuh sur des ordinateurs personnels et des VM, avec Sysmon et Tailscale.

Repères vérifiés dans l'exemplaire fourni : section 1.5 « Périmètre et exclusions », page PDF 19 ; chapitre 5 « Tests, validation et résultats », pages PDF 55 à 61 ; section 6.1 « Répartition collaborative », pages PDF 62 à 63. Les intitulés permettent de retrouver les passages si une autre version du rapport est utilisée.

Le rapport décrit notamment un essai avec calc.exe le 24 août 2026 et un script PowerShell bénin contenant des commentaires déclenchant un motif YARA. Il présente les événements Wazuh, l'analyse des faux positifs et les limites des essais.

### Conclusion utilisable

Le rapport documente une intégration de laboratoire et l'observation de résultats SIEM pour les scénarios décrits. Il permet d'expliquer une chaîne de preuves : fichier, empreinte, tâche sandbox, rapport, événement et décision.

### Conclusions non établies par H01

H01 ne démontre pas un déploiement sur les systèmes de TMPA, un taux de détection, une analyse sur un corpus de malwares réels, les quatre nouveaux tests T, la conformité d'un contrôle de toute une organisation ou une expérience opérationnelle complète d'analyste SOC.

Les contributions sont collectives. Anas doit distinguer ses scripts d'orchestration, son intégration API et son travail Wazuh des installations principalement réalisées par son partenaire.

Le dossier de stage n'est pas recopié dans le portfolio public : ses captures et données doivent être examinées avant toute publication.
