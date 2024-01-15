#!/usr/python3

from models.base_model import BaseModel
"""
a class User that inherits from BaseModel
"""


class User(BaseModel):
    """
    Public class attributes:
    email: empty string
    password: empty string
    first_name: empty string
    last_name: empty string
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
