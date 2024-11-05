###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_food = fields.Boolean(
        string=' Is food',
    )
    food_allergen_ids = fields.Many2many(
        comodel_name='product.template.allergen',
        relation='product_template_allergen_relation',
        column1='template_id',
        column2='allergen_id',
        string='Allergens',
    )
    food_energy_cal = fields.Float(
        string='Energy cal',
        digits='Stock Weight',
    )
    food_energy_kj = fields.Float(
        string='Energy Kj',
        digits='Stock Weight',
    )
    food_fat = fields.Float(
        string='Fat',
        digits='Stock Weight',
    )
    food_saturated_fat = fields.Float(
        string='Saturated fat',
        digits='Stock Weight',
    )
    food_proteins = fields.Float(
        string='Proteins',
        digits='Stock Weight',
    )
    food_carbohydrates = fields.Float(
        string='Carbohydrates',
        digits='Stock Weight',
    )
    food_sugar = fields.Float(
        string='Sugar',
        digits='Stock Weight',
    )
    food_salt = fields.Float(
        string='Salt',
        digits='Stock Weight',
    )
    food_fiber = fields.Float(
        string='Fiber',
        digits='Stock Weight',
    )
    food_nutritional_uom = fields.Many2one(
        comodel_name='uom.uom',
        string='Nutritional uom',
        default=lambda self: self.env.ref('uom.product_uom_gram'),
    )
    food_energy_uom = fields.Many2one(
        comodel_name='uom.uom',
        string='Energy uom',
    )
