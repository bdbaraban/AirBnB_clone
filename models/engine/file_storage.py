#!/usr/bin/python3
"""file_storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all method"""
        return FileStorage.__objects

    def new(self, obj):
        """new method"""
        odict = FileStorage.__objects
        ocname = obj.__class__.__name__
        odict["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """save method"""
        objdict = {}
        for i, o in FileStorage.__objects.items():
            objdict[i] = o.to_dict()
        with open(FileStorage.__file_path, "w+") as f:
            json.dump(objdict, f)

    def reload(self):
        """reload method"""
        try:
            objl = []
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for i, o in objdict.items():
                    objdict[i] = BaseModel(**o)
            FileStorage.__objects = objdict
        except FileNotFoundError:
            return
