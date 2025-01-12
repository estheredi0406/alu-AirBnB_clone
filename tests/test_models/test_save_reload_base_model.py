import unittest
from models.base_model import BaseModel
from models.engine import storage
import os


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
        """Test that the save method saves the BaseModel instance to a JSON file."""
        self.model.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test that the reload method loads a BaseModel instance from a JSON file."""
        model1 = BaseModel()
        model1.save()
        model1_id = model1.id
        del model1
        storage.reload()
    
        new_model = storage.all().get(f"BaseModel.{model1_id}")
        self.assertIsNotNone(new_model)
        self.assertEqual(new_model.id, model1_id)
