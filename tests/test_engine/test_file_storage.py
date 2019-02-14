#!/usr/bin/python3
# test_base_model.py
# Brennan D Baraban <375@holbertonschool.com>
# Samie Azad <530@holbertonschool.com>
"""Defines unittests for models/file_storage.py.

Unittest classes:

"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.file_storage import FileStorage
from models import storage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_storage_class(self):
        """test_storage_class method"""
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_all_method(unittest.TestCase):
    """Unittests for testing all method of the FileStorage class."""
    def test_storage_all(self):
        """test_storage_all method"""
        self.assertEqual(type(storage.all()), dict)
    
    def test_storage_new(self, obj):
        """test_storage_new method"""
        bm = BaseModel()
        storage.new(bm)
        self.assertIn(bm, storage.all().values())

    def test_storage_save_reload(self):
        """test_storage_save method"""
        storage.save()
        with open(storage.file_path):
            self.assertEqual(type(storage.reload()), dict)


if __name__ == "__main__":
    unittest.main()
