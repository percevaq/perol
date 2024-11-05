###############################################################################
# For copyright and license notices, see __manifest__.py file in root directory
###############################################################################
import base64
import logging
import os
from tempfile import NamedTemporaryFile
from zipfile import ZipFile

from odoo import _, fields, models

_log = logging.getLogger(__name__)


class ImportPerolMedia(models.TransientModel):
    _name = 'import.perol.media'
    _description = 'Import perol media'

    file = fields.Binary(
        string='File zip',
        required=True,
    )
    file_name = fields.Char(
        string='File Name',
    )
    perol_id = fields.Many2one(
        comodel_name='perol',
        string='Perol',
        required=True,
        default=lambda self: self.env.context.get('active_id', None),
    )
    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        required=True,
        copy=False,
        default=lambda self: self.env.company,
    )
    state = fields.Selection(
        string='State',
        selection=[
            ('draft', 'Draft'),
            ('done', 'Done'),
        ],
        required=True,
        default='draft',
    )

    def _reopen(self, res_id=None, model=None):
        return {
            'name': _('Import perol media'),
            'type': 'ir.actions.act_window', 'view_mode': 'form',
            'view_type': 'form', 'res_id': res_id, 'res_model': self._name,
            'target': 'new', 'nodestroy': True,
            'context': {'default_model': model},
        }

    def button_import(self):
        def process_file(local_file=None, media_name=None):
            image_file = base64.b64encode(open(local_file, 'rb').read())
            data = {
                'name': media_name,
                'perol_id': self.perol_id.id,
                'image_1920': image_file,
            }
            self.env['perol.media'].create(data)
            os.remove(local_file)

        import_file = self.env['import.perol.media'].create({
            'file': self.file,
            'file_name': self.file_name,
            'perol_id': self.perol_id.id,
            'company_id': self.company_id.id,
            'state': self.state,
        })
        (__, ftype) = os.path.splitext(import_file.file_name)
        if ftype.lower() == '.zip':
            file_obj = NamedTemporaryFile('wb+', suffix='.zip', delete=False)
            file_obj.write(base64.decodebytes(import_file.file))
            file_import = file_obj.name
            file_path = os.path.dirname(file_import)
            file_obj.close()
            zip_file = ZipFile(file_import, 'r')
            zip_file.extractall(file_path)
            _log.info('Processing ZIP File: %s' % file_import)
            count = 1
            for file in zip_file.filelist:
                (__, zip_ftype) = os.path.splitext(file.filename)
                if not zip_ftype.lower().endswith((
                        '.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    continue
                sequence = str(count).zfill(4)
                name = f'{self.perol_id.name} {sequence}'
                process_file(os.path.join(file_path, file.filename), name)
                count += 1
        import_file.write({'state': 'done'})
        return {'type': 'ir.actions.act_window_close'}
