from odoo import models, fields

class lbxGetChains(models.Model):
    _name = "lbx_getchains"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    Description = fields.Char(string="Description")
    GC_ID = fields.Char(string='GC_ID')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")