from odoo import models, fields

class ItlComponents(models.Model):
    _name = "itl_components"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    ComponentsId = fields.Char(string="Components Id")
    Description = fields.Char(string='Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")