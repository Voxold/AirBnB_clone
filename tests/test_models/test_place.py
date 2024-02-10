#!/usr/bin/python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """unittest for Place"""

    def test_attributes(self):
        """Place attributes Test"""

        result = Place()
        self.assertEqual(result.city_id, '')
        self.assertEqual(result.user_id, '')
        self.assertEqual(result.name, '')
        self.assertEqual(result.description, '')
        self.assertEqual(result.number_rooms, 0)
        self.assertEqual(result.number_bathrooms, 0)
        self.assertEqual(result.max_guest, 0)
        self.assertEqual(result.price_by_night, 0)
        self.assertEqual(result.latitude, 0.0)
        self.assertEqual(result.longitude, 0.0)
        self.assertEqual(result.amenity_ids, [])

if __name__ == "__main":
    unittest.main()
