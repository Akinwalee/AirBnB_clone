#!/usr/bin/env python3
"""A module that act as a Base class for all other classes \
        in the AirBnB clone package"""

import uuid
import json
import datetime
import re
from .__init__ import storage


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
                        if isinstance(val, str):
                            val = date.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = date.now()
            self.updated_at = date.now()
            storage.new(self)

    def __str__(self):
        """Prints details about the class name \
                object id, and instance variable"""

        class_name = self.get_class()
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """Updates the updated_at instance attribute"""

        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Generates the dictionary representation of \
                a BaseModel instance (Serializing the class)"""
        
        self_dict = self.__dict__.copy()
        self_dict["__class__"] = self.get_class()
        self_dict["updated_at"] = self_dict["updated_at"].isoformat()
        self_dict["created_at"] = self_dict["created_at"].isoformat()
        return (self_dict)

    def get_class(self):
        """"handler to get class name"""
        
        classes = {
                "base_model": "BaseModel",
                "user": "User",
                "state": "State",
                "city": "City",
                "amenity": "Amenity",
                "place": "Place",
                "review": "Review"
                }
        class_str = str(self.__class__)
        match = re.search(r"\.(\w+)", class_str)
        class_name = match.group(1)
        if class_name in classes:
            return (classes[class_name])
