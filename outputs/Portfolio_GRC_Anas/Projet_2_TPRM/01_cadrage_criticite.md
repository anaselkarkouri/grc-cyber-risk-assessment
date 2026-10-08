# Projet 2 - Cadrage et criticité du fournisseur SaaS

**Third-Party Cyber Risk Assessment**  
**Cas pédagogique simulé - version 1.0 - 7 octobre 2026**

## 1. Service et décision étudiés

Atlas Services envisage d'utiliser SupportCloud - cas pédagogique comme outil SaaS de support B2B. Le contrat envisagé est la **formule Standard**. Les fonctionnalités d'une formule supérieure ne sont pas présumées disponibles.

Le pilote contient vingt tickets artificiels, sans donnée personnelle réelle, pièce client, secret ni connexion aux systèmes de production. La présente évaluation prépare la décision de passer en production ; elle ne constate pas une fuite réelle ou un incident fournisseur réel.

Le service cible serait utilisé par 40 collaborateurs et traiterait des noms, courriels professionnels, textes de support et pièces techniques. Les données de santé, pièces d'identité et secrets d'accès sont interdits par la politique proposée.

## 2. Périmètre

Examiner le service SaaS et les responsabilités liées aux données : droits client, accès support fournisseur, sécurité applicative, chiffrement, journaux, restauration, sous-traitants, incident, retour et suppression des données.

L'évaluation ne porte ni sur la solidité financière du fournisseur, ni sur ses risques commerciaux généraux. Les effets métier servent uniquement à apprécier les conséquences d'un scénario cyber.

Les systèmes du fournisseur ne sont pas accessibles à l'évaluateur. Les tests intrusifs ne sont pas autorisés. Les preuves opérationnelles proviennent de pièces simulées fournies dans le dossier.

## 3. Criticité de l'usage cible

La criticité se détermine avant l'examen de maturité du fournisseur. Un fournisseur peut présenter de bons documents tout en restant critique par la nature du service.

| Dimension | Situation de l'usage envisagé | Niveau local |
|---|---|---|
| Données | Informations clients confidentielles et données personnelles professionnelles | Haut |
| Disponibilité | Interruption du support si la plateforme devient indisponible ; objectif métier huit heures | Haut |
| Intégrité | Tickets, affectations et états nécessaires au suivi client | Haut |
| Privilèges | Administration du tenant et accès support fournisseur ; aucun connecteur de production envisagé | Haut pour les données du tenant |
| Dépendance | Export et reprise encore à démontrer | Haut |
| Remplacement | Migration nécessaire, sans solution immédiate équivalente démontrée | Haut |

**Classe retenue : fournisseur critique pour le support envisagé.** Cette classe est un choix local motivé, pas une catégorie obligatoire imposée par NIST.

Le pilote artificiel a une exposition plus limitée. Cela ne réduit pas automatiquement la criticité de l'usage en production.

## 4. Exigences client retenues pour l'exercice

| Exigence | Critère |
|---|---|
| Authentification | Comptes administrateurs client et fournisseur nominatifs, MFA imposé et récupération contrôlée |
| Autorisation | Isolation des données entre clients et droits limités au besoin |
| Assurance applicative | Aucun défaut ouvert permettant un accès non autorisé aux données clients avant production |
| Reprise | RTO huit heures et RPO 24 heures sur le service complet, à valider avec le métier |
| Journaux | Événements utiles disponibles 90 jours ou solution équivalente testée et approuvée |
| Incident | Première notification client sous 24 heures après confirmation d'un incident affectant ses données ou son service |
| Données et tiers | Localisations, accès support et sous-traitants identifiés et changements notifiés |
| Sortie | Export complet utilisable et fenêtre de récupération de trente jours proposée |
| Suppression | Délais distincts pour données actives et sauvegardes, engagements et preuve de fin de traitement |
| Conformité applicable | Revue compétente des obligations contractuelles et relatives aux données avant production |

Les durées ci-dessus sont des besoins contractuels locaux. Elles ne sont pas attribuées à une loi ou à une norme.

## 5. Responsabilités

| Rôle fictif | Responsabilité |
|---|---|
| RS | Propriétaire du risque fournisseur et du service de support |
| RSSI | Examine preuves, risques, remédiation et conditions de sécurité |
| RI | Vérifie droits du tenant, journaux et moyens de reprise client |
| RJ | Examine contrat, traitement de données et destinations |
| DG | Autorise la production et les exceptions importantes |
| SupportCloud | Fournit les pièces, décrit son périmètre et traite ses écarts |

Le client garde la responsabilité de ses comptes, données envoyées et usages. Le fournisseur garde celle des composants et opérations relevant de son service. Une matrice de responsabilités doit confirmer les frontières avant signature.

## 6. Méthode d'examen

Les réponses Q01 à Q20 sont recoupées avec V01 à V09. Un document doit correspondre au bon service, à la bonne formule, au bon tenant ou à la bonne population et à une période pertinente.

Quatre appréciations sont utilisées : documenté pour la conception, partiel, écart confirmé dans le cas, non démontré. Il n'y a pas de moyenne pondérée ni de score global de conformité.

Les risques S01 à S08 utilisent la même échelle V × I que le projet 1. Un manque de preuve diminue l'assurance ; la cotation du risque repose aussi sur un scénario, une exposition et un impact.

## 7. Lien avec le projet 1

Le risque R08 reprend le scénario fournisseur S08, score actuel estimé 16, comme risque prospectif du passage en production. Les huit risques fournisseur ne sont pas additionnés à R08.

Les autres risques fournisseur sont suivis dans ce dossier. Le registre global pourra être enrichi selon les décisions de périmètre, sans créer deux fois le même événement.

## Références

[NIST SP 1305](https://csrc.nist.gov/pubs/sp/1305/final), [NIST CSF 2.0](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf).
