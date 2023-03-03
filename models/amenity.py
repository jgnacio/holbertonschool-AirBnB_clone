#!/usr/bin/python3
"""
Created on Mon Feb 28 23:08:00 2023.

@authors: jgnacio
@description:
    Class for Amenity model.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class."""

    name = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity."""
        BaseModel.__init__(self, *args, **kwargs)
