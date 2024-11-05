###############################################################################
#    GutierrezTI Team
#    Copyright (C) 2024-Today Joaquin Gutierrez Pedrosa <www.gutierrezti.es>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
{
    'name': 'Perol',
    'category': 'Perol/Perol',
    'summary': 'Perol management system',
    'version': '17.0.1.0.0',
    'author': 'GutierrezTI Team (info@gutierrezti.es)',
    'website': 'https://gutierrezti.es',
    'license': 'AGPL-3',
    'depends': [
        'product',
        'portal',
        'sale',
        'web',
    ],
    'data': [
        'data/uom_data.xml',
        'data/perol_data.xml',
        'data/product_template_allergen_data.xml',
        'security/perol_security.xml',
        'security/ir.model.access.csv',
        'views/perol_menu_views.xml',
        'views/perol_category_views.xml',
        'views/perol_media_tag_category_views.xml',
        'views/perol_media_tag_views.xml',
        'views/perol_media_views.xml',
        'views/perol_tag_category_views.xml',
        'views/perol_tag_views.xml',
        'views/perol_views.xml',
        'views/perol_ingredient_views.xml',
        'views/perol_step_views.xml',
        'views/product_template_allergen_views.xml',
        'views/product_template_views.xml',
        'views/res_config_settings_views.xml',
        'wizards/wizard_import_perol_media.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'perol/static/src/scss/perol.scss',
        ],
    },
    'installable': True,
    'application': True,
}
