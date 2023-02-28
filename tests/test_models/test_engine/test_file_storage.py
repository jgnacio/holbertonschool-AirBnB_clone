#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""File for testing the FileStorage class."""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

# Global variables
file_storage = FileStorage()


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_all(self):
        """Test all() method."""
        self.assertEqual(file_storage.all(), {})
        new_bm = BaseModel()
        self.assertEqual(file_storage.all(), {
            f"{new_bm.__class__.__name__}.{new_bm.id}" : new_bm
        })

    def test_new(self):
        """Test creating a new model obj with new method."""
        new_bm = BaseModel()
        file_storage.new(new_bm)
        self.assertNotEqual(file_storage.all(), {
            f"{new_bm.__class__.__name__}.{new_bm.id}" : new_bm
        })
        

if __name__ == '__main__':
    unittest.main()