from random import random
from classes.Automaat.BroodAutomaat import BroodAutomaat
from classes.Automaat.GroteBroodAutomaa import GroteBroodAutomaat
from classes.Brood import MeergranenBrood as meergranen, RozijnenBrood as rozijn, VolkorenBrood as volkoren, WitBrood as wit, ZuurdesemBrood as zuurdes
from classes.Persoon import Koerier


class BroodCo():
    def __init__(self):
        self.automatenlist = []
        self.koeriers = []
        self.magazijn = []
        self.fillAutomatenList()
        self.bakMoment(300, "meergranen")
        self.bakMoment(300, "rozijnen")
        self.bakMoment(300, "volkoren")
        self.bakMoment(300, "wit")
        self.bakMoment(300, "zuurdesem")
        self.distributeBroodToKoeriers()
        self.distributeBroodToAutomaten()

    def fillAutomatenList(self):
        for i in range(0, 20):
            self.automatenlist.append(BroodAutomaat.__new__())
        for i in range(0, 5):
            self.automatenlist.append(GroteBroodAutomaat.__new__())

    def bakMoment(self, amount, type):
        if type == "meergranen":
            for i in range(0, amount):
                self.magazijn.append(meergranen.__new__())
        elif type == "rozijnen":
            for i in range(0, amount):
                self.magazijn.append(rozijn.__new__())
        elif type == "volkoren":
            for i in range(0, amount):
                self.magazijn.append(volkoren.__new__())
        elif type == "wit":
            for i in range(0, amount):
                self.magazijn.append(wit.__new__())
        elif type == "zuurdesem":
            for i in range(0, amount):
                self.magazijn.append(zuurdes.__new__())
        else:
            print("Error")

    def distributeBroodToKoeriers(self):
        for i in range(0, 5):
            self.koeriers.append(Koerier.__new__())

        for k in self.koeriers:
            for i in range(0, 300):
                k.storage.append(self.magazijn.pop(random.randint(0, 1500)))

    def distributeBroodToAutomaten(self):
        for k in self.koeriers:
            self.automatenlist[random.randint(0, len(self.automatenlist) - 1)].storage.append(
                k.storage.pop(random.randint(0, len(k.storage) - 1)))
