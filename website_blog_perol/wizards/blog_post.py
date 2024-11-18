###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import fields, models


class PerolBlogPost(models.TransientModel):
    _name = 'perol.blog.post'
    _description = 'Perol blog post'
    _rec_name = 'perol_id'

    blog_id = fields.Many2one(
        comodel_name='blog.blog',
        string='Blog',
    )
    perol_id = fields.Many2one(
        comodel_name='perol',
        string='Perol',
    )

    def button_create(self):
        for post in self:
            post_id = self.env['blog.post'].create({
                'blog_id': self.blog_id.id,
                'perol_id': self.perol_id.id,
                'name': self.perol_id.name,
                'subtitle': self.perol_id.introduction or None,
            })
            post.perol_id.blog_post_id = post_id
