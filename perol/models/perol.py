###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import api, fields, models


class Perol(models.Model):
    _name = 'perol'
    _description = 'Perol'
    _inherit = ['mail.thread', 'portal.mixin', 'image.mixin',
                'mail.activity.mixin']
    _order = 'sequence,id'
    _check_company_auto = True

    name = fields.Char(
        string='Name',
        required=True,
        translate=True,
    )
    sequence = fields.Integer(
        string='Sequence',
        default=10,
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        required=True,
        index=True,
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(
        string='Active',
        default=True,
        help='If unchecked, it will allow you to hide the perol without '
             'removing it.',
    )
    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'Draft'),
            ('enabled', 'Enabled'),
            ('canceled', 'Canceled'),
        ],
        required=True,
        copy=False,
        index=True,
        tracking=3,
        default='draft',
    )
    priority = fields.Selection(
        string='Favorite',
        selection=[
            ('0', 'Normal'),
            ('1', 'Favorite')
        ],
        default='0',
    )
    ingredient = fields.One2many(
        comodel_name='perol.ingredient',
        inverse_name='perol_id',
        string='Ingredients',
        copy=True,
        auto_join=True,
    )
    step = fields.One2many(
        comodel_name='perol.step',
        inverse_name='perol_id',
        string='Steps',
        copy=True,
        auto_join=True,
    )
    category_ids = fields.Many2one(
        comodel_name='perol.category',
        string='Category',
        required=True,
    )
    tag_ids = fields.Many2many(
        comodel_name='perol.tag',
        relation='perol_tag_perol_relation',
        column1='tag_id',
        column2='perol_id',
        string='Tags',
    )
    media_ids = fields.One2many(
        comodel_name='perol.media',
        inverse_name='perol_id',
        string='Media',
        copy=True,
        auto_join=True,
    )
    media_count = fields.Integer(
        string='Media count',
        compute='_compute_media_count',
    )
    food_allergen_ids = fields.Many2many(
        comodel_name='product.template.allergen',
        relation='product_template_allergen_perol_relation',
        column1='template_id',
        column2='perol_id',
        string='Allergens',
    )
    barcode = fields.Char(
        string='Barcode',
        copy=False,
    )
    default_code = fields.Char(
        string='Reference',
        copy=False,
    )
    preparation_hours = fields.Float(
        string='Preparation',
        required=True,
    )
    manufacturing_hours = fields.Float(
        string='Manufacturing',
        required=True,
    )
    amount_hours = fields.Float(
        string='Total time',
        compute='compute_amount_time',
        store=True,
    )
    portion_number = fields.Integer(
        string='Portions',
        required=True,
    )
    internal_note = fields.Html(
        string='Internal note',
        translate=True,
    )
    introduction = fields.Text(
        string='Introduction',
        translate=True,
    )
    description = fields.Text(
        string='Description',
        translate=True,
    )
    history = fields.Text(
        string='History',
        translate=True,
    )
    tricks = fields.Html(
        string='Tricks',
        translate=True,
    )

    difficulty = fields.Selection(
        string='Difficulty',
        selection=[
            ('10', 'Low'),
            ('30', 'Medium'),
            ('60', 'High'),
            ('90', 'Very high'),
        ],
        required=True,
        default='10'
    )
    difficulty_gauge = fields.Integer(
        string='% difficulty',
        compute='_compute_difficulty_gauge',
    )

    @api.model
    def default_get(self, default_fields):
        res = super().default_get(default_fields)
        default_code = self.env['ir.sequence'].next_by_code('perol') or 'P/'
        res.update({'default_code': default_code})
        return res

    @api.depends('difficulty')
    def _compute_difficulty_gauge(self):
        for perol in self:
            if perol.difficulty == '10':
                progress = 10
            elif perol.difficulty == '30':
                progress = 30
            elif perol.difficulty == '60':
                progress = 60
            else:
                progress = 90
            perol.difficulty_gauge = progress

    def _compute_media_count(self):
        for perol in self:
            perol.media_count = self.env['perol.media'].search_count([
                ('perol_id', '=', perol.id)])

    @api.depends('preparation_hours', 'manufacturing_hours')
    def compute_amount_time(self):
        for perol in self:
            perol.amount_hours = (perol.preparation_hours
                                  + perol.manufacturing_hours)

    @api.depends('ingredient_allergen')
    def compute_ingredient_allergen(self):
        for perol in self:
            perol_allergen = perol.mapped('food_allergen_ids')
            ingredient_allergen = perol.ingredient.mapped(
                'product_id').mapped('food_allergen_ids')
            differences = perol_allergen - ingredient_allergen
            if len(differences) == 0:
                continue
            for difference in differences:
                perol.food_allergen_ids = [(4, difference.id)]
