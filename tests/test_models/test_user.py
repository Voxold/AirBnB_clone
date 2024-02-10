#!/usr/bin/python3


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """User Unittest"""

    def test_atr(self):
        """User attributes Test"""

        result = User()

        self.assertEqual(result.email, '')
        self.assertEqual(result.password, '')
        self.assertEqual(result.first_name, '')
        self.assertEqual(result.last_name, '')

if __name__ == "__main__":
    unittest.main()
