from odoo import models, api, exceptions, _

class PosOrder(models.Model):
    _inherit = 'pos.order'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            config = self.env['pos.config'].browse(vals.get('config_id'))
            user = self.env.user

            # 🔒 BLOQUAGE STRICT DES COMMANDES HORS CAISSE AUTORISÉE
            if config.allowed_user_ids and user not in config.allowed_user_ids:
                raise exceptions.AccessError(_(
                    "Action interdite : caisse non autorisée pour cet utilisateur."
                ))

        return super().create(vals_list)