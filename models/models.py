# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class zhafron_keda_test(models.Model):
#     _name = 'zhafron_keda_test.zhafron_keda_test'
#     _description = 'zhafron_keda_test.zhafron_keda_test'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
