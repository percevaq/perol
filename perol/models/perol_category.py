###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PerolCategory(models.Model):
    _name = 'perol.category'
    _description = 'Perol category'
    _parent_name = 'parent_id'
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(
        string='Name',
        index='trigram',
        required=True,
    )
    complete_name = fields.Char(
        string='Complete name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
    )
    parent_id = fields.Many2one(
        comodel_name='product.category',
        string='Parent category',
        index=True,
        ondelete='cascade',
    )
    parent_path = fields.Char(
        string='Parent path',
        index=True,
        unaccent=False,
    )
    child_id = fields.One2many(
        comodel_name='perol.category',
        inverse_name='parent_id',
        string='Child categories',
    )
    perol_count = fields.Integer(
        string='# Perol',
        compute='_compute_perol_count',
    )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_perol_count(self):
        read_group_res = self.env['trees'].read_group(
            [('category_id', 'child_of', self.ids)],
            ['category_id'],
            ['category_id'],
        )
        group_data = dict((data['category_id'][0], data['category_id_count'])
                          for data in read_group_res)
        for category in self:
            perol_count = 0
            for sub_category_id in category.search(
                    [('id', 'child_of', category.ids)]).ids:
                perol_count += group_data.get(sub_category_id, 0)
            category.perol_count = perol_count

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))

    @api.model
    def name_create(self, name):
        category = self.create({'name': name})
        return category.id, category.display_name

    @api.depends_context('hierarchical_naming')
    def _compute_display_name(self):
        if self.env.context.get('hierarchical_naming', True):
            return super()._compute_display_name()
        for record in self:
            record.display_name = record.name
