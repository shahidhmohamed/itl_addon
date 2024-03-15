from odoo import api, models, fields, _


class test(models.Model):
    _name = "test"
    test = fields.Char(string="reference",required=True, copy=False, readonly=True, default=lambda self: _('New'))
    Name = fields.Char(string='name')

    @api.model
    def create(self, vals):
        print("test create vals",vals)
        vals['test'] = self.env['ir.sequence'].next_by_code('purchase.order.new')
        return super(test, self).create(vals)