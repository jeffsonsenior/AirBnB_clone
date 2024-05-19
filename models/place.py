#!/usr/bin/python3
from models.base_model import BaseModel
class Place(BaseModel):
    """
    Represents a place with various attributes
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: str = ""
    number_bathrooms: str = ""
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []
