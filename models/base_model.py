#!/usr/bin/python3
"""This module contains the BaseModel class"""


import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Initialization of the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String representation of the BaseModel class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated_at attribute with the current datetime and save to storage"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dict representation of BaseModel class"""
        return {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
