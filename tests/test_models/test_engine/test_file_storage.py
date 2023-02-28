#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""File for testing the FileStorage class."""

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from pathlib import Path

# Global variables
file_storage = FileStorage()


def del_old_files():
    try:
        os.remove("recover_objs.json")
    except FileNotFoundError:
        pass


# Setup files and current objects.
del_old_files()


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_file_path(self):
        """ Test for FileStorage __file_path attribute"""
        new_bm = BaseModel()
        file_storage.save()
        __file_path = Path('recover_objs.json')
        assert __file_path.is_file()
        del_old_files()

    def test_objects(self):
        """ Test for FileStorage __objects attribute"""
        new_bm = BaseModel()
        FileStorage.__objects = {
            f"{new_bm.__class__.__name__}.{new_bm.id}": new_bm
        }
        self.assertEqual(file_storage.__objects, {
            f"{new_bm.__class__.__name__}.{new_bm.id}": new_bm
        })

    def test_all(self):
        """Test all() method."""
        self.assertEqual(file_storage.all(), {})
        new_bm = BaseModel()
        self.assertEqual(file_storage.all(), {
            f"{new_bm.__class__.__name__}.{new_bm.id}": new_bm
        })

    def test_new(self):
        """Test creating a new model obj with new method."""
        new_bm = BaseModel()
        new_bm.save()
        file_storage.new(new_bm)
        self.assertNotEqual(file_storage.all(), {
            f"{new_bm.__class__.__name__}.{new_bm.id}": new_bm
        })

    def test_reload(self):
        """Test reload old objects."""
        file_storage.save()
        file_storage.reload()
        self.assertNotEqual(file_storage.all(), {})
        del_old_files()

    def test_save(self):
        """Test save method to save the objects on json file."""
        del_old_files()
        file_storage.save()

        with open("recover_objs.json", encoding="UTF-8"):
            pass
        del_old_files()


if __name__ == '__main__':
    unittest.main()
