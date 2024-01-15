#!/usr/bin/python3
"""A console model that is the entry point of cmd interpreter."""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """A command line interpreter class."""
    # All classes
    classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
    # list of all methods
    cmd_list = ["all", "create", "count", "destroy", "show", "update"]
    # methods that need id passed
    id_list = ["destoy", "show", "update"]
    # method that dont need id passed
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
        """Doing nothing."""
        pass

    def do_create(self, command):
        """Instantiate a new create method to save in JSON."""
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

    def do_show(self, command):
        """Print the string rep of an instance based on class name and id."""
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
        if not command:
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
                del storage.all()[key]
                storage.save()

    def do_all(self, command):
        """Print all string rep of all instances based on class name."""
        args = shlex.split(command)
        if not command:
            obj_list = [str(value) for value in storage.all().values()]
            print(obj_list)
            return
        else:
            all_list = []
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for k, value in storage.all().items():
                    if args[0] == type(value).__name__:
                        all_list.append(str(value))
                print(all_list)

    @staticmethod
    def class_count(class_name):
        """Count the number of classes in an instance."""
        instance_count = sum(1 for instance in storage.all().values()
                             if instance.__class__.__name__ == class_name)
        return instance_count

    def default(self, line):
        """Overwrite the default method to handle more cases."""
        # split the command with 1st instance of "." [User, all()]
        class_list = line.split(".", 1)
        if len(class_list) < 2:
            print("Uknown syntax: {}".format(line))
            return False
        # split the second command in class_list [all, )]
        command = class_list[1].split("(", 1)
        if len(command) < 2:
            print("Uknown syntax: {}".format(line))
            return False
        # split the second command in command list with of "("
        class_id = command[1].split(")", 1)

        # variables to handle the update method
        class_name = class_list[0]
        method = command[0]
        args = command[1][:-1]  # getting all args with no paranthesis
        args_list = [arg.strip('\'" ') for arg in args.split(",")]

        if class_name not in self.classes and method not in self.cmd_list:
            print("Unknown syntax:{}".format(line))
            return False
        if method in self.no_id_list and not command[1].startswith(")"):
            print("Uknown syntax:{}".format(line))
            return False
        if method in self.id_list and not command[1].endswith(")"):
            print("Uknown syntax: {}".format(line))
            return False

        elif method == self.cmd_list[0]:  # all
            self.do_all(class_list[0])

        elif method == self.cmd_list[2]:  # count
            print(self.class_count(class_list[0]))

        elif method == self.cmd_list[4]:  # show
            self.do_show(class_list[0] + " " + class_id[0])

        elif method == self.cmd_list[3]:  # destroy
            self.do_destroy(class_list[0] + " " + class_id[0])

        elif method == self.cmd_list[5]:
            self.handle_update(class_name, args_list)
            self.do_update(class_name + " " + " ".join(args_list))
        else:
            print("Unknown syntax: {}".format(line))

    def handle_update(self, class_name, args_list):
        """
        Handle the update command.

        Args:
            class_name (str): The name of the class.
            args_list (list): List of arguments for update command.
        """
        if len(args_list) == 3:
            obj_id, attribute_name, attribute_value = args_list
            key = class_name + "." + obj_id
            obj = storage.all().get(key)
            if obj:
                if hasattr(obj, attribute_name):
                    attr_type = type(getattr(obj, attribute_name))
                    setattr(obj, attribute_name, attr_type(attribute_value))
                    obj.save()

    def do_update(self, command):
        """Update an instance based on clsname & id by adding/updating attr."""
        arg_list = shlex.split(command)
        if not arg_list:
            print("** class name missing **")
            return
        class_name = arg_list[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        obj_id = arg_list[1]

        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        attribute_name = arg_list[2]

        if len(arg_list) < 4:
            print("** value missing **")
            return

        attribute_value = " ".join(arg_list[3:])


        key = class_name + "." + obj_id
        obj = storage.all().get(key)

        if not obj:
            print("** no instance found **")
        else:
            setattr(obj, attribute_name, attribute_value)
            obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
