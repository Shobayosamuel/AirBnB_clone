#!/usr/bin/python3
"""Define a Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    state class
    """
    city.id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
