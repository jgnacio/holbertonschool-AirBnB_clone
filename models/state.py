
#!/usr/bin/python3
"""
    State Class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ''

    def __init__(self, *args, **kwargs):
        BaseModel.__init__(self, *args, **kwargs)