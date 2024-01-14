#!/usr/bin/python3
from models.base_model import BaseModel
"""
A class that inherits from BaseModel
"""


class Place(BaseModel):
    """
    Public class attributes:
    city_id: empty string: it will be the City.id
    user_id: empty string: it will be the User.id
    name: empty string
    description: empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list:
    it will be the list of Amenity.id later
    """

    city_id: str = ''
    user_id: str = ''
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids = []
