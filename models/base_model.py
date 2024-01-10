#!usr/bin/env python3
"""A module that act as a Base class for all other classes \
        in the AirBnB clone package"""

import uuid
import json
import datetime


class BaseModel:
    """Base class for other classes in the AirBnB \
            module"""
    
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Prints details about the class name \
                object id, and instance variable"""

        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))

    def save(self):
        """Updates the updated_at instance attribute"""

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Generates the dictionary representation of \
                a BaseModel instance (Serializing the class)"""
        self.__dict__["__class__"] = "BaseModel"
        self.__dict__["updated_at"] = self.__dict__.get("updated_at").isoformat()
        self.__dict__["created_at"] = self.__dict__.get("created_at").isoformat()
        return (self.__dict__)
