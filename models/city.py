#!/usr/bin/python3
from models.base_model import BaseModel
class City(BaseModel):
    """
    Represents a city with a state id and a name
    """
    state_id: str = ""
    name: str = ""
