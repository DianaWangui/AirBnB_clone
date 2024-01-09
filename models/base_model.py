#!/usr/bin/python3
"""A model that defines all common attributes."""
import uuid
from datetime import datetime


class BaseModel:
    """instantiating public instance attributes."""
    def __init__(self, *args, **kwargs):
        """Initialize new instance for BaseModel.
        Args:
            - *args: this will not be used
            - **kwargs: dictionary with key and value args
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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
