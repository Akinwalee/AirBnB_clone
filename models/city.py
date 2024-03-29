#!/usr/bin/python3
"""Defines a class City."""
from .base_model import BaseModel
from .state import State


class City(BaseModel):
    """City class displays information of the city \
            where the house is located."""
    state_id = ""
    name = ""
