#!/usr/bin/python3
import unittest
from models import amenity


class test_Amenity(unittest.TestCase):
    def setUp(self):
        self.amenity1 = amenity.Amenity()

    def tearDown(self):
        del self.amenity1

    def test_instantiation(self):
        self.assertIsInstance(self.amenity1, amenity.Amenity)
        self.assertTrue(hasattr(self.amenity1, 'id'))
        self.assertTrue(hasattr(self.amenity1, 'created_at'))
        self.assertTrue(hasattr(self.amenity1, 'updated_at'))
        self.assertTrue(hasattr(self.amenity1, 'name'))

    def str_rep(self):
        str_rep = str(self.amenity1)
        self.assertIn('id', str_rep)
        self.assertIn(self.amenity1, str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        self.assertIn('name', str_rep)

    def to_dict(self):
        obj_dict = self.amenity1.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if '__name__' == '__main__':
    unittest.main()
