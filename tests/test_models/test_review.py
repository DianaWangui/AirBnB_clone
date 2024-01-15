#!/usr/bin/python3
import unittest
from models import review

""""
a test module for Review class
"""


class Test_review(unittest.TestCase):
    """
    Testing the Review class and it's methods
    """

    def setUp(self):
        """
        a setup method that creates a Review object to be tested
        It runs before every test
        """
        self.review_obj = review.Review()

    def tearDown(self):
        """
        a teardown method that deletes the Review object
        It runs after every test
        """
        del self.review_obj

    def test_instantiation(self):
        """
        test that the Review object is instantiated correctly
        """
        self.assertIsInstance(self.review_obj, review.Review)
        self.assertTrue(hasattr(self.review_obj, 'id'))
        self.assertTrue(hasattr(self.review_obj, 'created_at'))
        self.assertTrue(hasattr(self.review_obj, 'updated_at'))
        self.assertTrue(hasattr(self.review_obj, 'text'))
        self.assertTrue(hasattr(self.review_obj, 'place_id'))
        self.assertTrue(hasattr(self.review_obj, 'user_id'))

    def str_rep(self):
        """tests the __str__ method"""
        str_rep = str(self.review_obj)
        self.assertIn('id', str_rep)
        self.assertIn(self.review_obj, str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        self.assertIn('text', str_rep)
        self.assertIn('place_id', str_rep)
        self.assertIn('user_id', str_rep)

    def to_dict(self):
        """tests the to_dict method"""
        obj_dict = self.review_obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertTrue(self.review_obj[__class__], review.Review)
        self.assertIn('id', obj_dict)
        self.assertIn('text', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('place_id', obj_dict)
        self.assertIn('user_id', obj_dict)


if '__name__' == '__main__':
    unittest.main()
