from odoo import models, fields

class lbxProductDescriptions(models.Model):
    _name = "lbx_productdescriptions"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    Description = fields.Char(string="Description")
    PD_ID = fields.Char(string='PD_ID')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")