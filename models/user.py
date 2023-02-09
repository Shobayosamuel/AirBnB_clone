#!/usr/bin/python3
"""Create a User class"""
from models import BaseModel


class User(BaseModel):
    """
    user model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
