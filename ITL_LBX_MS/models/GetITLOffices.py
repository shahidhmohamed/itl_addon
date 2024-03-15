from odoo import models, fields

class lbxGetITLOffices(models.Model):
    _name = "lbx_getitloffices"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    Description = fields.Char(string="Description")
    SEASON_ID = fields.Char(string='SEASON_ID')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")