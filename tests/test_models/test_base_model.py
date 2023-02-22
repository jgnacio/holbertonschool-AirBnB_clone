#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""File for testing the base model class."""

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
        old_update = test.updated_at
        test.save()
        self.assertNotEqual(old_update, test.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        self.assertIsInstance(test.to_dict(), dict)

    def test__str__(self):
        """Test __str__ special method."""
        self.assertEqual(str(test)[:11], "[BaseModel]")


if __name__ == '__main__':
    unittest.main()