from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class LbxMivpod001(models.Model):
    _name = "lbx_mi_vpo_d001"
    _inherit =["mail.thread",'mail.activity.mixin']
    _description = "VPO"
    _rec_name = 'Po_number_get'

    vpo_lines = fields.One2many('lbx_mi_vpo_lines_d001', 'vpo_line_c', string="vpo_lines")
    vpo_to_po = fields.One2many('lbx_mi_gpo_d001', 'lvp_lpo', string="PurchaseorderNum")
    VPONo = fields.Char(string='VPO NO')
    PoNumber = fields.Char(string='PO NUMBER')
    VpoUniqNo = fields.Char(string="VPO NO", required=True, copy=False, readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        print("ADD VPO",vals)
        vals['VpoUniqNo'] = self.env['ir.sequence'].next_by_code('vpo.seq')
        return super(LbxMivpod001, self).create(vals)

    Po_number_get = fields.Char(string='PO NUMBER')

    def getVPOdetails(self):
        other_model = self.env['vpo']
        size_master_model = self.env['lbx_size_master']
        data = other_model.search([('po', '=', self.Po_number_get)])

        # Check if get_po_lines is already set
        if self.vpo_lines:
            raise UserError(_('Data already fetched. Cannot perform operation again.'))

        if not self.Po_number_get:
            raise ValidationError(_('Please Enter The Po Number.'))

        po_line_values_list = []
        data_fetched = False
        
        for record in data:
            if not record.size:
                print(f"Skipping record with empty size field for VPO: {record.po}")
                continue

            size_master_record = size_master_model.search([('size_id', '=', record.size)], limit=1)
            if not size_master_record:
                raise ValidationError(f"No matching size ID found for VPO with size ID: {record.size}")
                
            vpo_line_values = {
                'PoNumber': record.po,
                'ProductReference': record.product_ref,
                'Style': record.style,
                'CC': record.color,
                'Size': record.size,
                'newsize': record.size,
                'RetailPrice1': record.retail1,
                'RetailPrice2': record.retail2,
                'RetailPrice3': record.retail3,
                'Sku': record.sku,
                'Desc1': record.description,
                'Article': record.art,
                'OrderQuantity': record.qty,
            }
            if size_master_record:
                # If a match is found, override the 'Size' field with size_master data
                vpo_line_values['newsize'] = size_master_record.size
            else:
                # If no match is found, set the 'Size' field to blank
                vpo_line_values['newsize'] = ''

            # Append po_line_values to the list
            po_line_values_list.append((0, 0, vpo_line_values))

            data_fetched = True

        if data_fetched:
        # Update self.get_po_lines with the collected values
            self.vpo_lines = po_line_values_list
            message = _("VPO GET SUCCESSFULLY.")
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
            message = _("No matching data found for VPO Number: %s" % self.PoNumber)
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'message': message,
                    'type': 'warning',
                    'sticky': False,
                }
            }


    # @api.model
    # def replace_sizes(self):
    #     # Loop through vpo_lines and replace sizes using lbx_size_master
    #     for record in self:
    #         for vpo_line in record.vpo_lines:
    #             size_id = self.env['lbx_size_master'].search([('size_id', '=', vpo_line.Size)], limit=1)
    #             if size_id:
    #                 vpo_line.write({'Size': size_id.size})

    
