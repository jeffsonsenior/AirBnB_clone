#!/usr/bin/python3
from models.base_model import BaseModel
class Amenity(BaseModel):
    """
    Represents an amenity with a name
    """
    name: str = ""
