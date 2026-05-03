import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_pos = fields.Many2many(
        comodel_name='pos.config',
        relation='pos_config_allowed_users_rel',
        column1='user_id',
        column2='pos_config_id',
        string='Caisses autorisées',
        help='Caisses POS que cet utilisateur peut voir et ouvrir. '
             'Laisser vide = accès à toutes les caisses.',
    )

    def write(self, vals):
        result = super().write(vals)
        # Synchroniser la page d'accueil POS dès que les groupes changent
        if 'groups_id' in vals and 'action_id' not in vals:
            self._sync_pos_home_action()
        return result

    def _sync_pos_home_action(self):
        """
        Définit automatiquement Point de Vente comme page d'accueil
        quand un utilisateur devient caissier (group_pos_user sans group_pos_manager).
        Retire l'action POS si l'utilisateur n'est plus caissier.
        Utilise SQL direct pour éviter une boucle récursive dans write().
        """
        pos_user_group = self.env.ref(
            'point_of_sale.group_pos_user', raise_if_not_found=False
        )
        pos_manager_group = self.env.ref(
            'point_of_sale.group_pos_manager', raise_if_not_found=False
        )
        pos_action = self.env.ref(
            'point_of_sale.action_pos_config', raise_if_not_found=False
        )

        if not pos_user_group or not pos_action:
            return

        invalidate = False

        for user in self:
            is_cashier = pos_user_group in user.groups_id
            is_manager = pos_manager_group and pos_manager_group in user.groups_id

            if is_cashier and not is_manager and not user.action_id:
                # Nouveau caissier sans home action → POS
                self.env.cr.execute(
                    'UPDATE res_users SET action_id = %s WHERE id = %s',
                    (pos_action.id, user.id),
                )
                invalidate = True

            elif not is_cashier and user.action_id and user.action_id.id == pos_action.id:
                # Plus caissier → on retire le home POS qu'on avait posé
                self.env.cr.execute(
                    'UPDATE res_users SET action_id = NULL WHERE id = %s',
                    (user.id,),
                )
                invalidate = True

        if invalidate:
            self.invalidate_recordset(['action_id'])
            _logger.info(
                'pos_access_restriction: home action synchronisée pour %s',
                self.mapped('login'),
            )
