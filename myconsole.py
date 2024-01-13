#!/usr/bin/env python3
"""Defines te entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
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

    def postloop(self):
        pass

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of the BaseModel class"""

        if len(line) == 0:
            print("** class name missing **")
        elif line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def do_show(self, line):
        """Show the dictionary representation of an object \
        by taking the class name and id"""

        #I think there's a problem with your implementation of this function.
        #The you're creating a new instance of BaseModel and printing it's details
        #In contrast, you're supposed to print the details of the instance with 
        #Id supplied from the console. 
        # The expression: "classId != model.instances[id]" will always be true!
        # Because model.id and classId are Ids of two different classes.
        model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()
        
        if len(line_list) == 2:
            class_name = line_list[0]
            class_id = line_list[1]
            if class_name == "BaseModel":
                key = "{}.{}".format(class_name, class_id)
                if key in obj_dict:
                    model = BaseModel(obj_dict[key])
                    print(model)
                else:
                    print("instance does not exist")
        elif len(line_list) == 1:
            print("id is missing")
            if line_list[0] != "BaseModel":
                print("class doesn't exist")
        else:
            print("class name is missing")


    def do_destroy(self, line):
        """Delete an object by class name and object id"""

        model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()

        if len(line_list) >= 2:
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
                #There's a problem with this implementation
                #The del function doesn't accept such expressions
                #del className and classId
                model.save()


    def do_all(self, line):
        """Prints the string representation of all instances \
        based on the class name"""

        #There's a problem with this implementation, similar to the issue
        # I raised with the do_show method.
        # Please check.
        all_list = []
        if line != "BaseModel":
            print("** class doesn't exist **")
        else:
            model = Basemodel()
            all_list.append(model.__str__())
            print(all_list)

    def do_update(self, line):
        """Update instance details based on class name and id"""

        model = BaseModel()
        # Split the arguments into a list
        line_list = line.split()

        if len(line_list) >= 4:
            className = line_list[0]
            classId = line_list[1]
            attributeName = line_list[2]
            attributeValue = line_list[3]

    def do_test(self, line):
        obj_dict = storage.all()
        line_l = line.split()
        class_name = line_l[0]
        class_id = line_l[1]
        key = "{}.{}".format(class_name, class_id)
        if key in obj_dict:
           # model = BaseModel(obj_dict[key])
            print(BaseModel(**obj_dict[key]))

    def do_all(self, line):
        all_dict = storage.all()
        if line != "BaseModel" and line != "":
            print("dn.....")
        else:
            print([str(BaseModel(**all_dict[i])) for i in all_dict.keys()])
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()