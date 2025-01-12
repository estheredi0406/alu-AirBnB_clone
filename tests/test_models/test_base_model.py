#!/usr/bin/env python3
"""
creation of a unittest for the base class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
from time import sleep


class TestBasemodel(unittest.TestCase):
    """creation of tester"""
    def test_init(self):
        """function which tests the constructor of the basemodel"""
        a = BaseModel()
        self.assertIsInstance(a.id, str)
        self.assertIsInstance(a.updated_at, datetime)
        self.assertIsInstance(a.updated_at, datetime)

    def test_str_(self):
        """method that tests for the string returned in basemodel"""
        b = BaseModel()
        exp = f"[BaseModel] ({b.id}) {b.__dict__}"
        self.assertEqual(str(b), exp)

    def test_save(self):
        """method that tests for the save method in basemodel"""
        c = BaseModel()
        past = c.updated_at
        sleep(2)
        c.save()
        present = c.updated_at
        self.assertNotEqual(past, present)

    def test_to_dict(self):
        """method that tests for the to_dict method in basemodel"""
        d = BaseModel()
        d_json = d.to_dict()
        self.assertEqual(d_json["id"], d.id)
        self.assertEqual(d_json["created_at"], d.created_at.isoformat())
        self.assertEqual(d_json["updated_at"], d.updated_at.isoformat())
        self.assertEqual(type(d_json["created_at"]), str)
        self.assertEqual(type(d_json["updated_at"]), str)
        self.assertEqual(d_json["__class__"], "BaseModel")


if __name__ == "__main__":
    unittest.main()
