class BroodAutomaat():

    nummer = 0

    def __init__(self, count):
        self.storage = []
        self.max_brood = 75
        self.count = count

    def __str__(self):
        string = type(self).__name__ + str(self.count)
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
    def __init__(self, count):
        super().__init__(count)
        self.max_brood = 105
