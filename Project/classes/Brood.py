from abc import ABC, abstractmethod


class Brood():
    weight = 0

    @abstractmethod
    def __init__(self):
        self.weight = 0
        self.timeOfProduction = 0


class KleinBrood (Brood):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.weight = 0.5


class GrootBrood(Brood):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.weight = 1

# speccefieke broden


class MeergranenBrood(GrootBrood):
    def __init__(self):
        super().__init__()


class RozijnenBrood(KleinBrood):
    def __init__(self):
        super().__init__()


class VolkorenBrood (GrootBrood):
    def __init__(self):
        super().__init__()


class WitBrood(GrootBrood):
    def __init__(self):
        super().__init__()


class ZuurdesemBrood(KleinBrood):
    def __init__(self):
        super().__init__()
