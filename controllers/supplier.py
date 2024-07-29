from odoo import http
from odoo.http import request, Response


class SupplierController(http.Controller):
    @http.route('/api/suppliers', type='json', auth='public', methods=['GET'])
    def get_suppliers(self):
        suppliers = request.env['keda.supplier'].search([])
        supplier_list = []
        for supplier in suppliers:
            supplier_list.append(
                {
                    'id': supplier.id,
                    'name': supplier.name,
                }
            )
        return supplier_list

    @http.route('/api/suppliers/<int:supplier_id>', type='json', auth='public', methods=['GET'])
    def get_supplier(self, supplier_id):
        supplier = request.env['keda.supplier'].browse(supplier_id)
        if not supplier.exists():
            return Response(status=404, content_type='application/json', response='{"error": "Supplier not found"}')
        return {
            'id': supplier.id,
            'name': supplier.name,
        }

    @http.route('/api/suppliers', type='json', auth='public', methods=['POST'])
    def create_supplier(self):
        data = request.jsonrequest
        supplier = request.env['keda.supplier'].create(data)
        return {
            'id': supplier.id,
            'name': supplier.name,
        }

    @http.route('/api/suppliers/<int:supplier_id>', type='json', auth='public', methods=['PUT'])
    def update_supplier(self, supplier_id):
        data = request.jsonrequest
        supplier = request.env['keda.supplier'].browse(supplier_id)
        if not supplier.exists():
            return Response(status=404, content_type='application/json', response='{"error": "Supplier not found"}')
        supplier.write(data)
        return {
            'id': supplier.id,
            'name': supplier.name,
        }

    @http.route('/api/suppliers/<int:supplier_id>', type='json', auth='public', methods=['DELETE'])
    def delete_supplier(self, supplier_id):
        supplier = request.env['keda.supplier'].browse(supplier_id)
        if not supplier.exists():
            return Response(status=404, content_type='application/json', response='{"error": "Supplier not found"}')
        supplier.unlink()
        return {'status': 'success'}
