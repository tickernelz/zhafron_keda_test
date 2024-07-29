# -*- coding: utf-8 -*-
# from odoo import http


# class ZhafronKedaTest(http.Controller):
#     @http.route('/zhafron_keda_test/zhafron_keda_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zhafron_keda_test/zhafron_keda_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zhafron_keda_test.listing', {
#             'root': '/zhafron_keda_test/zhafron_keda_test',
#             'objects': http.request.env['zhafron_keda_test.zhafron_keda_test'].search([]),
#         })

#     @http.route('/zhafron_keda_test/zhafron_keda_test/objects/<model("zhafron_keda_test.zhafron_keda_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zhafron_keda_test.object', {
#             'object': obj
#         })
