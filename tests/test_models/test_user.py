#!/usr/bin/python3
import unittest
from models import user

""""
a test module for User class
"""


class Test_user(unittest.TestCase):
    """
    Testing the User class and it's methods
    """

    def setUp(self):
        """
        a setup method that creates a User object to be tested
        It runs before every test
        """
        self.user_obj = user.User()

    def tearDown(self):
        """
        a teardown method that deletes the User object
        It runs after every test
        """
        del self.user_obj

    def test_instantiation(self):
        """
        test that the User object is instantiated correctly
        """
        self.assertIsInstance(self.user_obj, user.User)
        self.assertTrue(hasattr(self.user_obj, 'id'))
        self.assertTrue(hasattr(self.user_obj, 'created_at'))
        self.assertTrue(hasattr(self.user_obj, 'updated_at'))
        self.assertTrue(hasattr(self.user_obj, 'email'))
        self.assertTrue(hasattr(self.user_obj, 'password'))
        self.assertTrue(hasattr(self.user_obj, 'first_name'))
        self.assertTrue(hasattr(self.user_obj, 'last_name'))

    def test_str(self):
        """
        tests the __str__ method
        """
        str_rep = str(self.user_obj)
        self.assertIsInstance(str_rep, str)
        self.assertEqual(str_rep, self.user_obj.__str__())
        self.assertIn('id', str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        # self.assertIn('email', str_rep)

    def test_to_dict(self):
        """tests the to_dict method"""
        obj_dict = self.user_obj.to_dict()
        # self.assertTrue(self.user_obj[__class__], user.User)
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
