#!/usr/bin/env python3
"""Module for the Places class"""

from base_model import BaseModel


class Places(BaseModel):
    """Places class, inheriting from the \
            BaseModel class. Holds information \
            listed places in the HBnB project"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_id = [""]
