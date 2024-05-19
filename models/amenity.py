#!/usr/bin/python3

"""
amenity class
"""

from models.base_model import BaseModel

class Amenity(BaseModel):

    name = ""

    def __init___(self, *args, **kwargs):
        """
        calling super class with args
        """
        super().__init__(**kwargs) 

