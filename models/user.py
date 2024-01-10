#!/usr/bin/python3
"""Defines a class User."""
from base_model import BaseModel


class User(BaseModel):
    """User class collects information of the user."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
