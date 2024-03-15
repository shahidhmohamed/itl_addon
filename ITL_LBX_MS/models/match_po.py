from odoo import models, fields, api, _


class LbxMiMpoD001(models.Model):
    _name = "lbx_mi_mpo_d001"

    PurchaseorderNum02 = fields.Many2one('lbx_mi_gpo_h001', string="PURCHASE ORDER NUMBER")
    
    PoNumber = fields.Char(string='PO NUMBER')
    PurchaseOrderVersion = fields.Char(string='PurchaseOrderVersion')
    ProductRef = fields.Char(string='PRODUCT REF')
    VsPoNumber = fields.Char(string='VS PO NUMBER')
    PoDate = fields.Datetime(string='PO DATE')
    lineItem = fields.Char(string='LINE ITEM')
    FactoryId = fields.Char(string='FACTORY ID')
    Silhouette = fields.Char(string='SILHOUETTE')
    Collection = fields.Char(string='COLLECTION')
    RnNumber = fields.Char(string='RN NUMBER')
    CaNumber = fields.Char(string='CA NUMBER')
    Coo = fields.Char(string='COO')
    OrderQuantity = fields.Char(string='ORDER QUANTITY')
    SizeId = fields.Char(string='SIZE ID')
    Size = fields.Char(string='SIZE')
    Style = fields.Char(string='STYLE')
    DeliveryDate = fields.Datetime(default=fields.Datetime.now)
    SoNumber = fields.Char(string='SO NUMBER')
    SoOrderItem = fields.Char(string='SO ORDER ITEM')
    SoRefLv = fields.Char(string='SO REF LV')
    ColorCode = fields.Char(string='COLOR CODE')
    Sku = fields.Char(string='SKU')
    ArticalNumber = fields.Char(string='ARTICLE NUMBER')
    RetailPrice = fields.Float(string='RETAIL PRICE')
    RetailPrice2 = fields.Float(string='RETAIL PRICE 2')
    RetailPrice3 = fields.Float(string='RETAIL PRICE 3')
    SizeQuantity = fields.Char(string='SIZE Quantity')
    CareInstructionSet = fields.Char(string='CARE INSTRUCTION SET')
    ComponentName = fields.Char(string='COMPONENT NAME')
    FiberName = fields.Char(string='FIBER NAME')
    FiberPercentage = fields.Char(string='FIBER PERCENTAGE')
    AdditionalCareInstruction = fields.Char(string='ADDITIONAL CARE INSTRUCTION')
    Vendor_Material = fields.Char(string='Vendor Material')

    @api.onchange('PurchaseorderNum02')
    def onchange_purchase_order_num(self):
        if self.PurchaseorderNum02:
            purchase_order = self.PurchaseorderNum02

            # Update fields in lbx_mi_mpo_d001 with values from lbx_mi_gpo_d001
            self.PoNumber = purchase_order.PoNumber
            self.PurchaseOrderVersion = purchase_order.PurchaseOrderVersion
            self.ProductRef = purchase_order.ProductRef
            self.VsPoNumber = purchase_order.ProductRef
            self.PoDate = purchase_order.PoDate

            self.lineItem = purchase_order.lineItem
            self.FactoryId = purchase_order.FactoryId
            self.Silhouette = purchase_order.Silhouette
            self.Collection = purchase_order.Collection
            self.RnNumber = purchase_order.RnNumber
            self.CaNumber = purchase_order.CaNumber
            self.Coo = purchase_order.Coo
            self.OrderQuantity = purchase_order.OrderQuantity
            self.SizeId = purchase_order.SizeId
            self.Size = purchase_order.Size
            self.Style = purchase_order.Style
            self.DeliveryDate = purchase_order.DeliveryDate
            self.SoNumber = purchase_order.SoNumber
            self.SoOrderItem = purchase_order.ProductRef
            self.SoRefLv = purchase_order.SoRefLv
            self.ColorCode = purchase_order.ColorCode
            self.RetailPrice = purchase_order.RetailPrice
            self.RetailPrice2 = purchase_order.RetailPrice2
            self.RetailPrice3 = purchase_order.RetailPrice3
            self.SizeQuantity = purchase_order.SizeQuantity
            self.CareInstructionSet = purchase_order.CareInstructionSet
            self.ComponentName = purchase_order.ComponentName
            self.FiberName = purchase_order.FiberName
            self.FiberPercentage = purchase_order.FiberPercentage
            self.AdditionalCareInstruction = purchase_order.AdditionalCareInstruction
            self.Vendor_Material = purchase_order.Vendor_Material