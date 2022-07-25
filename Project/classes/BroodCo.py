from itertools import count
import random as rnd
from classes.Brood import MeergranenBrood as meergranen, RozijnenBrood as rozijn, VolkorenBrood as volkoren, WitBrood as wit, ZuurdesemBrood as zuurdes
from classes.Persoon import Courier, Client
from classes.Automaat import BroodAutomaat, GroteBroodAutomaat


class BroodCo():
    def __init__(self):
        self.count = 0
        self.automatenlist = []
        self.couriers = []
        self.clients = []
        self.storage = []
        self.breadTypes = ['ZuurdesemBrood', 'WitBrood',
                           'VolkorenBrood', 'RozijnenBrood', 'MeergranenBrood']
        self.fillAutomatenList()
        self.bakMoment(300, "meergranen")
        self.bakMoment(300, "rozijnen")
        self.bakMoment(300, "volkoren")
        self.bakMoment(300, "wit")
        self.bakMoment(300, "zuurdesem")
        self.distributeBroodToCouriers()
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
                self.storage.append(meergranen())
        elif type == "rozijnen":
            for i in range(0, amount):
                self.storage.append(rozijn())
        elif type == "volkoren":
            for i in range(0, amount):
                self.storage.append(volkoren())
        elif type == "wit":
            for i in range(0, amount):
                self.storage.append(wit())
        elif type == "zuurdesem":
            for i in range(0, amount):
                self.storage.append(zuurdes())
        else:
            print("Error")

    def distributeBroodToCouriers(self):
        for i in range(0, 5):
            self.couriers.append(Courier())

        for k in self.couriers:
            for i in range(0, 300):
                k.storage.append(self.storage.pop(
                    rnd.randint(0, len(self.storage)-1)))

    def distributeBroodToAutomaten(self):
        for k in self.couriers:
            while len(k.storage) > 0:
                self.automatenlist[rnd.randint(0, len(
                    self.automatenlist) - 1)].addBread(k.storage.pop(rnd.randint(0, len(k.storage) - 1)))

    def printMachineStatus(self):
        for i in self.automatenlist:
            print(i)
        print('\n')

    def printClientStatus(self):
        for k in self.clients:
            print(k)
        print('\n')

    def createKlanten(self, count):
        kCount = 0
        for i in range(count):
            kCount += 1
            self.clients.append(Client(kCount))
        for klant in self.clients:
            machine = rnd.randint(0, len(self.automatenlist)-1)
            btype = self.breadTypes[rnd.randint(
                0, len(self.breadTypes)-1)].upper()
            bread = self.buyBread(machine, btype)
            klant.addToStorage(bread, machine+1)

    def buyBread(self, machineNr, bType):
        return self.automatenlist[machineNr].buyBread(bType)

    def buyBreadInteractive(self):
        client = int(input("als welke client wil je brood kopen? "))
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
        for b in self.breadTypes:
            print('\t'+b)
        bType = input('welke wil je kopen? ').upper()
        bread = self.buyBread(machineNr, bType)
        self.clients[client-1].addToStorage(bread, machineNr)
