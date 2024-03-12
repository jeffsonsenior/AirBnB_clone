#!/usr/bin/python3

"""
this files defines the BaseModel class that serve as base class in this project.
"""
from datetime import datetime
from uuid import uuid4

class BaseModel:
# base class for our model

   def _init_(self,*args, **kwargs):
#  initialize a new instance or deserialized an existing one
      if kwargs == {}:
# initialize if no argument passed
	self.id = str(uuid.uuid4())
	self.created_at = datetime.utcnow()
	self.update_at = datetime.utcnow()
	model.storage.new(self)
	return
# deserializing using keywor arguments
      for key, val in kwargs.items():
         if key == '_class_':
		continue
		self._dict_[key] = val

# convert string representation  of date to datetime
      if 'creat_at' in kwargs:
		self.created_at = datetime.strptime(kwargs['created_at'],'%Y-%m-%dT%H:%M:%S.%f')
      if 'updateed_at' in kwargs:
		self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
   def __str__(self):
	"""overide string rep of self."""
	fmt = "[{}] ({}) {}"
	return fmt.format(type(self).__name, self.id, self.__dict__)
   
   def save(self):
       """ updates the 'updated_at variable,save the instance."""
       self.updated_at = datetime.utcnow()
       models.storage.save()

   def to_dict(self):
      """Return a dict representation of self"""
      #copy objects atribute to dict
      temp = self.__dict__.copy()
      # add class name to dict
      temp['__class__'] = type(self).__name__
      # format the creation of time to a string
      temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
      # format the update time to a string and add it to dict
      temp['updated_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
      #return the resulting dict
      return temp

   @classmethod
   def all(cls):
      """retreve all current instances."""
      return models.storage.find_all(cls.__name__)

   @classmethod
   def coount(cls):
      """the number of all current instances of cls."""
      return len(model.storage.find.all(clls.__name__))
