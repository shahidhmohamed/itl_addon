from odoo import models, fields, api

class PurchaseOrderLine(models.Model):
    _name = 'lbx_mi_gpo_i001.line'
    _description = 'Purchase Order Lines'

    order_id = fields.Many2one('lbx_mi_gpo_i001', string='Purchase Order')
    order_number  = fields.Char(string='order_number')
    PurchaseOrderItem = fields.Char(string='Purchase Order Item')
    material_code = fields.Char(string='Material Code')