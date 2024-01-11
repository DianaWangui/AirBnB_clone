#!/usr/python3

from models.base_model import BaseModel
"""
a class User that inherits from BaseModel
"""

# task 8
class User(BaseModel):
    """
    Public class attributes:
    email: empty string
    password: empty string
    first_name: empty string
    last_name: empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
