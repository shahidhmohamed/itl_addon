from odoo import models, fields

class lbxProducts(models.Model):
    _name = "lbx_products"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    Description = fields.Char(string="Description")
    Product_ref = fields.Char(string="Product_ref")
    Classification = fields.Char(string="Classification")
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")