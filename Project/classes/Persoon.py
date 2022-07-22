from datetime import datetime
from platform import machine
import uuid
from classes.Brood import Brood


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
        breadDict = {}
        if breadItem != None:
            breadDict['bType'] = breadItem._type()
            breadDict['datetime'] = str(
                datetime.now().strftime("%m-%d at %H:%M"))
            # ensures the dict item is actually overwrtitten because its unique
            breadDict['guid'] = uuid.uuid4()
            breadDict['machineNr'] = machine
            self.storage.append(breadDict)

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
            breadString += 'Bread: '+btype+'\n\t'+'purchase date: ' + \
                date+'\n\t'+'machine Nr: '+machine+'\n\t'+'ID:'+guid+'\n\t\n\t'
            dictArr = []
        return breadString
