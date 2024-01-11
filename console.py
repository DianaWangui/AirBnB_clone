#!/usr/bin/python3
"""A console model that is the entry point of cmd interpreter."""
import cmd
from models.base_model import BaseModel
from models.user import User #task8


class HBNBCommand(cmd.Cmd):
    """A command line interpreter class."""

    prompt = "(hbnb)"

    def do_quit(self, command):
        """Exit the interpreter when ctr+D is presses."""
        return True

    def do_EOF(self, command):
        """Exit the interpreter when EOF or ctr+D is pressed."""
        return True

    def help_quit(self):
        """Print help message to the end user for help quit cmd."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Doing nothing"""
        pass

    def do_create(self, command):
        """Instantiating a new create method to save in JSON."""
        self.object = arg[0]
        if self.object is None:
            print("**class name missind **")
        elif


if __name__ == '__main__':
    HBNBCommand().cmdloop()
