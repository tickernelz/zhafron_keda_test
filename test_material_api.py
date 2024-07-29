import json
import unittest

import requests


class TestMaterialAPI(unittest.TestCase):
    BASE_URL = 'http://localhost:3003/api/materials'
    SUPPLIER_URL = 'http://localhost:3003/api/suppliers'
    HEADERS = {'Content-Type': 'application/json'}
    created_material_id = None
    created_supplier_id = None

    def test_create_supplier(self):
        new_supplier = {'name': 'Test Supplier'}
        response = requests.post(self.SUPPLIER_URL, headers=self.HEADERS, data=json.dumps(new_supplier))
        result = response.json()['result']
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)
        self.assertIn('id', result)
        TestMaterialAPI.created_supplier_id = result['id']

    def test_create_material(self):
        self.test_create_supplier()  # Ensure supplier is created before creating material
        new_material = {
            'name': 'Test Material',
            'material_code': 'TM001',
            'material_type': 'fabric',
            'material_buy_price': 150.0,
            'supplier_id': TestMaterialAPI.created_supplier_id,
        }
        response = requests.post(self.BASE_URL, headers=self.HEADERS, data=json.dumps(new_material))
        result = response.json()['result']
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)
        self.assertIn('id', result)
        TestMaterialAPI.created_material_id = result['id']

    def test_get_material(self):
        self.test_create_material()  # Ensure material is created before getting it
        material_id = TestMaterialAPI.created_material_id
        response = requests.get(f'{self.BASE_URL}/{material_id}', headers=self.HEADERS, data=json.dumps({}))
        result = response.json()['result']
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)

    def test_update_material(self):
        self.test_create_material()  # Ensure material is created before updating it
        material_id = TestMaterialAPI.created_material_id
        updated_data = {
            'name': 'Updated Material',
            'material_code': 'TM002',
            'material_type': 'jeans',
            'material_buy_price': 200.0,
            'supplier_id': TestMaterialAPI.created_supplier_id,
        }
        response = requests.put(f'{self.BASE_URL}/{material_id}', headers=self.HEADERS, data=json.dumps(updated_data))
        result = response.json()['result']
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, dict)

    def test_get_materials(self):
        response = requests.get(self.BASE_URL, headers=self.HEADERS, data=json.dumps({}))
        result = response.json()['result']
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)

    def test_delete_material(self):
        self.test_create_material()  # Ensure material is created before deleting it
        material_id = TestMaterialAPI.created_material_id
        response = requests.delete(f'{self.BASE_URL}/{material_id}', headers=self.HEADERS, data=json.dumps({}))
        result = response.json()['result']
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result.get('status'), 'success')
