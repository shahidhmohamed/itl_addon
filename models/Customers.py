from odoo import models, fields

class Customers(models.Model):
    _name = "lbx_customers"
    _inherit =["mail.thread",'mail.activity.mixin']
    No = fields.Char(string='NO', required=True)
    ocscustno = fields.Char(string="ocscustno")
    name = fields.Char(string="name")
    delivery_name = fields.Char(string="delivery_name")
    address1 = fields.Char(string="address1")
    address2 = fields.Char(string="address2")
    address3 = fields.Char(string="address3")
    Country = fields.Char(string="Country")
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")