# POS Ticket 58mm (Odoo 18)

Module Odoo 18 qui adapte le ticket de caisse du Point of Sale à une
imprimante thermique **58 mm**.

## Ce que fait le module

- Force la largeur du ticket à **~215 px** (58 mm) pour qu'il s'imprime
  correctement, sans débordement ni décalage.
- **Cache** la mention « Généré par Odoo » / *Powered by Odoo*.
- **Cache** les lignes de paiement affichées sur le ticket (Wave, Carte,
  Mobile Money, Espèces, etc.).
- Ajuste **police** (monospace) et **espacement** pour rester lisible
  sur papier étroit.
- Ajoute des règles `@media print` avec `@page size: 58mm auto`.

## Installation

1. Copier le dossier `pos_ticket_58mm/` dans votre dossier `addons`
   (ex: `/mnt/extra-addons/pos_ticket_58mm/`).
2. Redémarrer Odoo :
   ```bash
   sudo service odoo restart
   ```
3. Activer le **mode développeur**, puis :
   *Apps → Mettre à jour la liste des applications → Rechercher
   « POS Ticket 58mm » → Installer*.
4. Ouvrir une session de Point of Sale et imprimer un ticket de test.
   > Si l'aperçu n'est pas mis à jour, videz le cache du navigateur
   > (Ctrl+Shift+R).

## Configuration imprimante

Dans le pilote de l'imprimante (Windows / CUPS), définir :
- Largeur papier : **58 mm**
- Marges : **0**
- Échelle : **100 %** (pas d'ajustement automatique)

## Personnalisation

- Pour changer la largeur : modifier la valeur `215px` (et `58mm` dans
  `@media print`) dans `static/src/css/receipt_58mm.css`.
- Pour changer la police : remplacer la `font-family` dans le même
  fichier.

## Compatibilité

- Odoo **18.0** (Community & Enterprise)
- Module : `point_of_sale`
