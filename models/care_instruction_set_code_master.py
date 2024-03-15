from odoo import models, fields

class CareInstructionSetCode(models.Model):
    _name = "lbx_care_instruction_set_code"
    _rec_name = "care_instruction_set_code"

    care_instruction_set_code = fields.Char(string='CARE INSTRUCTION SET CODE')
    care_instruction_set_code_2 = fields.Char(string='CARE INSTRUCTION SET CODE')