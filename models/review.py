#!/usr/bin/python3
"""Defines the Review class."""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new Review.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        super().__init__(**kwargs)
