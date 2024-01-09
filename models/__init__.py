#!/usr/bin/python3

"""
to create a unique FileStorage
instance for your application
"""
#task 5
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
