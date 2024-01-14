#!/usr/bin/python3

import unittest
from models import state


class Test_state(unittest.TestCase):
    def setUp(self):
        self.state_obj = state.State()

    def tearDown(self):
        del self.state_obj

    def test_instantiation(self):
        self.assertIsInstance(self.state_obj, state.State)
        self.assertTrue(hasattr(self.state_obj, 'id'))
        self.assertTrue(hasattr(self.state_obj, 'created_at'))
        self.assertTrue(hasattr(self.state_obj, 'updated_at'))
        self.assertTrue(hasattr(self.state_obj, 'name'))

    def test_str_rep(self):
        str_state = str(self.state_obj)
        self.assertIn('[State]', str_state)
        self.assertIn('id', str_state)
        self.assertIn('created_at', str_state)
        self.assertIn('updated_at', str_state)
        # self.assertIn('name', str_state)

    def test_to_dict(self):
        obj_dict = self.state_obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue(obj_dict['__class__'], state.State)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if '__name__' == '__main__':
    unittest.main()
