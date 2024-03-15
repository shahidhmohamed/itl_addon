from odoo import models, fields

class Brands(models.Model):
    _name = "brands"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    BrandId = fields.Char(string="Brand ID")
    ChainID = fields.Char(string='Chain ID')
    Branddescription = fields.Char(string='Brands Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")