from odoo import models, fields

class CareInstruction(models.Model):
    _name = "care_instruction"
    _inherit =['mail.thread','mail.activity.mixin']
    _rec_name = 'Description'


    No = fields.Char(string='NO', required=True)
    CareInstructionsId = fields.Char(string="Care Instruction ID")
    Description = fields.Char(string='Description')
    image = fields.Image(string = "Image")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")