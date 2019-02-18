#!/usr/bin/python3
"""Defines unittests for models/__init__.py."""
import unittest
import models
from models.engine.file_storage import FileStorage


class Test__init__(unittest.TestCase):
    """Unittests for testing storage setup of __init__py."""

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_storage_file_path_is_file_json(self):
        self.assertEqual(models.storage._FileStorage__file_path, "file.json")

    def test_storage_objects_is_dict(self):
        self.assertEqual(type(models.storage._FileStorage__objects), dict)
