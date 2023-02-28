#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""File for testing the BaseModel class."""

import os
import json
import unittest
from models.base_model import BaseModel

# Global variables
test = BaseModel()


class Tests(unittest.TestCase):
    """Test the base model class."""

    def test_id(self):
        """Test the id attribute."""
        test_dict = {}
        # Create a multiple instances of the base model
        for index in range(1, 101):
            test_dict[f"model{index}"] = BaseModel()
        # Check the id attribute for each model
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.id, test_dict.get(
                f"model{index + 1}", test).id
            )

    def test_created_at(self):
        """Test create_at attribute."""
        test_dict = {}
        for index in range(1, 20):
            test_dict[f"model{index}"] = BaseModel()
        for index, value in enumerate(test_dict.values(), 1):
            self.assertNotEqual(value.created_at, test_dict.get(
                f"model{index + 1}", test).created_at
            )

    def test_save(self):
        """Test saving the model."""
        with open("recover_objs.json", "w", encoding="UTF-8") as json_file:
            json.dump({}, json_file)
        test.save()
        with open("recover_objs.json", encoding="UTF-8"):
            pass

    def test_to_dict(self):
        """Test to_dict method."""
        test_dict = test.to_dict()

    def test__str__(self):
        """Test __str__ special method."""
        self.assertEqual(str(test)[:11], "[BaseModel]")

    def test_json_deserializing(self):
        test_new_model = test.to_dict()
        new_model = BaseModel(**test_new_model)
        self.assertIsInstance(new_model, BaseModel)


if __name__ == '__main__':
    unittest.main()
    try:
        os.remove("recover_objs.json")
    except FileNotFoundError:
        pass
