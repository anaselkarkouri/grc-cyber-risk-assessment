# Projet 1 - Méthode et registre des risques

**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**

## 1. Méthode retenue

Chaque risque décrit une menace, une faiblesse exploitable, les actifs concernés et une conséquence SSI. La méthode est inspirée de la gestion des risques SSI, avec une cotation locale définie pour l'exercice.

Le score est **vraisemblance V × impact I**. Les valeurs ordinales servent à prioriser. Elles ne représentent ni une probabilité annuelle chiffrée, ni une perte monétaire attendue.

L'horizon de comparaison est les douze mois suivant la situation de référence du 7 octobre 2026. Pour le SaaS, il correspond aux douze premiers mois d'un éventuel usage en production dans les conditions décrites. Cet horizon commun ne transforme pas les indices en fréquences mesurées.

Trois niveaux sont conservés :

- **Inhérent** : scénario considéré sans les mesures existantes retenues dans l'analyse.
- **Actuel estimé** : mesures existantes prises en compte dans la limite des justificatifs.
- **Cible estimée** : résultat envisagé si les actions sont déployées et leur efficacité vérifiée.

Le risque résiduel doit être réévalué sur la base de mesures effectivement mises en œuvre et de preuves de leur efficacité. Cette réévaluation après traitement n'est pas encore réalisée. Elle n'est pas remplacée par le risque cible.

## 2. Échelles

### Vraisemblance

| V | Interprétation locale |
|---|---|
| 1 | Peu plausible : chemin d'attaque restreint et plusieurs barrières vérifiées seraient nécessaires |
| 2 | Possible : exposition limitée et contrôles crédibles, avec limites connues |
| 3 | Plausible : chemin identifiable et mesures partielles |
| 4 | Probable dans le scénario : faiblesse directement exploitable ou exposition importante |
| 5 | Très probable : répétition ou exploitation active documentée dans le cas |

Ces appréciations exigent un raisonnement sur le scénario. Une pièce manquante ne suffit pas à attribuer V = 4 ou 5.

### Impact

| I | Confidentialité | Intégrité | Disponibilité du service concerné |
|---|---|---|---|
| 1 | Information publique ou divulgation négligeable | Correction immédiate sans effet métier | Interruption brève sans effet significatif |
| 2 | Information interne limitée | Erreur locale réversible | Perturbation limitée, contournement disponible |
| 3 | Information confidentielle limitée | Reprise manuelle de dossiers | Interruption significative, activité dégradée |
| 4 | Ensemble important de données clients ou de code | Altération étendue avec reprise difficile | Arrêt du support sans contournement immédiat, ou interruption dépassant l'objectif métier |
| 5 | Identités privilégiées ou exposition susceptible de compromettre largement les systèmes | Perte de maîtrise majeure des systèmes ou dossiers | Arrêt prolongé de la fonction critique, reprise incertaine |

L'impact retenu est le maximum des dimensions **du scénario**, pas automatiquement le maximum de la fiche actif. Une mesure de sauvegarde peut réduire un impact de disponibilité si la reprise est démontrée. Elle ne réduit pas, à elle seule, l'impact d'une fuite.

### Priorités

| Score | Niveau | Décision attendue |
|---|---|---|
| 1 à 4 | Faible | Acceptation possible par le propriétaire, avec justification et revue |
| 5 à 9 | Modéré | Traitement proportionné ou acceptation documentée, approuvée par le propriétaire et le RSSI |
| 10 à 15 | Élevé | Plan obligatoire ; exception temporaire soumise à la DG |
| 16 à 25 | Critique | Mesure de réduction immédiate ou suspension du nouvel usage ; arbitrage DG |

Un faible score ne dispense pas d'une obligation applicable. Une preuve insuffisante impose une demande complémentaire avant d'affirmer l'efficacité du contrôle.

## 3. Registre synthétique

Notation : chaque triplet indique **V / I / score**. Les douze risques ne sont pas additionnés, car leurs événements et conséquences peuvent se recouper.

| ID | Scénario et actifs | Propriétaire du risque | Inhérent | Actuel estimé | Niveau actuel | Cible conditionnelle | Traitement |
|---|---|---|---|---|---|---|---|
| R01 | Vol ou partage d'un compte privilégié permettant une prise de contrôle d'A01/A04 | RI | 4/5/20 | 4/5/20 | Critique | 1/5/5 | Réduire, M01 |
| R02 | Phishing d'un collaborateur puis accès aux échanges clients A02 | RS | 4/4/16 | 3/4/12 | Élevé | 2/4/8 | Réduire, M02 |
| R03 | Chiffrement ou perte de l'application A04 avec restauration A06 inutilisable | RI | 4/5/20 | 4/5/20 | Critique | 2/4/8 | Réduire, M03 |
| R04 | Incident persistant faute de collecte et de revue suffisantes sur A07 | RI | 4/4/16 | 3/4/12 | Élevé | 2/4/8 | Réduire, M04 |
| R05 | Exploitation d'une faiblesse applicative non traitée sur A04 | RD | 4/4/16 | 3/4/12 | Élevé | 2/4/8 | Réduire, M05 |
| R06 | Secret applicatif commité puis réutilisé pour accéder aux services A05/A04 | RD | 4/4/16 | 4/4/16 | Critique | 1/4/4 | Réduire, M06 |
| R07 | Maintien d'un accès après départ et consultation des tickets A01/A04 | RI | 3/4/12 | 3/4/12 | Élevé | 1/4/4 | Réduire, M07 |
| R08 | Futur accès inter-clients non autorisé dans SupportCloud A08 | RS | 4/4/16 | 4/4/16 | Critique, prospectif | 2/4/8 | Éviter l'exposition en production puis réduire, M08 |
| R09 | Export A10 conservé sans justification et partagé trop largement | RS | 3/3/9 | 3/3/9 | Modéré | 2/3/6 | Réduire, M09 |
| R10 | Absence d'un administrateur et documentation A09 insuffisante pour reprendre le service | RI | 3/3/9 | 3/3/9 | Modéré | 2/3/6 | Réduire, M10 |
| R11 | Perte d'un portable A03 non chiffré exposant des informations clients | RI | 4/4/16 | 4/4/16 | Critique | 1/4/4 | Réduire, M11 |
| R12 | Modification non validée d'A04 altérant les tickets sans retour arrière préparé | RD | 3/4/12 | 3/4/12 | Élevé | 2/4/8 | Réduire, M12 |

## 4. Fondement des cotations actuelles

| Risque | Éléments du cas et mesures existantes | Justification de l'appréciation et limite |
|---|---|---|
| R01 | E02 : un compte partagé et deux comptes privilégiés sans MFA sur trois | V4 reflète un chemin d'accès direct ; I5 la portée d'un compte privilégié. Le MFA du troisième compte ne couvre pas les deux autres |
| R02 | E10 : sensibilisation ponctuelle ; protection de base de messagerie déclarée | V3 tient compte d'une barrière partielle. Aucun exercice récent ne démontre une efficacité durable |
| R03 | E02 : accès privilégiés insuffisamment protégés ; E04 : sept sauvegardes annoncées réussies, aucune preuve de restauration | V4 est une hypothèse conservatrice du scénario composé de compromission puis reprise insuffisante. L'exposition des accès étaye la possibilité d'une compromission ; l'absence de rapport ne prouve pas un échec de restauration. Confiance limitée sur V et la reprise |
| R04 | E03 : un événement visible, deux sources sur six déclarées couvertes | V3 concerne la persistance non détectée. Le dispositif pilote apporte un signal limité, insuffisant pour généraliser |
| R05 | E09 : faiblesse élevée ouverte sur le serveur local ; accès réseau déjà limité | V3 reconnaît la restriction d'accès, mais le correctif reste nécessaire |
| R06 | E05 : marqueur de secret de démonstration présent dans l'historique fictif | La cotation suppose, dans le scénario uniquement, qu'un secret utilisable aurait été exposé. Aucune clé réelle n'est fournie |
| R07 | E07 : compte fictif actif sept jours après départ | Chemin plausible et accès client résiduel. L'échantillon ne mesure pas tous les départs |
| R08 | V06 du projet 2 : défaut d'autorisation inter-clients ouvert dans le rapport simulé | Le risque est conditionné à l'usage réel futur. Il reprend S08, sans additionner les huit risques fournisseur |
| R09 | E10 : conservation et règles de partage non formalisées | V3 est un jugement de scénario lié à la présence d'exports, pas une conclusion tirée uniquement d'un document absent |
| R10 | E10 : procédures détenues par un seul administrateur | La dépendance humaine justifie l'étude de continuité. Aucun arrêt réel n'est inventé |
| R11 | E06 : un portable non chiffré sur trois examinés | V4 est une hypothèse prudente pour la perte de ce poste et son exposition. Le taux observé sur trois postes n'est pas extrapolé aux 40 |
| R12 | E08 : déploiement explicitement marqué sans approbation et sans retour arrière | V3/I4 portent sur une modification affectant la base de tickets. Pas de test réel de corruption |

La confiance est suffisante **pour suivre le raisonnement du cas simulé** lorsqu'un artefact précis soutient le constat. Elle est limitée pour l'efficacité dans la durée, les populations non échantillonnées et tous les risques cible.

## 5. Conditions des cotations cible

- R01 : MFA applicable aux accès privilégiés, suppression du partage, récupération sécurisée et vérification des exceptions.
- R02 : protections d'accès et de messagerie complétées, exercice de sensibilisation et contrôle des accès clients.
- R03 : sauvegarde isolée et protégée, restauration répétable, intégrité et objectifs métier vérifiés. I5 devient I4 uniquement dans cette hypothèse.
- R04 : sources prioritaires couvertes, alerte et revue démontrées, conservation et accès aux journaux examinés.
- R05 : correction validée et suivi des vulnérabilités opérationnel.
- R06 : secret invalidé, rotation démontrée, historique traité et accès au dépôt revus. Le scanner automatique reste une option, pas une condition du présent travail documentaire.
- R07 : sortie testée jusqu'au retrait des sessions, jetons et comptes.
- R08 : fermeture et retest de S08, puis levée de tous les autres blocages du projet 2.
- R09 : minimisation, durée justifiée et partage limité réellement appliqués.
- R10 : suppléance et procédure exercées.
- R11 : chiffrement du poste testé et récupération maîtrisée.
- R12 : approbation, séparation des droits, test et retour arrière vérifiés.

Pour R03, I4 reste une estimation conservatrice d'un arrêt complet du support, même si la reprise devient maîtrisée. Atteindre un RTO ne rend pas l'interruption sans conséquence. La réduction I5 vers I4 doit être justifiée par une reprise réelle et une validation métier ; elle n'est pas automatique à partir d'un job réussi.

### Sensibilité des hypothèses prudentes

R03 et R11 nécessitent une attention particulière : la fréquence d'incident destructif, de déplacement ou de perte de portable n'est pas mesurée. Leur V4 est une hypothèse de priorisation, pas un constat statistique.

| Variante à discuter | Score résultant | Effet sur la priorité |
|---|---|---|
| R03 : V3 au lieu de V4, I5 conservé | 15, élevé | Le traitement et la preuve de reprise restent nécessaires |
| R11 : V3 au lieu de V4, I4 conservé | 12, élevé | Le chiffrement du poste exposé reste nécessaire |

Si ces deux variantes étaient retenues ensemble, la répartition serait trois critiques, sept élevés et deux modérés, au lieu de cinq critiques, cinq élevés et deux modérés. La version de référence conserve V4 ; cette sensibilité explique pourquoi les nombres ne doivent pas être présentés comme une mesure objective du marché, d'incidents ou de conformité.

## 6. Arbitrage et suivi

**Répartition actuelle : cinq risques critiques, cinq élevés et deux modérés.** Parmi les cinq critiques, R08 concerne le projet SaaS avant production. Les onze expositions existantes comprennent quatre critiques, cinq élevées et deux modérées.

**Répartition cible estimée : trois faibles et neuf modérés**, seulement si les conditions ci-dessus sont satisfaites. Aucun risque n'est clôturé à ce stade.

Le registre sera revu après preuve de traitement, changement d'architecture, incident, ajout de données sensibles ou changement fournisseur. Une acceptation précisera le risque, le niveau actuel, les mesures compensatoires, le propriétaire, l'autorité, une échéance et une condition de réexamen.

### Exemple d'acceptation correctement bornée

R09, score actuel 9 : maintien temporaire d'un export limité sur un espace à accès restreint, durée de trente jours, sous responsabilité RS, avec revue RSSI. **Décision proposée, non signée.** Aucune acceptation automatique de R01 ou R08 n'en découle.

## Référence

[ISO/IEC 27005:2022](https://www.iso.org/standard/80585.html). Les échelles, niveaux, exemples et décisions sont propres au cas.
