class BroodAutomaat():
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
            print(f"Broodautomaat: {self.count} is full")

    def removeBread(self):
        if len(self.storage) > 0:
            self.storage.pop()
        else:
            print("Broodautomaat is empty")

    def buyBread(self, btype):
        counter = -1
        for b in self.storage:
            counter += 1
            # set to always pass for debugging reasons
            if b._type == btype or True:
                return self.storage.pop(counter)
            else:
                return None


class GroteBroodAutomaat(BroodAutomaat):
    def __init__(self, count):
        super().__init__(count)
        self.max_brood = 105
        self.capacity = self.max_brood
