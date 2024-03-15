from odoo import models, fields, api, _



class SubChain(models.Model):
    _name = "sub_chain"
    _description = "Submaster Chain Details"
    _rec_name = 'ChainName'

    ChainId = fields.Char(string='CHAIN ID')
    ChainName = fields.Char(string='CHAIN NAME')