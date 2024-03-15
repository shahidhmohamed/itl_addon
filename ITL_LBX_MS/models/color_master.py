from odoo import models, fields, api, _

class SizeRangeMaster(models.Model):
    _name = "color_code_master"

    color_po = fields.Char(string= 'COLOR')
    color_vpo = fields.Char(string= 'COLOR VPO')