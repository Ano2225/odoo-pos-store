import logging

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """
    Après installation : définit Point de Vente comme page d'accueil
    pour les caissiers existants qui n'en ont pas encore.

    Seul travail légitime pour un hook : initialisation de données.
    La gestion des menus et des groupes est faite en XML/security.
    """
    pos_user_group = env.ref(
        'point_of_sale.group_pos_user', raise_if_not_found=False
    )
    pos_manager_group = env.ref(
        'point_of_sale.group_pos_manager', raise_if_not_found=False
    )
    pos_action = env.ref(
        'point_of_sale.action_pos_config', raise_if_not_found=False
    )

    if not pos_user_group or not pos_action:
        _logger.warning('pos_access_restriction: groupes ou action POS introuvables')
        return

    cashiers = env['res.users'].with_context(active_test=False).search([
        ('groups_id', 'in', [pos_user_group.id]),
        ('groups_id', 'not in', [pos_manager_group.id] if pos_manager_group else []),
        ('share', '=', False),
    ])

    count = 0
    for user in cashiers:
        if not user.action_id:
            env.cr.execute(
                'UPDATE res_users SET action_id = %s WHERE id = %s',
                (pos_action.id, user.id),
            )
            count += 1

    if count:
        env['res.users'].invalidate_model(['action_id'])
        _logger.info(
            'pos_access_restriction: home POS défini pour %d caissier(s)', count
        )


def uninstall_hook(env):
    """
    Lors de la désinstallation : retire la home action POS
    des utilisateurs à qui on l'avait assignée.
    """
    pos_action = env.ref(
        'point_of_sale.action_pos_config', raise_if_not_found=False
    )
    if not pos_action:
        return

    env.cr.execute(
        'UPDATE res_users SET action_id = NULL WHERE action_id = %s',
        (pos_action.id,),
    )
    env['res.users'].invalidate_model(['action_id'])
    _logger.info('pos_access_restriction: home action POS retirée à la désinstallation')
