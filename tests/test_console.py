#!/usr/bin/python3
"""Defines unittests for console.py."""
import sys
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        correct = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_create(self):
        correct = "Usage: create <class>\n        "
        correct += "Create a new class instance and print its id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_EOF(self):
        correct = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_show(self):
        correct = "Usage: show <class> <id>\n        Display the string "
        correct += "representation of a class instance of a given id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_help_show(self):
        correct = "Usage: destroy <class> <id>\n        "
        correct += "Delete a class instance of a given id."
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(correct, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting from the HBNB command interpreter."""

    def test_quit_exits(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))
