#!/usr/bin/python3

import unittest
from models import state

""""
a test module for State class
"""


class Test_state(unittest.TestCase):
    """
    Testing the State class and it's methods
    """

    def setUp(self):
        """
        a setup method that creates a State object to be tested
        It runs before every test
        """
        self.state_obj = state.State()

    def tearDown(self):
        """
        a teardown method that deletes the State object
        It runs after every test
        """
        del self.state_obj

    def test_instantiation(self):
        """
        test that the State object is instantiated correctly
        """
        self.assertIsInstance(self.state_obj, state.State)
        self.assertTrue(hasattr(self.state_obj, 'id'))
        self.assertTrue(hasattr(self.state_obj, 'created_at'))
        self.assertTrue(hasattr(self.state_obj, 'updated_at'))
        self.assertTrue(hasattr(self.state_obj, 'name'))

    def test_str_rep(self):
        """
        tests the __str__ method
        """
        str_state = str(self.state_obj)
        self.assertIn('[State]', str_state)
        self.assertIn('id', str_state)
        self.assertIn('created_at', str_state)
        self.assertIn('updated_at', str_state)
        # self.assertIn('name', str_state)

    def test_to_dict(self):
        """tests the to_dict method"""
        obj_dict = self.state_obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue(obj_dict['__class__'], state.State)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if '__name__' == '__main__':
    unittest.main()
