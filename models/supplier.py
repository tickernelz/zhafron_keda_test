# -*- coding: utf-8 -*-
from odoo import models, fields


class Supplier(models.Model):
    _name = 'keda.supplier'
    _description = 'Supplier'

    name = fields.Char(required=True)
