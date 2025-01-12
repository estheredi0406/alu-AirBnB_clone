#!/usr/bin/python3
"""This module contains the BaseModel class"""


import uuid
from datetime import datetime


class BaseModel:
    def _init_(self, *args, **kwargs):
        """Initialization of the BaseModel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "_class_":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def _str_(self):
        """String representation of the BaseModel class"""
        return f"[{self._class.name}] ({self.id}) {self.dict_}"

    def save(self):
        """
        Update the updated_at
        attribute with the current datetime and save to storage
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns the dict representation of BaseModel class"""
        dictionary = self._dict_.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
