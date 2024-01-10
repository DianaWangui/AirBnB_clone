#!/usr/bin/python3

"""
a class that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import os
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Private class attributes:
    __file_path: path to the JSON file
    __objects: dictionary - empty but will store all objects
    """
    __filepath = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary object
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        # convert object to JSON
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
            # Write JSON string to file
        with open(self.__filepath, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        # Create an empty dictionary
        if os.path.exists(self.__filepath):
            # Open the JSON file and load the data into the dictionary
            with open(self.__filepath, "r") as f:
                json_objects = json.load(f)
                # update __objects
            self.__objects = json_objects
