#!/usr/bin/python3
"""A console model that is the entry point of cmd interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User #task8
# task10
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """A command line interpreter class."""
    classes = { "BaseModel" : BaseModel,
            "User": User
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
            obj = args[0]
            if obj in self.classes.keys():
                new_instance = self.classes[obj]()
            print("{}".format(new_instance.id))
            new_instance.save()

    def do_show(self, command):
        """print the string rep of an instance based on class name and id."""
        args = command.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, command):
        """Delete an instance based on class name and id."""
        args = command.split()
        if not args:
            print("** class name missing **")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        if len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, command):
        """Prints all string rep of all instances based on class name."""
        args = command.split()
        if not args:
            print([str(value) for key, value in storage.all().items()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            result = [str(value) for key, value in storage.all().items()
                if key.startswith(args[0] + '.')]

            print(result)

    def do_update(self, command):
        """Update an instance based on classname and id by adding/updating attr."""
        arg_list = command.split()
        if not command:
            print("** class name missing **")

        try:
            class_name = arg_list[0]
            obj_id = arg_list[1]
            attribute_name = arg_list[2]
            attribute_value = arg_list[3]

            key = class_name + "." + obj_id
            obj = storage.all().get(key)

            if not obj:
                raise KeyError
            setattr(obj, attribute_name, eval(attribute_value))
            obj.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")



if __name__== '__main__':
    HBNBCommand().cmdloop()
