#!/usr/bin/python3


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittest for Amenity file"""

    def test_attributes(self):
        """Test for Amenity attributes"""

        result = Amenity()
        self.assertEqual(result.name, '')


if __name__ == "__main__":
    unittest.main()