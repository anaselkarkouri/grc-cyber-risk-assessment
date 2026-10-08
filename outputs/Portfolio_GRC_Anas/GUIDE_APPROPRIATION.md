# Guide d'appropriation du portfolio

**Anas El Karkouri - préparation d'un PFE GRC cyber / audit SSI / Cyber Risk**  
**Version 1.1 - 07/10/2026**

## 1. Ton point de départ

Tu débutes sur les référentiels GRC et tu as un socle technique issu de tes stages et du laboratoire SOC. C'est un point de départ cohérent pour un projet étudiant. Les documents livrés ne suffisent cependant pas à prouver une maîtrise personnelle : tu dois comprendre les choix, les vérifier et savoir les modifier.

Le portfolio comporte deux analyses documentaires renseignées. Les entreprises, incidents hypothétiques et justificatifs E/V sont fictifs. Quatre tests ont des opérations réelles documentées : trois réussites bornées et T02 partiel : source, réception et alerte prouvées ; durée de conservation non démontrée.

Le travail personnel le plus utile consiste maintenant à reprendre les décisions, refaire quelques cotations, trouver les limites des preuves et produire les résultats réels du laboratoire lorsque celui-ci sera disponible.

## 2. Référentiels à étudier

| Référence | Ce que tu dois comprendre pour ces projets | Application immédiate |
|---|---|---|
| ISO/IEC 27001:2022, avec l'amendement 2024 à connaître | Organisation d'un SMSI : contexte, responsabilités, risques, objectifs, pilotage, évaluation et amélioration | Périmètre, PSSI proposée, responsables et limites de l'étude |
| ISO/IEC 27005:2022 | Construire, évaluer, traiter et suivre un scénario de risque SSI | Registres R et S, vraisemblance, impact, risque actuel/cible |
| ISO/IEC 27002:2022 | Comprendre les mesures et les adapter au besoin ; guide, pas certificat personnel ni certification indépendante du SMSI | Justifications des vingt mesures et critères de vérification |
| NIST Cybersecurity Framework **CSF 2.0** | Organiser des résultats attendus avec Govern, Identify, Protect, Detect, Respond, Recover ; comparer actuel et cible | Treize sous-catégories du projet 1 et huit repères GV.SC du projet 2 |
| NIST SP 1305 | Relier le CSF à la gestion du risque cyber des fournisseurs | Criticité, exigences, diligence, coordination et sortie |

Le « NIST » principal demandé ici est **NIST CSF 2.0**. NIST n'est pas le nom d'une certification unique. NIST SP 800-53 ou d'autres publications ne sont pas nécessaires pour terminer ce portfolio.

Les fiches publiques ISO donnent une entrée utile mais ne remplacent pas les normes complètes. Utiliser, si possible, l'accès autorisé de ton école ou une copie sous licence. Ne pas apprendre uniquement des listes de numéros de contrôles.

Une ISO 27001 Foundation peut compléter la candidature si tu l'obtiens réellement. Elle n'est pas une condition pour comprendre ou présenter cette étude de cas, et elle ne doit pas apparaître comme obtenue ou en préparation si ce n'est pas vrai.

## 3. Ordre de travail proposé

Quatorze séances d'environ deux heures, avec des séances de laboratoire pouvant durer davantage. Ce sont des estimations de préparation, **pas un relevé d'heures travaillées ni une garantie de maîtrise**. Adapter le rythme jusqu'à janvier selon tes cours et la disponibilité du laboratoire.

| Séance | Travail personnel | Résultat à conserver |
|---|---|---|
| 1 | Lire README, les deux synthèses et les limites. Expliquer les deux décisions sans jargon | Une page de résumé personnel |
| 2 | Étudier le rôle de 27001/27002/27005 et du CSF ; noter les différences | Fiche de repères avec sources |
| 3 | Reprendre le périmètre, les parties intéressées et les dix actifs. Justifier les exclusions et dépendances | Trois corrections ou confirmations motivées du cadrage |
| 4 | Refaire R01/R03/R08 à la main. Expliquer V, I, score et seuil ; distinguer pilote et production | Trois fiches de risque écrites avec tes mots |
| 5 | Examiner E01 à E10 et C01 à C08. Classer écart, déclaration, non démontré | Tableau annoté de la portée des preuves |
| 6 | Relier les douze traitements aux risques. Reprendre cinq lignes de SoA | Cinq justifications et critères de clôture personnels |
| 7 | Relire PSSI et procédures. Choisir qui décide, qui exécute et qui vérifie | Une procédure expliquée étape par étape |
| 8 | Préparer le laboratoire et T01/T02 ; les exécuter seulement si les moyens sont présents | Résultats datés, limites et captures assainies, ou blocage explicite |
| 9 | Préparer puis exécuter T03/T04 si possible | Résultats datés et distinction avec une preuve de production |
| 10 | Reprendre les treize résultats NIST actuel/cible, sans inventer de maturité globale | Trois écarts présentés et reliés à leurs actions |
| 11 | Lire V01 à V09 et répondre toi-même aux vingt questions avant de comparer | Questionnaire annoté et divergences expliquées |
| 12 | Refaire S04/S05/S08 et les conditions G1 à G6. Contester une preuve insuffisante | Avis fournisseur d'une page |
| 13 | Reformuler la synthèse en anglais et présenter chaque projet en trois minutes | Notes d'oral en français et anglais |
| 14 | Relecture finale des preuves, dates, statuts, versions et lignes CV | Version personnelle revue et liste des limites restantes |

Les séances 8 et 9 peuvent attendre le laboratoire. Tu peux poursuivre la lecture et le projet fournisseur pendant cette attente. Ne pas remplacer les résultats manquants par des captures fictives.

## 4. Exercices pour vérifier ta compréhension

### Exercice A - Une correction annoncée

Le fournisseur annonce avoir corrigé V06, sans rapport ni retest.

Question : peux-tu passer S08 de 16 à 8 et autoriser la production ?

Réponse attendue : non. La cible dépend de la correction vérifiée. Demander version, périmètre, test d'autorisation entre tenants, résultat et limites. La production reste bloquée.

### Exercice B - Une preuve absente

Le fournisseur ne transmet pas le compte rendu de revue des droits.

Question : peux-tu conclure qu'il ne fait aucune revue ?

Réponse attendue : non. Le fonctionnement n'est pas démontré. Demander une preuve pertinente ou limiter l'assurance. Ne pas confondre cette situation avec SUPPORT-PARTAGE explicitement décrit.

### Exercice C - Un MFA disponible

La présentation commerciale dit « MFA disponible » et montre des fonctions Enterprise.

Question : le besoin Standard est-il satisfait ?

Réponse attendue : vérifier formule, population, obligation, récupération et comportement effectif. Une possibilité technique ne démontre pas une règle imposée.

### Exercice D - Une sauvegarde réussie

Sept jobs sont marqués réussis et trois fichiers sont récupérés en laboratoire.

Question : cela prouve-t-il le RTO/RPO du SaaS ou de toute l'entreprise ?

Réponse attendue : non. Les fichiers démontrent uniquement le périmètre testé. Une reprise métier couvre données, application, accès, dépendances et intégrité ; le point de reprise doit être mesuré.

### Exercice E - Une nouvelle pièce

Tu disposes d'un relevé couvrant les 40 postes et non plus trois postes.

Travail : préciser ce que cela change pour E06, C06, R11, M11 et la synthèse. Un relevé montrant chiffrement activé ne prouve pas à lui seul récupération des clés ou bonne gestion de leur accès.

### Exercice F - Une hypothèse différente

Le métier exige désormais RTO quatre heures.

Travail : mettre à jour le critère, la justification d'impact et les exigences de reprise, puis noter les pièces qui ne répondent plus au besoin. Ne pas modifier tous les scores sans examiner chaque scénario.

### Exercice G - Risque fournisseur et registre global

Question : pourquoi ne pas additionner R08 et S08 ?

Réponse attendue : ils représentent le même scénario à deux niveaux de lecture. Les indices ordinaux ne sont pas une perte monétaire ou un risque probabiliste cumulable.

### Exercice H - Référentiel et certification

Question : « ISO 27001 dans mes compétences » veut-il dire que je suis certifié ?

Réponse attendue : non. Préciser niveau étudié, application dans le cas, et certification obtenue seulement si attestée. Une étude de cas ne certifie ni personne ni entreprise.

## 5. Transformer les protocoles en résultats réels

Commencer par l'inventaire du laboratoire : outils déjà installés, comptes autorisés, données artificielles, état des sauvegardes et interfaces disponibles. Choisir un environnement isolé que tu contrôles.

Pour chaque test, compléter la fiche de résultat du [projet 1](Projet_1_SSI/06_tests_manuels.md) :

1. Date, exécutant, version, périmètre et autorisation.
2. Étapes réellement suivies et conditions préalables.
3. Résultat attendu et résultat observé.
4. Justificatifs datés, lisibles et sans donnée sensible.
5. Conclusion limitée au test, anomalie et prochain traitement.

Ne pas changer directement « NON EXÉCUTÉ » en « réussi ». Les captures, observations et limites doivent soutenir cette conclusion.

Les résultats seront de nouvelles preuves du laboratoire personnel. Ils **ne remplaceront pas automatiquement** E01 à E10, qui décrivent une autre organisation fictive. Pour les intégrer au cas, créer une variante explicite du scénario et documenter les hypothèses, sans prétendre avoir testé une entreprise réelle.

### Partie technique prise en charge

Les scripts Git, sauvegarde/restauration et tests HTTP Keycloak ont été développés et exécutés dans cette mission. Le script Windows T02 a produit un événement réel après élévation ; la réception et l’alerte Wazuh sont prouvées après correction des diagnostics VM ; conservation longue durée non démontrée. Il n’est plus nécessaire de renvoyer ces tâches à un autre chat. Relire les scripts, relancer uniquement dans le laboratoire dédié et expliquer chaque preuve avec ses limites. Consulter [la notice](NOTICE_PERSONNELLE.md).

## 6. Ce que tu peux présenter dans le CV

Après lecture, vérification et appropriation personnelle, le périmètre documentaire peut être décrit ainsi :

**Évaluation des risques cyber et des contrôles SSI — étude de cas simulée**

- Cadrage du périmètre SSI, inventaire de dix actifs et registre de douze risques avec propriétaires et plan de traitement.
- Évaluation documentaire de contrôles, PSSI et procédures proposées, extrait de SoA et profil actuel/cible NIST CSF 2.0.

**Évaluation du risque cyber d'un fournisseur SaaS — étude de cas simulée**

- Évaluation de criticité, questionnaire de vingt points et recoupement de neuf pièces simulées ; huit scénarios de risque cyber.
- Plan de remédiation, conditions de production et recommandation motivée ; synthèse exécutive en anglais.

Les tests techniques ne figurent comme exécutés qu'après réalisation et preuve. Le nombre de livrables ne justifie pas une affirmation de conformité ISO, de certification ou d'audit réel.

Le CV cible est préservé. Le CV final décrit les études, les trois mécanismes entièrement prouvés et la collecte/alerte Wazuh observée ; il ne revendique pas la conservation de 90 jours. La portée partielle de T02 figure en annexe. La maîtrise des référentiels doit être formulée au niveau réellement acquis au moment de la candidature.

## 7. Questions d'entretien à préparer

- Pourquoi ce périmètre et ces actifs ?
- Quelle différence entre risque, vulnérabilité, contrôle et preuve ?
- Pourquoi V × I, et quelles limites possède cette méthode ?
- Qui est propriétaire du risque et qui approuve l'acceptation ?
- Comment as-tu choisi les mesures et pourquoi seulement un extrait de SoA ?
- Qu'est-ce qui prouve l'efficacité, au-delà d'une procédure écrite ?
- Pourquoi le fournisseur est-il critique et la production refusée ?
- Que ferais-tu avec un certificat ISO pertinent mais une faiblesse ouverte ?
- Quelle partie as-tu réellement testée et quelle partie reste simulée ?
- Quelle décision changerait avec une nouvelle preuve ?

L'objectif est de répondre avec un exemple du dossier, une justification et une limite. Il est plus convaincant de défendre une décision précise que de réciter des numéros de normes.

## 8. Petit lexique pour la lecture

| Terme | Sens dans les projets |
|---|---|
| SSI | Sécurité des systèmes d'information |
| SMSI | Système de management qui organise et pilote la sécurité de l'information |
| PSSI | Politique fixant les règles et responsabilités SSI |
| GRC | Gouvernance, gestion des risques et conformité ; ici limitée à la cybersécurité |
| Actif | Information, service, équipement ou autre élément important du périmètre |
| Risk owner | Responsable qui porte le risque et le traitement selon les pouvoirs définis |
| Asset owner | Responsable de l'actif ; il peut être distinct du propriétaire d'un risque |
| SoA | Déclaration d'applicabilité : mesures retenues, raisons, état et exclusions justifiées dans un dossier complet |
| MFA | Authentification avec plusieurs facteurs ; sa présence ne démontre pas son obligation |
| RTO | Délai cible pour rétablir le service après interruption |
| RPO | Perte de données admissible exprimée en durée entre le point récupérable et l'incident |
| Tenant | Espace d'un client dans un service partagé |
| TPRM | Gestion des risques liés aux tiers ; le projet traite le volet cyber d'un SaaS |
| Retest | Nouvelle vérification ciblée après correction |
| Risque cible | Estimation conditionnelle après les mesures envisagées |
| Risque résiduel | Risque restant après mesures existantes ou mises en œuvre ; à estimer avec les preuves disponibles |

## Références utiles

[ISO/IEC 27001](https://www.iso.org/standard/27001), [ISO/IEC 27002](https://www.iso.org/standard/75652.html), [ISO/IEC 27005](https://www.iso.org/standard/80585.html), [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf) et [NIST SP 1305](https://csrc.nist.gov/pubs/sp/1305/final).
