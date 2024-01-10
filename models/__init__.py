#!/usr/bin/python3

"""
to create a unique FileStorage
instance for your application
"""
# task 5
from .engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
