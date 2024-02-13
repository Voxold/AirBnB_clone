#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel"""

    def setUp(self):
        """Set up a BaseModel instance for testing"""
        self.obj = BaseModel()
        self.obj.name = "My First Model"
        self.obj.my_number = 89

    def test_attributes(self):
        """Test attributes types and values"""

        self.assertEqual(self.obj.name, "My First Model")
        self.assertEqual(self.obj.my_number, 89)

        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.updated_at, datetime)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.name, str)
        self.assertIsInstance(self.obj.__class__.__name__, str)
        self.assertEqual(self.obj.__class__.__name__, 'BaseModel')
        self.assertIsInstance(self.obj.my_number, int)

    def test_str_representation(self):
        """Test __str__ representation"""

        expected_str = f"[{self.obj.__class__.__name__}]\
        ({self.obj.id}) {self.obj.__dict__}"
        self.assertEqual(str(self.obj), expected_str)

    def test_to_dict(self):
        """Test to_dict method"""

        obj_json = self.obj.to_dict()
