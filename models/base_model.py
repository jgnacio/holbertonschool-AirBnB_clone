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

import uuid
from datetime import datetime


class BaseModel:
    """Base class for creating models."""

    def __init__(self):
        """Initialize the model."""
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.id = str(uuid.uuid4())

    def __str__(self):
        """Return a human readable string for the model."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update date of the model."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
