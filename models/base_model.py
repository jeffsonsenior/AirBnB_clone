#!/usr/bin/python 3
"""

"""

import uuid
from datetime import datetime

class BaseModel:
	def _init_(self):
		self.id = str(uuid4())

		self.created_at = datetime.utcnow()
		self.updated_at = datetime.utcnow()

	def save(self):
	
"""

"""
		self.updated_at = datetime.utcnow()

	def to_dict(self):
"""

"""
		inst_dict  = self._dict_.copy()
		inst_dict["_class_"] = self._class._name_
		inst_dict["created_at"] = self.created_at.isoformat()
		inst_dict{"updated_at"]= self.updated_at.isoformat()

		return inst_dict

	def _str_(self):
"""

"""
		class_name = self._class_._name_
		return "[{}] ({}) {}".format(class_name, self.id, self._dict_)


