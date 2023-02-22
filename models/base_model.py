#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 11:55:00 2023.

@authors: jgnacio & Mauro Trenche
@description:
    BaseModel - (class):
        That is the base class for all models
        of the project.

        save - (method):
            Update the last modified time.

        to_dict - (method):
            Return a dictionary representation of the
            instance.
"""

import json
import uuid
from datetime import datetime


class BaseModel:
    """Base class for creating models."""

    def __init__(self, *args, **kwargs):
        """Initialize the model."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Return a human readable string for the model."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update date of the model."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
