#!/usr/bin/python3
from models.base_model import BaseModel
class Review(BaseModel):
    """
    Represents a review with a place
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
