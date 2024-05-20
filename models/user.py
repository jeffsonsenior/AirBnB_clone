#!/usr/bin/env python3
"""
model-user
"""

from model.base_model import BaseModel

class User(BaseModel):
    """
    Different attributes of user
    email(str): user email
    password(str):user password
    first_name(str): first name
    last_name(str): name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
