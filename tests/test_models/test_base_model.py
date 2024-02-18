#!/usr/bin/python3

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Unittests for testing of the BaseModel class"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        Base1 = BaseModel()
        Base2 = BaseModel()
        self.assertNotEqual(Base1.id, Base2.id)

    def test_two_models_different_created_at(self):
        Base1 = BaseModel()
        sleep(0.05)
        Base2 = BaseModel()
        self.assertLess(Base1.created_at, Base2.created_at)

    def test_two_models_different_updated_at(self):
        Base1 = BaseModel()
        sleep(0.05)
        Base2 = BaseModel()
        self.assertLess(Base1.updated_at, Base2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        Dic = repr(date)
        Base = BaseModel()
        Base.id = "123456"
        Base.created_at = Base.updated_at = date
        BaseStr = Base.__str__()
        self.assertIn("[BaseModel] (123456)", BaseStr)
        self.assertIn("'id': '123456'", BaseStr)
        self.assertIn("'created_at': " + Dic, BaseStr)
        self.assertIn("'updated_at': " + Dic, BaseStr)

    def test_args_unused(self):
        Base = BaseModel(None)
        self.assertNotIn(None, Base.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        Base = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Base.id, "345")
        self.assertEqual(Base.created_at, date)
        self.assertEqual(Base.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        Base = BaseModel("12", id="345", \
                created_at=date_iso, updated_at=date_iso)
        self.assertEqual(Base.id, "345")
        self.assertEqual(Base.created_at, date)
        self.assertEqual(Base.updated_at, date)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        Base = BaseModel()
        sleep(0.05)
        first_updated_at = Base.updated_at
        Base.save()
        self.assertLess(first_updated_at, Base.updated_at)

    def test_two_saves(self):
        Base = BaseModel()
        sleep(0.05)
        first_updated_at = Base.updated_at
        Base.save()
        second_updated_at = Base.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        Base.save()
        self.assertLess(second_updated_at, Base.updated_at)

    def test_save_with_arg(self):
        Base = BaseModel()
        with self.assertRaises(TypeError):
            Base.save(None)

    def test_save_updates_file(self):
        Base = BaseModel()
        Base.save()
        Baseid = "BaseModel." + Base.id
        with open("file.json", "r") as f:
            self.assertIn(Baseid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method"""

    def test_to_dict_type(self):
        Base = BaseModel()
        self.assertTrue(dict, type(Base.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        Base = BaseModel()
        self.assertIn("id", Base.to_dict())
        self.assertIn("created_at", Base.to_dict())
        self.assertIn("updated_at", Base.to_dict())
        self.assertIn("__class__", Base.to_dict())

    def test_to_dict_contains_added_attributes(self):
        Base = BaseModel()
        Base.name = "Holberton"
        Base.my_number = 98
        self.assertIn("name", Base.to_dict())
        self.assertIn("my_number", Base.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        Base = BaseModel()
        Base_dict = Base.to_dict()
        self.assertEqual(str, type(Base_dict["created_at"]))
        self.assertEqual(str, type(Base_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        Base = BaseModel()
        Base.id = "123456"
        Base.created_at = Base.updated_at = date
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat()
        }
        self.assertDictEqual(Base.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        Base = BaseModel()
        self.assertNotEqual(Base.to_dict(), Base.__dict__)

    def test_to_dict_with_arg(self):
        Base = BaseModel()
        with self.assertRaises(TypeError):
            Base.to_dict(None)


if __name__ == "__main__":
    unittest.main()
