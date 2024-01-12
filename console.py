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
        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, line):
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
        all_list = []
        if line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = Basemodel()
            all_list.append(model.__str__())
            print(all_list)











if __name__ == '__main__':
    HBNBCommand().cmdloop()