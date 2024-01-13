#!/usr/bin/python3
"""A console model that is the entry point of cmd interpreter."""
import cmd
import shlex
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

    # All classes
    classes = { "BaseModel" : BaseModel,
            "User": User,
            "State" : State,
            "City" : City,
            "Amenity" : Amenity,
            "Place" : Place,
            "Review" : Review
            }
    # list of all methods
    cmd_list = ["all", "create", "count", "destroy", "show", "update"]
    # methods that need id passed
    id_list = ["destoy", "show", "update"]
    #method that dont need id passed
    no_id_list = ["all", "count"]

    prompt = "(hbnb) "

    def do_quit(self, command):
        """Exit the interpreter when ctr+D is presses."""
        return True

    def do_EOF(self, command):
        """Exit the interpreter when EOF or ctr+D is pressed."""
        print()
        return True

    def help_quit(self):
        """Print help message to the end user for help quit cmd."""
        print("Quit command to exit the program")

    def emptyline(self):
        """Doing nothing"""
        pass

    def do_create(self, command):
        """Instantiating a new create method to save in JSON."""
        args = shlex.split(command)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = args[0]
            if obj in self.classes.keys():
                new_instance = self.classes[obj]()
                if new_instance is not None:
                    print("{}".format(new_instance.id))
                    new_instance.save()
                    #if new instance is not create
                else:
                    print("No instance was created")

    def do_show(self, command):
        """print the string rep of an instance based on class name and id."""
        args = shlex.split(command)
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
        args = shlex.split(command)
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
        args = shlex.split(command)
        if not command:
            obj_list = [str(value) for value in storage.all().values()]
            print(obj_list)
            return
        else: 
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                result = [str(value) for key, value in storage.all().items()
                        if key.startswith(args[0] + '.')]
                print(result)


    @staticmethod
    def class_count(class_name):
        """Count the number of classes in an instance."""
        # initialize an empty set to store all unique class names
        class_set = set()

        for instance in storage.all().values():
            class_set.add(instance.__class__.__name__)
        return len(class_set)


    def default(self, line):
        """Overwriting the default method to handle more cases."""
        # split the command with 1st instance of "." [User, all()]
        class_list = line.split(".", 1)
        # split the second command in class_list [all, )]
        command = class_list[1].split("(", 1)
    
        # split the second command in command list with of "("
        class_id = command[1].split(")", 1)


        if len(class_list) < 2 and len(command) < 2:
            print("Uknown syntax:{}".format(line))
            return False
        if class_list[0] not in self.classes and command[0] not in self.cmd_list:
            print("Unknown syntax:{}".format(line))
            return False
        if command[0] in self.no_id_list and not command[1].startswith(")"):
            print("Uknown syntax:{}".format(line))
            return False
        if command[0] in self.id_list and not command[1].endswith(")"):
            print("Uknown syntax: {}".format(line))
            return False

        if command[0] == self.cmd_list[0]:  # all
            self.do_all(class_list[0])
            return

        if command[0] == self.cmd_list[2]:  # count
            print(self.class_count(class_list[0]))
            

        if command[0] == self.cmd_list[4]:  # show
            self.do_show(class_list[0] + " " + class_id[0])

        if command[0] == self.cmd_list[3]:  # destroy
            self.do_destroy(class_list[0] + " " + class_id[0])





    def do_update(self, command):
        """Update an instance based on classname and id by adding/updating attr."""
        arg_list = shlex.split(command)
        if not command:
            print("** class name missing **")

        try:
            class_name = arg_list[0]
            obj_id = arg_list[1]
            attribute_name = arg_list[2]
            attribute_value = " ".join(arg_list[3:])

            key = class_name + "." + obj_id
            obj = storage.all().get(key)

            if not obj:
                raise KeyError
            setattr(obj, attribute_name, attribute_value)
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
