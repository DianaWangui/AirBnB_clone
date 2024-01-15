#!/usr/bin/python3
import unittest
from models import place

""""
a test module for Place class
"""


class Test_place(unittest.TestCase):
    """
    Testing the Place class and it's methods
    """

    def setUp(self):
        """
        a setup method that creates a Place object to be tested
        It runs before every test
        """
        self.place_obj = place.Place()

    def tearDown(self):
        """
        a teardown method that deletes the Place object
        It runs after every test
        """
        del self.place_obj

    def test_instantiation(self):
        """
        test that the Place object is instantiated correctly
        """
        self.assertIsInstance(self.place_obj, place.Place)
        self.assertTrue(hasattr(self.place_obj, 'id'))
        self.assertTrue(hasattr(self.place_obj, 'created_at'))
        self.assertTrue(hasattr(self.place_obj, 'updated_at'))
        self.assertTrue(hasattr(self.place_obj, 'name'))
        self.assertTrue(hasattr(self.place_obj, 'city_id'))
        self.assertTrue(hasattr(self.place_obj, 'user_id'))
        self.assertTrue(hasattr(self.place_obj, 'description'))
        self.assertTrue(hasattr(self.place_obj, 'number_rooms'))
        self.assertTrue(hasattr(self.place_obj, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place_obj, 'max_guest'))
        self.assertTrue(hasattr(self.place_obj, 'price_by_night'))
        self.assertTrue(hasattr(self.place_obj, 'latitude'))
        self.assertTrue(hasattr(self.place_obj, 'longitude'))
        self.assertTrue(hasattr(self.place_obj, 'amenity_ids'))

    def str_rep(self):
        """
        tests the __str__ method
        """
        str_rep = str(self.place_obj)
        self.assertIn('id', str_rep)
        self.assertIn(self.place_obj, str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        self.assertIn('name', str_rep)
        self.assertIn('description', str_rep)
        self.assertIn('number_rooms', str_rep)
        self.assertIn('max_guests', str_rep)
        self.assertIn('number_bathrooms', str_rep)
        self.assertIn('price_by_night', str_rep)
        self.assertIn('latitude', str_rep)
        self.assertIn('longitude', str_rep)
        self.assertIn('amenity_ids', str_rep)

    def to_dict(self):
        """tests the to_dict method"""
        obj_dict = self.place_obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('description', obj_dict)
        self.assertIn('number_rooms', obj_dict)
        self.assertIn('max_guests', obj_dict)
        self.assertIn('number_bathrooms', obj_dict)
        self.assertIn('price_by_night', obj_dict)
        self.assertIn('latitude', obj_dict)
        self.assertIn('longitude', obj_dict)
        self.assertIn('amenity_ids', obj_dict)


if '__name__' == '__main__':
    unittest.main()
