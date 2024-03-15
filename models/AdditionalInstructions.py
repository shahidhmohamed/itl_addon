from odoo import models, fields

class lbxAdditionalInstructions(models.Model):
    _name = "lbx_additionalinstructions"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    description = fields.Char(string="Description")
    AIID = fields.Char(string='AI ID')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")