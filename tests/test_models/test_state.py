#!/usr/bin/python3

import unittest
from models.state import state


class TestState(unittest.TestCase):
    """State Test"""

    def test_atr(self):
        """State Attribytes Test"""

        result = State()
        self.assertEqual(result.name, '')


if __name__ == "__main":
    unittest.main()
