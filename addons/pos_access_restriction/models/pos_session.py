from odoo import models, api, exceptions, _


class PosSession(models.Model):
    _inherit = 'pos.session'

    @api.model_create_multi
    def create(self, vals_list):
        """Bloque l'ouverture d'une session non autorisée pour les caissiers."""
        if not self.env.user.has_group('point_of_sale.group_pos_manager'):
            for vals in vals_list:
                config = self.env['pos.config'].browse(vals.get('config_id'))
                allowed = config.allowed_user_ids
                if allowed and self.env.user not in allowed:
                    raise exceptions.AccessError(
                        _("Vous n'êtes pas autorisé à ouvrir la caisse « %s ».\n"
                          "Contactez votre manager.") % config.name
                    )
        return super().create(vals_list)
