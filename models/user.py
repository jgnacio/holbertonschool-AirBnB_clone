#!/usr/bin/python3
"""
Created on Mon Feb 28 23:08:00 2023.

@authors: jgnacio
@description:
    Class for User model.
"""


from models.base_model import BaseModel


class User(BaseModel):
    """User class."""

    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        BaseModel.__init__(self, *args, **kwargs)
