FROM odoo:18

# Copier les modules custom et la configuration Odoo
COPY ./addons /mnt/extra-addons
COPY ./config/odoo.conf /etc/odoo/odoo.conf

# Assurer les bonnes permissions
RUN chown -R odoo:odoo /mnt/extra-addons /etc/odoo/odoo.conf
