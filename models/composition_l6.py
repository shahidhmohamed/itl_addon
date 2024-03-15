from odoo import models, fields, api, _


class ClinesTab(models.Model):
    _name = "composition_lines_tab_06"
    _description = "composition lines"
    _rec_name = 'discription'

    connect06 = fields.Many2one('set_fiber', string="connect")
    Component = fields.Many2one('sub_components', string='COMPONENT')
    
    

    Fiber1 = fields.Many2one('sub_fiber', string='SELECT FIBER 1')
    Fiber1_Percentage = fields.Char(string='Fiber 1 Percentage')

    Fiber2 = fields.Many2one('sub_fiber', string='SELECT FIBER 2')
    Fiber2_Percentage = fields.Char(string='Fiber 2 Percentage')

    # Fiber3 = fields.Many2one('sub_fiber', string='SELECT FIBER 3')
    # Fiber3_Percentage = fields.Char(string='Fiber 3 Percentage')

    # Fiber4 = fields.Many2one('sub_fiber', string='SELECT FIBER 4')
    # Fiber4_Percentage = fields.Char(string='Fiber 4 Percentage')

    discription = fields.Char(string='Composition' , compute = '_compute_so_ref_lv')

    @api.depends('Component', 'Fiber1','Fiber1_Percentage','Fiber2','Fiber2_Percentage')
    def _compute_so_ref_lv(self):
        for record in self:
            # Check if both SoNumber and SoOrderItem have values
            if record.Component and record.Fiber1 and record.Fiber1_Percentage and record.Fiber2 and record.Fiber2_Percentage:
                record.discription = f"{record.Component.ComponentName}: {record.Fiber1_Percentage}% {record.Fiber1.fibername}, {record.Fiber2_Percentage}% {record.Fiber2.fibername}"
            else:
                record.discription = False
