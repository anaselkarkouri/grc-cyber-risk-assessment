# Revue finale du dossier fournisseur

**Version 1.1 - 07/10/2026 ; données de référence fictives inchangées au 7 octobre 2026.**

## Conclusion

Les vingt réponses ont été rapprochées des neuf pièces ; huit chaînes F/S/VM correspondent aux six conditions G. La recommandation défavorable à la production reste justifiée. Aucune nouvelle preuve fournisseur réelle n’a été obtenue. Les tests personnels ne lèvent aucune condition G.

## Recoupement de chaque question

| Question | Pièces examinées | Chaîne ou sujet | Appréciation conservée |
| --- | --- | --- | --- |
| Q01 | V01 | cadrage | Documenté pour le cadrage. Ne pas retenir les fonctions Enterprise |
| Q02 | V01 | usage et minimisation | Partiel : le client doit maîtriser ce qu'il envoie |
| Q03 | V01,V07 | F05/S05/VM05/G5 | Partiel : distinguer stockage et accès distant ; partenaire externe encore inconnu |
| Q04 | V07 | F05/S05/VM05/G5 | Non démontré pour la liste complète et les modalités de changement |
| Q05 | V03 | F01/S01/VM01/G2 | Conception documentée ; fonctionnement sur un tenant à vérifier |
| Q06 | V03 | F01/S01/VM01/G2 | Écart au besoin du cas : activation possible ne démontre pas obligation |
| Q07 | V03 | F02/S02/VM02/G2 | Écart confirmé dans le dossier simulé |
| Q08 | V03 | F02/S02/VM02/G2 | Non démontré. Ne pas conclure que la revue n'existe pas |
| Q09 | V02 | assurance de chiffrement transversale | Documenté pour la conception ; configuration et opérations non démontrées |
| Q10 | V04 | F03/S03/VM03/G4 | Écart au besoin de 90 jours, solution compensatoire non validée |
| Q11 | V04 | F03/S03/VM03/G4 | Non démontré, information complémentaire nécessaire |
| Q12 | V06 | F08/S08/VM08/G1 | Écart confirmé, blocage de production |
| Q13 | V06 | F08/S08/VM08/G1 | Partiel : rapport utile, pas assurance exhaustive ni preuve de retest |
| Q14 | V05,V08 | F04/S04/VM04/G3 | Non démontré pour le service complet et le RPO |
| Q15 | V08 | F04/F06/S04/S06/VM04/VM06/G3/G6 | Partiel, avec écart à la fenêtre proposée de trente jours |
| Q16 | V08 | F06/S06/VM06/G6 | Partiel : engagements et preuve de fin de traitement à préciser |
| Q17 | V09 | assurance ISO transversale non demontree | Certification du service non démontrée ; ne pas la déclarer inexistante |
| Q18 | V02,V08 | F07/S07/VM07/G4 | Écart au besoin contractuel de 24 heures ; ce besoin n'est pas présenté comme légal |
| Q19 | V08 | cadre contractuel transversal G4/G5/G6 | Partiel ; examen et négociation nécessaires |
| Q20 | V02 | F07/S07/VM07/G4 | Coordination opérationnelle non démontrée |


## Vérification des produits et des niveaux

24 produits S inhérent/actuel/cible recalculés et huit niveaux actuels contrôlés ; aucun écart. S01/S02 : actuel 3×4=12, cible 1×4=4. S03 à S07 : actuel 3×4=12, cible 2×4=8. S08 : actuel 4×4=16, cible 2×4=8. Un critique/sept élevés actuellement pour l’usage cible ; deux faibles/six modérés conditionnels. Le miroir R08/S08 n’est pas additionné.

## Contradictions et portée des preuves

- MFA : V03 contredit le « tous protégés » ; Standard facultatif et SUPPORT-PARTAGE sans obligation. Cela établit un écart décrit ; Q08, sans rapport de revue, reste non démontré.
- Reprise : V05 exclut base, index et authentification. Six heures de fichiers ne prouvent ni RTO du SaaS entier ni RPO. Des sauvegardes sont déclarées ; leur absence n’est pas conclue.
- Localisations : Irlande/France pour stockage, Maroc/Portugal pour accès support et partenaire inconnu V07. Cartographie insuffisante, sans conclusion de transfert illicite.
- Standard/Enterprise : fédération avancée, durée de journaux supérieure et intégrations Enterprise ne sont pas attribuées à Standard. Une migration est une option à réévaluer.
- V09 : certification alléguée non démontrée pour le service, organisme et validité ; jamais déclarée inexistante.
- Q09 : conception de chiffrement décrite, configuration et opérations non démontrées. Q02 reste un besoin de minimisation client, pas un neuvième risque artificiel.
- Délais : 24 h incident, 90 jours logs, 30 jours de récupération, échéances et revues sont des exigences locales proposées. Aucun faux délai légal ni prescription ISO universelle.
- Version anglaise : même périmètre Standard, vingt tickets artificiels, un critique/sept élevés, conditions ouvertes, pilote proposé jusqu’au 6 novembre 2026 ; cibles conditionnelles concordantes.

## Trace automatisée et examen qualitatif

[VERIFICATION_DOCUMENTAIRE.json](../Annexes_laboratoire/preuves/INVENTAIRE/VERIFICATION_DOCUMENTAIRE.json) conserve 109 contrôles pour les deux projets. Ils vérifient produits, niveaux actuels, références Q, correspondances F/S/VM et miroir. La pertinence, les contradictions, les limites et la décision ont été relues qualitativement en complément ; une présence de référence ne constitue pas une preuve d’efficacité.

Scores et décision inchangés : aucune erreur de cotation trouvée. Actions VM01 à VM08 et conditions G1 à G6 restent ouvertes/non satisfaites ou non démontrées selon leur état initial.
