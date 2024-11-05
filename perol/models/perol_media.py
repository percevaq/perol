###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
import base64

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

from odoo.addons.web_editor.tools import get_video_embed_code, get_video_thumbnail


class PerolMedia(models.Model):
    _name = 'perol.media'
    _description = 'Perol media'
    _inherit = ['image.mixin']
    _order = 'sequence,id'

    name = fields.Char(
        string='Name',
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        string='sequence',
        default=10,
    )
    perol_id = fields.Many2one(
        comodel_name='perol',
        string='Perol',
        required=True,
        index=True,
        ondelete='cascade',
    )
    video_url = fields.Char(
        string='Video url',
        help='URL of a video for showcasing your trees.',
    )
    embed_code = fields.Html(
        compute='_compute_embed_code',
        sanitize=False,
    )

    @api.onchange('video_url')
    def _onchange_video_url(self):
        if not self.image_1920:
            preview = get_video_thumbnail(self.video_url)
            self.image_1920 = preview and base64.b64encode(preview) or False

    @api.depends('video_url')
    def _compute_embed_code(self):
        for image in self:
            image.embed_code = get_video_embed_code(image.video_url) or False

    @api.constrains('video_url')
    def _check_valid_video_url(self):
        for image in self:
            if not image.video_url:
                continue
            if image.video_url and image.embed_code:
                continue
            raise ValidationError(_(
                'Provided video URL for %s is not valid. Please enter a '
                'valid video URL.', image.name))
