#!/usr/bin/python3
# test_base_model.py
# Brennan D Baraban <375@holbertonschool.com>
# Samie Azad <530@holbertonschool.com>
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        bm = BaseModel()
        self.assertEqual(BaseModel, type(bm))

    def test_id_is_public_str(self):
        bm = BaseModel()
        self.assertEqual(str, type(bm.id))

    def test_created_at_is_public_datetime(self):
        bm = BaseModel()
        self.assertEqual(datetime, type(bm.created_at))

    def test_updated_at_is_public_datetime(self):
        bm = BaseModel()
        self.assertEqual(datetime, type(bm.updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        tuuid = "123456"
        bm1 = BaseModel()
        bm1.id = tuuid
        bm1.created_at = datetime.min
        bm1.updated_at = datetime.min
        output = "[BaseModel] (123456)"
        bstr = bm1.__str__()
        self.assertIn(output, bstr)
        self.assertIn("'id': '123456'", bstr)
        self.assertIn("'created_at': datetime.datetime(1, 1, 1, 0, 0)", bstr)
        self.assertIn("'updated_at': datetime.datetime(1, 1, 1, 0, 0)", bstr)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    def test_one_save(self):
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(1)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 98
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(str, type(bm_dict["created_at"]))
        self.assertEqual(str, type(bm_dict["updated_at"]))

    def test_to_dict_output(self):
        tuuid = "123456"
        bm = BaseModel()
        bm.id = tuuid
        bm.created_at = datetime.min
        bm.updated_at = datetime.min
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': datetime.min.isoformat(),
            'updated_at': datetime.min.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(1)


if __name__ == "__main__":
    unittest.main()
