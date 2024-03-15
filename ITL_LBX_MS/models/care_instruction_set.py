from odoo import models, fields

class CareInstructionSet(models.Model):
    _name = "care_instruction_set"
    _inherit =["mail.thread"]
    No = fields.Char(string='NO', required=True)
    CareInstructionsSetId = fields.Char(string="Care Instruction Set ID")
    Description = fields.Char(string='Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")