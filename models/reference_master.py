from odoo import models, fields, api, _


class LbxMiReferenceMaster(models.Model):
    _name = "reference_master"
    _description = "PRODUCT REFERENCE MASTER"
    _rec_name = 'ProductRef'

    ProductRef = fields.Char(string='PRODUCT REFERENCE')
    ProductRef_name = fields.Char(string='PRODUCT REFERENCE NAME')
    is_default = fields.Boolean(string='Is Default')
