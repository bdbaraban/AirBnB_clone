#!/usr/bin/python3
# test_file_storage.py
# Brennan D Baraban <375@holbertonschool.com>
# Samie Azad <530@holbertonschool.com>
"""Defines unittests for models/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""
    def setUp(self):
        """setUp method for TestBaseModel"""
        _FileStorage__file_path = "testfile.json"

    @classmethod
    def tearDown(self):
        """tearDown method for TestBaseModel"""
        try:
            _FileStorage__file_path = "testfile.json"
            os.remove(_FileStorage__file_path)
            _FileStorage__file_path = "file.json"
        except IOError:
            pass

    def test_storage_class(self):
        """test_storage_class method"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing all method of the FileStorage class."""
    def setUp(self):
        """setUp method for TestBaseModel"""
        _FileStorage__file_path = "testfile.json"

    @classmethod
    def tearDown(self):
        """tearDown method for TestBaseModel"""
        try:
            _FileStorage__file_path = "testfile.json"
            os.remove(_FileStorage__file_path)
            _FileStorage__file_path = "file.json"
        except IOError:
            pass

    def test_storage_all(self):
        """test_storage_all method"""
        self.assertEqual(type(models.storage.all()), dict)

    def test_storage_new(self, obj):
        """test_storage_new method"""
        bm = BaseModel()
        storage.new(bm)
        self.assertIn(bm, models.storage.all().values())

    def test_storage_save_reload(self):
        """test_storage_save method"""
        storage.save()
        with open(storage.file_path):
            self.assertEqual(type(models.storage.reload()), dict)


if __name__ == "__main__":
    unittest.main()
