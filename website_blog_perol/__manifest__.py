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
    'name': 'Website blog Perol',
    'category': 'Perol/Perol',
    'summary': 'Website blog perol',
    'version': '17.0.1.0.0',
    'author': 'GutierrezTI Team (info@gutierrezti.es)',
    'website': 'https://gutierrezti.es',
    'license': 'AGPL-3',
    'depends': [
        'perol',
        'website_blog',
    ],
    'data': [
        'security/ir.model.access.csv',
        'templates/website_blog_perol_templates.xml',
        'templates/website_blog_templates.xml',
        'views/perol_views.xml',
        'wizards/blog_post.xml',
    ],
    'installable': True,
}
