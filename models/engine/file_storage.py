#!/usr/bin/python3
"""Define a class FileStorage"""
import json
import os


class FileStorage:
    """The class serializes and deserializes JSON files"""

    def __init__(self):
        """initialize the base class"""
        __file_path = "file.json"
        __objects = {}

    def all(self):
        """
        Return the dictionary __object
        """
        return (self.__objects)

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to json file
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fil:
            d_store = {}
            for k, v in self.__objects.items():
                d_store[k] = v.to_dict()
            json.dumps(d_store, fil)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist
        , no exception should be raised)
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
