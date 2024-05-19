#!/bin/env python3
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
    __file_path = "file.path"
    __objects = {}
    def __init__(self):
        """Initialize methode"""
        pass

    def all(self):
        """
        Returns the objct dict
        provide access to all stored obj
        """
        self.reload()
        return self.__objects


    def save(self):
        """
        Serializes ojct dict into
        Json format and save it to __file_path
        """
        new_dict = {}
        for key, value in self._objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        Deserialising the Json file to object
        """

        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, "r") as f:
                    for key, value in json.load(f).items():
                        self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            return
        except json.JSONDedeError:
            return

    def delete(self, obj=None):
        """
        deleting obj from __objects if present
        """
        if obj is None:
            return
        if obj in self.__objects:
            del self.__objects[obj]
        self.save()       

    def update(self, obj, k, v):
        """
        updating obj withk:v as attributes
        """
        if obj in self.__objects:
           setattr(self.__objects[obj], k, eval(v))
        self.save()

    def getid(self, obj):
        """
        Return the id obj
        """
        if obj in self.__objects:
            return self.__objects[obj].id
