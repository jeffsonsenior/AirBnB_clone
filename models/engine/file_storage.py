#!/bin/env python3
""" 
Defines the FileStorage class
"""
import json
from medels.base_model import BaseModel
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from model.amenity import Amenity
from model.review import Review
from model.place import Place

class FileStorage:
    __file_path = "file.path"
    __objects = {}

    def all(self):
        returm FileStorage.__objects

    def save(self):
        with open(FileStorage.__filePath,
                  mode="w",
                  encoding+"utf-8") as f:
            json_str = json.dumps(FileStore._objects,
                                  default=     
