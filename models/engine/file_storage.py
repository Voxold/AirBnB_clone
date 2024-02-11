#!/usr/bin/python3

import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        s_objects = {}
        for key, obj in self.__objects.items():
            s_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(s_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dicc = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "Place": Place,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Review": Review
                }

        try:
            with open(self.__file_path, 'r') as file:
                s_objects = json.load(file)
                for value in s_objects.values():
                    self.new(dicc[value['__class__']](**value))
        except FileNotFoundError:
            pass
