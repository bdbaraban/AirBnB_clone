#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def parse(arg):
    return tuple(arg.split())


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Create a new BaseModel, print its id, and save it to file.json"""
        arg_tup = parse(arg)
        classes = ["BaseModel"]
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif arg_tup[0] == classes[0]:
            print(BaseModel().id)
            FileStorage().save()

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
        classes = ["BaseModel"]
        objdict = FileStorage()._FileStorage__objects
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_tup[0], arg_tup[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_tup[0], arg_tup[1])].__str__())

    def help_show(self):
        """Displays help information for the show command"""
        print("Displays an object's string representation based on the objects class and id")

    def do_destroy(self, arg):
        """Deletes instance based on class name and id updating JSON file"""
        arg_tup = parse(arg)
        classes = ["BaseModel"]
        if len(arg_tup) == 0:
            print("** class name missing **")
        elif arg_tup[0] not in classes:
            print("** class doesn't exist **")
        elif len(arg_tup) == 1:
            print("** instance id missing **")
        elif 
if __name__ == "__main__":
    HBNBCommand().cmdloop()
