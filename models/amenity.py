#!/usr/bin/python3
"""Defines the Amenity class."""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Amenity.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(**kwargs)
