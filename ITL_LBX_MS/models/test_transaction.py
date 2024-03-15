from odoo import api, models, fields, _

class TestTransaction(models.Model):
    _name = "test_transaction"
    _inherit =["mail.thread",'mail.activity.mixin']
    name = fields.Char(string='Name', required=True)
    PO_NO = fields.Char(string="Po_No",required=True, copy=False, readonly=True, default=lambda self: _('New'))
    Confirmationdate = fields.Date(string='Confirmation Date')
    Vandor = fields.Many2one('product.product',string=' Vandor')
    Company = fields.Many2one('res.partner',string='Company')
    Buyer = fields.Many2one('res.users',string='Buyer')
    Activities = fields.Char(string='Activities')
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    # Feeld that on po order
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
    Total = fields.Monetary(string='Total' , compute='_compute_Test')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")

    @api.model
    def create(self, vals):
        print("Create Purchase Order",vals)
        vals['PO_NO'] = self.env['ir.sequence'].next_by_code('purchase.order.new')
        return super(TestTransaction, self).create(vals)

    @api.depends('Quantity','NetPrice')
    def _compute_Test(self):
        for rec in self:
            rec.Total = rec.Quantity * rec.NetPrice



