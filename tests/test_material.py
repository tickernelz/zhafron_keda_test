from odoo.exceptions import ValidationError, AccessError
from odoo.tests.common import TransactionCase


class TestMaterialModel(TransactionCase):
    def setUp(self):
        super(TestMaterialModel, self).setUp()
        self.Material = self.env['keda.material']
        self.Supplier = self.env['keda.supplier']
        self.supplier = self.Supplier.create({'name': 'Test Supplier'})

    def test_create_material(self):
        material = self.Material.create(
            {
                'name': 'Test Material',
                'material_code': 'TM001',
                'material_type': 'fabric',
                'material_buy_price': 150.0,
                'supplier_id': self.supplier.id,
            }
        )
        self.assertTrue(material.id)

    def test_create_material_without_required_fields(self):
        with self.assertRaises(ValidationError):
            self.Material.create(
                {
                    'name': 'Test Material',
                    # Missing required fields
                }
            )

    def test_read_material(self):
        material = self.Material.create(
            {
                'name': 'Test Material',
                'material_code': 'TM001',
                'material_type': 'fabric',
                'material_buy_price': 150.0,
                'supplier_id': self.supplier.id,
            }
        )
        read_material = self.Material.browse(material.id)
        self.assertEqual(read_material.name, 'Test Material')

    def test_update_material(self):
        material = self.Material.create(
            {
                'name': 'Test Material',
                'material_code': 'TM001',
                'material_type': 'fabric',
                'material_buy_price': 150.0,
                'supplier_id': self.supplier.id,
            }
        )
        material.write(
            {
                'name': 'Updated Material',
                'material_code': 'TM002',
                'material_type': 'jeans',
                'material_buy_price': 200.0,
            }
        )
        self.assertEqual(material.name, 'Updated Material')

    def test_delete_material(self):
        material = self.Material.create(
            {
                'name': 'Test Material',
                'material_code': 'TM001',
                'material_type': 'fabric',
                'material_buy_price': 150.0,
                'supplier_id': self.supplier.id,
            }
        )
        material_id = material.id
        material.unlink()
        self.assertFalse(self.Material.browse(material_id).exists())

    def test_material_buy_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.Material.create(
                {
                    'name': 'Test Material',
                    'material_code': 'TM001',
                    'material_type': 'fabric',
                    'material_buy_price': 50.0,  # Less than 100, should raise ValidationError
                    'supplier_id': self.supplier.id,
                }
            )

    def test_access_rights(self):
        with self.assertRaises(AccessError):
            self.env['keda.material'].sudo(self.env.ref('base.public_user')).create(
                {
                    'name': 'Test Material',
                    'material_code': 'TM001',
                    'material_type': 'fabric',
                    'material_buy_price': 150.0,
                    'supplier_id': self.supplier.id,
                }
            )
