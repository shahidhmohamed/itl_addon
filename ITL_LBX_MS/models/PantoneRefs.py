from odoo import models, fields

class lbxPantoneRefs(models.Model):
    _name = "lbx_pantonerefs"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    Description = fields.Char(string="Description")
    PR_ID = fields.Char(string='PR_ID')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")