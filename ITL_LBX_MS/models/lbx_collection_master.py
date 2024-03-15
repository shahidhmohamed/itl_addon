from odoo import models, fields, api, _


class LbxMiCollectionmaster(models.Model):
    _name = "lbx_collection_master"
    _description = "LBX COLLECTION MASTER"
    _rec_name = 'Collection'


    Collection = fields.Char (string = 'COLLECTION')
    Collection_name = fields.Char (string = 'COLLECTION NAME')