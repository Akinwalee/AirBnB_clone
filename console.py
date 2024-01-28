#!/usr/bin/env python3
"""Defines te entry point of the command interpreter."""
import cmd
import os
import json
import datetime
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """A simple console for manipulating object in the Airbnb project."""

    prompt = "(hbnb) "
    classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            ]
    date = datetime.datetime

    def do_EOF(self, line):
        """Function quits the prgram with EOF."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """Makes the console execute nothing when nothing is typed."""
        pass

    def do_create(self, line):
        """Creates a new instance of the BaseModel class"""

        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            if line == "BaseModel":
                model = BaseModel()
            elif line == "User":
                model = User()
            elif line == "State":
                model = State()
            elif line == "City":
                model = City()
            elif line == "Amenity":
                model = Amenity()
            elif line == "Place":
                model = Place()
            else:
                model = Review()
            print(model.id)
            model.save()

    def do_show(self, line):
        """Show the dictionary representation of an object \
        by taking the class name and id"""
        obj_list = storage.all()
        # Split the arguments into a list
        line_list = line.split()

        if len(line_list) == 2:
            class_name = line_list[0]
            class_id = line_list[1]

            if class_name in self.classes:
                key = "{}.{}".format(class_name, class_id)
                if key in obj_list:
                    if class_name == "BaseModel":
                        model = BaseModel(**obj_list[key])
                    elif class_name == "User":
                        model = User(**obj_list[key])
                    elif class_name == "State":
                        model = State(**obj_list[key])
                    elif class_name == "City":
                        model = City(**obj_list[key])
                    elif class_name == "Amenity":
                        model = Amenity(**obj_list[key])
                    elif class_name == "Place":
                        model = Place(**obj_list[key])
                    else:
                        model = Review(**obj_list[key])
                    print(model)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """Delete an object by class name and object id"""
        obj_list = storage.all()
        # Split the arguments into a list
        line_list = line.split()

        if len(line_list) == 2:
            class_name = line_list[0]
            class_id = line_list[1]
            if class_name in self.classes:
                key = "{}.{}".format(class_name, class_id)
                if key in obj_list:
                    del obj_list[key]
                    self.save_destroy()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints the string representation of all instances \
        based on the class name"""
        obj_dict = storage.all()
        if line not in self.classes and line != "":
            print("** class doesn't exist **")
        else:
            all_list = []
            for key in obj_dict.keys():
                if "BaseModel" in key:
                    all_list.append(str(BaseModel(**obj_dict[key])))
                elif "User" in key:
                    all_list.append(str(User(**obj_dict[key])))
                elif "State" in key:
                    all_list.append(str(State(**obj_dict[key])))
                elif "City" in key:
                    all_list.append(str(City(**obj_dict[key])))
                elif "Place" in key:
                    all_list.append(str(Place(**obj_dict[key])))
                elif "Amenity" in key:
                    all_list.append(str(Amenity(**obj_dict[key])))
                else:
                    all_list.append(str(Review(**obj_dict[key])))
            print(all_list)

    def do_update(self, line):
        """Update instance details based on class name and id"""

        obj_dict = storage.all()
        # Split the arguments into a list
        line_list = line.split()

        if len(line_list) == 0:
            print("** class name missing **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        elif len(line_list) == 2:
            print("** attribute name missing **")
        elif len(line_list) == 3:
            print("** value missing **")
        else:
            class_name = line_list[0]
            class_id = line_list[1]
            attribute = line_list[2]
            value = eval(line_list[3])
            key = "{}.{}".format(class_name, class_id)
            if class_name in self.classes:
                key = "{}.{}".format(class_name, class_id)
                if key in obj_dict:
                    if class_name == "BaseModel":
                        model = BaseModel(**obj_dict[key])
                    elif class_name == "User":
                        model = User(**obj_dict[key])
                    elif class_name == "State":
                        model = State(**obj_dict[key])
                    elif class_name == "City":
                        model = City(**obj_dict[key])
                    elif class_name == "Amenity":
                        model = Amenity(**obj_dict[key])
                    elif class_name == "Place":
                        model = Place(**obj_dict[key])
                    else:
                        model = Review(**obj_dict[key])
                    setattr(model, attribute, value)
                    model.updated_at = self.date.now()
                    self.handle_save(model, key)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def handle_save(self, model, key):
        """handles the saving for update"""

        obj, path = storage.get_obj()
        obj[key] = model.to_dict()

        if os.path.exists(path):
            with open("{}".format(path), "r", encoding="utf-8") as f:
                current = json.load(f)
        else:
            current = {}

        current.update(obj)
        with open("{}".format(path), "w", encoding="utf-8") as f:
            json.dump(current, f)

    def save_destroy(self):
        """handles saving after destroy"""

        obj, path = storage.get_obj()
        with open("{}".format(path), "w", encoding="utf-8") as f:
            json.dump(obj, f)
    
    def default(self, line):
        """Handles other function usage"""
    
        line_list = line.split(".")
        
        class_name, method = line_list
        
        if method == "all()":
            print(f"[{', '.join(self.c_all(class_name))}]")
        if method == "count()":
            print(len(self.c_all(class_name)))
            
        if method.startswith("show") or method.startswith("destroy"):
            match = re.search(r'"(.+)"', method)
            id = match.group(1)
            arg = class_name + " " + id
            if method.startswith("show"):
                self.do_show(arg)
            else:
                self.do_destroy(arg)
    

    def c_all(self, class_name):
        """Handles alternative all call"""

        obj_dict = storage.all()
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        all_list = []
        for key, value in obj_dict.items():
            if key.startswith(class_name):
                all_list.append(str(classes[class_name](**value)))
        return (all_list)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
