#!/usr/bin/python3
""" class review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ class review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ super class with the args"""
        super().__init__(**kwargs)
