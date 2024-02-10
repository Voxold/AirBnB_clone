#!/usr/bin/python3

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Review Unittest"""

    def test_atr(self):
        """Review Attributes Test"""

        result = Review()

        self.assertEqual(result.place_id, '')
        self.assertEqual(result.user_id, '')
        self.assertEqual(result.text, '')

if __name__ == "__main__":
    unittest.main()
