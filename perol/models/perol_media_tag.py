###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from random import randint

from odoo import fields, models


class PerolMediaTag(models.Model):
    _name = 'perol.media.tag'
    _description = 'Perol media tag'
    _order = 'category_id, sequence, name'

    @staticmethod
    def _default_color():
        return randint(1, 11)

    name = fields.Char(
        string='Tag Name',
        required=True,
        translate=True,
    )
    media_ids = fields.Many2many(
        comodel_name='perol.media',
        string='Media',
    )
    color = fields.Integer(
        string='Color Index',
        default=lambda self: self._default_color(),
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    category_id = fields.Many2one(
        comodel_name='perol.media.tag.category',
        string='Category',
        ondelete='set null',
    )
    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Tag name already exists !'),
    ]
