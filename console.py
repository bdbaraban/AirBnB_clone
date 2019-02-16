#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    argl = split(arg)
    return [i.strip(",") for i in argl]


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argl = arg.split('.')
        command = argl[1].split('(')
        command[1] = command[1].strip(')')
        argdict = {'all': self.do_all,
                   'show': self.do_show, 'destroy': self.do_destroy,
                   'update': self.do_update}
        if command[0] in argdict.keys():
            return argdict[command[0]]("{} {}".format(argl[0], command[1]))
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Create a new BaseModel, print its id, and save it to file.json"""
        arg_tup = parse(arg)
        classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_tup[0])().id)
            storage.save()

    def help_create(self):
        """Dislay information about the create command."""
        print("Usage: create <class>")
        print("Create a new class, print its id, and save it to file.json")

    def do_quit(self, arg):
        """Return upon receiving quit command."""
        return True

    def help_quit(self):
        """Display information about the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Return upon receiving an EOF signal."""
        print("")
        return True

    def help_EOF(self):
        """Display information about EOF signal handling."""
        print("EOF signal to exit the program")

    def do_show(self, arg):
        """Display string representation of an instance w/ class and id info"""
        arg_tup = parse(arg)
        objdict = storage.all()
        classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_tup[0], arg_tup[1])])

    def help_show(self):
        """Display help information for the show command"""
        print("Displays an object's string repr based on the object's id")

    def do_destroy(self, arg):
        """Delete instance based on class name and id updating JSON file"""
        arg_tup = parse(arg)
        objdict = storage.all()
        classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict.keys():
            print("** no instance found**")
        else:
            del objdict["{}.{}".format(arg_tup[0], arg_tup[1])]
            storage.save()

    def help_destroy(self):
        """Display info about destroy command"""
        print("Destroys an object based on its id and updates the JSON file")

    def do_all(self, arg):
        """Display string representations of all instantiated objects"""
        arg_tup = parse(arg)
        classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }
        if len(arg_tup) > 0 and arg_tup[0] not in classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(arg_tup) > 0 and arg_tup[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(arg_tup) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def help_all(self):
        """Display help information for the all command"""
        print("Prints a list of string reprs of all instantiated objects")

    def do_update(self, arg):
        """Updates instance based on id by adding or updating attribute"""
        arg_tup = parse(arg)
        objdict = storage.all()
        classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
        }
        if len(arg_tup) == 0:
            print("** class name is missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict.keys():
            print("** no instance found **")
        elif len(arg_tup) == 2:
            print("** attribute name missing **")
        elif len(arg_tup) == 3:
            print("** value missing **")
        else:
            obj = objdict["{}.{}".format(arg_tup[0], arg_tup[1])]
            if arg_tup[2] in obj.__dict__.keys():
                valtype = type(obj.__dict__[arg_tup[2]])
                obj.__dict__[arg_tup[2]] = valtype(arg_tup[3])
            else:
                obj.__dict__[arg_tup[2]] = arg_tup[3]


if __name__ == "__main__":
    HBNBCommand().cmdloop()
