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
        cls_name = parse(arg)[0]
        classes = ["BaseModel"]
        if cls_name is None:
            print("** class name missing **")
        elif cls_name not in classes:
            print("** class doesn't exist **")
        elif cls_name == classes[0]:
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
        """Dispay information about the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Return upon receiving an EOF signal."""
        print("")
        return True

    def help_EOF(self):
        """Display information about EOF signal handling."""
        print("EOF signal to exit the program")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
