# Projet 1 - Contexte, périmètre SSI et actifs

**Évaluation des risques cyber et des contrôles SSI**  
**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**

## 1. Organisation étudiée

Atlas Services - cas pédagogique est une PME fictive de services informatiques installée à Tanger. Ses 40 collaborateurs réalisent du support B2B et du développement applicatif pour des PME. Elle emploie deux administrateurs systèmes, une équipe de développement et un responsable support.

Elle utilise une messagerie, un annuaire, un serveur de tickets local, des postes portables, un dépôt Git privé, des sauvegardes et une instance Wazuh limitée à un périmètre pilote.

Le fournisseur SupportCloud est évalué pour remplacer le serveur de tickets. **Le SaaS est seulement testé avec vingt tickets artificiels. Il n'est pas en production.** Les risques de ce futur usage sont distingués des expositions actuelles.

Toutes les personnes, quantités, configurations et dates d'artefacts de ce cas sont fictives.

## 2. Objectifs et mandat de l'atelier

La direction fictive demande une évaluation des risques SSI et un premier dossier de gouvernance. Les critères choisis pour l'exercice sont :

- protéger les comptes privilégiés et les informations clients ;
- rétablir le service local de tickets en huit heures, avec au plus 24 heures de données perdues, **objectifs à valider par le métier** ;
- disposer de preuves suffisantes pour les contrôles retenus ;
- décider des conditions de passage en production du SaaS ;
- affecter chaque risque à un responsable et chaque action à un pilote.

L'évaluation porte sur le contexte et des justificatifs documentaires. Elle ne vaut pas autorisation de modifier un système réel, ni audit de certification.

## 3. Périmètre proposé du SMSI

**Déclaration de périmètre de travail**

Les activités de support client et de développement applicatif d'Atlas Services, ainsi que les informations, identités, postes, applications, dépôts, sauvegardes et services d'infrastructure qui les soutiennent, sont inclus dans le périmètre proposé. Le projet d'adoption SupportCloud est inclus dans le processus d'évaluation fournisseur. Les systèmes internes du fournisseur ne sont pas administrés ni audités directement par Atlas Services.

### Inclus

Support B2B, développement, utilisateurs de ces activités, accès à distance, comptes techniques, application de tickets, dépôt Git, sauvegardes, journalisation et gestion des fournisseurs associés.

### Limites et interfaces

La paie et la comptabilité sont hors du périmètre d'analyse détaillée. Leurs interfaces avec l'annuaire, les postes et les comptes partagés restent identifiées. Cette limite pédagogique ne démontre pas qu'elles seraient excluables d'un SMSI réel.

Les infrastructures clientes et les systèmes internes du fournisseur sont des dépendances externes. Aucun test intrusif n'y est autorisé. L'étude fournisseur examine les garanties, documents, interfaces et responsabilités partagées.

### Laboratoire technique

Le laboratoire d'Anas, s'il est disponible, est séparé de la PME fictive. Il sert à démontrer des mécanismes avec des comptes et données de test. Un test de laboratoire ne prouve pas l'efficacité globale d'un contrôle dans l'entreprise.

## 4. Parties intéressées

| Partie | Attente SSI retenue | Réponse proposée |
|---|---|---|
| Direction | Comprendre les risques et arbitrer les ressources | Registre, propriétaires, priorités et revue mensuelle |
| Clients B2B | Confidentialité des tickets et continuité du support | Accès limités, engagements, sauvegardes et traitement des incidents |
| Collaborateurs | Accès nécessaires et consignes compréhensibles | Habilitations nominatives, sensibilisation et canal d'alerte |
| Administrateurs | Rôles explicites et accès de secours contrôlés | Séparation des comptes, MFA et procédure de récupération |
| Développeurs | Accès au code et changements traçables | Protection des secrets, revue et validation des déploiements |
| Fournisseur SaaS | Exigences de sécurité compatibles avec le service acheté | Questionnaire, accord, suivi et plan de sortie |
| Fonction juridique/protection des données | Informations suffisantes pour qualifier obligations et transferts | Cartographie des données et revue séparée avant production |

## 5. Gouvernance proposée

| Rôle fictif | Responsabilité |
|---|---|
| Direction générale - DG | Approuve le périmètre, les critères, la PSSI et les exceptions importantes |
| Responsable SSI - RSSI | Coordonne l'analyse, vérifie les preuves et suit le traitement |
| Responsable infrastructure - RI | Pilote identités, postes, journaux et sauvegardes |
| Responsable développement - RD | Pilote code, secrets, vulnérabilités et changements |
| Responsable support - RS | Porte les besoins métier, les données de tickets et le risque fournisseur |
| RH | Signale les arrivées, changements et départs |
| Référent juridique/protection des données - RJ | Qualifie les points contractuels et de données personnelles |

Le propriétaire d'un risque décide du traitement dans son domaine et rend compte à la direction. Le pilote d'une action réalise la mesure. Le RSSI examine les preuves. Une seule personne peut cumuler des fonctions dans une PME, mais ne doit pas valider seule toutes ses propres actions sensibles.

## 6. Inventaire de travail

Cet inventaire de dix actifs est **une proposition issue de l'étude**. Les propriétaires restent à valider par les rôles fictifs. Il ne remplace pas l'inventaire initial incomplet E01.

C, I et D expriment les besoins de confidentialité, intégrité et disponibilité sur l'échelle locale 1 à 5. Ils ne constituent pas automatiquement l'impact de chaque scénario.

| ID | Actif et information associée | Propriétaire proposé | C/I/D | Dépendances ou interfaces | Statut |
|---|---|---|---|---|---|
| A01 | Annuaire, identités et comptes privilégiés | RI | 5/5/4 | Postes, messagerie, administration | Existant dans le cas |
| A02 | Messagerie et échanges clients | RS | 4/4/3 | Annuaire, Internet, postes | Existant |
| A03 | 40 postes portables | RI | 4/3/3 | Identités, accès distant, chiffrement | Existant |
| A04 | Application locale de tickets et base | RS | 4/4/5 | VM, comptes, sauvegardes | Existant |
| A05 | Dépôt Git privé et code applicatif | RD | 4/4/3 | Identités, revues, secrets | Existant |
| A06 | Sauvegardes du serveur de tickets | RI | 4/4/5 | Stockage séparé, compte de sauvegarde, restauration | Existant, restaurabilité non démontrée |
| A07 | SIEM Wazuh pilote et journaux | RI | 3/4/3 | Sources, agents, heure, stockage | Existant, couverture limitée |
| A08 | SupportCloud et données du futur service | RS | 4/4/4 | Fournisseur, contrats, export, sous-traitants | Pilote avec données artificielles |
| A09 | Documentation d'exploitation et procédures | RI | 3/4/4 | Dépôt documentaire, personnes, accès | Existant, documentation partielle |
| A10 | Exports locaux de tickets et pièces jointes | RS | 4/3/2 | Postes, partages, conservation, suppression | Existant |

## 7. Flux d'information

1. Un client adresse une demande de support. Le service support crée un ticket dans A04 et peut recevoir une pièce jointe.
2. Les collaborateurs accèdent au ticket selon leur rôle. Des exports A10 peuvent être créés.
3. Une correction applicative est préparée dans A05 puis déployée sur l'application locale.
4. A06 sauvegarde les données. A07 reçoit une partie des événements techniques.
5. Le pilote A08 reçoit uniquement des tickets artificiels. Le futur transfert de données réelles demeure suspendu à la décision fournisseur.

Les tickets réels du scénario peuvent contenir noms, courriels professionnels et descriptions techniques. La PSSI proposée interdit mots de passe, clés privées, données de santé et documents d'identité dans les tickets.

## 8. Contexte climatique et continuité

L'analyse du contexte retient les interruptions d'alimentation et la chaleur comme hypothèses pouvant affecter les équipements et la disponibilité. Elles doivent être examinées avec les dépendances électriques, réseau et d'hébergement. Aucune étude climatique locale ni probabilité d'événement n'est inventée.

Le point de contexte est documenté pour prendre en compte l'amendement 2024. Il ne transforme pas ce projet cyber en audit environnemental.

## 9. Hypothèses à confirmer

| Hypothèse | Effet sur l'analyse |
|---|---|
| RTO local de huit heures et RPO de 24 heures | Si le métier exige moins, les mesures et certains impacts doivent être réévalués |
| Pas de données sensibles réglementaires dans les tickets | Si elles apparaissent, la criticité et les obligations doivent être revues |
| Aucun accès SupportCloud aux systèmes de production | Tout connecteur ou compte technique étendu impose une nouvelle évaluation |
| Usage fournisseur en pilote artificiel | Les risques fournisseur sont prospectifs, non une preuve d'exposition de clients réels |
| Sources internes simulées | Conclusions limitées à la cohérence du cas |

## Références

[ISO/IEC 27001](https://www.iso.org/standard/27001), [amendement 2024](https://www.iso.org/standard/88435.html), [communiqué ISO/IAF](https://www.iso.org/files/live/sites/isoorg/files/standards/popular_standards/management_systems/ISO-IAF%20Joint%20Communique%20Feb%202024.pdf).
