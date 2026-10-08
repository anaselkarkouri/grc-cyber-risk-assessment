# Projet 2 - Dossier fournisseur simulé

**Version 1.0 - 7 octobre 2026**  
**Tous les documents V01 à V09 sont fictifs et créés pour cet exercice.**

Ces pièces sont des extraits narratifs et tableaux. Elles ne sont ni des captures réelles, ni des contrats signés, ni des certificats ISO. Les dates sont internes au scénario.

## V01 - Fiche de service et données, 1er octobre 2026

Service : SupportCloud. Formule proposée : Standard. Fonction : tickets, comptes, commentaires, pièces jointes et rapports.

Traitements cibles : noms, courriels professionnels, descriptions de demandes et pièces techniques. Les contenus sont fournis par le client. La plateforme ne garantit pas le blocage automatique des secrets déposés dans les tickets.

Localisations déclarées : hébergement principal en Irlande et sauvegardes en France. La fiche commerciale indique « vos données restent dans l'Union européenne ».

La fiche opérationnelle mentionne cependant des collaborateurs support au Maroc et au Portugal, avec accès possible aux tickets lorsqu'une assistance est demandée. L'accès d'un partenaire support externe est également mentionné sans localisation confirmée.

**Point d'examen :** hébergement, sauvegarde et accès distant doivent être distingués. La phrase commerciale ne couvre pas clairement tous les accès.

## V02 - Politique SSI et réponse aux incidents, 15 septembre 2026

La politique déclare TLS pour les échanges, chiffrement des données stockées, procédure de signalement et équipe de réponse.

L'annexe incident prévoit une première information des clients « sous 72 heures après confirmation ». Le dossier ne comporte pas de compte rendu d'exercice coordonné avec un client.

Le document d'architecture décrit la protection des données et une gestion de clés par le fournisseur, mais aucun relevé de configuration ou exercice de récupération de clés n'est fourni.

**Point d'examen :** le document étaye la conception. Il ne prouve pas toutes les configurations ou l'efficacité des opérations. Le délai de 72 heures diffère du besoin contractuel de 24 heures du cas.

## V03 - Identités et accès support, 3 octobre 2026

| Population | Configuration décrite |
|---|---|
| Administrateurs du tenant client | MFA disponible, activation laissée au titulaire, pas d'obligation dans la formule Standard |
| Lecteurs du tenant | Rôle limité documenté |
| Administrateurs techniques nominatifs du fournisseur | MFA annoncé |
| SUPPORT-PARTAGE | Compte utilisé par plusieurs opérateurs, MFA non imposé |
| Fédération et règles avancées | Présentées pour la formule Enterprise, hors formule Standard évaluée |

Le fournisseur déclare dans le questionnaire que « tous les accès administrateurs sont protégés par MFA ». Cette déclaration ne distingue pas le tenant client, les administrateurs techniques et le compte support.

Une revue trimestrielle est annoncée, mais la liste de revue avec décideur et résultat n'est pas fournie.

**Point d'examen :** disponibilité d'une fonctionnalité et obligation effective sont différentes. Les caractéristiques Enterprise ne sont pas attribuées au contrat Standard.

## V04 - Journaux du service, 2 octobre 2026

Événements décrits : connexions, modifications de rôles, accès support et certaines opérations sur les tickets.

Formule Standard : historique client disponible trente jours. Export manuel annoncé pour certains événements. La complétude de l'export, son intégrité, les limites de volume et sa disponibilité après résiliation ne sont pas démontrées.

Conservation 90 jours présentée dans une offre supérieure. Aucune méthode de protection contre la modification des journaux ni liste des droits d'administration des logs n'est fournie.

**Point d'examen :** un export manuel peut être une piste compensatoire, mais n'est pas considéré équivalent à 90 jours de journaux utiles tant qu'il n'est pas testé, complet et protégé.

## V05 - Sauvegarde et exercice de restauration, 4 octobre 2026

Le document indique une sauvegarde quotidienne et une conservation de 90 jours. Sept jobs récents sont indiqués réussis.

Un compte rendu d'exercice du 20 août 2026 indique une restauration de fichiers en six heures. Le périmètre exclut explicitement la base de tickets, les index et l'authentification du service.

Le questionnaire affirme : « Notre reprise en huit heures est démontrée. » Le dossier ne contient pas de restauration du service complet ni de mesure du point de reprise.

**Point d'examen :** le résultat de six heures sur des fichiers n'établit pas un RTO huit heures pour le SaaS entier. Le RPO 24 heures reste à démontrer.

## V06 - Rapport de sécurité applicative, 12 septembre 2026

Le dossier fournit un résumé de test sur le portail et l'API de tickets. L'auteur du résumé est une équipe de test fictive. Aucun véritable prestataire n'est nommé.

| Constat de test simulé | Gravité du résumé | État déclaré au 7 octobre |
|---|---|---|
| Autorisation inter-clients insuffisante sur une consultation de ticket | Élevée | Ouvert, correctif annoncé, pas de retest |
| En-tête de sécurité incomplet | Faible | Corrigé selon déclaration, preuve partielle |

Les modules d'intégration de la formule Enterprise sont hors du périmètre du rapport. Aucune URL, charge d'exploitation ou cible réelle n'est fournie.

La gravité de ce résumé est distincte du score de risque V × I calculé dans notre étude.

**Point d'examen :** un défaut d'autorisation ouvert sur les données clients constitue un blocage de production dans les critères du cas. Le rapport ne prouve pas l'absence de toutes les autres vulnérabilités.

## V07 - Sous-traitants et accès, 1er octobre 2026

| Fonction | Localisation déclarée | Assurance fournie |
|---|---|---|
| Hébergement principal | Irlande | Fiche de service |
| Stockage de sauvegarde | France | Fiche de service |
| Support interne | Maroc et Portugal | Description opérationnelle |
| Partenaire support externe | Non confirmée | Identité, localisation et responsabilités incomplètes |

La procédure de notification d'un nouveau sous-traitant est mentionnée, mais le délai et le droit d'objection ne figurent pas clairement dans le projet de contrat.

**Point d'examen :** liste incomplète et cartographie des accès insuffisante. Cela ne démontre pas à soi seul un transfert illicite ; cela empêche une décision éclairée.

## V08 - Conditions contractuelles de démonstration, 2 octobre 2026

**Projet de contrat, non signé.**

- Export de tickets annoncé en CSV depuis l'interface ; export complet des pièces jointes non démontré.
- Accès après résiliation : 48 heures proposées dans la rédaction actuelle.
- Données actives : suppression annoncée sous trente jours.
- Sauvegardes : expiration progressive annoncée sous 90 jours, avec exceptions non détaillées.
- Preuve de suppression : aucun format de compte rendu convenu.
- Notification d'incident : renvoi à la politique interne, sans engagement contractuel de 24 heures.
- Droit d'audit : documents de synthèse seulement ; modalités de demandes complémentaires à préciser.
- Modification des sous-traitants : modalités incomplètes.

**Point d'examen :** les besoins du client ne sont pas encore contractualisés. Une promesse technique dans une présentation ne vaut pas engagement signé.

## V09 - Fiche de vérification d'une allégation ISO, 7 octobre 2026

La page commerciale fictive contient l'allégation « ISO 27001 certified ». Le dossier ne fournit pas de certificat actuel lisible.

Une ancienne fiche d'assurance concerne une activité d'hébergement mutualisé et ne permet pas d'établir que SupportCloud et la formule Standard sont dans le périmètre. Organisme certificateur, dates de validité et portée du service ne sont pas démontrés.

**Conclusion : certification actuelle du service non démontrée.** Le portfolio ne dit ni que le fournisseur est certifié, ni qu'il ne l'est pas. Il ne fabrique pas de certificat ou de référence d'accréditation.

L'absence de certificat ne prouve pas l'absence de contrôles de sécurité. Elle impose d'examiner les autres pièces et de limiter l'assurance apportée par l'allégation commerciale.

## Cohérence volontaire du dossier

Trois rapprochements illustrent les limites d'une réponse déclarative :

1. « Tous les administrateurs utilisent le MFA » doit être comparé aux différentes populations de V03.
2. « Reprise en huit heures démontrée » doit être comparé au périmètre limité de V05.
3. « Données uniquement en Europe » doit être comparé aux accès support et tiers de V01/V07.

Les contradictions sont des données de l'exercice, pas des accusations concernant un fournisseur réel.
