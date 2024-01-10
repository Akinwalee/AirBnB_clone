#!usr/bin/env python3
"""A module that act as a Base class for all other classes \
        in the AirBnB clone package"""

import uuid
import json
import datetime


class BaseModel:
    """Base class for other classes in the AirBnB \
            module"""

    def __init__(self, *args, **kwargs):
        """Initialize instance variabls"""

        date = datetime.datetime
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = date.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = date.now()
            self.updated_at = date.now()

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

        self_dict = self.__dict__
        self_dict["__class__"] = "BaseModel"
        self_dict["updated_at"] = self_dict.get("updated_at").isoformat()
        self_dict["created_at"] = self_dict.get("created_at").isoformat()
        return (self_dict)
