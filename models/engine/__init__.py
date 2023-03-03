# -*- coding: utf-8 -*-
"""Initalizes the engine module of the package."""

from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity, "City": City,
    "Place": Place, "Review": Review,
    "State": State
}
