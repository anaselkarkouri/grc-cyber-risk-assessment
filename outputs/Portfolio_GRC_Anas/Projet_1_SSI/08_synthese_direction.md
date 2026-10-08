# Projet 1 - Synthèse pour la direction

**Évaluation des risques cyber et des contrôles SSI**  
**Atlas Services - entreprise fictive**  
**Version 1.0 - situation simulée au 7 octobre 2026**

## Décision proposée

Prioriser la protection des accès privilégiés, la réaction à l'exposition d'un secret, la restaurabilité des sauvegardes et le chiffrement du poste identifié. Maintenir le fournisseur SaaS hors production jusqu'à la levée des conditions du projet 2.

La direction fictive reçoit une évaluation documentaire renseignée. Les mesures proposées de la PME restent non exécutées. Les trois tests personnels T01/T03/T04 et le parcours partiel T02 sont documentés dans des annexes distinctes, sans effet automatique sur les cotations du cas.

## Résultats principaux

Le registre comprend douze risques : **cinq critiques, cinq élevés et deux modérés**. R08 est prospectif et concerne le SaaS avant production. Les onze risques liés aux activités existantes comprennent quatre critiques, cinq élevés et deux modérés.

Ces niveaux sont des jugements du cas, pas des fréquences mesurées. R03 et R11 comportent des hypothèses prudentes à valider ; la méthode documente une variante de cotation et son effet sur les priorités.

Le dossier examine dix actifs et huit constats documentaires. Les principaux écarts du scénario portent sur les comptes privilégiés, un secret exposé, un compte de départ encore actif, un poste non chiffré et un changement sans approbation.

La présence de sauvegardes est déclarée, mais leur restauration n'est pas démontrée. Le SIEM montre un signal sur une partie du périmètre ; la couverture et l'efficacité durable restent limitées.

Le registre prévoit trois risques faibles et neuf modérés **à l'état cible conditionnel**. Cette répartition n'est pas une amélioration déjà obtenue.

## Priorités

| Échéance proposée | Décision et action | Responsables |
|---|---|---|
| 8 octobre, J+1 | Invalider le secret du scénario et retirer l'accès de départ | RD, RI, RH |
| 9 octobre, J+2 | Réduire l'exposition des comptes privilégiés et du poste non chiffré ; protéger la reprise | RI |
| 17 octobre, J+10 | Corriger et faire valider la faiblesse applicative locale | RD |
| 22 octobre, J+15 | Obtenir une restauration documentée et une vision du parc | RI et RS |
| 6 novembre, J+30 | Étendre surveillance, sensibilisation, exports et maîtrise des changements | RI, RS, RD |
| 6 décembre, J+60 | Exercer la suppléance et la reprise documentaire | RI |
| Avant production SaaS | Lever les blocages fournisseur et obtenir les validations de sécurité et de données | RS, RSSI, RJ, DG |

## Indicateurs proposés

Ces indicateurs sont locaux. Les valeurs actuelles sont limitées aux pièces simulées disponibles.

| Indicateur | Valeur actuelle du cas | Cible | Limite et source |
|---|---|---|---|
| Comptes privilégiés avec MFA imposé | 1 sur 3 | 3 sur 3, ou exception maîtrisée et approuvée | E02 ; configuration, pas test de fonctionnement |
| Sources prioritaires déclarées couvertes | 2 sur 6 | 6 sur 6 ou exclusions justifiées | E03 ; pertinence et qualité de collecte à examiner |
| Rapports de restauration fournis | 0 | Un test du service et une revue périodique | E04 ; absence de preuve, pas preuve d'échec |
| Postes chiffrés dans l'échantillon | 2 sur 3 | 3 sur 3, puis couverture du parc vérifiée | E06 ; aucune extrapolation aux 40 |
| Actions M01 à M12 clôturées avec preuve | 0 sur 12 | Clôture progressive à l'échéance | Plan proposé, aucune exécution déclarée |
| Tests personnels exécutés | 4 sur 4 exécutés ; trois réussites bornées, un partiel | Conservation et couverture T02 à approfondir | Annexes réelles ; ne modifie pas les indicateurs E02/E03/E04 |

Ne pas présenter ces fractions comme un taux de conformité ISO.

## Arbitrages à obtenir

1. Valider le périmètre et les propriétaires des actifs et risques.
2. Confirmer avec le support les objectifs de reprise huit heures/24 heures.
3. Affecter ressources et suppléance aux actions.
4. Approuver PSSI, méthode et processus d'exception.
5. Décider du maintien du pilote SaaS avec données artificielles et des conditions de production.

## Assurance et limites

Cette étude montre le chemin entre actifs, scénarios, justificatifs, constats, traitement et décision. Les sources de l'entreprise sont fictives. L'efficacité réelle des contrôles n'est pas attestée. L'extrait de SoA porte sur vingt mesures et le profil NIST sur treize sous-catégories.

La lecture historique du rapport Tanger Med apporte une illustration technique distincte. Elle n'étend pas les conclusions à l'entreprise fictive.

## Message à retenir en entretien

« J'ai construit une étude de cas GRC documentée : le périmètre et les actifs conduisent aux scénarios, les preuves conditionnent les constats et les mesures ont des propriétaires et des critères de clôture. Je distingue les documents simulés, les observations historiques de stage et les trois tests de laboratoire prouvés et le parcours SIEM T02 partiel. »

## Historique de finalisation

07/10/2026 : annexes personnelles ajoutées ; scores, actions M et décision SaaS de référence inchangés.
