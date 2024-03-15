from odoo import models, fields, api, _


class LbxMiCoomaster(models.Model):
    _name = "lbx_coo_master"
    _description = "LBX COO MASTER"
    _rec_name = 'Coo_1'


    Coo_1 = fields.Char (string = 'COO')
    coo_name = fields.Char (string = 'COO NAME')