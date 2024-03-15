from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SizeRangeMaster(models.Model):
    _name = "size_range_master"
    _rec_name = 'Size_Range'

    Size_Range = fields.Char(string= 'SIZE RANGE')
    Size_Range_name = fields.Char(string= 'SIZE RANGE LV')
    Size_Range_DESC = fields.Char(string= 'SIZE RANGE DESC')

    @api.constrains('Size_Range')
    def _check_unique_size_range(self):
        for record in self:
            duplicate_records = self.env['size_range_master'].search([
                ('Size_Range', '=', record.Size_Range),
                ('id', '!=', record.id),
            ])
            if duplicate_records:
                raise ValidationError(_('Size Range must be unique!'))
