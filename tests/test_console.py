#!/usr/bin/python3
"""Unittests for console.py.

Unittest class:
    TestHBNBCommand
"""
import os
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        self.assertTrue(self.console.onecmd("quit"))
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF_command(self, mock_stdout):
        self.assertTrue(self.console.onecmd("EOF"))
        self.assertEqual(mock_stdout.getvalue(), "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline_command(self, mock_stdout):
        self.console.onecmd("\n")
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_prompt(self, mock_stdout):
        self.console.cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

if __name__ == '__main__':
    unittest.main()