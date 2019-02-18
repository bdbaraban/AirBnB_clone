#!/usr/bin/python3
"""Defines the User class."""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the User of the HBnB project."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(**kwargs)
