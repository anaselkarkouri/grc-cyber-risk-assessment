# Matrice des preuves et traçabilité

**Version 1.1 - opérations réelles du 07/10/2026. Horodatages techniques en UTC.**

Exécution automatisée par Codex sur le poste personnel d’Anas. Les preuves sont réelles ; elles ne décrivent ni Atlas Services ni SupportCloud. Les pièces E/V restent simulées.

Les chemins ci-dessous désignent les exports réels de référence finale. Les SHA-256 vérifient l’identité du fichier conservé ; ils n’attestent ni signature indépendante ni immutabilité du stockage. Les exports T01 sont assainis à la création ; les commandes Git et ACL et les objets artificiels T03 sont conservés. Les diagnostics retranscrits indiquent leur nature.

| Pièce | Lien | Origine et portée |
| --- | --- | --- |
| REFERENCE | [REFERENCE_MANIFEST.json](preuves/20261007T192733Z/REFERENCE_MANIFEST.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T03-P01 | [T03-P01_attendus.json](preuves/20261007T192733Z/T03-P01_attendus.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T03-P02 | [T03-P02_copie.json](preuves/20261007T192733Z/T03-P02_copie.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T03-P03 | [T03-P03_comparaison.json](preuves/20261007T192733Z/T03-P03_comparaison.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T03-P04 | [T03-P04_chronologie.json](preuves/20261007T192733Z/T03-P04_chronologie.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T03 | [T03_copie_artificielle.zip](preuves/20261007T192733Z/T03_copie_artificielle.zip) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T04-P01 | [T04-P01_perimetre_droits.json](preuves/20261007T192733Z/T04-P01_perimetre_droits.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T04-P02 | [T04-P02_premier_commit.json](preuves/20261007T192733Z/T04-P02_premier_commit.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T04-P03 | [T04-P03_historique.json](preuves/20261007T192733Z/T04-P03_historique.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T04-P04 | [T04-P04_conclusion.json](preuves/20261007T192733Z/T04-P04_conclusion.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01-P01 | [T01-P01_regles_roles.json](preuves/20261007T193900Z/T01-P01_regles_roles.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01-P02 | [T01-P02_autorisations.json](preuves/20261007T193900Z/T01-P02_autorisations.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01-P03 | [T01-P03_mfa.json](preuves/20261007T193900Z/T01-P03_mfa.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01-P04 | [T01-P04_revocation_recuperation.json](preuves/20261007T193900Z/T01-P04_revocation_recuperation.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01 | [T01_chemins_alternatifs.json](preuves/20261007T193900Z/T01_chemins_alternatifs.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01 | [T01_evenements_assainis.json](preuves/20261007T193900Z/T01_evenements_assainis.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01 | [T01_statut.json](preuves/20261007T193900Z/T01_statut.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| inventaire | [inventaire_initial.json](preuves/INVENTAIRE/inventaire_initial.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T01-D01 | [T01-D01_diagnostics.txt](preuves/INVENTAIRE/T01-D01_diagnostics.txt) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| T02-D01 | [T02-D01_acces_refuses.txt](preuves/INVENTAIRE/T02-D01_acces_refuses.txt) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |
| VERIFICATION | [VERIFICATION_DOCUMENTAIRE.json](preuves/INVENTAIRE/VERIFICATION_DOCUMENTAIRE.json) | Commande locale / réponse serveur / diagnostic limité ; voir fiche du test |


Le fichier [MANIFEST_FINAL.json](MANIFEST_FINAL.json) contient taille, date et SHA-256 de chaque pièce finale. Les anciens dossiers T01 conservent les essais et retests ; leurs T01-P01 ne sont pas substitués aux pièces finales ci-dessus. T02-P01/P02 source, P01 gestionnaire, P03 réception, P04 alerte, P05/P05b revue et P06 rapprochement disponibles ; conservation longue durée non démontrée.

## Chaîne documentaire du cas

E02 → C01 → R01 → M01 → T01 ; E03 → C02 → R04 → M04 → T02 ; E04 → C03 → R03 → M03 → T03 ; E05 → C04 → R06 → M06 → T04. Ce rapprochement est pédagogique et n’est pas une clôture des actions fictives.

V03 → F01/S01/VM01/G2 et F02/S02/VM02/G2 ; V04 → F03/S03/VM03/G4 ; V05/V08 → F04/S04/VM04/G3 ; V01/V07 → F05/S05/VM05/G5 ; V08 → F06/S06/VM06/G6 ; V02/V08 → F07/S07/VM07/G4 ; V06 → F08/S08/VM08/G1. V09/Q17 reste une assurance transversale non démontrée.

## Pièces réelles T02 ajoutées

- [T02-D02_preparation_VM.json](preuves/20261007T195320Z/T02-D02_preparation_VM.json)
- [T02-D03_console_apres_cpu.png](preuves/20261007T195320Z/T02-D03_console_apres_cpu.png)
- [T02-D03_console_hyperv.png](preuves/20261007T195320Z/T02-D03_console_hyperv.png)
- [T02-D03_console_initiale.png](preuves/20261007T195320Z/T02-D03_console_initiale.png)
- [T02-D03_console_sans_ioapic.png](preuves/20261007T195320Z/T02-D03_console_sans_ioapic.png)
- [T02-D04_diagnostics_VM.json](preuves/20261007T195320Z/T02-D04_diagnostics_VM.json)
- [T02-P01_source.json](preuves/20261007T195320Z/T02-P01_source.json)
- [T02-P02_evenement_local.json](preuves/20261007T195320Z/T02-P02_evenement_local.json)

## Exports Wazuh et rapprochement final

- [T02-D05_diagnostic_export.txt](preuves/20261007T202438Z/T02-D05_diagnostic_export.txt)
- [T02-D06_diagnostic_https.txt](preuves/20261007T202438Z/T02-D06_diagnostic_https.txt)
- [T02-D06_diagnostic_installer.txt](preuves/20261007T202438Z/T02-D06_diagnostic_installer.txt)
- [T02-D06_diagnostic_reseau.txt](preuves/20261007T202438Z/T02-D06_diagnostic_reseau.txt)
- [T02-P01_gestionnaire.json](preuves/20261007T202438Z/T02-P01_gestionnaire.json)
- [T02-P03_reception.json](preuves/20261007T202438Z/T02-P03_reception.json)
- [T02-P04_alerte.json](preuves/20261007T202438Z/T02-P04_alerte.json)
- [T02-P05_droits_conservation.json](preuves/20261007T202438Z/T02-P05_droits_conservation.json)
- [T02-P05b_parametres_retention.json](preuves/20261007T202438Z/T02-P05b_parametres_retention.json)
- [T02-P06_rapprochement.json](preuves/20261007T202438Z/T02-P06_rapprochement.json)
