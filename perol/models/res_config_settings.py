###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_website_blog_perol = fields.Boolean(
        string='Website blog perol: publish your recipes on the blog',
    )
