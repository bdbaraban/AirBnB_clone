#!/usr/bin/python3
"""Defines unittests for console.py."""
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import create_autospec
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    @classmethod
    def create(self):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    @classmethod
    def setUp(self):
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_quit_exits(self):
        HBnB = self.create()
        self.assertTrue(HBnB.onecmd("quit"))

    def test_help_quit(self):
        HBnB = self.create()
        correct = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBnB.onecmd("help quit"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_create(self):
        HBnB = self.create()
        correct = "Usage: create <class>\n"
        correct += "Create a new class, print its id, and save it to file.json"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBnB.onecmd("help create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_EOF(self):
        HBnB = self.create()
        correct = "EOF signal to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBnB.onecmd("help EOF"))
            self.assertEqual(correct, output.getvalue().strip())
