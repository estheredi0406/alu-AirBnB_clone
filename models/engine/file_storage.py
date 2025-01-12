import json
from models.base_model import BaseModel
import models


class FileStorage:
    """Serializes instances to
    a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def file_path(self):
        """Getter for __file_path."""
        return self.__file_path
    
    def objects(self):
        """Getter for __objects."""
        return self.__objects

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict()
                       for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)."""
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
                for key, value in objects.items():
                    self.__objects[key] = \
                        self.classes()[value["__class__"]](**value)
        except FileNotFoundError:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        return {
            "BaseModel": BaseModel,
        }
