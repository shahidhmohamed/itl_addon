from odoo import models, fields, api, _



class SubCareInstructionSet(models.Model):
    _name = "care_instruction_set_code"
    _description = "Submaster Care Instruction Set"
    _rec_name = 'CareInstructionSetCode'

    CareInstructionSetCode = fields.Char(string='CARE INSTRUCTION SET CODE')