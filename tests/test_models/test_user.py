#!/usr/bin/python3
import unittest
from models import user


class Test_user(unittest.TestCase):
    def setUp(self):
        self.user_obj = user.User()

    def tearDown(self):
        del self.user_obj

    def test_instantiation(self):
        self.assertIsInstance(self.user_obj, user.User)
        self.assertTrue(hasattr(self.user_obj, 'id'))
        self.assertTrue(hasattr(self.user_obj, 'created_at'))
        self.assertTrue(hasattr(self.user_obj, 'updated_at'))
        self.assertTrue(hasattr(self.user_obj, 'email'))
        self.assertTrue(hasattr(self.user_obj, 'password'))
        self.assertTrue(hasattr(self.user_obj, 'first_name'))
        self.assertTrue(hasattr(self.user_obj, 'last_name'))

    def test_str(self):
        str_rep = str(self.user_obj)
        self.assertIsInstance(str_rep, str)
        self.assertEqual(str_rep, self.user_obj.__str__())
        self.assertIn('id', str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        # self.assertIn('email', str_rep)

    def test_to_dict(self):
        obj_dict = self.user_obj.to_dict()
        # self.assertTrue(self.user_obj[__class__], user.User)
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
