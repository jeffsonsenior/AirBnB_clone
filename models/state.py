#!/usr/bin/python3
from models.base_model import BaseModel
class State(BaseModel):
    """
    Represents a state with a name
    """
    name: str = ""
