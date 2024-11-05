###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class PerolStep(models.Model):
    _name = 'perol.step'
    _description = 'Perol step'
    _order = 'sequence,name'

    name = fields.Char(
        string='Name',
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    perol_id = fields.Many2one(
        comodel_name='perol',
        string='Perol',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
    )
    description = fields.Html(
        string='Description',
        translate=True,
    )
    manufacturing_hours = fields.Float(
        string='Time',
    )
    ingredient_ids = fields.Many2many(
        comodel_name='perol.ingredient',
        relation='perol_ingredient_perol_step_rel',
        column1='ingredient_id',
        column2='step_id',
        string='Consume',
    )
    step_type = fields.Selection(
        string='Type',
        selection=[
            ('preparation', 'Preparation'),
            ('elaboration', 'Elaboration'),
        ],
        required=True,
        default='elaboration',
    )
