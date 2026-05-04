{
    'name': 'POS Access Restriction',
    'version': '18.0.2.0.0',
    'category': 'Point of Sale',
    'summary': "Restreindre l'accès aux caisses POS par utilisateur",
    'description': """
        - Définir par utilisateur quelles caisses il peut voir/ouvrir
        - Managers : accès à toutes les caisses
        - Caissiers : uniquement leurs caisses assignées
        - Menus Reporting/Commandes/Produits/Configuration cachés aux caissiers
        Configuration : Paramètres → Utilisateurs → onglet "Caisses POS autorisées"
    """,
    'author': 'Arouna Ouattara',
    'depends': [
        'point_of_sale',
        'pos_hr',
    ],
    'data': [
        'security/pos_access_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/res_users_views.xml',
        'views/pos_config_views.xml',
        'views/pos_menus.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_access_restriction/static/src/css/hide_backend.css',
            'pos_access_restriction/static/src/js/block_cashier_navbar.js',
            'pos_access_restriction/static/src/xml/pos_hr_override.xml',
    ]
    },
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
