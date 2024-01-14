#!/usr/bin/python3
"""Defines a class Review."""
from .base_model import BaseModel


class Review(BaseModel):
    """Review class displays a short review of the house."""
    place_id = ""
    user_id = ""
    text = ""
