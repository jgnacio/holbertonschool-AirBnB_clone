
#!/usr/bin/python3
"""
Created on Mon Feb 28 23:08:00 2023.

@authors: jgnacio
@description:
    Class for Review model.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class."""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Initialize a new Review."""
        BaseModel.__init__(self, *args, **kwargs)
