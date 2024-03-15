from odoo import models, fields

class SizeLines(models.Model):
    _name = "lbx_size_master"

    size_id = fields.Char(string='SIZE ID')
    size = fields.Char(string='SIZE')