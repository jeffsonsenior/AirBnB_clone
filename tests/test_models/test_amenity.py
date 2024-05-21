#!/usr/bin/python3
"""Defines unittests for amenity.py
Unittest classes:
    TestAmenity_instatiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instatiation(unittest.TestCase):
    """Unittests for testing instatiation of Amenity class"""
    def test_no_args_instatiates(self):
        # It checks if the class if class is the same type as instance
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        # It checks if the class is stored
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        # It checks that the id is a string
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        # It checks if the type of the created_at attribute is datetime
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        # It checks if the type updated_at attribute is datetime
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        # We are creating a new class called Amenity
        # Creating a new instance of Amenity called am
        # Checking that the type of the name attribute is a string
        # Checking that the name of the attribute is in the Amenity class
        # Checking that the name attribute is not in the am instance
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        # we create two instances of the amenity class
        # check that the id of each instance is different
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        # create an instance of amenity
        # wait for 0.05 seconds
        # we check that the first instance was created
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_t(self):
        # check for the updated_attribute of the first instance
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        # create dattime object and store it in dt
        # create a string representation of dt
        # create an amenity object and store it in am
        # set the id attribute to "123456"
        # set the created_at and updated_at attributes of am to dt
        # create a string representation of am and store it
        # check the string representation
        dt = datetime.today()
        dt_repr = repr(dt)
        a = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenty] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        # create a new instance of Amenity
        # check the instances
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instatiation_with_kwargs(self):
        """instatiation with kwargs test method"""
        # import datetime module from the datetime library
        # create datetime object using the datetime.today() method
        # covert datetime object to a string using isoformat
        # create n Amenity object with the id "345" and the datetime
        # check that created_at and updated_at are datetime objects
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instatiation_with_None_kwargs(self):
        # import unittest model
        # import the class to be tested
        # create a class that inherits from unittest.TestCase
        # create a method called test_upper
        # self.assertRaises checks if the result raises a TypeError
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """Unittests for testing save method of Amenity class"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        # create a new instance
        # save current time
        # save instance of the amenity
        # compare current time wiht updated_at  attribute
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        # create new instance of amenity
        # save it to database
        # update instance with new data
        # save it to the database again
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, am.updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """unitests for testing to_dict method"""
    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()i
