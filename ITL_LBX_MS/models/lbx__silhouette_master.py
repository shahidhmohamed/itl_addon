from odoo import models, fields, api, _


class LbxMisilhouettemaster(models.Model):
    _name = "lbx_silhouette_master"
    _description = "LBX SILHOUETTE MASTER"
    _rec_name = 'SILHOUETTE'


    SILHOUETTE = fields.Char (string = 'SILHOUETTE')
    SILHOUETTE_name = fields.Char (string = 'SILHOUETTE NAME')