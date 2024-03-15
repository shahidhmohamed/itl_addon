from odoo import models, fields

class getVSStoresOptions(models.Model):
    _name = "get.vs.stores.options"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    StoresId = fields.Char(string="Stores ID")
    Storesdescription = fields.Char(string='Stores Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")