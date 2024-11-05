###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class PerolIngredient(models.Model):
    _name = 'perol.ingredient'
    _description = 'Perol ingredient'
    _order = 'sequence,id'
    _rec_name = 'product_id'

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Product',
        required=True,
    )
    perol_reference = fields.Many2one(
        comodel_name='perol',
        string='Perol related',
        required=False,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    perol_id = fields.Many2one(
        comodel_name='perol',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    uom_id = fields.Many2one(
        related='product_id.uom_id',
        string='UoM',
        store=True,
        readonly=False,
    )
    uom_name = fields.Char(
        string='Uom',
        related='uom_id.name',
        readonly=True,
    )
    product_qty = fields.Float(
        string='Quantity',
        digits='UoM',
        default=1.0,
        required=True,
    )
    recipe_uom_id = fields.Many2one(
        comodel_name='uom.uom',
        string='UoM recipe',
    )
    recipe_qty = fields.Float(
        string='Recipe qty',
        digits='UoM',
    )
    recipe_uom_name = fields.Char(
        related='recipe_uom_id.name',
        readonly=True,
    )
    uom_recipe_category_id = fields.Many2one(
        comodel_name='uom.category',
        string='Recipe uom category',
        compute='_compute_uom_recipe_category_id',
    )

    @api.depends('product_id')
    def _compute_uom_recipe_category_id(self):
        recipe_uom_type = self.env.ref('perol.product_uom_category_perol')
        for record in self:
            record.uom_recipe_category_id = recipe_uom_type
