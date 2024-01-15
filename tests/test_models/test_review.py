#!/usr/bin/python3
import unittest
from models import review


class Test_city(unittest.TestCase):
    def setUp(self):
        self.review_obj = review.Review()

    def tearDown(self):
        del self.review_obj

    def test_instantiation(self):
        self.assertIsInstance(self.review_obj, review.Review)
        self.assertTrue(hasattr(self.review_obj, 'id'))
        self.assertTrue(hasattr(self.review_obj, 'created_at'))
        self.assertTrue(hasattr(self.review_obj, 'updated_at'))
        self.assertTrue(hasattr(self.review_obj, 'text'))
        self.assertTrue(hasattr(self.review_obj, 'place_id'))
        self.assertTrue(hasattr(self.review_obj, 'user_id'))

    def str_rep(self):
        str_rep = str(self.review_obj)
        self.assertIn('id', str_rep)
        self.assertIn(self.review_obj, str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        self.assertIn('text', str_rep)
        self.assertIn('place_id', str_rep)
        self.assertIn('user_id', str_rep)

    def to_dict(self):
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
