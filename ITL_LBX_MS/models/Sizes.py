from odoo import models, fields

class lbxSizes(models.Model):
    _name = "lbx_sizes"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    size_range_name = fields.Char(string='size_range_name')
    No = fields.Char(string='NO', required=True)
    size = fields.Char(string="size")
    Description = fields.Char(string='Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")