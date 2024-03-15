from odoo import models, fields

class AdditionalIns(models.Model):
    _name = "lbx_additional_instruction_master"
    _rec_name = 'additional_ins'

    additional_ins = fields.Char(string='ADDITIONAL INSTRUCTION')
    additional_ins_name = fields.Char(string='ADDITIONAL INSTRUCTION NAME')