from abc import ABC, abstractmethod


class Brood():
    @abstractmethod
    def __init__(self):
        self.weight = 0
        self.timeOfProduction = 0
