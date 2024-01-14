#!/usr/bin/env python3
"""Defines te entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """A simple console for manipulating object in the Airbnb project."""

    prompt = "(hbnb)"
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
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
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

            if class_name == "BaseModel":
                key = "{}.{}".format(class_name, class_id)
                if key in obj_list:
                    model = BaseModel(**obj_list[key])
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
        model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()

        if len(line_list) == 2:
            class_name = line_list[0]
            class_id = line_list[1]
            if class_name == "BaseModel":
                key = "{}.{}".format(class_name, class_id)
                if key in obj_list:
                    #model = BaseModel(**obj_list[key])
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
        if line != "BaseModel" and line != "":
            print("** class doesn't exist **")
        else:
            print([str(BaseModel(**obj_dict[i])) for i in obj_dict.keys()])

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
            value_s = line_list[3]
            key = "{}.{}".format(class_name, class_id)
            if class_name != "BaseModel":
                print("** class doesn't exist ")
            elif key not in obj_dict:
                print("** no instance found")
            else:
                model = BaseModel(**obj_dict[key])
                value = eval(value_s)
                setattr(model, attribute, value)
                model.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
