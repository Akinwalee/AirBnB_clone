#!/usr/bin/env python3
"""Defines te entry point of the command interpreter."""
import cmd
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
                print("** class name doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            print("** class name is missing **")

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
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(line_list) == 1:
            print("** instance id missing **")
        else:
            print("** class name is missing **")

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
            if class_name != "BaseModel":
                print("** class doesn't exist **")
            elif key not in obj_dict:
                print("** no instance found **")
            else:
                model = BaseModel(**obj_dict[key])
                setattr(model, attribute, value)
                print(model.id)
                self.handle_save(model)

    def handle_save(self, model):
        """handles the saving for update"""
        storage.__objects[key] = model

        path = storage.__file_path
        if os.path.exists(path):
            with open("{}".format(path), "r", encoding="utf-8") as f:
                current = json.load(f)
        else:
            current = {}

        current.update(storage.__objects)
        with open("{}".format(path), "w", encoding="utf-8") as f:
            json.dump(current, f)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
