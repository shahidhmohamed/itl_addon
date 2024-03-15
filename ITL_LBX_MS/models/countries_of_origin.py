from odoo import models, fields

class CountriesOfOrigin(models.Model):
    _name = "countries.of.origin"
    _inherit =["mail.thread"]
    No = fields.Char(string='NO', required=True)
    CountriesOfOriginId = fields.Char(string="Coo ID")
    Description = fields.Char(string='Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")