from odoo import models, fields

class referancemaster(models.Model):
    _name = "referance_master"

    No = fields.Char(string='NO')
    name = fields.Char(string='Name', required=True)
    
    