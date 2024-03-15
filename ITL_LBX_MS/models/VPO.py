from odoo import models, fields, api, _


class lbxVpo(models.Model):
    _name = "vpo"


    po = fields.Char(string='PO NUMBER')
    product_ref = fields.Char(string='VPO NO')
    style = fields.Char(string='CUSTOMER STYLE')
    color = fields.Char(string='CUSTOMER COLOR CODE')
    size = fields.Char(string='CUSTOMER SIZE CODE')
    retail1 = fields.Char(string='RETAIL PRICE')
    retail2 = fields.Char(string='RETAIL PRICE')
    retail3 = fields.Char(string='RETAIL PRICE')
    sku = fields.Char(string='sku')
    description = fields.Char(string='description')
    art = fields.Char(string='art')
    qty = fields.Char(string='qty')
