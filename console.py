#!/usr/bin/python3
"""A console model that is the entry point of cmd interpreter."""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """A command line interpreter class."""
    classes = { "BaseModel" : BaseModel
            }

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
        args = command.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg[0]]()
            new_instance.save()
            print(new_instance.id)

if __name__== '__main__':
    HBNBCommand().cmdloop()
