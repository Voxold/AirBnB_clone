#!/usr/bin/python3

import json
import models.base_model import BaseModel
import models.user import User

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    __file_path = "file.json"
    __objects = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
