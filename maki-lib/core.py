from typing import Type, Union
import os
import json
import maki_errors

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

class Note:
    pass

class Model:
    path: str
    name: str
    id: int
    parent: "Deck | None"
    children: list["Deck"]

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
    pass
