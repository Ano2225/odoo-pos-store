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
    'author': 'Custom — basé sur l\'approche Cybrosys Technologies',
    'depends': ['point_of_sale'],
    'data': [
        'security/pos_access_groups.xml',
        'security/ir.model.access.csv',
        'security/ir_rules.xml',
        'views/res_users_views.xml',
        'views/pos_config_views.xml',
        'views/pos_menus.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
