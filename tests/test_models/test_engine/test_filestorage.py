#!/usr/bin/python3
"""
test file for the filestorage class
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import os
import unittest
from datetime import datetime
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class Test_filestorage(unittest.TestCase):
    """
    Testing the filestorage class and it's methods
    """
    def setUp(self):
        """
        create a FileStorage object to be tested
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """
        delete the FileStorage object
        """
        del self.file_storage

    def test_all(self):
        """
        test the all() method
        """
        self.assertIsInstance(self.file_storage.all(), dict)
        # self.assertEqual(self.file_storage.all(),
        # self.file_storage.FileStorage.__objects)

    def test_new(self):
        """
        test the new() method
        """
        # test BaseModel
        new_obj = BaseModel()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)
        # test Amenity
        new_obj = Amenity()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)
        # test City
        new_obj = City()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)
        # test Place
        new_obj = Place()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)
        # test Review
        new_obj = Review()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)
        # test State
        new_obj = State()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)
        # test User
        new_obj = User()
        self.file_storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        new_dict = self.file_storage.all()
        self.assertIn(key, new_dict)

    def test_save_method(self):
        """
        test save method
        """
        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()

        self.file_storage.new(a)
        self.file_storage.new(b)
        self.file_storage.new(c)
        self.file_storage.new(p)
        self.file_storage.new(r)
        self.file_storage.new(s)
        self.file_storage.new(u)

        self.file_storage.save()
        # check if file exists
        self.assertTrue(os.path.exists("file.json"))

        # Test Reload Method
    def test_reload(self):
        """
        test reload method
        """
        a = Amenity()
        b = BaseModel()
        c = City()
        p = Place()
        r = Review()
        s = State()
        u = User()

        self.file_storage.new(a)
        self.file_storage.new(b)
        self.file_storage.new(c)
        self.file_storage.new(p)
        self.file_storage.new(r)
        self.file_storage.new(s)
        self.file_storage.new(u)

        self.file_storage.save()

        self.file_storage.reload()
        object_dict = self.file_storage.all()

        self.assertIn("Amenity." + a.id, object_dict)
        self.assertIn("BaseModel." + b.id, object_dict)
        self.assertIn("City." + c.id, object_dict)
        self.assertIn("Place." + p.id, object_dict)
        self.assertIn("Review." + r.id, object_dict)
        self.assertIn("State." + s.id, object_dict)
        self.assertIn("User." + u.id, object_dict)


if '__name__ ' == '__main__':
    unittest.main()
