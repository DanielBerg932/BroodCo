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
        self.klanten = []
        self.magazijn = []
        self.broodTypes = ['ZuurdesemBrood', 'WitBrood',
                           'VolkorenBrood', 'RozijnenBrood', 'MeergranenBrood']
        self.fillAutomatenList()
        self.bakMoment(300, "meergranen")
        self.bakMoment(300, "rozijnen")
        self.bakMoment(300, "volkoren")
        self.bakMoment(300, "wit")
        self.bakMoment(300, "zuurdesem")
        self.distributeBroodToKoeriers()
        self.distributeBroodToAutomaten()
        self.createKlanten(5)

    def start(self):
        self.printMachineStatus()
        self.printClientStatus()

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
            while len(k.storage) > 0:
                self.automatenlist[rnd.randint(0, len(
                    self.automatenlist) - 1)].addBread(k.storage.pop(rnd.randint(0, len(k.storage) - 1)))

    def printMachineStatus(self):
        for i in self.automatenlist:
            print(i)
        print('\n')

    def printClientStatus(self):
        for k in self.klanten:
            print(k)
        print('\n')

    def createKlanten(self, count):
        kCount = 0
        for i in range(count):
            kCount += 1
            self.klanten.append(Klant(kCount))
        for k in self.klanten:
            machine = rnd.randint(0, len(self.automatenlist)-1)
            btype = self.broodTypes[rnd.randint(0, len(self.broodTypes)-1)]
            bread = self.buyBread(machine, btype)
            k.addToStorage(bread, machine)

    def buyBread(self, machineNr, bType):
        return self.automatenlist[machineNr].buyBread(bType)

    def buyBreadInteractive(self):
        klant = int(input("als welke klant wil je brood kopen? "))
        machine = input(
            'uit welke machine wil je kopen, b1 voor BroodAutomaat 1, g1 voor GroteBroodAutomaat 1 enz: ')
        machineNr = 0
        if machine[0] == 'g':
            machineNr = int(machine[1])+20
        elif machine[0] == 'b':
            machineNr = int(machine[1])
        else:
            machineNr = int(machine[1]+machine[2])
        print('welke brood wil je kopen? de opties zijn:')
        for b in self.broodTypes:
            print('\t'+b)
        bType = input('welke wil je kopen? ')
        bread = self.buyBread(machineNr, bType)
        self.klanten[klant-1].addToStorage(bread, machineNr)
