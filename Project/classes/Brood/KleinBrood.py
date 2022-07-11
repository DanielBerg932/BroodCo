from abc import abstractmethod
from classes.Brood.Brood import Brood


class KleinBrood (Brood):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.weight = 0.5
