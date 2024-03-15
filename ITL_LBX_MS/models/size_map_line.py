from odoo import models, fields, api, _



class SizeRangeline(models.Model):
    _name = "size_map_lines"
    _rec_name = 'Size_Range'

    size_main = fields.Many2one('size_map_main', string="size ranges")
    Size_Range = fields.Many2one(string= 'SIZE RANGE', related='size_main.Size_Range')
    Size = fields.Char(string= 'SIZE')
    Size_LV= fields.Char(string= 'SIZE LV')

    

