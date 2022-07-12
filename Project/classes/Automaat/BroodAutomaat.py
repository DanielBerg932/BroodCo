class BroodAutomaat():

    def __init__(self):
        self.storage = []
        self.max_brood = 75

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
