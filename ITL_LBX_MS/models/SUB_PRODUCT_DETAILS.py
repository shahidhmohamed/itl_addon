from odoo import models, fields, api, _



class SubProduct(models.Model):
    _name = "sub_product_details"
    _description = "Submaster Product Details"
    _rec_name = 'ProductDescription'

    ProductRef = fields.Char(string='PRODUCT REF')
    ProductDescription = fields.Char(string='PRODUCT DESCRIPTION')
    Classification = fields.Char(string='CLASSIFICSTION')