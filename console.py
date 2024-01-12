#!/usr/bin/env python3
"""Defines te entry point of the command interpreter."""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
