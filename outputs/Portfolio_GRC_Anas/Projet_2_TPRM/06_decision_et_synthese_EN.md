# Projet 2 - Décision proposée et executive summary

**SupportCloud - cas pédagogique / formule Standard**  
**Version 1.0 - 7 octobre 2026**  
**Dossier simulé ; aucune décision d'une entreprise réelle ni signature réelle.**

## 1. Décision en français

### Avis de sécurité proposé

**Ne pas autoriser le passage en production en l'état.**

Le défaut d'autorisation inter-clients décrit dans V06 est ouvert et n'a pas de retest. Il expose potentiellement les tickets de l'usage cible. Le registre contient **un risque critique et sept risques élevés**, évalués pour cet usage futur avec données clients, et non pour une production déjà déployée.

Le pilote peut continuer dans le scénario uniquement avec ses vingt tickets artificiels, sans données personnelles réelles, documents clients, secrets, connecteurs de production ni dépendance opérationnelle. Cette poursuite limitée ne vaut pas homologation de production.

La décision de pilote est proposée jusqu'au **6 novembre 2026**, soit J+30. À cette date, l'absence de preuves suffisantes impose de réexaminer ou arrêter le pilote, et non de le transformer automatiquement en production.

### Motifs déterminants

1. **Isolation non démontrée après correction** : défaut inter-clients toujours ouvert, correctif annoncé mais non retesté.
2. **Accès privilégiés incomplets** : MFA facultatif sur le tenant Standard et compte support partagé sans MFA imposé.
3. **Reprise et investigation insuffisamment étayées** : exercice limité aux fichiers, RPO non démontré, journaux trente jours et solution d'export non validée.
4. **Encadrement des données et de la relation incomplet** : tiers support non identifié complètement, délai incident de 72 heures, sortie de 48 heures et export des pièces non démontré.

La certification alléguée n'est pas démontrée pour le service actuel. Cela limite l'assurance disponible, sans constituer une preuve que le fournisseur n'est pas certifié. Même une certification pertinente ne clôturerait pas les défauts spécifiques du dossier.

## 2. Ce qui permettrait de reconsidérer la production

Les six conditions G1 à G6 du [plan de remédiation](05_remediation_suivi.md) doivent être vérifiées :

| Condition | Résultat attendu avant décision favorable |
|---|---|
| G1 | Correctif et retest inter-clients pertinents pour le service retenu |
| G2 | Administrateurs client et accès support nominatifs, MFA imposé, exceptions et récupération examinées |
| G3 | Objectifs métier confirmés, reprise complète et récupération client effectivement démontrées |
| G4 | Journaux utiles et protégés sur la durée retenue ; notification et coordination d'incident convenues et exercées |
| G5 | Tiers, accès, lieux et responsabilités documentés ; revue compétente des engagements et obligations applicables |
| G6 | Export complet utilisable, fenêtre suffisante et fin de traitement encadrée |

Les huit cibles de risque seraient alors **deux faibles et six modérées**, sous réserve de réévaluation. Ces valeurs sont des estimations conditionnelles et ne sont pas déjà atteintes.

Une solution compensatoire doit répondre au besoin du client et être testée dans son périmètre. Une autre formule est une nouvelle option à évaluer, pas un traitement déjà réalisé. Les contraintes de prix ou de calendrier ne suffisent pas à accepter un accès inter-clients ouvert sur des données réelles.

## 3. Fiche de décision renseignée

| Champ | Valeur de l'exercice |
|---|---|
| Objet | Usage du SaaS de tickets SupportCloud Standard |
| Périmètre évalué | Service et données envisagés ; pièces documentaires simulées |
| Propriétaire du risque | RS |
| Avis du dossier | Production défavorable en l'état |
| Pilote limité proposé | Vingt tickets artificiels, sans connexions de production |
| Fin de validité proposée du pilote | 6 novembre 2026 |
| Risque critique ouvert | S08, score 16 ; miroir R08 |
| Conditions favorables acquises | Aucune condition G satisfaite |
| Traitements ouverts | VM01 à VM08 |
| Acceptation de risque approuvée | Aucune |
| Avis juridique réel | Aucun |
| Autorisation et signature réelles | Aucune |
| Prochaine décision | Après réception et vérification des preuves ; sinon réexamen à J+30 |

DG fictive devrait enregistrer son arbitrage dans le scénario. Le présent document fournit une recommandation motivée et ne prétend pas tenir lieu de cette approbation.

## 4. Executive summary in English

### Third-party cybersecurity risk assessment

**Provider:** SupportCloud, fictional training case  
**Service:** B2B support ticketing SaaS, Standard plan  
**Assessment date:** 7 October 2026  
**Recommendation:** Do not approve production use under the conditions currently documented.

#### Purpose and scope

Atlas Services, a fictional company with 40 employees, is considering this SaaS for customer support. The intended production dataset includes professional names, email addresses, ticket content and technical attachments. Customer credentials, health data and identity documents are excluded from the proposed use.

The current pilot contains twenty synthetic tickets. It has no production connectors or operational dependency. This assessment examines the proposed production use through twenty questions and nine simulated provider documents. It is a documentary learning exercise, not an audit of a real provider or an operational security test.

#### Risk position

The intended service is considered critical because it would hold confidential customer information and support daily operations. Under the documented conditions, the register contains **one critical and seven high risks**. These ratings apply to future production exposure; they are not evidence of a real compromise.

The most significant blocker is an open cross-tenant authorization defect described in the simulated application test summary. A promised fix without a relevant retest does not establish that customers' data is isolated.

The other seven scenarios concern client administrator compromise, shared provider support access, insufficient investigation records, incomplete recovery, inadequately understood third-party access, loss or uncontrolled retention of data at exit, and delayed incident coordination.

#### Main evidence limitations

Three comparisons are particularly useful:

- The statement that all administrators use MFA conflicts with the Standard tenant configuration and the shared support account. MFA being available is different from MFA being enforced.
- A six-hour file restoration exercise does not demonstrate an eight-hour recovery objective for the full SaaS. Database, indexes and authentication were outside that exercise; the recovery point is also unproven.
- The statement that data remains in Europe does not explain all remote support access or the unidentified external support partner. Storage locations and access locations must be assessed separately.

Additional gaps include thirty-day client log availability, an unvalidated partial export, a proposed 72-hour incident notification period, and a 48-hour post-termination access window. The client's proposed requirements are 90-day useful log availability, initial notification within 24 hours after confirmation of an incident affecting the client, and an adequate recovery window, initially proposed as thirty days.

These durations are requirements designed for this exercise. They are not presented as statutory deadlines or universal ISO/NIST requirements.

The marketing claim of ISO certification is not supported by a current certificate with demonstrated scope and validity in the available dossier. This means the claim is unverified, not that certification does not exist. A suitable certificate could add assurance but would not resolve the service-specific findings.

#### Required conditions before production

1. Correct and retest the cross-tenant authorization defect within the relevant service scope.
2. Enforce individual privileged identities and MFA for both the client tenant and provider support, including controlled recovery and emergency access.
3. Demonstrate full service recovery against agreed business objectives and prove that customer data can be retrieved and used.
4. Provide useful, protected investigation records and agree and exercise incident notification and coordination.
5. Complete the access and subprocessor map, establish responsibilities, and obtain a competent review of contractual and applicable data protection requirements.
6. Demonstrate complete export and establish workable exit, retention and deletion arrangements.

All eight remediation actions remain open. If their effectiveness is verified, the estimated target position would be **two low and six moderate risks**. Those target ratings are conditional; residual risks have not been reassessed on the basis of verified remediation.

#### Limited pilot decision

A synthetic-data pilot may continue in the training scenario until **6 November 2026**, subject to the existing restrictions: no real personal data, customer documents, secrets or production connections. If adequate evidence is not available by that date, the client should reassess or stop the pilot.

The limited pilot must not be interpreted as production approval or as acceptance of the critical data isolation risk.

#### Accountability and monitoring

The support service owner is accountable for the client's risk. Security evaluates evidence, IT verifies tenant and recovery functions, the legal/privacy role reviews the relevant commitments, and management decides whether production can be approved.

If the provider later becomes acceptable, access, security findings, incidents, subprocessors and changes should be reviewed on the proposed quarterly cycle, with a fuller reassessment at least annually in this case. Significant changes or incidents require earlier review.

**Decision status: production approval not recommended; remediation and evidence review outstanding. No real approval or contract is represented by this exercise.**

## 5. Présentation orale possible

« J'ai évalué un SaaS fictif pour un usage de support client. J'ai d'abord fixé la criticité et les exigences, puis recoupé vingt réponses avec neuf pièces simulées. J'ai distingué un écart explicite d'un contrôle non démontré. Le défaut inter-clients ouvert bloque la production malgré des réponses favorables sur d'autres sujets. J'ai proposé huit actions, leurs preuves de clôture et une décision limitée au pilote artificiel. »

Cette présentation est fidèle lorsque le dossier est compris et que le caractère simulé est annoncé. Ne pas dire avoir audité un fournisseur réel, négocié un contrat réel, exécuté son pentest ou obtenu ses preuves opérationnelles.

## Références

[NIST SP 1305](https://csrc.nist.gov/pubs/sp/1305/final) pour la démarche fournisseur ; [ISO/IEC 27005:2022](https://www.iso.org/standard/80585.html) pour les risques SSI. Les critères, scores, exigences et décisions sont propres au cas pédagogique.

## Revue de finalisation

07/10/2026 : [recoupement intégral](07_revue_documentaire.md), produits et chaînes vérifiés ; aucune nouvelle pièce fournisseur. Recommandation, scores et conditions conservés. Personal lab results do not establish SupportCloud control effectiveness or satisfy any production gate.
