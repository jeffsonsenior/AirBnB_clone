#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import unittest
import uuid
import json
import os
import models
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        """ Initializing the BaseModel """
        super().__init__(*args, **kwargs)
        self.name = "BaseModel"
        self.value = BaseModel

    def setUp(self):
        """
        Set up method to prepare each test
        """
        self.model = BaseModel()

    def test_instance(self):
        """
        Test if the created object is an instance of BaseModel
        """
        self.assertIsInstance(self.model, BaseModel)

    def tearDown(self):
        """
        temporary files path
        """
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:

    def test_base_model_docstrings(self):
        """
        test for docstring method
        """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to__dict.__doc__)

    def test_Isinstanceof(self):
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_id(self):
        """
        test if a new id is created
        """
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm.id, bm2.id)

    def test_base_model_str(self):
        bm = BaseModel()
        self.assertEqual(str(bm), "[BaseModel] ({}) {}".format(bm.id, bm.__dict__))

    def test_basemodel_save(self):
        bm = BaseModel()
        created_at = bm.created_at
        bm.save()
        self.assertEqual(bm.created_at, created_at)
        self.assertNotEqual(bm.updated_at, created_at)

    def test_basemodel_to_dict(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assetIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict["id"], bm.id)
        self.assertEqual(bm_dict["created_at"], bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(bm_dict["__class__"], "BaseModel")


if __name__ == '__main__':
    unittest.main()
