from odoo import api, fields, models

class materialmap(models.Model):
    _name = 'material.mapping'
    _description = 'Material Mapping'

    name = fields.Char(string='Type of label')
    sizeid = fields.Boolean(string='Size')
    style = fields.Boolean(string="Style")
    color = fields.Boolean(string='Color Code')
    date = fields.Boolean(string="Date Code")
    bgcolor = fields.Boolean(string='BGcolor')
    season = fields.Boolean(string="Season")
    RN = fields.Boolean(string='RN')
    CA = fields.Boolean(string="CA")
    ID = fields.Boolean(string='ID')
    silhouette = fields.Boolean(string="Silhouette")
    carecode = fields.Boolean(string='CareCode')
    composition = fields.Boolean(string="Composition")
    collection = fields.Boolean(string='Collection')
    article = fields.Boolean(string="Article Nu")
    sizes = fields.Boolean(string='Sizes')
    qty = fields.Boolean(string="QTY")
    def getPOdetails(self):
        other_model = self.env['care_instruction_set']
        data = other_model.search([('No', '=', self.test)])
        for record in data:
            po_line_values = {
                'test03': record.No,
                'test04': record.CareInstructionsSetId,
                'test05': record.Description,
            }
            self.get_po_lines = [(0, 0, po_line_values)]
            print("PO IMPORT SUCCESSFULLY!")
    def exportpo(self):
        print("PO IMPORT SUCCESSFULLY!")
    # care_special = fields.Selection([('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F')], string='Care Special')
    # sizeid = fields.Boolean(string='Size ID')
    # style = fields.Boolean(string='Style')
    # checkbox_3 = fields.Boolean(string='Checkbox 3')
    # checkbox_4 = fields.Boolean(string='Checkbox 4')
    # checkbox_5 = fields.Boolean(string='Checkbox 5')
    # checkbox_6 = fields.Boolean(string='Checkbox 6')
    
    # name = field.Char(string="name")