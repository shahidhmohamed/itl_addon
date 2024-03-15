from odoo import models, fields

class lbxProductBenifits(models.Model):
    _name = "lbx_productbenifits"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    Description = fields.Char(string="Description")
    PB_ID = fields.Char(string='PB_ID')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")