###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class WebsiteBlogPost(models.Model):
    _inherit = 'blog.post'

    perol_id = fields.Many2one(
        comodel_name='perol',
        string='Perol',
    )
