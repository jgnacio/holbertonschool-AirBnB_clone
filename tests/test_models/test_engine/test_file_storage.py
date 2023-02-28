#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""File for testing the FileStorage class."""

import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def del_old_files():
    try:
        os.remove("recover_objs.json")
    except FileNotFoundError:
        pass


# Delete files and current objects.
del_old_files()

# Global variables
file_storage = FileStorage()
new_bm = BaseModel()


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_all(self):
        """Test all() method."""
        with open("recover_objs.json", "w", encoding="UTF-8 ") as json_file:
            json.dump({}, json_file)
        file_storage.reload()
        self.assertEqual(file_storage.all(), {})
        file_storage.new(new_bm)
        self.assertEqual(file_storage.all(), {
            f"{new_bm.__class__.__name__}.{new_bm.id}": new_bm
        })

    def test_file_path(self):
        """Test __file_path attribue."""
        self.assertTrue(type(file_storage._FileStorage__file_path) is str)

    def test_objects(self):
        """Test __objects attribute."""
        self.assertTrue(type(file_storage._FileStorage__objects) is dict)

    def test_new(self):
        """Test creating a new model obj with new method."""
        file_storage.new(new_bm)
        self.assertEqual(file_storage.all(), {
            f"{new_bm.__class__.__name__}.{new_bm.id}": new_bm
        })

    def testReload(self):
        """Test reloading json file."""
        file_storage.save()
        with open("recover_objs.json", "w", encoding="UTF-8") as json_file:
            json.dump({}, json_file)
        file_storage.reload()
        self.assertEqual(file_storage.all(), {})
        file_storage.new(new_bm)
        file_storage.save()
        file_storage.reload()
        self.assertTrue(len(file_storage.all()) == 1)

    def test_save(self):
        """Test save method to save the objects on json file."""
        update_time = new_bm.updated_at
        file_storage.save()
        new_bm.save()
        BaseModel.save(self)
        self.assertTrue(update_time < new_bm.updated_at)
        with open("recover_objs.json", encoding="UTF-8"):
            pass
        del_old_files()


if __name__ == '__main__':
    unittest.main()
