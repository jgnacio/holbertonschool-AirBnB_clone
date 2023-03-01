
#!/usr/bin/python3
"""
    This module creates the Review Class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)