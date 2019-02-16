#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        odict = FileStorage.__objects
        ocname = obj.__class__.__name__
        odict["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for i, o in objdict.items():
                    if o["__class__"] == "BaseModel":
                        del o["__class__"]
                        self.new(BaseModel(**o))
                    elif o["__class__"] == "User":
                        del o["__class__"]
                        self.new(User(**o))
                    elif o["__class__"] == "State":
                        del o["__class__"]
                        self.new(State(**o))
                    elif o["__class__"] == "City":
                        del o["__class__"]
                        self.new(City(**o))
                    elif o["__class__"] == "Amenity":
                        del o["__class__"]
                        self.new(Amenity(**o))
                    elif o["__class__"] == "Place":
                        del o["__class__"]
                        self.new(Place(**o))
                    elif o["__class__"] == "Review":
                        del o["__class__"]
                        self.new(Review(**o))
        except FileNotFoundError:
            return
