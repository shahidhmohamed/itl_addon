from odoo import models, fields, api, _



class SubFiber(models.Model):
    _name = "sub_fiber"
    _description = "Submaster fiber details"
    _rec_name = "fibername"

    fibername = fields.Char(string='FIBER NAME')
    id = fields.Integer(string='ID')