###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class Uom(models.Model):
    _inherit = 'uom.uom'

    no_show_quantity = fields.Boolean(
        string='No show quantity',
    )
