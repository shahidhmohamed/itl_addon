from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class SizeRange(models.Model):
    _name = "size_map_main"
    _rec_name = 'Size_Range'

    Size_Range = fields.Many2one('size_range_master', string= 'SIZE RANGE')
    Size_Range_uniq = fields.Char(string= 'SIZE RANGE')
    Size_Range_01 = fields.Many2one(string= 'SIZE RANGE', related ='size_lines.Size_Range')
    size_lines = fields.One2many('size_map_lines', 'size_main', string="size range")

    CustomerID = fields.Char(string='CUSTOMER ID', compute = '_compute_c_id', store=True)
    @api.depends('Size_Range')
    def _compute_c_id(self):
        for record in self:
            if record.Size_Range:
                record.Size_Range_uniq = record.Size_Range
            else:
                record.Size_Range_uniq = False 

    _sql_constraints = [
        ('unique_size_in_range', 'UNIQUE(Size_Range_uniq)', 'Size Map for this Size Range already exists.'),
    ]

    @api.constrains('Size_Range_uniq')
    def _check_unique_size_in_range(self):
        for record in self:
            if record.Size_Range_uniq:
                size_map = self.search([
                    ('Size_Range_uniq', '=', record.Size_Range_uniq),
                    ('id', '!=', record.id),  # Exclude the current record from the search
                ])
                if size_map:
                    raise ValidationError(_("Size Map for this Size Range already exists."))
