# Sources et limites de vérification

**Version 1.0 - 7 octobre 2026**

## Sources officielles

| Référence | Source primaire | Utilisation dans le portfolio |
|---|---|---|
| SRC01 | [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) | Référence des exigences de SMSI ; distinction entre étude de cas et certification |
| SRC02 | [ISO/IEC 27002:2022](https://www.iso.org/standard/75652.html) | Guide de mesures de sécurité ; les mesures retenues répondent aux risques du cas |
| SRC03 | [ISO/IEC 27005:2022](https://www.iso.org/standard/80585.html) | Référence de gestion des risques SSI ; notre échelle et nos seuils sont des choix locaux |
| SRC04 | [ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/standard/88435.html) | Existence de l'amendement relatif au climat |
| SRC05 | [Communiqué conjoint ISO/IAF, février 2024](https://www.iso.org/files/live/sites/isoorg/files/standards/popular_standards/management_systems/ISO-IAF%20Joint%20Communique%20Feb%202024.pdf) | Prise en compte du climat dans l'analyse du contexte et des parties intéressées |
| SRC06 | [NIST CSF 2.0, CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) | Vérification des identifiants de sous-catégories utilisés dans les deux projets |
| SRC07 | [NIST Organizational Profiles](https://www.nist.gov/cyberframework/profiles) | Comparaison actuel/cible et suivi des écarts |
| SRC08 | [NIST SP 1305, guide C-SCRM](https://csrc.nist.gov/pubs/sp/1305/final) | Lien entre diligence fournisseur, criticité, exigences et suivi |
| SRC09 | [CNDP : transfert de données à l'étranger](https://www.cndp.ma/transfert-de-donnees-a-letranger/) | Point de vérification du projet d'hébergement et de support à l'étranger |
| SRC10 | [BSI : présentation de la révision ISO/IEC 27002](https://www.bsigroup.com/globalassets/localfiles/en-my/event/2022-event/iso-iec-27002-revision-slides-deck.pdf) | Recoupement public de références de mesures ; support informatif, pas remplacement de la norme |

Les résumés du portfolio sont rédigés pour le cas. Les textes normatifs complets ne sont pas reproduits.

## Ce qui est vérifié et ce qui reste à vérifier

Les fiches officielles ISO confirment les éditions utilisées et le rôle des trois normes. Les pages et publications NIST consultées confirment les sous-catégories sélectionnées. Le communiqué ISO/IAF documente l'ajout des considérations climatiques.

SRC10 a été identifié dans les résultats publics pour recouper certains repères. Son contenu intégral n'a pas été contrôlé ; il n'est pas utilisé pour affirmer une vérification exhaustive des vingt mesures.

L'intégralité des normes ISO sous licence n'a pas été fournie. Les correspondances de clauses et de mesures sont des repères de travail, avec libellés reformulés. Avant un audit professionnel, un examen de certification ou une déclaration de conformité, relire les textes autorisés et vérifier le référentiel applicable.

La sélection de vingt mesures dans l'extrait de SoA n'est pas une revue complète de l'annexe A. Aucune mesure omise de cet extrait n'est déclarée non applicable.

Le profil NIST est volontairement limité à treize sous-catégories. Il ne constitue pas une couverture de tout le CSF. Aucune note de maturité inventée n'est attribuée au NIST.

Le projet fournisseur utilise en complément huit sous-catégories GV.SC, sans prétendre évaluer toute cette catégorie. Les correspondances ISO et NIST décrivent des rapprochements de travail, pas une certification de couverture.

L'analyse CNDP est limitée au signalement d'un point à examiner : finalités, catégories de données, destinations, accès à distance et formalités applicables. Une certification ISO, un contrat ou une localisation européenne ne démontrent pas à eux seuls la licéité d'un transfert. Aucun dossier CNDP ni avis juridique réel n'a été établi.

## Sources internes de l'exercice

| Source | Nature | Portée |
|---|---|---|
| Contexte Atlas Services | Hypothèse créée pour l'exercice | Effectifs, activités, actifs, contraintes et besoins |
| E01 à E10 | Documents fictifs écrits pour l'atelier | Conclusions documentaires du projet 1 |
| V01 à V09 | Documents et déclarations fictifs | Conclusions documentaires du projet 2 |
| Rapport de stage Tanger Med fourni par Anas | Document utilisateur réel | Observation historique H01 exclusivement |

Le document réel est « rapport stage.pdf », fourni par Anas. Les sections pertinentes décrivent le périmètre du laboratoire, les essais contrôlés, les faux positifs, la répartition du travail et les limites du prototype.

Aucun certificat, signature, logo de certification, numéro d'accréditation ou preuve fournisseur réelle n'a été fabriqué. V09 est une fiche narrative de vérification d'allégation, pas un faux certificat ISO.

## Choix de méthode propres au cas

Les éléments suivants sont des conventions pédagogiques, et non des prescriptions ISO ou NIST : douze risques internes, vingt questions fournisseur, huit risques fournisseur, vingt mesures dans l'extrait de SoA, quatre tests manuels, cotation 1 à 5, seuils d'acceptation, exigences MFA, durées de conservation et délais de remédiation.

Le délai de notification fournisseur de 24 heures est une exigence contractuelle proposée dans l'exercice. Ce document ne le présente pas comme un délai légal marocain.

## Sources techniques et nouvelle revue du 07/10/2026

- [Keycloak 26.8 OpenJDK](https://www.keycloak.org/getting-started/getting-started-zip), [administration](https://www.keycloak.org/docs/26.8.0/server_admin/) et [TLS](https://www.keycloak.org/server/enabletls) : composant réel, OTP, rôles et sessions ; seules les fonctions testées sont revendiquées.
- [Release Keycloak](https://github.com/keycloak/keycloak/releases/tag/26.8.0) et [Temurin 25](https://github.com/adoptium/temurin25-binaries/releases/tag/jdk-25.0.4.1%2B1) : téléchargements officiels ; empreintes attendues et observées dans T01-P01.
- [Wazuh Windows log collection](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/configuration.html), [image VM](https://documentation.wazuh.com/current/deployment-options/virtual-machine/virtual-machine.html) et [Microsoft 4625](https://learn.microsoft.com/windows/security/threat-protection/auditing/event-4625) : source, réception et alerte T02 prouvées ; conservation longue durée non démontrée.
- [Python zipfile](https://docs.python.org/3/library/zipfile.html) et [Git git-show](https://git-scm.com/docs/git-show) : mécanismes locaux T03/T04.

Les fiches publiques ISO 27001/27002/27005, CSF 2.0 et SP 1305 ont été revues. Les textes ISO complets restent non fournis ; cette revue ne prétend pas vérifier exhaustivement toutes leurs exigences. Les preuves techniques se trouvent dans [la matrice](Annexes_laboratoire/MATRICE_PREUVES.md), séparées de E/V et H01.

- [Installation Wazuh manager](https://documentation.wazuh.com/current/installation-guide/wazuh-server/step-by-step.html), [journaux et archives](https://documentation.wazuh.com/current/user-manual/manager/event-logging.html), [options internes](https://documentation.wazuh.com/current/user-manual/reference/internal-options.html#monitord), [Ubuntu officiel daté](https://cloud-images.ubuntu.com/noble/20260926/) et [manuel VirtualBox 7.1](https://docs.oracle.com/en/virtualization/virtualbox/7.1/user/EN-VBOX-7-1-USER.pdf) : préparation/diagnostic T02. Paramètres observés séparés d’une preuve de conservation durable.
