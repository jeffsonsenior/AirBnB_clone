#!/usr/bin/env python3
"""
medel- state
"""
from model.base_model import BaseModel

class State(BaseModel):
    """
    class containing of state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """super class with args"""
        super().__init__(**kwargs)

