import json
from models.base_model import BaseModel
import models
import os


class FileStorage:
    """Serializes instances to
    a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        """Getter for __file_path."""
        return self.__file_path

    @property    
    def objects(self):
        """Getter for __objects."""
        return self.__objects

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict()
                       for key, obj in FileStorage.__objects.items()}, f)
        # print(f"File saved to {self.__file_path}")
        # print(f"File exists: {os.path.exists(self.__file_path)}")

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)."""
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    FileStorage.__objects[key] = \
                        self.classes()[value["__class__"]](**value)
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        return {
            "BaseModel": BaseModel,
        }
