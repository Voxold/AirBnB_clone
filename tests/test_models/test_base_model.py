#!/usr/bin/python3
"""Unittest for BaseModel"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """unittest_BaseModel"""

    def test_types(self):
        """test for types"""

        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 89
        self.assertEqual(obj.name, "My First Model")
        self.assertEqual(obj.my_number, 89)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.name, str)
        self.assertIsInstance(obj.__class__.__name__, str)
        self.assertEqual(obj.__class__.__name__, 'BaseModel')
        self.assertIsInstance(obj.my_number, int)
        pr = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), pr)

        obj_json = obj.to_dict()

        self.assertEqual(obj_json['name'], "My First Model")
        self.assertEqual(obj_json['my_number'], 89)
        self.assertIsInstance(obj_json['id'], str)
        self.assertIsInstance(obj_json['updated_at'], str)
        self.assertIsInstance(obj_json['created_at'], str)
        self.assertIsInstance(obj_json['name'], str)
        self.assertIsInstance(obj_json['__class__'], str)
        self.assertEqual(obj_json['__class__'], 'BaseModel')
        self.assertIsInstance(obj_json['my_number'], int)
        self.assertIsInstance(obj_json, dict)
        self.assertEqual
        (obj_json['updated_at'], datetime.isoformat(obj.updated_at))
        self.assertEqual
        (obj_json['created_at'], datetime.isoformat(obj.created_at))

        update_time = obj.updated_at

        obj.save()

        update_time2 = obj.updated_at
        self.assertNotEqual(update_time, update_time2)

        self.assertNotEqual(obj.updated_at, obj.created_at)

        obj2 = BaseModel()
        self.assertNotEqual(obj.id, obj2.id)
        self.assertNotEqual(obj, obj2)
