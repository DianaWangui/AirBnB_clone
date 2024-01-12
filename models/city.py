#!/usr/bin/python3
from models.base_model import BaseModel
"""
A class that inherits from BaseModel
"""


class City(BaseModel):
    """
    Public class attributes:
    state_id: empty string: it will be the State.id
    name: empty string
    """
    state_id: str = ''
    name: str = ''
