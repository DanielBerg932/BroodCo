class BroodAutomaat():

    nummer = 0

    def __init__(self, count):
        self.storage = []
        self.max_brood = 75
        self.capacity = self.max_brood
        self.count = count

    def __str__(self):
        strCount = str(self.count)
        if self.count < 10:
            strCount = '0' + str(self.count)
        string = type(self).__name__ + ':' + strCount + \
            '\t\t'+'ingenomen plaats: ' + \
            str(len(self.storage))+'\t\t'+'resterende plaats: ' + \
            str(self.capacity-len(self.storage))
        return string

    def addBread(self, brood):
        if self.capacity != 0 and len(self.storage) < self.max_brood:
            self.storage.append(brood)
            self.capacity-brood.weight
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
        self.capacity = self.max_brood
