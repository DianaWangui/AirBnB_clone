#!/usr/bin/python3
"""A model that defines all common attributes."""
import uuid
from datetime import datetime
import models  # task 5


class BaseModel:
    """instantiating public instance attributes."""

    def __init__(self, *args, **kwargs):
        """Initialize new instance for BaseModel.

        Args:
            - *args: this will not be used
            - **kwargs: dictionary with key and value args
        """
        f_time = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, f_time))
                    else:
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Print the class_name id and dict in a specified format."""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Update the public instance updated_at with current time."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
