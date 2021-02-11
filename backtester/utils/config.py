import os
import yaml
from .meta.singleton import Singleton

class Config (metaclass=Singleton):
    def __init__ (self):
        self.__path     = os.path.join (
            os.path.dirname (
                os.path.abspath(os.path.join(__file__ , ".."))),
                'config.yaml'
                )
        with open(self.__path, "r") as stream:
            self.__data = yaml.load(stream, Loader=yaml.CLoader)

    def get (self):
        return self.__data
