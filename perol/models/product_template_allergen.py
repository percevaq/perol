###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ProductTemplateAllergen(models.Model):
    _name = 'product.template.allergen'
    _description = 'Product allergen'

    name = fields.Char(
        string='Name',
        translate=True,
    )
    description = fields.Text(
        string='Description',
        translate=True,
    )
    icon_128 = fields.Image(
        string='Icon',
    )
    avatar_128 = fields.Image(
        related='icon_128',
        string='avatar 128',
    )
