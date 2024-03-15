from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError



class LbxMiGpoH001(models.Model):
    _name = "lbx_mi_gpo_h001"
    _inherit =["mail.thread",'mail.activity.mixin']
    _description = "PO"
    _rec_name = 'PoNumber'

    get_po_lines = fields.One2many('lbx_mi_gpo_d001', 'PurchaseorderNum', string="PurchaseorderNum")
    system = fields.Selection([('PDM300', 'PDM300'), ('PSI100', 'PSI100')],
                              string='SYSTEM', default='PDM300')
    PoNumber = fields.Char(string='INPUT PO NUMBER', store=True)
    ChainID = fields.Selection([('VS22', 'VS22'), ('LB8', 'LB8')],
                              string='CHAIN ID', default='VS22')
    ChainID02 = fields.Many2one('sub_chain',string='CHAIN ID', store=True)
    ChoosePo = fields.Selection([('RFID', 'RFID'), ('CARE LABELS', 'CARE LABELS'), ('PRICE TKT / BARCODE STK', 'PRICE TKT / BARCODE STK'), ('MAIN LABELS', 'MAIN LABELS')],
                              string='CHOOSE PO', default='RFID')
    
    Customer = fields.Many2one('res.partner',string='CUSTOMER', store=True)
    Customer_name = fields.Char(string='CUSTOMER NAME', compute = '_compute_customer_name')
    @api.depends('Customer')
    def _compute_customer_name(self):
        for record in self:
            if record.Customer:
                record.Customer_name = record.Customer.name
            else:
                record.Customer_name = False

    # CustomerID = fields.Char(string='CUSTOMER ID')

    # delete_line_items = fields.Boolean(string='Delete Line Items', default=False)

    # ... (other methods)

    def delete_records_from_related_model(self):
        if not self.PoNumber:
            raise UserError(_('Please provide a PO Number for deleting records.'))

        # Assuming lbx_mi_gpo_d001 is the related model
        gpo_d001_model = self.env['lbx_mi_gpo_d001']

        # Find records based on PoNumber
        records_to_delete = gpo_d001_model.search([('PoNumber', '=', self.PoNumber)])

        if not records_to_delete:
            raise UserError(_('No records found with PO Number %s' % self.PoNumber))

        # Delete the records in the related model
        records_to_delete.unlink()

        # Check if any records were deleted
        if records_to_delete:
            # Notification for success
            message = _("PO deleted successfully.")
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': True,
                    'next': {
                        'type': 'ir.actions.client',
                        'tag': 'reload',
                    }
                }
            }
        else:
            # No records deleted, show a different message or do nothing
            return {'type': 'ir.actions.do_nothing'}



    DeliveryAddress = fields.Many2one('res.partner', string='DELIVERY ADDRESS',
                                      domain="[('id', 'child_of', Customer)]")

    @api.onchange('Customer')
    def onchange_customer(self):
        if self.Customer:
            # Set DeliveryAddress domain to show only addresses related to the selected customer
            return {'domain': {'DeliveryAddress': [('id', 'child_of', self.Customer.id)]}}
        else:
            return {'domain': {'DeliveryAddress': []}}

    # @api.depends('DeliveryAddress')
    # def _compute_d_add(self):
    #     for record in self:
    #         if record.Customer:
    #             record.DeliveryAddress = record.Customer.street
    #         else:
    #             record.DeliveryAddress = False  # Set a default value or handle the case when ChainID02 is not set

    DeliveryAddressId = fields.Char(string='DELIVERY ADDRESS ID', compute='_compute_d_add_id', store=True)
    @api.depends('DeliveryAddress')
    def _compute_d_add_id(self):
        for record in self:
            if record.DeliveryAddress:
                record.DeliveryAddressId = record.DeliveryAddress.phone
            else:
                record.DeliveryAddressId = False

    # 2023-12-22
    Dateofmanu = fields.Date(string='DATE OF MANUFACTURE')
    date = fields.Char(string='Date', compute='_compute_last_four_letters', store=True)

    @api.depends('Dateofmanu')
    def _compute_last_four_letters(self):
        for record in self:
            if record.Dateofmanu:
                month = str(record.Dateofmanu.month).zfill(2)  # Ensure two digits for the day
                year = str(record.Dateofmanu.year)[-2:]  # Extract last two digits of the year
                record.date = month + ' ' + year
            else:
                record.date = ''


    DeliveryContact = fields.Char(string='DELIVERY CONTACT')
    DeliveryMethod = fields.Selection([('TRUCK', 'TRUCK')],
                              string='DELIVERY METHOD', default='TRUCK')
    DeliveryAccount = fields.Selection([('ITL', 'ITL')],
                              string='DELIVERY ACCOUNT', default='ITL')
    DelDate = fields.Date(string ="DELIVERY DATE")
    User = fields.Many2one('res.users', string='USER', default=lambda self: self.env.user)
    PrimaryKey = fields.Char(string='PrimaryKey')
    DateTime = fields.Datetime(default=fields.Datetime.now)
    UpdateDateTime = fields.Datetime(default=fields.Datetime.now)
    Status = fields.Selection([('Success', 'Success'), ('Open', 'Open'), ('Cancelled', 'Cancelled'), ('Progress', 'Progress')],
                              string='STATUS', default='Open')

    # SizeId011 = fields.Many2one('size_range_master', string='SIZE RANGE')

    size_range = fields.Many2one('size_range_master', string='SIZE RANGE')

    Size_Range_name = fields.Char(string='SIZE RANGE', compute ='_compute_size_range_name' , store=True)
    @api.depends('size_range')
    def _compute_size_range_name(self):
        for record in self:
            if record.size_range:
                record.Size_Range_name = record.size_range.Size_Range_name
            else:
                record.Size_Range_name = ''

    FactoryID = fields.Char(string='FACTORY ID')
    




                                
    # Related Fields
    PoNumber01 = fields.Char(string='PO NUMBER', related="get_po_lines.PoNumber")
    PurchaseOrderVersion = fields.Char(string='PurchaseOrderVersion', related="get_po_lines.PurchaseOrderVersion" )
    # ProductRef = fields.Char(string='PRODUCT REF', related="get_po_lines.ProductRef")
    VsPoNumber = fields.Char(string='VS PO NUMBER', related="get_po_lines.VsPoNumber")
    PoDate = fields.Datetime(string='PO DATE', related="get_po_lines.PoDate")
    lineItem = fields.Char(string='LINE ITEM', related="get_po_lines.lineItem")
    # FactoryId = fields.Char(string='FACTORY ID')


    Silhouette = fields.Many2one('lbx_silhouette_master', string='SILHOUETTE')
    SILHOUETTE_name = fields.Char(string='SILHOUETTE', compute='_compute_silhouette')
    @api.depends('Silhouette')
    def _compute_silhouette(self):
        for record in self:
            if record.Silhouette:
                record.SILHOUETTE_name = record.Silhouette.SILHOUETTE_name
            else:
                record.SILHOUETTE_name = False

    Collection = fields.Many2one('lbx_collection_master' , string='COLLECTION')
    Collection_name = fields.Char(string='COLLECTION', compute='_compute_collection')
    @api.depends('Collection')
    def _compute_collection(self):
        for record in self:
            if record.Collection:
                record.Collection_name = record.Collection.Collection_name
            else:
                record.Collection_name = False

    RnNumber = fields.Selection([('54867', '54867')],
                              string='RN NUMBER', default='54867')
    CaNumber = fields.Selection([('67359', '67359')],
                              string='CA NUMBER', default='67359')
    OrderQuantity = fields.Char(string='ORDER QUANTITY', related="get_po_lines.OrderQuantity")
    SizeId = fields.Char(string='SIZE ID', related="get_po_lines.SizeId")
    Size = fields.Char(string='SIZE', related="get_po_lines.Size")
    Style = fields.Char(string='STYLE', related="get_po_lines.Style")
    # DeliveryDate = fields.Datetime(default=fields.Datetime.now , related="get_po_lines.DeliveryDate")
    SoNumber = fields.Char(string='SO NUMBER', related="get_po_lines.SoNumber")
    SoOrderItem = fields.Char(string='SO ORDER ITEM', related="get_po_lines.SoOrderItem")
    SoRefLv = fields.Char(string='SO REF LV', related="get_po_lines.SoRefLv")
    ColorCode = fields.Char(string='COLOR CODE', related="get_po_lines.ColorCode")
    ColorCode2 = fields.Char(string='COLOR CODE 2', related="get_po_lines.ColorCode2")
    Sku = fields.Char(string='SKU', related="get_po_lines.Sku")
    ArticalNumber = fields.Char(string='ARTICLE NUMBER', related="get_po_lines.ArticalNumber")
    RetailPrice = fields.Float(string='RETAIL PRICE', related="get_po_lines.RetailPrice")
    RetailPrice2 = fields.Float(string='RETAIL PRICE 2', related="get_po_lines.RetailPrice2")
    RetailPrice3 = fields.Float(string='RETAIL PRICE 3', related="get_po_lines.RetailPrice3")
    SizeQuantity = fields.Char(string='SIZE Quantity', related="get_po_lines.SizeQuantity")
    CareInstructionSet = fields.Char(string='CARE INSTRUCTION SET', related="get_po_lines.CareInstructionSet")
    ComponentName = fields.Char(string='COMPONENT NAME', related="get_po_lines.ComponentName")
    FiberName = fields.Char(string='FIBER NAME', related="get_po_lines.FiberName")
    FiberPercentage = fields.Char(string='FIBER PERCENTAGE', related="get_po_lines.FiberPercentage")
    AdditionalCareInstruction = fields.Char(string='ADDITIONAL CARE INSTRUCTION', related="get_po_lines.AdditionalCareInstruction")
    Vendor_Material = fields.Char(string='Vendor Material', related="get_po_lines.Vendor_Material")

    rfid_user = fields.Char(string='RFID USER')
    main_user = fields.Char(string='MAIN USER')

    # po from vpo
    PoFromVpo = fields.Many2one('lbx_mi_vpo_lines_d001', string='VPO FROM PO')

    # po from vpo
    PoFromVpoHeader = fields.Many2one('lbx_mi_vpo_d001', string='VPO FROM PO')


    # to get Chain id
    Chain_id_get_02 = fields.Char(string='CHAIN ID', compute = '_compute_chain_id', store=True)
    @api.depends('ChainID02')
    def _compute_chain_id(self):
        for record in self:
            if record.ChainID02:
                record.Chain_id_get_02 = record.ChainID02.ChainId
            else:
                record.Chain_id_get_02 = False  # Set a default value or handle the case when ChainID02 is not set
                
    # To get Customer ID
    CustomerID = fields.Char(string='CUSTOMER ID', compute = '_compute_c_id', store=True)
    @api.depends('Customer')
    def _compute_c_id(self):
        for record in self:
            if record.Customer:
                record.CustomerID = record.Customer.vat
            else:
                record.CustomerID = False  # Set a default value or handle the case when ChainID02 is not set

    # To get Address ID
    AddressID = fields.Char(string='ADDRESS ID', compute = '_compute_a_id', store=True)
    @api.depends('Customer')
    def _compute_a_id(self):
        for record in self:
            if record.Customer:
                record.AddressID = record.Customer.mobile
            else:
                record.AddressID = False  # Set a default value or handle the case when ChainID02 is not set


    # ProductRef = fields.Char(string='PRODUCT REF')

    # 2023-12-14
    composition_01_lines = fields.One2many('composition_lines_01', 'composition_connect', string="vpo_lines")
    
    # llll
    vendor_id = fields.Char(string='VENDOR ID')

    style_number = fields.Char(string='STYLE NUMBER')

    color_desc = fields.Char(string='COLOR DESC')

    season_01 = fields.Selection([('FALL 21', 'FALL 21')],
                              string='SEASON', default='FALL 21')

    season = fields.Many2one('lbx_seson_master' , string = 'SEASON')
    season_name = fields.Char(string='SEASON', compute='_compute_season_name')
    @api.depends('season')
    def _compute_season_name(self):
        for record in self:
            if record.season:
                record.season_name = record.season.season_name
            else:
                record.season_name = False

    ProductRef = fields.Many2one('reference_master' , string = 'PRODUCT REF')
    ProductRef_name = fields.Char(string='PRODUCT REF', compute='_compute_PRODUCT_REF_name')
    @api.depends('ProductRef')
    def _compute_PRODUCT_REF_name(self):
        for record in self:
            if record.ProductRef:
                record.ProductRef_name = record.ProductRef.ProductRef_name
            else:
                record.ProductRef_name = False

    additional_ins = fields.Many2one('lbx_additional_instruction_master' , string = 'ADDITIONAL INSTRUCTION')
    additional_ins_name = fields.Char(string='ADDITIONAL INSTRUCTION', compute='_compute_additional_ins')
    @api.depends('additional_ins')
    def _compute_additional_ins(self):
        for record in self:
            if record.additional_ins:
                record.additional_ins_name = record.additional_ins.additional_ins_name
            else:
                record.additional_ins_name = False


    

    Coo = fields.Many2one('lbx_coo_master',string='COO')

    Coo_1 = fields.Char(string='COO', compute='_compute_coo')
    @api.depends('Coo')
    def _compute_coo(self):
        for record in self:
            if record.Coo:
                record.Coo_1 = record.Coo.coo_name
            else:
                record.Coo_1 = False

    care_instruction_set_code = fields.Many2one('lbx_care_instruction_set_code', string='CARE INSTRUCTION SET CODE')
    care_instruction_set_code_2 = fields.Char(string='CARE INSTRUCTION SET CODE', compute = '_compute_care_instruction_set_code_2')
    @api.depends('care_instruction_set_code')
    def _compute_care_instruction_set_code_2(self):
        for record in self:
            if record.care_instruction_set_code:
                record.care_instruction_set_code_2 = record.care_instruction_set_code.care_instruction_set_code_2
            else:
                record.care_instruction_set_code_2 = False


    


    # def compare_and_extract_data(self):
    #     VPO = self.env['lbx_mi_vpo_d001']
    #     data = VPO.search([('CustomerColorCode', '=', self.ColorCode)])
    #     data = VPO.search([('CustomerStyle', '=', self.Style)])
    #     data = VPO.search([('CustomerSizeCode', '=', self.Size)])
    #     for record in data:
    #         po_line_values = {
    #             'Sku': record.Upc,
    #             'ArticalNumber': record.CustomerArticle,
    #             'RetailPrice': record.RetailPrice1,
    #             'RetailPrice2': record.RetailPrice2,
    #             'RetailPrice3': record.RetailPrice3,
    #         }
    #         self.get_po_lines = [(0, 0, po_line_values)]


    # def getPOdetails(self):
    #     if not self.PoNumber:
    #         raise ValidationError(_('Please Enter The Po Number.'))

    #     # Check if get_po_lines is already set
    #     if self.get_po_lines:
    #         raise UserError(_('Data already fetched. Cannot perform operation again.'))

    #     if not self.ChainID02:
    #         raise ValidationError(_('Please select the Chain details before Get Po Details.'))

    #     if not self.Customer:
    #         raise ValidationError(_('Please select the Customer details before Get Po Details.'))

    #     if not self.DeliveryAddress:
    #         raise ValidationError(_('Please select the Delivery Address details before Get Po Details.'))


    #     if not self.DeliveryMethod:
    #         raise ValidationError(_('Please select the Delivery Method details before Get Po Details.'))

    #     if not self.DeliveryAccount:
    #         raise ValidationError(_('Please select the Delivery Account details before Get Po Details.'))

    #     if not self.DelDate:
    #         raise ValidationError(_('Please select the Delivery Date details before Get Po Details.'))

    #     if not self.Status:
    #         raise ValidationError(_('Please select the Status before Get Po Details.'))

    #     VPO = self.env['getpo_new']
    #     data = VPO.search([('order_number', '=', self.PoNumber)])

    #     for record in data:
    #         po_line_values = {
    #             'PoNumber': record.order_number,
    #             'PurchaseOrderVersion': record.purchaseorderversion,
    #             # 'ProductRef': record.refmaterial,
    #             'ProductRef01': record.materialdescription,
    #             'VsPoNumber': record.order_number,
    #             'PoDate': record.purchaseorderdate,
    #             'lineItem': record.purchaseorderitem,
    #             'material_code':record.material_code,
    #             # 'FactoryId': record.,
    #             # 'Silhouette': record.,
    #             # 'Collection': record.,
    #             # 'RnNumber': record.,
    #             # 'CaNumber': record.,
    #             # 'Coo': record.,
    #             'OrderQuantity': record.quantity1,
    #             # 'SizeId': record.,
    #             'Size': record.grid_value,
    #             # 'NewSize': record.GridValue,
    #             'Style': record.customerstyle,
    #             # 'DeliveryDate': record.DeliveryDate,
    #             'SoNumber': record.salesorder1,
    #             'SoOrderItem': record.salesorderitem,
    #             # 'SoRefLv': record.,
    #             'ColorCode': record.colorcode,
    #             # 's_Quantity1':record.Quantity1,
    #             # 'RetailPrice': record.,
    #             # 'RetailPrice2': record.,
    #             # 'RetailPrice3': record.,
    #             'SizeQuantity': record.quantity,
    #             'PurchaseOrderItem': record.purchaseorderitem,
    #             # 'ArticalNumber': record.ArticalNumber,
    #             # 'CareInstructionSet': record.,
    #             # 'ComponentName': record.,
    #             # 'FiberName': record.,
    #             'CustomerStyleDesc': record.CustomerStyleDesc,
    #             # 'AdditionalCareInstruction': record.,Vendor_Material
                
    #         }
    #         self.get_po_lines = [(0, 0, po_line_values)]
    #         # Display success message and reload the view
    #         message = _("PO GET SUCCESSFULLY.")
    #         return {
    #             'type': 'ir.actions.client',
    #             'tag': 'display_notification',
    #             'params': {
    #                 'message': message,
    #                 'type': 'success',
    #                 'sticky': True,
    #                 'next': {
    #                     'type': 'ir.actions.client',
    #                     'tag': 'reload',
    #                 }
    #             }
    #         }
    

    def getPOdetails(self):
        if not self.PoNumber:
            raise ValidationError(_('Please Enter The Po Number.'))

        # Check if get_po_lines is already set
        if self.get_po_lines:
            raise UserError(_('Data already fetched. Cannot perform operation again.'))

        if not self.ChainID02:
            raise ValidationError(_('Please select the Chain details before Get Po Details.'))

        if not self.Customer:
            raise ValidationError(_('Please select the Customer details before Get Po Details.'))

        if not self.DeliveryAddress:
            raise ValidationError(_('Please select the Delivery Address details before Get Po Details.'))

        if not self.DeliveryMethod:
            raise ValidationError(_('Please select the Delivery Method details before Get Po Details.'))

        if not self.DeliveryAccount:
            raise ValidationError(_('Please select the Delivery Account details before Get Po Details.'))

        if not self.DelDate:
            raise ValidationError(_('Please select the Delivery Date details before Get Po Details.'))

        if not self.Status:
            raise ValidationError(_('Please select the Status before Get Po Details.'))

        VPO = self.env['getpo_new']
        data = VPO.search([('order_number', '=', self.PoNumber)])
        
        # Initialize a list to store po_line_values
        po_lines_values_list = []
        data_fetched = False

        for record in data:
            # Populate po_line_values for each record
            po_line_values = {
                'PoNumber': record.order_number,
                'PurchaseOrderVersion': record.purchaseorderversion,
                # 'ProductRef': record.refmaterial,
                'ProductRef01': record.materialdescription,
                'VsPoNumber': record.order_number,
                'PoDate': record.purchaseorderdate,
                'lineItem': record.purchaseorderitem,
                'material_code':record.material_code,
                'ColorCode2': record.ColorCode2,
                # 'Silhouette': record.,
                # 'Collection': record.,
                # 'RnNumber': record.,
                # 'CaNumber': record.,
                # 'Coo': record.,
                'OrderQuantity': record.quantity1,
                # 'SizeId': record.,
                'Size': record.grid_value,
                # 'NewSize': record.GridValue,
                'Style': record.customerstyle,
                'Style': record.vss,
                # 'DeliveryDate': record.DeliveryDate,
                'SoNumber': record.salesorder1,
                'SoOrderItem': record.salesorderitem,
                # 'SoRefLv': record.,
                'ColorCode': record.colorcode,
                # 's_Quantity1':record.Quantity1,
                # 'RetailPrice': record.,
                # 'RetailPrice2': record.,
                # 'RetailPrice3': record.,
                'SizeQuantity': record.quantity,
                'PurchaseOrderItem': record.purchaseorderitem,
                # 'ArticalNumber': record.ArticalNumber,
                # 'CareInstructionSet': record.,
                # 'ComponentName': record.,
                # 'FiberName': record.,
                'CustomerStyleDesc': record.CustomerStyleDesc,
                # 'AdditionalCareInstruction': record.,Vendor_Material
            }
            po_lines_values_list.append((0, 0, po_line_values))

            # Set the flag to True since data is fetched
            data_fetched = True

        if data_fetched:
            # Update the get_po_lines field with the list of po_line_values
            self.get_po_lines = po_lines_values_list

            message = _("RECEIVED SUCCESSFULLY.")
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'success',
                    'sticky': True,
                    'next': {
                        'type': 'ir.actions.client',
                        'tag': 'reload',
                    }
                }
            }
        else:
            # If no data is fetched, display a warning message
            message = _("No matching data found for PO Number: %s" % self.PoNumber)
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'warning',
                    'sticky': False,
                }
            }

    selected_vpo_details = fields.Many2one('lbx_mi_vpo_d001', string='SELECT VPO')



    def compare_and_extract_data(self):
        if not self.selected_vpo_details:
            raise ValidationError(_('Please select the VPO details before comparing and extracting data.'))

        VPO = self.env['lbx_mi_vpo_lines_d001']

        missing_records_details = []

        # Iterate through existing records and update values
        for existing_record in self.get_po_lines:
            # Find data based on matching criteria
            data = VPO.search([
                ('PoNumber', '=', existing_record.PoNumber),
                ('newsize', '=', existing_record.Size),
                ('Style', '=', existing_record.Style),
            ])

            new_values = self._extract_po_line_values(data, existing_record.ColorCode)

            if not self.ColorCode:
                raise ValidationError(_('Color Code Missing.'))

            if new_values:
                existing_record.write(dict(new_values))
            else:
                missing_records_details.append({
                    'line_number': existing_record.line_number,
                    'details': {
                        'PoNumber': existing_record.PoNumber,
                        'Size': existing_record.Size,
                        'Style': existing_record.Style,
                        'ColorCode': existing_record.ColorCode,
                    },
                    'reason': 'Matching criteria not found in VPO.',
                })

        if missing_records_details:
            error_message = "Data not transferred for the following line numbers:\n"
            for record_details in missing_records_details:
                error_message += (
                    f"Line Number: {record_details['line_number']}, "
                    f"Details: {record_details['details']}, "
                    f"Reason: {record_details['reason']}\n"
                )

            raise UserError(error_message)

        # Display success message and reload the view
        message = _("Data fetched and updated successfully.")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': message,
                'type': 'success',
                'sticky': True,
                'next': {
                    'type': 'ir.actions.client',
                    'tag': 'reload',
                }
            }
        }
            

        

    def _extract_po_line_values(self, data, existing_color_code):
        # Extract and return values for each record in data
        new_values = {}
        success_flag = False  # Flag to indicate if any record meets the conditions

        for record in data:
            # Check if the color code matches
            if record.CC == existing_color_code:
                # Update new_values dictionary
                new_values.update({
                    'Sku': record.Sku,
                    'ArticalNumber': record.Article,
                    'RetailPrice': record.RetailPrice1,
                    'RetailPrice2': record.RetailPrice2,
                    'RetailPrice3': record.RetailPrice3,
                    'c_id': record.c_id,
                })

                # Check if all specified fields are non-empty
                if record.Sku and record.Article:
                    success_flag = True

        if not success_flag:
            return None

        return new_values

    vss = fields.Char(string='VSS')
    vsd = fields.Char(string='VSD')

    # def compare_and_extract_data(self):
    #     color_model = self.env['color_code_master']
    #     data = color_model.search([('order_number', '=', record.new_color)])
    #     for record in data:
    #         if po_line_values_list.ColorCode = record.new_color:



    # def compare_and_extract_data(self):
    #     if not self.selected_vpo_details:
    #         raise ValidationError(_('Please select the VPO details before comparing and extracting data.'))

    #     VPO = self.env['lbx_mi_vpo_lines_d001']

    #     # List to store notifications for multiple records
    #     notifications = []

    #     # Iterate through existing records and update values
    #     for existing_record in self.get_po_lines:
    #         # Find data based on matching criteria
    #         data = VPO.search([
    #             ('newsize', '=', existing_record.Size),
    #             ('Style', '=', existing_record.Style),
    #         ])

    #         new_values = self._extract_po_line_values(data, existing_record.ColorCode)

    #         if not existing_record.ColorCode:
    #             raise ValidationError(_('Color Code Missing.'))

    #         if new_values:
    #             # Update existing record with values
    #             existing_record.write(dict(new_values))

    #             # Build notification message for this record
    #             message = _("Data Fetched Successfully for record with Color Code: %s" % existing_record.ColorCode)
    #             notifications.append({
    #                 'message': message,
    #                 'type': 'success',
    #                 'sticky': False,
    #             })

    #     # Check if any notifications were generated
    #     if notifications:
    #         return {
    #             'type': 'ir.actions.client',
    #             'tag': 'display_notification',
    #             'params': {
    #                 'notifications': notifications,
    #             }
    #         }
    #     else:
    #         # If no data is fetched, you might want to handle this case
    #         # with an appropriate message or action.
    #         message = _("No matching data found.")
    #         return {
    #             'type': 'ir.actions.client',
    #             'tag': 'display_notification',
    #             'params': {
    #                 'message': message,
    #                 'type': 'warning',
    #                 'sticky': False,
    #             }
    #         }


    # def _extract_po_line_values(self, data, existing_color_code):
    #     # Extract and return values for each record in data
    #     new_values = {}
    #     for record in data:
    #         # Check if the color code matches
    #         if record.CC == existing_color_code:
    #             new_values.update({
    #                 'Sku': record.Sku,
    #                 'ArticalNumber': record.Article,
    #                 'RetailPrice': record.RetailPrice1,
    #                 'RetailPrice2': record.RetailPrice2,
    #                 'RetailPrice3': record.RetailPrice3,
    #                 'c_id': record.c_id,
    #             })
                

    #     # Return the extracted values if the loop doesn't exit early
    #     return new_values


        



    


    # def compare_and_extract_data(self):
    #     VPO = self.env['lbx_mi_vpo_lines_d001']

    #     # Iterate through existing records
    #     for existing_record in self.get_po_lines:
    #         # Find data based on Size
    #         data = VPO.search([('CustomerSizeCode', '=', existing_record.Size)])

    #         # Update values for the existing record
    #         new_values = self._extract_po_line_values(data)
    #         if new_values:
    #             existing_record.write({'get_po_lines': new_values})

    # def _extract_po_line_values(self, data):
    #     # Extract and return values for each record in data
    #     new_values = []
    #     for record in data:
    #         new_values.append((0, 0, {
    #             'Sku': record.Upc,
    #             'ArticalNumber': record.CustomerArticle,
    #             'RetailPrice': record.RetailPrice1,
    #             'RetailPrice2': record.RetailPrice2,
    #             'RetailPrice3': record.RetailPrice3,
    #         }))
    #     return new_values

# model of po lines
