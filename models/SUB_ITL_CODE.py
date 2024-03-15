from odoo import models, fields, api, _



class SubChain(models.Model):
    _name = "sub_itl_code"
    _description = "Submaster Itl Code Details"
    _rec_name = 'ItlCode'

    ItlCode = fields.Char(string='ITL CODE')