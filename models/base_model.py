#!/usr/bin/python3
import uuid
from datetime import datetime
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
      date_format = '%Y-%m-%dT%H:%M:%S.%f'
      if kwargs:
         for key, value in kwargs.items():
            if key != '__class__':
               setattr(self, key, value)
         if "created_at" in kwargs:
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                          date_format)
         if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                          date_format)
      else:
          self.id = str(uuid.uuid4())
          elf.created_at = datetime.now()
          self.updated_at = datetime.now()
          models.storage.new(self)

   def __str__(self):
       """
       fuction _str_ to return the class name i.d and dictionary
      """
       return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

   def save(self):
      """
      this is instance methode to 
      update current datetime
      save() function to keep update at time
      and serialize file
      """

      self.update_at = datetime.now()
      model.storage.save()

   def to_dict(self):
      """
      dictionary() function of basemodel
      to return created dictionary with 
      string format ot times
      """
      dict_obj = self.__dict__.copy()
      dict_obj["created_at"] = self.created_at.isoformat()
      dict_obj["updated_at"] = self.updated_at.isoformat()
      dict_obj["__class__"] = self.__class__.__name__
      return dict_obj
