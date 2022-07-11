from abc import abstractclassmethod, abstractmethod
from classes.Brood.Brood import Brood


class GrootBrood(Brood):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.weight = 1
