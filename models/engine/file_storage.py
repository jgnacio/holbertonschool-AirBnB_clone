#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:33:00 2023.

@authors: jgnacio & Mauro Trenche
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
        ] = obj.to_dict()

    def save(self):
        """Save the model to the path file."""
        if FileStorage.__objects:
            with open(
                FileStorage.__file_path, "w", encoding="UTF-8"
            ) as json_file:
                json_file.write(json.dumps(FileStorage.__objects, indent=4))

    def reload(self):
        """Reload the model from the path."""
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as json_file:
                print(json_file.read())
                json_file.seek(0)
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
