#!/usr/bin/python3

form models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel"""

    # Public class attribute
    state_id = ""
    name = ""
