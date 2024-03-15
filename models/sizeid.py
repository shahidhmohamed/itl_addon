from odoo import models, fields

class sizeid(models.Model):
    _name = "size_id"

    No = fields.Char(string='NO')
    name = fields.Char(string='Name', required=True)
    