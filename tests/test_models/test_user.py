#!/usr/bin/python3


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """unittest_User"""

    def test_attributes(self):
        """test for User attributes"""

        result = User()

        self.assertEqual(result.email, '')
        self.assertEqual(result.password, '')
        self.assertEqual(result.first_name, '')
        self.assertEqual(result.last_name, '')

if __name__ == "__main__":
    unittest.main()
