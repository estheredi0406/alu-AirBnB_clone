import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.engine.file_storage import FileStorage


class TestBaseModel_save_reload(unittest.TestCase):
    """Tests for the save and reload methods of the BaseModel class."""

    def setUp(self):
        """Set up test fixtures."""
        self.model = BaseModel()
        self.model.name = "Holberton"
        self.model.my_number = 89

    def tearDown(self):
        """Tear down test fixtures."""
        del self.model

    def test_save(self):
        """Test that the save method saves the
        BaseModel instance to a JSON file."""
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test that the reload method loads a
        BaseModel instance from a JSON file."""
        model1 = BaseModel()
        model1.save()
        model1_id = model1.id
        del model1
        storage.reload()

        new_model = storage.all().get(f"BaseModel.{model1_id}")
        self.assertIsNotNone(new_model)
        self.assertEqual(new_model.id, model1_id)

    def test__file_path(self):
        """Test that the file_path
        attribute is a string and the file exists."""
        new_object = FileStorage()
        file_path = new_object.file_path()
        self.assertIsInstance(file_path, str)
        self.assertTrue(os.path.exists(file_path), "File path does not exist")

    def test__objects(self):
        """Test that the objects
        attribute is a dictionary."""
        new_object = FileStorage()
        f = new_object.objects()
        self.assertIsInstance(f, dict)

    def test_all(self):
        """Test that the all method
        returns the __objects attribute."""
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test that the new method adds
        an object to the __objects attribute."""
        storage.new(self.model)
        self.assertIn(f"BaseModel.{self.model.id}", storage.all())

    def test_save_storage(self):
        """Test that the save method of storage
        serializes __objects to the JSON file."""
        storage.new(self.model)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_storage(self):
        """Test that the reload method of storage
        deserializes the JSON file to __objects."""
        storage.new(self.model)
        storage.save()
        storage.reload()
        self.assertIn(f"BaseModel.{self.model.id}", storage.all())
