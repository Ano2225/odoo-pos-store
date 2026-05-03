from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    allowed_user_ids = fields.Many2many(
        comodel_name='res.users',
        relation='pos_config_allowed_users_rel',
        column1='pos_config_id',
        column2='user_id',
        string='Vendeurs autorisés',
        help='Utilisateurs autorisés à ouvrir cette caisse. '
             'Laisser vide = tous les utilisateurs POS y ont accès.',
    )
