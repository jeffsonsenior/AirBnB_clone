#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models
"""
this the parent class of all classes in this project
"""

class BaseModel:
    """
    the parent class and the base class of AirBnB clone project
    """

    def __init__(self, *args, **kwargs):
        """
        initializing the base model variables:
        uuid4, dates when the class is created or updated.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs.items():
            for k, v in kwargs.items():
                if k == "created_at" or k == " updated_at":
                    self.__dict__[k] = datetime.strtime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.now(self)

    def __str__(self):
        """
        fuction _str_ to return the class name i.d and dictionary
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict___)

    def save(self):
        """
        this is instance methode to 
        update current datetime
        save() function to keep update at time
        and serialize file
        """
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        dictionary() function of basemodel
        to return created dictionary with 
        string format ot times
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
