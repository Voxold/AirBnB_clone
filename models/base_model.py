#!/usr/bin/python3
"""initialization, serialization and deserialization"""

import datetime
import uuid


class BaseModel:
    """class BaseModel that defines all common \
    attributes/methods for other classes"""

    def __init__(self) -> None:
        """Public instance attributes"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """should print..."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the public instance attribute """

        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values"""

        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = \
            datetime.isoformat(dictionary.get('created_at'))
        dictionary['updated_at'] = \
            datetime.isoformat(dictionary.get('updated_at'))
        return dictionary
