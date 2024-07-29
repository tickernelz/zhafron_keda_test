# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Material(models.Model):
    _name = 'keda.material'
    _description = 'Material'

    name = fields.Char('Material Name', required=True)
    material_code = fields.Char(required=True)
    material_type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')], required=True)
    material_buy_price = fields.Float(required=True)
    supplier_id = fields.Many2one('keda.supplier', string="Related Supplier", required=True)

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise ValidationError("Material buy price cannot be less than 100.")
