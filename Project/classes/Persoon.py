from datetime import datetime
import uuid


class Courier():
    def __init__(self):
        self.storage = []


class Client(Courier):
    def __init__(self, count):
        super().__init__()
        self.count = 0
        self.count = count
        self.name = 'empty'

    def addToStorage(self, breadItem, machine):
        breadObj = {}
        if breadItem != None:
            breadObj['bType'] = breadItem._type()
            breadObj['datetime'] = str(
                datetime.now().strftime("%m-%d at %H:%M"))
            # ensures the dict item is actually overwrtitten because its unique
            breadObj['guid'] = uuid.uuid4()
            breadObj['machineNr'] = machine
            self.storage.append(breadObj)

    def __str__(self):
        dictArr = []
        defaultString = type(self).__name__ + ':' + \
            str(self.count) + \
            '----------------------------------------' + '\n\t'
        breadString = defaultString
        for d in self.storage:
            for value in d.values():
                dictArr.append(value)

            btype = str(dictArr[0])
            date = str(dictArr[1])
            guid = str(dictArr[2])
            machine = str(dictArr[3])
            breadString += 'Bread: '+btype.lower()+'\n\t'+'purchase date: ' + \
                date+'\n\t'+'machine Nr: '+machine+'\n\t'+'ID:'+guid+'\n\t\n\t'
            dictArr = []
        print(self.storage)
        return breadString
