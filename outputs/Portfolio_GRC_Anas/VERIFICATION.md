# Vérification finale et historique

**Version 1.1 - 07/10/2026.**

## Conclusion actuelle

Deux dossiers documentaires relus et finalisés ; quatre tests exécutés, dont trois réussis dans leurs critères bornés et T02 partiel : source, réception et alerte prouvées ; conservation longue durée non démontrée. Les états E/V et les actions fictives sont conservés. CV final sur une page adapté aux opérations prouvées des quatre tests et aux bases GRC.

## Contrôles de contenu

109 contrôles automatiques : 60 produits V×I, vingt niveaux actuels, vingt rapprochements Q/pièces, huit chaînes F/S/VM et un miroir R08/S08. Zéro divergence. Relecture qualitative des vingt questions, neuf pièces, contradictions MFA/reprise/localisation, Standard/Enterprise, absence de preuve, allégation ISO, durées locales et synthèse anglaise. Les distributions de référence sont confirmées : P1 cinq critiques/cinq élevés/deux modérés ; cible trois faibles/neuf modérés ; P2 un critique/sept élevés ; cible deux faibles/six modérés.

## Pièces et livrables

18 Markdown initiaux conservés dans la copie de référence ; revue fournisseur 07 et annexes/notice ajoutées. [Matrice finale](Annexes_laboratoire/MATRICE_PREUVES.md), manifestes SHA-256 et scripts reproductibles. Rapports consolidés en PDF avec Markdown éditable ; registre XLSX avec formules et suivi ; CV final distinct du CV cible. Les contrôles de rendu et de fichier sont consignés dans CONTROLE_LIVRAISON.json à côté des rapports.

## Limites restantes

T02-P01 à P06 disponibles ; source, réception et alerte prouvées, accès/configuration examinés ; conservation longue durée non démontrée. Récupération IAM documentée, sans exercice complet ni second appareil ; prototype local, pas architecture de production. ZIP même volume et privilège, pas sauvegarde résiliente d’entreprise. Git local sans rotation ni exhaustivité. Référentiels étudiés avec assistance, maîtrise personnelle à approfondir ; normes ISO sous licence non fournies. Aucune clôture de M, VM, R, S ou G à partir du laboratoire.

## Historique

1.0 : études documentaires du 7 octobre, zéro nouveau test. 1.1 : finalisation du 07/10/2026, trois réussites bornées, un test partiel, revue et CV fidèles. Copie initiale : reference_v1_20261007T192733Z.

## Vérification documentaire 1 0 conservée pour historique

Le texte suivant décrit exclusivement la livraison initiale ; ses mentions de tests non exécutés ne décrivent pas l’état 1.1 ci-dessus.

# Compte rendu de vérification du portfolio

**Version livrée : 1.0 - 7 octobre 2026**  
**Nature du contrôle : relecture documentaire, recoupement des références et vérification manuelle des cotations.**

## 1. Conclusion de la vérification

Le dossier est cohérent pour **deux études de cas pédagogiques documentaires renseignées**. Les risques, constats, actions et décisions disposent d'identifiants et d'un chemin de justification.

Le dossier ne prétend pas démontrer une conformité professionnelle complète, des contrôles opérant en entreprise, un engagement fournisseur réel ou des tests de laboratoire exécutés.

**La partie documentaire est livrée. La partie de démonstration technique comporte quatre protocoles prêts à utiliser, avec zéro nouveau test exécuté.** L'appropriation personnelle du contenu par Anas reste nécessaire avant de revendiquer une maîtrise en entretien.

## 2. Inventaire de livraison

| Partie | Contenu | Nombre de fichiers |
|---|---|---|
| Racine | Index, sources, guide et présent compte rendu | 4 |
| Projet 1 | Cadrage, risques, traitement/SoA, justificatifs/constats, PSSI/procédures, tests, profil NIST, synthèse | 8 |
| Projet 2 | Criticité, pièces fournisseur, questionnaire, constats/risques, remédiation, décision et synthèse anglaise | 6 |
| Ensemble | Documents Markdown modifiables | 18 |

Les fichiers cités par l'index existent. Les liens internes ont été rapprochés des noms et emplacements des fichiers. Le lien entre les projets utilise le même scénario fictif et le même fournisseur Standard.

## 3. Contrôle des populations

| Élément | Population vérifiée | Limite |
|---|---|---|
| Actifs | A01 à A10 : dix | Inventaire proposé, non validé par une organisation réelle |
| Risques du projet 1 | R01 à R12 : douze | Onze usages existants fictifs et un scénario prospectif SaaS |
| Traitements du projet 1 | M01 à M12 : douze | Tous proposés ; zéro clôture avec preuve de déploiement |
| Justificatifs internes | E01 à E10 : dix | Tous simulés |
| Constats du projet 1 | C01 à C08 : huit | Examen documentaire ciblé, pas audit exhaustif |
| SoA | Vingt repères de mesures | Extrait ; aucune exclusion de l'annexe A décidée |
| Profil CSF du projet 1 | Treize sous-catégories | Six fonctions représentées ; couverture partielle |
| Nouveaux tests | T01 à T04 : quatre | Protocoles rédigés ; tous NON EXÉCUTÉS |
| Observation de stage | H01 : une | Document historique fourni ; test non reproduit |
| Pièces fournisseur | V01 à V09 : neuf | Toutes simulées ; aucun certificat fabriqué |
| Questionnaire | Q01 à Q20 : vingt | Réponses renseignées et recoupées avec le dossier simulé |
| Constats fournisseur | F01 à F08 : huit | Écarts et éléments non démontrés distingués |
| Risques fournisseur | S01 à S08 : huit | Usage cible en production, pas exposition actuelle du pilote |
| Actions fournisseur | VM01 à VM08 : huit | Toutes ouvertes |
| Conditions de production | G1 à G6 : six | Aucune satisfaite au dossier actuel |
| Repères fournisseur CSF | Huit sous-catégories GV.SC | Sélection limitée |

## 4. Contrôle manuel des produits et niveaux

### Projet 1 : version de référence

| Risque | Actuel : V × I = score | Niveau | Cible : V × I = score | Niveau cible conditionnel |
|---|---|---|---|---|
| R01 | 4 × 5 = 20 | Critique | 1 × 5 = 5 | Modéré |
| R02 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| R03 | 4 × 5 = 20 | Critique | 2 × 4 = 8 | Modéré |
| R04 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| R05 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| R06 | 4 × 4 = 16 | Critique | 1 × 4 = 4 | Faible |
| R07 | 3 × 4 = 12 | Élevé | 1 × 4 = 4 | Faible |
| R08 | 4 × 4 = 16 | Critique, prospectif | 2 × 4 = 8 | Modéré |
| R09 | 3 × 3 = 9 | Modéré | 2 × 3 = 6 | Modéré |
| R10 | 3 × 3 = 9 | Modéré | 2 × 3 = 6 | Modéré |
| R11 | 4 × 4 = 16 | Critique | 1 × 4 = 4 | Faible |
| R12 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |

Les produits des cotations inhérentes ont également été rapprochés du registre : 4 × 5 = 20, 4 × 4 = 16 et 3 × 3 ou 3 × 4 = 9 ou 12 selon le scénario.

La répartition actuelle est **cinq critiques, cinq élevés et deux modérés**. Hors R08, elle est **quatre critiques, cinq élevés et deux modérés**. La cible est **trois faibles et neuf modérés**.

L'analyse de sensibilité discutée dans la méthode, avec V3 pour R03 et R11, donne **trois critiques, sept élevés et deux modérés**. Elle est clairement séparée de la version de référence et n'est pas substituée silencieusement dans la synthèse.

### Projet 2 : usage cible

| Risque | Actuel : V × I = score | Niveau | Cible : V × I = score | Niveau cible conditionnel |
|---|---|---|---|---|
| S01 | 3 × 4 = 12 | Élevé | 1 × 4 = 4 | Faible |
| S02 | 3 × 4 = 12 | Élevé | 1 × 4 = 4 | Faible |
| S03 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| S04 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| S05 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| S06 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| S07 | 3 × 4 = 12 | Élevé | 2 × 4 = 8 | Modéré |
| S08 | 4 × 4 = 16 | Critique | 2 × 4 = 8 | Modéré |

Les cotations inhérentes 4 × 4 = 16 pour S01/S02/S08 et 3 × 4 = 12 pour S03 à S07 concordent avec le registre.

Répartition actuelle : **un critique et sept élevés**. Cible : **deux faibles et six modérés**. Les versions française et anglaise concordent.

R08 et S08 ont le même événement, le même score actuel 16 et la même cible 8. Ils ne sont pas additionnés. Aucun total de scores ordinal ne sert à calculer un risque global.

## 5. Contrôles de traçabilité et décision

- Chaque R dispose d'un propriétaire, d'actifs et d'un M correspondant.
- Chaque constat C dispose d'un critère, d'une pièce et d'un risque/action.
- T01/T02/T03/T04 sont liés respectivement à accès, journalisation, restauration et secrets.
- Les dix actifs proposés sont séparés de l'inventaire initial E01 incomplet.
- Chaque S dispose d'un scénario, d'un F, de pièces et d'une VM.
- Les questions sur certification, chiffrement et revue non démontrée ne sont pas transformées en faux incidents.
- Les six conditions G regroupent les huit traitements et restent ouvertes.
- La production est défavorable en l'état ; le pilote artificiel est limité jusqu'au 6 novembre.
- Le contrat Standard est évalué ; les fonctions Enterprise ne sont pas supposées acquises.

## 6. Contrôle des preuves et du vocabulaire

Le dossier distingue :

1. Documents E/V simulés et sources officielles réelles.
2. Conception, configuration décrite et efficacité dans la durée.
3. Contrôle absent explicitement dans le cas et preuve non fournie.
4. Risque inhérent, actuel estimé, cible conditionnelle et réévaluation du résiduel après traitement effectif.
5. Pièces de stage historiques, nouveaux tests personnels et efficacité en production.
6. Critères contractuels locaux et obligations applicables à faire examiner.

Exemples vérifiés : MFA 1 sur 3 comptes internes ; collecte 2 sur 6 sources déclarées ; chiffrement 2 sur 3 postes examinés. Les trois postes ne sont pas extrapolés à 40. Sept jobs ne deviennent pas sept restaurations.

Les repères de H01 ont été corrigés et rapprochés de l'exemplaire fourni : périmètre page PDF 19, chapitre 5 pages 55 à 61 et collaboration pages 62 à 63. Le rapport décrit les essais bénins et les faux positifs, sans démontrer un taux de détection de malwares réels.

Les cibles et décisions ne contiennent aucune signature réelle, aucune attestation inventée et aucune approbation tacite. La terminologie française a été harmonisée ; la synthèse anglaise reprend les mêmes périmètres et conditions.

## 7. Contrôle des références

Les fiches officielles ISO et les publications NIST ont été utilisées selon le [registre des sources](SOURCES.md).

Le CSF utilisé est **NIST CSF 2.0**. Les numéros sélectionnés ont été rapprochés de sa publication officielle. Le SP 1305 soutient la démarche fournisseur, sans imposer notre nombre de questions ou nos seuils.

Les références ISO sont des repères de travail. Les normes complètes sous licence n'ayant pas été fournies, aucune vérification exhaustive de toutes leurs exigences n'est déclarée. Les intitulés reformulés et la sélection de vingt mesures ne remplacent pas le texte autorisé.

Le contexte climatique de l'amendement 2024 est mentionné de manière proportionnée, sans statistiques locales inventées. Les points CNDP sont signalés pour une revue compétente ; aucun dossier de formalités ni avis juridique réel n'est établi.

## 8. Limites restantes et suite concrète

| Point restant | Action nécessaire |
|---|---|
| Laboratoire non confirmé | Identifier outils, accès et état avant exécution |
| Quatre nouveaux tests non exécutés | Suivre les protocoles, conserver résultats et limites |
| Maîtrise personnelle débutante des référentiels | Lire, refaire les choix et réaliser les exercices du guide |
| Textes ISO complets | Utiliser une source autorisée pour approfondir et vérifier |
| Organisations et fournisseur fictifs | Présenter toujours le caractère simulé de ces deux projets |
| Format documentaire | Fichiers Markdown ; pas de PDF, Word ou tableur généré dans cette livraison |

Consigne technique de la livraison initiale remplacée par l’autorisation explicite de cette mission Codex.

## Historique de livraison

| Version | Date | Objet |
|---|---|---|
| 1.0 | 7 octobre 2026 | Deux études de cas rédigées, sources recoupées, cotations contrôlées, limites explicites et guide d'appropriation |
