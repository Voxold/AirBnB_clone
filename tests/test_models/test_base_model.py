#!/usr/bin/python3
"""Unittest for base model"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """test class BaseModel"""

    base = BaseModel()
    base.name = "My First Model"
    base.my_number = 89

    def test_create_instance_without_kwargs(self):
        """create an instance of class without kwargs"""

        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.assertIsInstance(self.base.created_at, datetime)
        self.assertIsInstance(self.base.updated_at, datetime)
        self.assertEqual(self.base.name, "My First Model")
        self.assertEqual(self.base.my_number, 89)

    def test_create_instance_with_kwargs(self):

        my_base_json = self.base.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertEqual(new_base.name, "My First Model")
        self.assertEqual(new_base.my_number, 89)
        self.assertNotEqual(new_base, self.base)
        self.assertDictEqual(new_base.__dict__, self.base.__dict__)

    def test_to_dict(self):
        """Test to_dict class method"""

        to_dict_returned_dict = self.base.to_dict()
        expected_dic = self.base.__dict__.copy()
        expected_dic["__class__"] = self.base.__class__.__name__
        expected_dic["updated_at"] = self.base.updated_at.isoformat()
        expected_dic["created_at"] = self.base.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)

    def test_save(self):
        """Test _save class method"""

        before_update_time = self.base.updated_at
        self.base.my_number = 90
        self.base.save()
        after_update_time = self.base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)

    def test_str(self):
        """Test STR Method"""
        
        n = self.base.__class__.__name__
        expected_str = f"[{n}] ({self.base.id}) <{self.base.__dict__}>"
        self.assertEqual(self.base.__str__(), expected_str)

if __name__ == '__main__':
    unittest.main()
