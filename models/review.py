#!/usr/bin/python3
from models.base_model import BaseModel
"""
A class that inherits from BaseModel
"""


class Review(BaseModel):
    """
    Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """

    place_id: str = ''
    user_id: str = ''
    text: str = ''
