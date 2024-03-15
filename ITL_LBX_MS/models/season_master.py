from odoo import models, fields

class seasonMaster(models.Model):
    _name = "lbx_seson_master"
    _rec_name = "season"

    season = fields.Char(string='SEASON')
    season_name = fields.Char(string='SEASON NAME')