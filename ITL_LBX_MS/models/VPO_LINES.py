from odoo import models, fields, api, _


class LbxMivpoLines(models.Model):
    _name = "lbx_mi_vpo_lines_d001"
    _description = "LBX MI vPO Lines"
    _rec_name = 'PoNumber'

    vpo_line_c = fields.Many2one('lbx_mi_vpo_d001', string="vpo_line_c")
    vpo_line_g = fields.Many2one('lbx_mi_gpo_d001', string="vpo_line_c")
    PoNumber = fields.Char(string='PO NUMBER')
    VPONo = fields.Char(string='VPO NO')
    CustomerStyle = fields.Char(string='CUSTOMER STYLE')
    CustomerColorCode = fields.Char(string='CUSTOMER COLOR CODE')
    CustomerSizeCode = fields.Char(string='CUSTOMER SIZE CODE')
    RetailPrice1 = fields.Float(string='RETAIL PRICE')
    Usd = fields.Char(string='USD')
    RetailPrice2 = fields.Float(string='RETAIL PRICE')
    Cad = fields.Char(string='CAD')
    RetailPrice3 = fields.Float(string='RETAIL PRICE')
    Gbp = fields.Char(string='GBP')
    OrderQuantity = fields.Char(string='ORDER QUANTITY')
    VarientNo = fields.Char(string='VARIENT NO')
    CustomerArticle = fields.Char(string='CUSTOMER ARTICLE')
    Upc = fields.Char(string='UPC')
    composition = fields.Char(string='COMPOSITION')
    Date_code = fields.Char(string='DATE CODE')
    ID = fields.Char(string='ID')
    Silhouette = fields.Char(string='SILHOUETTE')
    CareCode = fields.Char(string='CARE CODE')
    Collection = fields.Char(string='COLLECTION')

    uniq = fields.Char(string='uniq')

    # 2023-12-18
    Desc = fields.Many2one('care_instruction',string='Desc')
    composition_Desc = fields.Many2one('set_fiber', string='COMPOSITION FINAL', store = True)

    c_id = fields.Integer(string ='COMPOSITION ID', compute = '_compute_c_id')
    @api.depends('c_id')
    def _compute_c_id(self):
        for record in self:
            if record.composition_Desc:
                record.c_id = record.composition_Desc.id
            else:
                record.c_id = False


    Style = fields.Char(string='STYLE')
    CC = fields.Char(string='CC')
    Size = fields.Char(string='SIZE')
    Sku = fields.Char(string='SKU')
    Desc1 = fields.Char(string='DESC')
    Article = fields.Char(string='ARTICLE')
    ProductReference = fields.Char(string='PRODUCT REFERENCE')

    newsize = fields.Char(string = 'NEW SIZE')

    