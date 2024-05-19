#!usr/bin/env python3
"""
model - city
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    class containing city and state
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Super class with args"""
        super().__init__(**kwargs)

