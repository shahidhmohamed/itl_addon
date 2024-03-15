from odoo import models, fields, api, _

class getpo(models.Model):
    _name = "getpo"

    MAS = fields.Char(string='MAS GET PO')
    BRANDIX = fields.Char(string='BRANDIX GET PO')

    #po export details
    PurchaseOrderNo = fields.Char(string='PurchaseOrderNo')
    LastRevisionDate = fields.Date(string='LastRevisionDate')
    PurchaseOrderLine = fields.Char(string='PurchaseOrderLine')
    MaterialCode = fields.Char(string='MaterialCode')
    RefMaterial = fields.Char(string='RefMaterial')
    MaterialDescription = fields.Char(string='MaterialDescription')
    Materialid = fields.Char(string='Materialid')
    SalesOrder = fields.Char(string='SalesOrder')
    Cus_order = fields.Char(string='CusOrder')
    Style = fields.Char(string='Style')
    Color_code = fields.Char(string='Color_code')
    Per = fields.Integer(string='Per')
    Reference = fields.Char(string='Reference')
    Size_id = fields.Char(string='SizeID')
    Net_value = fields.Float(string='Net value')
    SOLine = fields.Char(string='SOLine')
    Quantity = fields.Integer(string='Quantity')
    UoM = fields.Char(string='UOM')
    NetPrice = fields.Float(string='Netprice')
    DDate = fields.Date(string='DDate')

    def getPOdetails(self):
        print("PO IMPORT SUCCESSFULLY!")