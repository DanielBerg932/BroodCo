class BroodAutomaat():

    def __init__(self):
        self.storage = []
        self.max_brood = 75

    nummer = 0

    @staticmethod
    def addMachineNmr():
        nummer = nummer+1

    def __str__(self):
        string = self.__name__ + self.nummer
        return string

    def startup(self):
        print("Broodautomaat is starting up")

    def addBread(self, brood):
        if len(self.storage) < self.max_brood:
            self.storage.append(brood)
        else:
            print("Broodautomaat is full")

    def removeBread(self):
        if len(self.storage) > 0:
            self.storage.pop()
        else:
            print("Broodautomaat is empty")

    def buyBread(self):
        print("Brood is being bought")
        return self.storage.pop()
