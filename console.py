#!/usr/bin/env python3
"""Defines te entry point of the command interpreter."""
import cmd
from models import base_model


class HBNBCommand(cmd.Cmd):
    """A simple console for manipulating object in the Airbnb project."""

    prompt = "(hbnb)"
    def do_EOF(self, line):
        """Function quits the prgram with EOF."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def postloop(self):
        pass

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it \
                (to the JSON file) and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, line):
        """Prints the string representation of an \
                instance based on the class name and id."""
        model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()

        if line_list >= 2:
            className = line_list[0]
            classId = line_list[-1]

            if len(className) == 0:
                print("** class name missing **")
            elif className != "BaseModel":
                print("** class doesn't exist **")
            elif len(classId) == 0:
                print("** instance id missing **")
            elif classId != model.instances[id]:
                print("** no instance found **")
            else:
                print(model.__str__())


    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
         model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()

        if line_list >= 2:
            className = line_list[0]
            classId = line_list[-1]

            if len(className) == 0:
                print("** class name missing **")
            elif className != "BaseModel":
                print("** class doesn't exist **")
            elif len(classId) == 0:
                print("** instance id missing **")
            elif classId != model.id:
                print("** no instance found **")
            else:
                del className and classId
                model.save()


    def do_all(self, line):
        """ Prints all string representation of all instances \
                based or not on the class name."""
        all_list = []
        if line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = Basemodel()
            all_list.append(model.__str__())
            print(all_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id by \
                adding or updating attribute (save the change into the JSON file)."""
        model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()

        if line_list >= 4:
            className = line_list[0]
            classId = line_list[1]
            attributeName = line_list[2]
            attributeValue = line_list[3]

            if len(className) == 0:
                print("** class name missing **")
            elif className != "BaseModel":
                print("** class doesn't exist **")
            elif len(classId) == 0:
                print("** instance id missing **")
            elif classId != model.id:
                print("** no instance found **")
            elif len(attributeName) == 0:
                print("** attribute name is missing **")
            elif len(attributeValue) == 0:
                print("** value missing **")
            else:
                model.to_dict()
                model.save()











if __name__ == '__main__':
    HBNBCommand().cmdloop()
