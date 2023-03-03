#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:33:00 2023.

@authors: jgnacio
@description:
    This module provides a simple implementation of json objects
    serialization and deserialization functions to get the application
    persistence.

    (class) - FileStorage:
        Is the main storage manager for json files.

        ClassAttributes:
            __file_path: The path to the json file
            __objects: Dictionary of objects to be serialized

        (method) - all():
            Get all objects in the dictionary and return them

        (method) - new(obj):
            Make or update a entry in the dictionary object of current program.

        (method) - save():
            Serialize the dictionary object and save it to __file_path, if
            not already exists create a new file.

        (method) - reload():
            Open the file in __file_path and then sets the new dict objects in
            the old dictionary.
"""

import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """File Storage manager class."""

    __file_path = "recover_objs.json"
    __objects = {}

    def all(self):
        """Return all objects in the current program."""
        return FileStorage.__objects

    def new(self, obj):
        """Add/update entries."""
        FileStorage.__objects[
            f"{obj.__class__.__name__}.{obj.id}"
        ] = obj

    def save(self):
        """Save the model to the path file."""
        all_objs = self.all()
        to_dump = {key: value.to_dict() for key, value in all_objs.items()}
        with open(
            FileStorage.__file_path, 'w', encoding='UTF-8'
        ) as json_file:
            json.dump(to_dump, json_file, indent=4)

    def reload(self):
        """Reload the model from the path."""
        classes = {"BaseModel": BaseModel, "User": User,
                   "Amenity": Amenity, "City": City,
                   "Place": Place, "Review": Review,
                   "State": State}

        try:
            with open(
                FileStorage.__file_path, 'r', encoding='utf-8'
            ) as json_file:
                loaded = json.load(json_file)

            for key, value in loaded.items():
                cls_name = value.get('__class__')
                if cls_name in classes.keys():
                    my_cls = classes.get(cls_name)
                    loaded[key] = my_cls(**value)
            FileStorage.__objects = loaded

        except FileNotFoundError:
            pass
