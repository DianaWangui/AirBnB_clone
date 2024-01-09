#!/usr/bin/python3
"""A model that defines all common attributes."""
import uuid
from datetime import datetime


class BaseModel:
    """instantiating public instance attributes."""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __str__(self):
        """ print the class_name id and dict in a specified format."""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update the public instance updated_at with current time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing all keys/values of __dict__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
