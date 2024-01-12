#!/usr/bin/env python3
"""File storage modulle for the AirBnB project"""

import json
import os


class FileStorage:
    """Class that handles serialization of \
            objects to json string and store in \
            a file, and vice versa"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns __object (the dictionary containing all \
                objects in the file storage)"""

        return (self.__objects)

    def new(self, obj):
        """Creates a new object obj in __objects \
                with key <obj class>.id"""

        obj.to_dict()
        obj_dict = obj.__dict__
        key = "{}.{}".format(obj_dict["__class__"], obj_dict["id"])
        self.__objects[key] = obj_dict

    def save(self):
        """Serializes and saves __object to JSON file \
                __file_path"""

        with open("{}".format(self.__file_path), "w", encoding="utf-8") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """Desrializes JSON file __file_path to \
                __objects"""

        if os.path.exists(self.__file_path):
            with open("{}".format(self.__file_path), "r", encoding="utf-8") as f:
                if f.read():
                    f.seek(0)
                    self.__objects = json.load(f)
