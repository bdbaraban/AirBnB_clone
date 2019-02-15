#!/usr/bin/python3
# test_user.py
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_no_args_instantiates(self):
        us = User()
        self.assertEqual(User, type(us))

    def test_id_is_public_str(self):
        us = User()
        self.assertEqual(str, type(us.id))

    def test_created_at_is_public_datetime(self):
        us = User()
        self.assertEqual(datetime, type(us.created_at))

    def test_updated_at_is_public_datetime(self):
        us = User()
        self.assertEqual(datetime, type(us.updated_at))

    def test_two_users_unique_ids(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    def test_two_users_different_created_at(self):
        us1 = User()
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_two_users_different_updated_at(self):
        us1 = User()
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        usstr = us.__str__()
        self.assertIn("[User] (123456)", usstr)
        self.assertIn("'id': '123456'", usstr)
        self.assertIn("'created_at': " + dt_repr, usstr)
        self.assertIn("'updated_at': " + dt_repr, usstr)

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "345")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)


class TestUser_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    def test_one_save(self):
        us = User()
        first_updated_at = us.updated_at
        us.save()
        self.assertLess(first_updated_at, us.updated_at)

    def test_two_saves(self):
        us = BaseModel()
        first_updated_at = us.updated_at
        us.save()
        second_updated_at = us.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        us.save()
        self.assertLess(second_updated_at, us.updated_at)

    def test_save_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.save(1)


class TestUser_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the User class."""

    def test_to_dict_type(self):
        us = User()
        self.assertTrue(dict, type(us.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        us = User()
        self.assertIn("id", us.to_dict())
        self.assertIn("created_at", us.to_dict())
        self.assertIn("updated_at", us.to_dict())
        self.assertIn("__class__", us.to_dict())
        self.assertIn("email", us.to_dict())
        self.assertIn("password", us.to_dict())
        self.assertIn("first_name", us.to_dict())
        self.assertIn("last_name", us.to_dict())

    def test_to_dict_contains_added_attributes(self):
        us = User()
        us.first_name = "Holberton"
        us.my_number = 98
        self.assertEqual("Holberton", us.first_name)
        self.assertIn("my_number", us.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))
        self.assertEqual(str, type(us_dict["email"]))
        self.assertEqual(str, type(us_dict["password"]))
        self.assertEqual(str, type(us_dict["first_name"]))
        self.assertEqual(str, type(us_dict["last_name"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        us = User()
        us.id = "123456"
        us.created_at = us.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            'email': '',
            'password': '',
            'first_name': '',
            'last_name': ''
        }
        self.assertDictEqual(us.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        us = User()
        self.assertNotEqual(us.to_dict(), us.__dict__)

    def test_to_dict_with_arg(self):
        us = User()
        with self.assertRaises(TypeError):
            us.to_dict(1)

if __name__ == "__main__":
    #need this?
    try:
        os.rename("file.json", "tmp")
    except IOError:
        pass
    unittest.main()
    try:
        os.rename("tmp", "file.json")
    except IOError:
        pass
    #need this?
