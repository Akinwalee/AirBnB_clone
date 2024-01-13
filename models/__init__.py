#!/usr/bin/env python3
"""The init file for the AirBnB package"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
