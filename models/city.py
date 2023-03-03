#!/usr/bin/python3
"""
Created on Mon Feb 28 23:08:00 2023.

@authors: jgnacio
@description:
    Class for City model.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class."""
    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new city."""
        BaseModel.__init__(self, *args, **kwargs)
