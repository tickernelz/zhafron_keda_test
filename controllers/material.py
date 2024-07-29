from odoo import http
from odoo.http import request, Response


class MaterialController(http.Controller):
    @http.route('/api/materials', type='json', auth='public', methods=['GET'])
    def get_materials(self):
        materials = request.env['keda.material'].search([])
        material_list = []
        for material in materials:
            material_list.append(
                {
                    'id': material.id,
                    'name': material.name,
                    'material_code': material.material_code,
                    'material_type': material.material_type,
                    'material_buy_price': material.material_buy_price,
                    'supplier_id': material.supplier_id.id,
                }
            )
        return material_list

    @http.route('/api/materials/<int:material_id>', type='json', auth='public', methods=['GET'])
    def get_material(self, material_id):
        material = request.env['keda.material'].browse(material_id)
        if not material.exists():
            return Response(status=404, content_type='application/json', response='{"error": "Material not found"}')
        return {
            'id': material.id,
            'name': material.name,
            'material_code': material.material_code,
            'material_type': material.material_type,
            'material_buy_price': material.material_buy_price,
            'supplier_id': material.supplier_id.id,
        }

    @http.route('/api/materials', type='json', auth='public', methods=['POST'])
    def create_material(self):
        data = request.jsonrequest
        material = request.env['keda.material'].create(data)
        return {
            'id': material.id,
            'name': material.name,
            'material_code': material.material_code,
            'material_type': material.material_type,
            'material_buy_price': material.material_buy_price,
            'supplier_id': material.supplier_id.id,
        }

    @http.route('/api/materials/<int:material_id>', type='json', auth='public', methods=['PUT'])
    def update_material(self, material_id):
        data = request.jsonrequest
        material = request.env['keda.material'].browse(material_id)
        if not material.exists():
            return Response(status=404, content_type='application/json', response='{"error": "Material not found"}')
        material.write(data)
        return {
            'id': material.id,
            'name': material.name,
            'material_code': material.material_code,
            'material_type': material.material_type,
            'material_buy_price': material.material_buy_price,
            'supplier_id': material.supplier_id.id,
        }

    @http.route('/api/materials/<int:material_id>', type='json', auth='public', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['keda.material'].browse(material_id)
        if not material.exists():
            return Response(status=404, content_type='application/json', response='{"error": "Material not found"}')
        material.unlink()
        return {'status': 'success'}
