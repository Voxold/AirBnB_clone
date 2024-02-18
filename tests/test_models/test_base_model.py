#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):

    def test_output(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_output = (
            f'[BaseModel] ({my_model.id}) '
            f"{{'my_number': 89, 'name': 'My First Model', "
            f"'updated_at': {repr(my_model.updated_at)}, "
            f"'id': '{my_model.id}', "
            f"'created_at': {repr(my_model.created_at)}}}"
        )

        with self.assertLogs() as logs:
            print(my_model)

        self.assertEqual(logs.output, [expected_output])

        my_model.save()
        expected_updated_output = (
            f'[BaseModel] ({my_model.id}) '
            f"{{'my_number': 89, 'name': 'My First Model', "
            f"'updated_at': {repr(my_model.updated_at)}, "
            f"'id': '{my_model.id}', "
            f"'created_at': {repr(my_model.created_at)}}}"
        )

        with self.assertLogs() as logs:
            print(my_model)

        self.assertEqual(logs.output, [expected_updated_output])

if __name__ == '__main__':
    unittest.main()
