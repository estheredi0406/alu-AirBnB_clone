import unittest
from models.base_model import BaseModel
from models import storage
import os
from models.engine.file_storage import FileStorage


class TestBaseModelStorage(unittest.TestCase):
    """Tests for the file_storage.py methods of the FileStorage class."""

    def setUp(self):
        """Set up test fixtures."""
        self.model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test fixtures."""
        del self.model

    def test_storage_save(self):
        """Test that storage.save() correctly saves the BaseModel instance."""
        self.model.save()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, storage.all())

    def test_storage_reload(self):
        """Test that storage.reload()
        correctly reloads the saved BaseModel instance."""
        self.model.save()
        storage.save()
        storage.reload()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, storage.all())

    def test_file(self):
        """Test the case where no file is present."""
        file_path = self.storage.file_path
        if os.path.exists(file_path):
            os.remove(file_path)
        self.storage.reload()
        self.assertNotEqual(len(self.storage.all()), 0)


if __name__ == "__main__":
    unittest.main()
