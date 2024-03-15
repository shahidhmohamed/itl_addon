from odoo import models, fields, api, _


class ComLines(models.Model):
    _name = "composition_lines_01"
    _description = "Composition Details"
    # _rec_name = 'PoNumber'

    composition_connect = fields.Many2one('lbx_mi_gpo_h001', string="vpo_line_c")
    Composition = fields.Many2one('set_fiber', string='SELECT COMPOSITION', store=True)