from odoo import api, models, fields, _

class Transaction(models.Model):
    _name = "transaction"
    _inherit =["mail.thread",'mail.activity.mixin']
    name = fields.Char(string='Name', required=True)
    Po_No = fields.Char(string="Po_No",required=True, copy=False, readonly=True, default=lambda self: _('New'))
    Confirmationdate = fields.Date(string='Confirmation Date')
    Vandor = fields.Many2one('product.product',string=' Vandor')
    Company = fields.Many2one('res.partner',string='Company')
    Buyer = fields.Many2one('res.users',string='Buyer')
    Activities = fields.Char(string='Activities')
    SourceDocument = fields.Char(string='Source Document')
    # Total = fields.Integer(string='Total')
    BillingStatus = fields.Char(string='BillingStatus')
    ExpectedArrival = fields.Char(string='Expected Arrival')
    PurchaseOrderNo = fields.Char(string='PurchaseOrderNo', related="purchaseorder_lines.PurchaseOrderNo")
    LastRevisionDate = fields.Date(string='LastRevisionDate', related="purchaseorder_lines.LastRevisionDate")
    PurchaseOrderLine = fields.Char(string='PurchaseOrderLine', related="purchaseorder_lines.PurchaseOrderLine")
    MaterialCode = fields.Char(string='MaterialCode', related="purchaseorder_lines.MaterialCode")
    Materialid = fields.Char(string='Materialid', related="purchaseorder_lines.Materialid")
    RefMaterial = fields.Char(string='MaterialRef', related="purchaseorder_lines.RefMaterial")
    MaterialDescription = fields.Char(string='MaterialCode')
    SalesOrder = fields.Char(string='SalesOrder', related="purchaseorder_lines.SalesOrder")
    SOLine = fields.Char(string='SOLine', related="purchaseorder_lines.SOLine")
    Quantity = fields.Integer(string='Quantity', related="purchaseorder_lines.Quantity")
    UoM = fields.Char(string='UOM', related="purchaseorder_lines.UoM")
    NetPrice = fields.Float(string='NetPrice', related="purchaseorder_lines.NetPrice")

    
    purchaseorder_lines = fields.One2many('purchase.order.lines','purchaseorder_id',string='Purchaseorder Lines')
    Material_lines =  fields.One2many('material.mapping.lines','Material',string='Material lines')
    Material_All_lines =  fields.One2many('all.lines','MaterialCode',string='Material All lines')
    Total =  fields.One2many('purchase.order.lines','total',string='Total')
    NetPrice_test = fields.Float(string='Netprice', related="purchaseorder_lines.NetPrice")
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    Test = fields.Monetary(string='Total' , compute='_compute_Test', related="purchaseorder_lines.Test")
    currency_test = fields.Many2one('res.currency',string='Currency')
    Cus_order = fields.Char(string='Cus_order', related="purchaseorder_lines.Cus_order")
    Style = fields.Char(string='Style', related="purchaseorder_lines.Style")
    Color_code = fields.Char(string='Color_code', related="purchaseorder_lines.Color_code")
    Per = fields.Integer(string='per', related="purchaseorder_lines.Per")
    Net_value = fields.Float(string='Net value',related="purchaseorder_lines.Net_value")
    Reference = fields.Char(string='Reference',related="purchaseorder_lines.Reference")
    DDate = fields.Date(string='DDate',related="purchaseorder_lines.DDate")
    Size_id = fields.Char(string='SizeID',related="purchaseorder_lines.Size_id")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
        ],string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)

    @api.model
    def create(self, vals):
        print("Create Purchase Order",vals)
        vals['Po_No'] = self.env['ir.sequence'].next_by_code('purchase.order.new')
        return super(Transaction, self).create(vals)
    
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")


class ItlPurchaseorderLines(models.Model):
    _name = "purchase.order.lines"
    product_id = fields.Many2one('product.product', string="Purchaseorder")
    price_unit = fields.Integer(string="Price")
    product_qty = fields.Integer(string='Quantity')
    purchaseorder_id = fields.Many2one('transaction',string='Quantity')
    PurchaseOrderNo = fields.Char(string='PurchaseOrderNo')
    LastRevisionDate = fields.Date(string='LastRevisionDate')
    PurchaseOrderLine = fields.Char(string='PurchaseOrderLine')
    MaterialCode = fields.Char(string='MaterialCode')
    RefMaterial = fields.Char(string='RefMaterial')
    MaterialDescription = fields.Char(string='MaterialCode')
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
    total = fields.Integer(string='Total')
    currency_id = fields.Many2one('res.currency', related='purchaseorder_id.currency_id')
    price_subtotal = fields.Monetary (string='Subtotal')
    Test = fields.Monetary(string='Total' , compute='_compute_Test')

    @api.depends('price_unit','Quantity')
    def _compute_Test(self):
        for rec in self:
            rec.Test = rec.price_unit * rec.Quantity
    

class ItlMaterialMapping(models.Model):
    _name = "material.mapping.lines"
    Material = fields.Many2one('transaction',string='Material')
    DateCode = fields.Date(string='Date')
    Silhouette = fields.Char(string='Silhouette')
    CareCode = fields.Char(string='CareCode')
    composition = fields.Char(string='composition')
    Collection = fields.Char(string='Collection')
    

class ItlMaterialAll(models.Model):
    _name = "all.lines"
    MaterialCode = fields.Many2one('transaction',string='Material Code')
    MaterialDescription  = fields.Char(string='Material Description')
    Reference = fields.Char(string='Reference')
    SizeID = fields.Char(string='Size ID')
    Style = fields.Char(string='Style')
    Colour_code = fields.Char(string='Colour_code')
    DateCode = fields.Date(string='DateCode')
    BGcolour = fields.Char(string='BGcolour')
    Season = fields.Char(string='Season')
    RN = fields.Char(string='RN')
    CA = fields.Char(string='CA')

    
