###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, fields, models


class Perol(models.Model):
    _inherit = 'perol'

    blog_post_id = fields.Many2one(
        comodel_name='blog.post',
        string='Post',
        required=False,
    )

    def action_blog_post(self):
        self.ensure_one()
        view_form_id = self.env.ref(
            'website_blog_perol.perol_blog_post_view_form').id
        action = {
            'type': 'ir.actions.act_window',
            'name': _('Blog post'),
            'view_mode': 'form',
            'res_model': 'blog.post',
            'target': 'new',
            'views': [[view_form_id, 'form']],
            'context': {'default_perol_id': self, 'default_name': self.name},
        }
        return action
