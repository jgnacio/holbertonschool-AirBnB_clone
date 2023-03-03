#!/usr/bin/python3
"""
Created on Mon Feb 28 23:08:00 2023.

@authors: jgnacio
@description:
    Class for Place model.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class."""
    name = ''
    description = ''
    number_rooms = 0
    city_id = ''
    user_id = ''
    price_by_night = 0
    max_guest = 0
    number_bathrooms = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """Initialize a new Place."""
        BaseModel.__init__(self, *args, **kwargs)
