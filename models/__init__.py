#!/usr/bin/python3
"""
to create a unique FileStorage
instance for your application
"""
# task 5
# from.engine import file_storage
# task 5
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
