from odoo import models, fields, api, _
import xlwt
from io import BytesIO
import base64
from odoo.http import request

class GetpoTest(models.Model):
    _name = "getpo_test"
    test = fields.Char(string='PO NUMBER')
    get_po_lines = fields.One2many('po.lines', 'test01', string="po details")
    test03 = fields.Char(string='Po Number', related="get_po_lines.test03")
    test04 = fields.Char(string='Po ID', related="get_po_lines.test04")
    test05 = fields.Char(string='Po', related="get_po_lines.test05")

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
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('PO Data')

        headers = ['Po Number', 'Po ID', 'Po']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)

        po_lines = self.get_po_lines
        for row, po_line in enumerate(po_lines, start=1):
            worksheet.write(row, 0, po_line.test03)
            worksheet.write(row, 1, po_line.test04)
            worksheet.write(row, 2, po_line.test05)

        excel_buffer = BytesIO()
        workbook.save(excel_buffer)
        excel_buffer.seek(0)

        filename = 'exported_po.xlsx'

        response_headers = [
            ('Content-Type', 'application/vnd.ms-excel'),
            ('Content-Disposition', 'attachment; filename=' + filename),
        ]

        return request.make_response(excel_buffer.read(), headers=response_headers)

class GetPoTree(models.Model):
    _name = "po.lines"
    test01 = fields.Many2one('getpo_test', string="Purchaseorder")
    test03 = fields.Char(string='Po Number 1')
    test04 = fields.Char(string='Po ID')
    test05 = fields.Char(string='Po')
