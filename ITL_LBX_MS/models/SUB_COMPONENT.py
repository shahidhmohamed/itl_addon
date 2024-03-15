from odoo import models, fields, api, _



class SubComponents(models.Model):
    _name = "sub_components"
    _description = "Submaster components details"
    _rec_name = 'ComponentName'

    ComponentName = fields.Char(string='COMPONENT NAME', required=True, index=True)

    _sql_constraints = [
        ('component_name_unique', 'UNIQUE(ComponentName)', 'Component Name must be unique!'),
    ]