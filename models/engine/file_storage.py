#!/usr/bin/env python3
"""File storage modulle for the AirBnB project"""

import json
import os
from .models_wrapper import to_model


class FileStorage:
    """Class that handles serialization of \
            objects to json string and store in \
            a file, and vice versa"""

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns __object (the dictionary containing all \
                objects in the file storage)"""

        return (FileStorage.__objects)

    def new(self, obj):
        """Creates a new object obj in __objects \
                with key <obj class>.id"""

        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj_dict["__class__"], obj_dict["id"])
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes and saves __object to JSON file \
                __file_path"""
        path = FileStorage.__file_path
        if os.path.exists(path):
            with open("{}".format(path), "r", encoding="utf-8") as f:
                current = json.load(f)
        else:
            current = {}

        current.update(FileStorage.__objects)
        with open("{}".format(FileStorage.__file_path), "w", encoding="utf-8") as f:
            serialized_objects = {key: obj.to_dict() for key, obj in current.items()}
            json.dump(serialized_objects, f)
            # json.dump(current, f)

    def reload(self):
        """Desrializes JSON file __file_path to \
                __objects"""

        path = FileStorage.__file_path
        if os.path.exists(path):
            with open("{}".format(path), "r+", encoding="utf-8") as f:
                if f.read():
                    f.seek(0)
                    # current = json.load(f)
                    # FileStorage.__objects = to_model(current)
                    FileStorage.__objects = json.load(f)

    def get_obj(self):
        """get the private class variables"""
        return (FileStorage.__objects, FileStorage.__file_path)
