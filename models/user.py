#!/usr/bin/python3
from models.base_model import BaseModel
class User(BaseModel):
    """
    represents a user with email, password, first name, and last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
