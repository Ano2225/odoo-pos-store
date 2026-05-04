{
    "name": "POS Ticket 58mm",
    "version": "18.0.1.0.0",
    "summary": "Adapte le ticket du POS pour impression sur imprimante thermique 58mm",
    "description": """
Module qui adapte le rendu du ticket POS Odoo pour une imprimante 58mm :
- Force la largeur du ticket à ~215px
- Cache la mention « Généré par Odoo »
- Cache les lignes de paiement (Wave, Carte, Mobile Money, etc.)
- Ajuste la police et l'espacement pour un papier étroit
    """,
    "author": "Custom",
    "category": "Point of Sale",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "data": [],
    "assets": {
        "point_of_sale._assets_pos": [
            "pos_ticket_58mm/static/src/css/receipt_58mm.css",
            "pos_ticket_58mm/static/src/xml/receipt_58mm.xml",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
}
