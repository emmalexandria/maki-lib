from enum import Enum

class BuildError(Exception):
    error_msg: str
    problem_in_file: str 

class DirectoryNotExistsError(Exception):
    pass

class DirectoryInvalidError(Exception):
    pass

class ConfigurationInvalidError(Exception):
    pass
