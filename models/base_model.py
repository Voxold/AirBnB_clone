#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class for common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initiates the BaseModel with a unique ID \
        and timestamps for creation and updates.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.
        """

        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = \
            self.created_at.isoformat(model_dict.get('created_at'))
        model_dict['updated_at'] = \
            self.updated_at.isoformat(model_dict.get('updated_at'))
        return model_dict
