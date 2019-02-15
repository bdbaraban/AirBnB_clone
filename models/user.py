#!/usr/bin/python3
"""Defines the User class."""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the User of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new User.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(**kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        models.storage.new(self)
