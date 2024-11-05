###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class PerolTagCategory(models.Model):
    _name = 'perol.tag.category'
    _description = 'Perol tag'
    _order = 'sequence'

    name = fields.Char(
        string='Name',
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    tag_ids = fields.One2many(
        comodel_name='perol.tag',
        inverse_name='category_id',
        string='Tags',
    )
