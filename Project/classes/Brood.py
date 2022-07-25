from abc import ABC, abstractmethod


class Brood():
    weight = 0

    @abstractmethod
    def __init__(self):
        self.weight = 0

    def _type(self):
        return 'BROOD'


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


class MeergranenBrood(GrootBrood):
    def __init__(self):
        super().__init__()

    def _type(self):
        return "MEERGRANENBROOD"


class RozijnenBrood(KleinBrood):
    def __init__(self):
        super().__init__()

    def _type(self):
        return "ROZIJNENBROOD"


class VolkorenBrood (GrootBrood):
    def __init__(self):
        super().__init__()

    def _type(self):
        return "VOLKORENBROOD"


class WitBrood(GrootBrood):
    def __init__(self):
        super().__init__()

    def _type(self):
        return "WITBROOD"


class ZuurdesemBrood(KleinBrood):
    def __init__(self):
        super().__init__()

    def _type(self):
        return "ZUURDESEMBROOD"
