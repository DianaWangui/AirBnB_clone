#!/usr/bin/python3
from models.base_model import BaseModel
"""
A class that inherits from BaseModel
"""


class Amenity(BaseModel):
    """
    Public class attributes:
    name: empty string
    """
    name: str = ''
