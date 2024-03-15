from odoo import models, fields

class WashSymbols(models.Model):
    _name = "wash.symbols"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    WashSymbolsId = fields.Char(string="Ws ID")
    Description = fields.Char(string='Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")

