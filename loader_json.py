from importlib.resources import path
from pydoc import importfile


import json

class JSONLoader:
    def __call__(self, path_of_file):
        with open(path_of_file, 'r') as file:
            return json.load(file)