from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError


class LbxbiGpod001(models.Model):
    _name = "lbx_bi_gpo_d001"
    
    PurchaseorderNum = fields.Many2one('lbx_bi_gpo_h001', string="PURCHASE ORDER NUMBER")
    # PurchaseorderNum01 = fields.Many2one('lbx_mi_vpo_lines_d001', string="PURCHASE ORDER NUMBER 02")

    # lvp_lpo = fields.Many2one('lbx_mi_vpo_d001', string="lvp_lpo")

    # Add the new field
    line_number = fields.Char(string='NO', default=1, store=True)

    @api.model
    def create(self, values):
        # Override create method to set the line_number when creating a new record
        lines = self.search([('PurchaseorderNum', '=', values.get('PurchaseorderNum'))])  # Assuming PurchaseorderNum is a reference field to link lines of the same set
        values['line_number'] = len(lines) + 1
        return super(LbxbiGpod001, self).create(values)

        

    PoNumber = fields.Char(string='PO NUMBER', store=True)
    PurchaseOrderVersion = fields.Char(string='PURCHASE ORDER VERSION')
    # ProductRef = fields.Char(string='DESCRIPTION', related="PurchaseorderNum.FactoryID" , store=True)
    ProductRef01 = fields.Char(string='DESC')
    VsPoNumber = fields.Char(string='VS PO NUMBER')
    PoDate = fields.Datetime(string='PO DATE')
    lineItem = fields.Char(string='LINE ITEM', store=True)
    FactoryId = fields.Char(string='FACTORY ID', related="PurchaseorderNum.FactoryID" , store=True)
    Silhouette = fields.Char(string='SILHOUETTE', related="PurchaseorderNum.SILHOUETTE_name" , store=True)
    # Collection = fields.Char(string='COLLECTION')
    RnNumber = fields.Selection(string='RN NUMBER', related="PurchaseorderNum.RnNumber", store=True)
    CaNumber = fields.Selection(string='CA NUMBER', related="PurchaseorderNum.CaNumber", store=True)
    OrderQuantity = fields.Char(string='ORDER QUANTITY', store=True)
    SizeId = fields.Char(string='SIZE ID')
    Size = fields.Char(string='SIZE', store=True)
    Style = fields.Char(string='STYLE', store=True)
    # DeliveryDate = fields.Datetime(default=fields.Datetime.now , string = 'DELIVERY DATE')
    SoNumber = fields.Char(string='SO NUMBER', store=True)
    SoOrderItem = fields.Char(string='SO ORDER ITEM', store=True)
    SoRefLv = fields.Char(string='SO REF LV', compute="_compute_so_ref_lv", store=True)
    ColorCode = fields.Char(string='COLOR CODE' , store=True)
    ColorCode2 = fields.Char(string='COLOR CODE 2' , store=True)
    new_color = fields.Char(string='COLOR CODE MAPPED' , store=True)
    Sku = fields.Char(string='SKU' , store=True)
    ArticalNumber = fields.Char(string='ARTICLE NUMBER', store=True)
    RetailPrice = fields.Float(string='RETAIL PRICE' , store=True)
    RetailPrice2 = fields.Float(string='RETAIL PRICE 2' , store=True)
    RetailPrice3 = fields.Float(string='RETAIL PRICE 3', store=True)
    SizeQuantity = fields.Char(string='SIZE QUANTITY', store=True)
    CareInstructionSet = fields.Char(string='CARE INSTRUCTION SET')
    ComponentName = fields.Char(string='COMPONENT NAME')
    FiberName = fields.Char(string='FIBER NAME')
    FiberPercentage = fields.Char(string='FIBER PERCENTAGE')
    AdditionalCareInstruction = fields.Char(string='ADDITIONAL CARE INSTRUCTION', related="PurchaseorderNum.additional_ins_name", store=True)
    Vendor_Material = fields.Char(string='Vendor Material')
    Chain_id_get_02 = fields.Char(string='CHAIN ID',  related="PurchaseorderNum.Chain_id_get_02", store=True)
    CustomerID = fields.Char(string='CUSTOMER ID', related="PurchaseorderNum.CustomerID", store=True)
    AddressID = fields.Char(string='ADDRESS ID', related="PurchaseorderNum.DeliveryAddressId", store=True)

    DeliveryContact = fields.Char(string='DELIVERY CONTACT', related="PurchaseorderNum.DeliveryContact", store=True)
    DeliveryMethod = fields.Selection(string='DELIVERY METHOD', related="PurchaseorderNum.DeliveryMethod", store=True)
    DeliveryAccount = fields.Selection(string='DELIVERY ACCOUNT', related="PurchaseorderNum.DeliveryAccount", store=True)
    FactoryID = fields.Char(string='FACTORY ID', related="PurchaseorderNum.FactoryID", store=True)
    DelDate = fields.Date(string ="DELIVERY DATE", related="PurchaseorderNum.DelDate", store=True)
    Status = fields.Selection(string='STATUS', related="PurchaseorderNum.Status", store=True)
    ProductRef = fields.Char(string='PRODUCT REF', related="PurchaseorderNum.ProductRef_name", store=True)
    size_range = fields.Char(string='SIZE RANGE', related="PurchaseorderNum.Size_Range_name", store=True)
    additional_instruction = fields.Char(string='ADDITIONAL INSTRUCTION')

    Customer_name = fields.Char(string='CUSTOMER NAME', related="PurchaseorderNum.Customer_name", store=True)

    date = fields.Char(string='DATE OF MANUFACTURE', related="PurchaseorderNum.date", store=True)

    # PO From VPO
    PoFromVpo = fields.Many2one(string='PO FROM VPO', related="PurchaseorderNum.PoFromVpo")
    PoNumber_from_vpo_h = fields.Many2one('lbx_mi_vpo_lines_d001', string='PoNumber_from_vpo_h')


    # 2023-12-11
    item_code = fields.Char(string='ITEM CODE')
    date_of_manuf = fields.Char(string='DATE OF MANUFACTURE')
    desc = fields.Char(string='DESC')
    care_instruction_set_code = fields.Char(string='CARE INSTRUCTION SET CODE', related ="PurchaseorderNum.care_instruction_set_code_2" , store=True)
    # additional_instruction = fields.Char(string='ADDITIONAL INSTRUCTION')
    

    #  Add SLASH SOREFLV TO 
    @api.depends('SoNumber', 'SoOrderItem')
    def _compute_so_ref_lv(self):
        for record in self:
            # Check if both SoNumber and SoOrderItem have values
            if record.SoNumber and record.SoOrderItem:
                # Remove two leading zeros from SoOrderItem and concatenate with SoNumber
                so_order_item_without_zeros = record.SoOrderItem.lstrip('0')
                record.SoRefLv = f"{record.SoNumber}/{so_order_item_without_zeros}"
            else:
                record.SoRefLv = False  # Set a default value or handle the case when either field is not set




    # 2023-12-18
    c_id = fields.Integer(string = 'COMPOSITION ID')


    material_code = fields.Char(string ='MATERIAL CODE', store=True)

    NewSize = fields.Char(string ='SIZE CODE', store=True)

    # To get item number
    PurchaseOrderItem = fields.Char(string ='PO ITEM', store=True)



    # 2023-12-28  New Field to get po number with line number
    POwithLine = fields.Char(string ='PO WITH LINE',  compute ='_compute_po_line', store=True)
    @api.depends('PoNumber', 'PurchaseOrderItem')
    def _compute_po_line(self):
        for record in self:
            if record.PoNumber and record.PurchaseOrderItem:
                PurchaseOrderItem_without_zeros = record.PurchaseOrderItem.lstrip('0')
                record.POwithLine = f"{record.PoNumber}-{PurchaseOrderItem_without_zeros}"
            else:
                record.POwithLine = False

    # 2023-12-29
    size_lv = fields.Char(string='LV SIZE')

    size_mapping = fields.Many2one('size_map_lines', string='Size Mapping', compute='_compute_size_mapping', store=True)

    @api.depends('Size')
    def _compute_size_mapping(self):
        for record in self:
            size_mapping = self.env['size_map_lines'].search([('Size_Range', '=', record.size_range), ('Size', '=', record.Size)], limit=1)
            record.size_mapping = size_mapping
            if size_mapping:
                record.size_lv = size_mapping.Size_LV
            else:
                record.size_lv = ''

    vendor_id = fields.Char(string='VENDOR ID', related="PurchaseorderNum.vendor_id", store=True)
    style_number = fields.Char(string='STYLE NUMBER', related="PurchaseorderNum.style_number", store=True)
    color_desc = fields.Char(string='COLOR DESC', related="PurchaseorderNum.color_desc", store=True)
    season_01 = fields.Selection(string='SEASON', related="PurchaseorderNum.season_01",store=True)
    season = fields.Char(string='SEASON', related="PurchaseorderNum.season_name",store=True)
    # Coo = fields.Char(string='COO', related="PurchaseorderNum.Coo_1", store=True)
    CustomerStyleDesc = fields.Char(string = 'CUSTOMER STYLE DESC', store=True)
    Collection = fields.Char(string = 'COLLECTION', related="PurchaseorderNum.Collection_name", store=True)
    Coo = fields.Char(string='COO', related="PurchaseorderNum.Coo_1", store=True)

    vss = fields.Char(string='VSS', store=True)
    vsd = fields.Char(string='VSD' , related="PurchaseorderNum.vsd", store=True)