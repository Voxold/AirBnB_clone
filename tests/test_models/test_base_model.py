#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_id_is_unique(self):
        base_model2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model2.id)

    def test_str_representation(self):
        expected = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected)

    def test_save(self):
        prev_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated_at, self.base_model.updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_contains_expected_keys(self):
        obj_dict = self.base_model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        self.assertCountEqual(obj_dict.keys(), expected_keys)

    def test_to_dict_datetime_format(self):
        obj_dict = self.base_model.to_dict()
        self.assertEqual(
            obj_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(
            obj_dict['updated_at'], self.base_model.updated_at.isoformat())

    def test_to_dict_class_name(self):
        obj_dict = self.base_model.to_dict()
        self.assertEqual(obj_dict['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
