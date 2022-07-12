class BroodAutomaat():

    #nummer = 0

    def __init__(self):
        self.storage = []
        self.max_brood = 75

    # @staticmethod
    # def addMachineNmr():
        #nummer = nummer+1

    def __str__(self):
        string = type(self).__name__
        return string

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


class GroteBroodAutomaat(BroodAutomaat):
    def __init__(self) -> None:
        super().__init__()
        self.max_brood = 105
