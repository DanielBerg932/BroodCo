from itertools import count
import random as rnd
from classes.Brood import MeergranenBrood as meergranen, RozijnenBrood as rozijn, VolkorenBrood as volkoren, WitBrood as wit, ZuurdesemBrood as zuurdes
from classes.Persoon import Koerier, Klant
from classes.Automaat import BroodAutomaat, GroteBroodAutomaat


class BroodCo():
    def __init__(self):
        self.count = 0
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

    def run(self):
        self.printMachineStatus()

    def fillAutomatenList(self):
        for i in range(0, 20):
            self.count += 1
            self.automatenlist.append(BroodAutomaat(self.count))
        self.count = 0
        for i in range(0, 5):
            self.count += 1
            self.automatenlist.append(GroteBroodAutomaat(self.count))

    def bakMoment(self, amount, type):
        if type == "meergranen":
            for i in range(0, amount):
                self.magazijn.append(meergranen())
        elif type == "rozijnen":
            for i in range(0, amount):
                self.magazijn.append(rozijn)
        elif type == "volkoren":
            for i in range(0, amount):
                self.magazijn.append(volkoren)
        elif type == "wit":
            for i in range(0, amount):
                self.magazijn.append(wit)
        elif type == "zuurdesem":
            for i in range(0, amount):
                self.magazijn.append(zuurdes)
        else:
            print("Error")

    def distributeBroodToKoeriers(self):
        for i in range(0, 5):
            self.koeriers.append(Koerier())

        for k in self.koeriers:
            for i in range(0, 300):
                k.storage.append(self.magazijn.pop(
                    rnd.randint(0, len(self.magazijn)-1)))

    def distributeBroodToAutomaten(self):
        for k in self.koeriers:
            self.automatenlist[rnd.randint(0, len(self.automatenlist) - 1)].storage.append(
                k.storage.pop(rnd.randint(0, len(k.storage) - 1)))

    def printMachineStatus(self):
        for i in self.automatenlist:
            print(i)
