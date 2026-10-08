# Projet 2 - Constats et registre des risques fournisseur

**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**  
**Évaluation de l'usage cible en production, formule Standard.**

## 1. Du justificatif au risque

Les constats F01 à F08 rapprochent une exigence du client et des pièces V01 à V09. Les risques S01 à S08 décrivent un événement cyber et ses conséquences. Un constat documentaire n'est pas, à lui seul, un scénario de risque.

Le fournisseur n'est actuellement utilisé que dans un pilote artificiel. Les scores ci-dessous sont **prospectifs pour la production avec des données clients**, en conservant les conditions décrites au 7 octobre. Ils ne représentent pas le risque actuel d'une production déjà existante.

« Écart » signifie écart au besoin défini pour ce cas. « Non démontré » signifie que la pièce ne permet pas d'établir un résultat. Aucun constat n'est présenté comme une non-conformité de certification ISO.

## 2. Huit constats documentaires

| Constat | Critère du cas | Pièces et questions | Analyse motivée | Conséquence et traitement |
|---|---|---|---|---|
| F01 - Authentification du tenant | Administrateurs client nominatifs et MFA imposé | V03 ; Q05/Q06 | Les rôles sont décrits, mais le MFA reste facultatif en Standard. Écart explicite à l'obligation recherchée ; les fonctions Enterprise ne compensent pas cet écart | S01 ; VM01 ; vérifier obligation et récupération sur le tenant retenu |
| F02 - Accès support fournisseur | Accès privilégiés nominatifs, MFA et revue traçable | V03 ; Q07/Q08 | SUPPORT-PARTAGE est utilisé par plusieurs opérateurs sans MFA imposé. Cet écart est décrit dans la pièce. La revue trimestrielle est annoncée mais son fonctionnement n'est pas démontré | S02 ; VM02 ; population complète, suppression du partage et revue documentée |
| F03 - Journaux et investigation | Événements utiles conservés 90 jours et protégés, ou équivalence démontrée | V04 ; Q10/Q11 | L'historique Standard est limité à trente jours. L'export partiel et sa protection ne sont pas démontrés. Écart sur la durée ; incertitude sur complétude, intégrité et accès | S03 ; VM03 ; obtenir une solution utile à l'investigation et la tester |
| F04 - Reprise du service | RTO huit heures et RPO 24 heures pour le service complet, objectifs métier à confirmer | V05/V08 ; Q14/Q15 | L'exercice de six heures couvre des fichiers, pas la base, les index ou l'authentification. Il ne démontre ni reprise SaaS complète ni RPO. L'export ne constitue pas encore une solution de secours exploitable | S04 ; VM04 ; restaurer le périmètre complet et vérifier les données récupérables |
| F05 - Accès et sous-traitants | Cartographie complète des lieux et tiers accédant aux données, responsabilités et changements | V01/V07 ; Q03/Q04 | Le support Maroc/Portugal et un partenaire incomplet limitent l'allégation « Europe uniquement ». La cartographie est partielle. Cela n'établit pas un transfert illicite, mais empêche une évaluation éclairée | S05 ; VM05 ; compléter le dossier et le faire examiner par RJ |
| F06 - Sortie et suppression | Export complet utilisable, trente jours de récupération proposés, suppression maîtrisée | V08 ; Q15/Q16 | Accès 48 heures dans le projet, export des pièces non démontré, exceptions de conservation inconnues. Écart sur la fenêtre ; incertitudes sur export et fin de traitement | S06 ; VM06 ; contrat de sortie, test d'export et assurance de suppression proportionnée |
| F07 - Coordination d'incident | Première notification sous 24 heures après confirmation d'un incident affectant le client, contacts et coordination | V02/V08 ; Q18/Q20 | La politique prévoit 72 heures. Aucun exercice coordonné n'est fourni. Écart contractuel proposé, pas constat d'infraction à une loi ; coordination non démontrée | S07 ; VM07 ; clause négociée et exercice de table documenté |
| F08 - Isolation inter-clients | Aucun défaut ouvert permettant un accès non autorisé aux données clients avant production | V06 ; Q12/Q13 | Le défaut d'autorisation demeure ouvert. Un correctif annoncé sans retest ne suffit pas. La portée limitée du rapport interdit une conclusion sur tout le service | S08 ; VM08 ; correction et retest avant toute donnée réelle |

### Assurance transversale : allégation ISO

Q17 et V09 ne démontrent pas une certification actuelle couvrant le service. Cette limite doit être portée à la décision et clarifiée. Elle n'est ni un neuvième risque automatique, ni une preuve d'absence de sécurité.

Un certificat valide et pertinent pourrait compléter le dossier. Il ne ferait pas disparaître le défaut ouvert de V06, ne prouverait pas le respect du contrat Standard et ne remplacerait pas les tests ciblés.

## 3. Convention de cotation

Appliquer la [méthode du projet 1](../Projet_1_SSI/02_methode_registre_risques.md) : vraisemblance V et impact I sur une échelle ordinale de 1 à 5 ; score V × I.

| Score | Niveau local |
|---|---|
| 1 à 4 | Faible |
| 5 à 9 | Modéré |
| 10 à 15 | Élevé |
| 16 à 25 | Critique |

Les indices ne sont pas des probabilités statistiques ni des montants financiers. Les conséquences évaluées restent la confidentialité, l'intégrité, la disponibilité et la capacité à répondre à un incident cyber.

L'horizon est les douze premiers mois d'un éventuel usage en production, selon la convention du projet 1. La vraisemblance reste un jugement motivé et non une fréquence annuelle calculée.

Le risque inhérent représente le scénario avant les mesures considérées. Le risque actuel estimé tient compte des mesures décrites et de leurs limites. Le risque cible suppose un traitement effectivement mis en œuvre et vérifié. **Aucune réévaluation du résiduel fondée sur des preuves de traitement effectif n'est disponible.**

## 4. Registre renseigné

RS est le propriétaire métier des huit risques. Les pilotes des traitements et les propriétaires des actifs sont distingués dans le plan de remédiation. Le fournisseur traite les composants relevant de sa responsabilité ; il ne décide pas seul de l'acceptation du client.

| ID | Événement cyber et effet sur les actifs | Inhérent V/I/score | Actuel estimé V/I/score | Niveau actuel | Cible conditionnelle V/I/score | Preuves et traitement |
|---|---|---|---|---|---|---|
| S01 | Compromission d'un administrateur du tenant sans MFA imposé ; consultation ou modification de tickets et données A08 | 4/4/16 | 3/4/12 | Élevé | 1/4/4 | V03, F01, VM01 |
| S02 | Compromission ou usage abusif du compte support partagé ; accès aux données A08 et attribution des actions difficile | 4/4/16 | 3/4/12 | Élevé | 1/4/4 | V03, F02, VM02 |
| S03 | Incident détecté tardivement et traces utiles expirées ou incomplètes ; investigation et confinement du tenant A08 retardés | 3/4/12 | 3/4/12 | Élevé | 2/4/8 | V04, F03, VM03 |
| S04 | Incident destructif ou altération du service suivis d'une reprise incomplète ; tickets A08 indisponibles ou données non récupérées | 3/4/12 | 3/4/12 | Élevé | 2/4/8 | V05/V08, F04, VM04 |
| S05 | Accès aux tickets A08 par un tiers insuffisamment identifié ou encadré ; divulgation non autorisée et difficulté de maîtrise du traitement | 3/4/12 | 3/4/12 | Élevé | 2/4/8 | V01/V07, F05, VM05 |
| S06 | Perte ou persistance non maîtrisée de données A08 lors d'une sortie ; export incomplet, accès trop court ou copies encore accessibles | 3/4/12 | 3/4/12 | Élevé | 2/4/8 | V08, F06, VM06 |
| S07 | Incident confirmé affectant le client mais notification et coordination tardives ; exposition prolongée et réponse client retardée | 3/4/12 | 3/4/12 | Élevé | 2/4/8 | V02/V08, F07, VM07 |
| S08 | Consultation inter-clients non autorisée de tickets A08 via le défaut applicatif ouvert ; divulgation de données confidentielles | 4/4/16 | 4/4/16 | Critique | 2/4/8 | V06, F08, VM08 ; miroir de R08 |

Tous les risques sont **ouverts**. Les scores cibles ne constituent pas des niveaux déjà atteints.

## 5. Justification des évaluations

### S01 - Authentification client

Le rôle lecteur et la séparation annoncée des droits réduisent l'exposition par rapport à l'absence de toute restriction ; une vraisemblance actuelle de 3 est retenue provisoirement. Cette réduction limitée repose sur la conception déclarée, pas sur un essai opérationnel. La confiance est donc moyenne.

Un administrateur compromis conserve un effet potentiel important, I = 4. Le passage cible à V = 1 exige MFA imposé, récupération contrôlée, revue des administrateurs et tests positifs/négatifs. Il ne signifie pas impossibilité d'attaque ou absence de risque de session.

### S02 - Compte support

Les comptes techniques nominatifs sont décrits comme protégés, mais le compte partagé demeure une voie d'accès. La protection d'une partie de la population justifie une réduction limitée de 4 à 3 ; le MFA universel n'est pas présumé. Confiance moyenne sur la population, élevée sur l'écart explicitement décrit dans V03.

La cible V = 1 exige suppression du compte partagé, comptes individuels, authentification renforcée, restriction des accès support et traces nominatives vérifiées. L'impact reste 4.

### S03 - Traces et investigation

Le scénario associe incident cyber et besoin d'historique au-delà de trente jours. Les journaux annoncés ont une utilité partielle mais n'établissent pas une investigation complète. V = 3 est un jugement pédagogique lié à cet usage, pas une conséquence automatique de la durée.

L'impact 4 correspond à une réponse compromise sur des données clients. La cible V = 2 suppose collecte utile, protection et conservation vérifiées ; aucune automatisation d'export n'est créée dans ce projet.

### S04 - Reprise

Un job réussi et un exercice limité aux fichiers ne prouvent pas la reprise de l'application. L'efficacité de reprise n'est donc pas retenue comme réduction du score dans ce cas. Cela ne veut pas dire qu'aucune sauvegarde n'existe.

V = 3 décrit la possibilité d'un incident destructif sur le service critique ; I = 4 décrit l'interruption et la perte de tickets envisagées. La confiance dans le RTO/RPO est faible. La cible V = 2 porte sur la probabilité du scénario composé « incident puis reprise insuffisante », à réévaluer après exercice complet.

### S05 - Tiers et données

L'existence d'accès support et d'un partenaire non identifié crée une exposition à examiner. Le manque d'identité, de localisation et de responsabilités diminue l'assurance ; il n'établit ni abus réel ni violation de droit.

V = 3 et I = 4 sont retenus pour un accès à des données confidentielles en production. Confiance moyenne sur l'exposition, faible sur l'encadrement. Une cartographie seule ne réduit pas le risque : la cible exige aussi vérification des droits, restrictions, responsabilités et changements.

### S06 - Fin de relation

Les 48 heures contractuelles et l'absence d'export des pièces démontré rendent plausible une sortie incomplète. Une copie persistante reste un scénario de confidentialité, pas une fuite observée.

V = 3 et I = 4 reflètent dépendance et sensibilité du service. La cible suppose un export exploitable testé, une fenêtre suffisante convenue et une suppression encadrée avec preuve adaptée. Une promesse d'attestation n'est pas une preuve reçue.

### S07 - Incident fournisseur

Le fournisseur annonce un plan, mais le délai proposé de 72 heures peut retarder les mesures client. Le besoin de 24 heures est local et reste à négocier. L'absence d'exercice fourni n'établit pas l'absence de tout entraînement fournisseur.

Le scénario de délai de réponse retient V = 3 et I = 4. La cible V = 2 exige clause acceptée, contacts disponibles et exercice coordonné. Une clause seule ne démontre pas le comportement réel.

### S08 - Isolation des clients

V06 décrit une faiblesse ouverte donnant accès à un autre client dans le scénario. V = 4 est motivé par une voie d'accès concrète, I = 4 par les données confidentielles exposables. Aucun taux d'exploitation, volume d'incident ou score CVSS n'est inventé.

La cible V = 2 suppose correction et retest couvrant les droits et tenants concernés. Le retest serait une preuve ciblée ; il n'établirait pas l'absence de toute autre vulnérabilité. **Sans cette preuve, le risque reste 16 et la production reste bloquée.**

## 6. Lecture consolidée

L'usage cible comporte **un risque critique et sept risques élevés** dans le dossier actuel. Les cibles comporteraient **deux risques faibles et six risques modérés**, si tous les traitements sont mis en œuvre et vérifiés.

Les risques peuvent se recouper : S01/S02/S08 affectent les mêmes données, S03/S07 influencent la réponse. Les scores ne sont ni additionnés ni convertis en une probabilité globale de compromission.

Le registre du projet 1 reprend S08 sous R08 : score actuel 16, cible 8. Il s'agit du même scénario vu au niveau de la PME. Ne pas compter deux fois cet événement.

## 7. Réévaluation et acceptation

Chaque nouvelle pièce doit préciser sa date, la formule, le périmètre, la population et les limites. L'évaluateur vérifie sa pertinence, RS réévalue le scénario, DG décide selon les conditions de production.

Le défaut inter-clients n'est pas accepté pour une production avec données réelles. Un traitement seulement prévu n'autorise pas l'utilisation du score cible.

**État du dossier : décision de production défavorable en l'état ; remédiation ouverte ; aucune acceptation signée.**

## Références

[ISO/IEC 27005:2022](https://www.iso.org/standard/80585.html) pour la gestion des risques SSI ; [NIST SP 1305](https://csrc.nist.gov/pubs/sp/1305/final) pour la démarche fournisseur. La méthode de cotation et les jugements du registre sont propres à l'exercice.
