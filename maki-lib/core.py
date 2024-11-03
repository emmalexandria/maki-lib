from typing import Type, Union, Tuple
import os
import json
import maki_errors
import util 
import sys
import subprocess

class Deck:
    path: str
    name: str
    id: int
    parent: "Deck | None"
    children: list["Deck"]

    def load_from_directory(self, directory: str):
        if not os.path.isdir(directory) or not os.path.exists(directory):
            raise maki_errors.DirectoryNotExistsError()

        config_path = os.path.join(directory, "deck.json")
        if not os.path.exists(config_path):
            raise maki_errors.DirectoryInvalidError()

        with open(config_path, "r") as config_fd:
            config = json.load(config_fd)
            try:
                self.id = config['id']
                self.name = config['name']
            except:
                raise maki_errors.ConfigurationInvalidError()

        self.path = directory

    def build(self):
        py_files = util.get_files_in_path(self.path, ".py")
        for py_file in py_files:
            result = subprocess.run([sys.executable, py_file]) 

        maki_files = util.get_files_in_path(self.path, ".maki")

class Note:
    pass

class Model:
    path: str
    name: str
    id: int
    children: list["Model"]

    def load_from_directory(self, directory: str):
        if not os.path.isdir(directory) or not os.path.exists(directory):
            raise maki_errors.DirectoryNotExistsError()

        config_path = os.path.join(directory, "model.json")
        if not os.path.exists(config_path):
            raise maki_errors.DirectoryInvalidError()

        with open(config_path, "r") as config_fd:
            config = json.load(config_fd)
            try:
                self.id = config['id']
                self.name = config['name']
            except:
                raise maki_errors.ConfigurationInvalidError()

        self.path = directory





class Project:
    decks: list[Deck]
    models: list[Model]
