from odoo import models, fields

class MultiPartSets(models.Model):
    _name = "multi_part_sets"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    UoMID = fields.Char(string="UoM ID")
    UomDdescription = fields.Char(string='UoM Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")