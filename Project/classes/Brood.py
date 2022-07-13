from abc import ABC, abstractmethod


class Brood():
    weight = 0

    @abstractmethod
    def __init__(self):
        self.weight = 0


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

    def _type(self):
        return "MeergranenBrood"


class RozijnenBrood(KleinBrood):
    def __init__(self):
        super().__init__()

    def _type():
        return "RozijnenBrood"


class VolkorenBrood (GrootBrood):
    def __init__(self):
        super().__init__()

    def _type():
        return "VolkorenBrood"


class WitBrood(GrootBrood):
    def __init__(self):
        super().__init__()

    def _type():
        return "WitBrood"


class ZuurdesemBrood(KleinBrood):
    def __init__(self):
        super().__init__()

    def _type():
        return "ZuurdesemBrood"
