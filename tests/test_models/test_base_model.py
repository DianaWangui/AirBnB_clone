#!/usr/bin/python3
"""
a test for the BaseModel class
"""
import unittest
from datetime import datetime
import models
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """
    Testing the BaseModel class and it's methods
    """
    def setUp(self):
        """
        a setup method that creates a Basemodel object to be tested
        It runs before every test
        """
        self.base_model = BaseModel()

    def tearDown(self):
        """
        a teardown method that deletes the BaseModel object
        It runs after every test
        """
        del self.base_model

    def test_instantiation(self):
        """
        test that the BaseModel object is instantiated correctly
        """
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id(self):
        """
        tests the id attribute
        """
        self.assertTrue(self.base_model.id, str)

    def test_created_at(self):
        """
        tests the created_at attribute
        """
        self.assertTrue(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """
        tests the updated_at attribute
        """
        self.assertTrue(self.base_model.updated_at, datetime)

    def test_str(self):
        """
        test the __str__ method
        """
        self.assertTrue(self.base_model.__str__(), str)
        self.assertEqual(str(self.base_model), self.base_model.__str__())

    def test_save_method(self):

        init_time = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(init_time, self.base_model.updated_at)

    def test_to_dict(self):
        """
        tests the to_dict method
        """
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        # self.assertIn(self.base_model.__class__.__name__, model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')


if '__name__ ' == '__main__':
    unittest.main()
