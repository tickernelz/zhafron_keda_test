# -*- coding: utf-8 -*-
{
    'name': "zhafron_keda_test",
    'summary': """
        Zhafron Keda Material Test""",
    'description': """
        Zhafron Keda Material Test
    """,
    'author': "Zhafron/tickernelz",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/material.xml',
        'views/supplier.xml',
        'views/menu.xml',
    ],
}
