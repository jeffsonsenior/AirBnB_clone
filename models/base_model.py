#!/usr/bin/python3

"""
this files defines the BaseModel class that serve as base class in this project.
"""
import models
from datetime import tatetime
from uuid import uuid4

class BaseModel:
""" base class for our model """

   def _init_(self,*args, **kwargs):
""" initialize a new instance or deserialized an existing one"""
      if kwargs == {}:
"""initialize if no argument passed"""
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
      """return a dict representation of self."""
     temp = {**self.__dict__}
     temp['__class__'] = type(self).__name__
     temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
     temp['updated_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
     return temp

   @classmethod
   def all(cls):
      """retreve all current instances."""
      return models.storage.find_all(cls.__name__)

   @classmethod
   def coount(cls):
      """the number of all current instances of cls."""
      return len(model.storage.find.all(clls.__name__))

   @classmethod
   def creat(cls, *args, **kwarg):
      """creat an instance"""
      new_instance = cls(*args, **kwargs):
      return new_instance.id

   @classmethod
   def show(cls, instance_id):
      """retrive an instance using id."""
     return models.storage.find_by_id(cls.__name__, instance_id)

   @classmethod
   def destroy(cls, instance_id):
      """delete an instance by id."""
     return model.storage.delete_by_id(cls.__name__, instance_id)

   @classmethod
   def update(cls, intance_id, *update_args):
      """ 
         update instances as per the arguments provided.

        If update_args has one element and its a dictionary,
        it updates by key-value pairs.Otherwise, it updates based 
        on pairs of arguments representing key-value pairs.
      """
   if not update_args:
      print(** attribute name missing)
      return
   if len(update_arg) == 1 and isinstance(update_args[0], dict):
      update_args = update_args[0].items()
   else:
      update_args = [update_args[:2]]
   for key,value in update_args:
       model.storage.update_one(cls.__name__, instance_id, key value)
 
