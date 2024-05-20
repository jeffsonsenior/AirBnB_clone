#!/usr/bin/python3
""" 
Defines the FileStorage class
"""
import json
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from model.amenity import Amenity
from model.review import Review
from model.place import Place
import os.path

class FileStorage:
    """Abstracted storage engine.
    Attributes:
        __file_path (str): json file path
        __objects (dict): dictionary where object will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the objct dict
        provide access to all stored obj
        """
        return FileStorage.__objects
   

    def new(self, obj):
        """
        new object set up with with key
        """
        ocname = obj.__class__.name
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serializes ojct dict into
        Json format and save it to __file_path
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """
        Deserialising the Json file to object
        """

        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.value():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
