#!/usr/bin/python3
"""Defines unittests for console.py."""
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing the HBNB command interpreter."""

    def test_quit_exits(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_help_quit(self):
        correct = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_create(self):
        correct = "Usage: create <class>\n"
        correct += "Create a new class, print its id, and save it to file.json"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_EOF(self):
        correct = "EOF signal to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(correct, output.getvalue().strip())
