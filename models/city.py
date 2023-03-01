#!/usr/bin/python3
"""
    City Class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    name = ''
    state_id = ''

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)