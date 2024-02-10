#!/usr/bin/python3

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """City Unittest"""

    def test_atr(self):
        """City Attributes Test"""

        result = City()

        self.assertEqual(result.name, '')
        self.assertEqual(result.state_id, '')

if __name__ == "__main__":
    unittest.main()
