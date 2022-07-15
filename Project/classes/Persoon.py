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
        self.breadDict = {
            'bType': 'null',
            'datetime': 'null',
            'machineNr': -1,
            'guid': 'null'}

    def addToStorage(self, breadItem, machine):
        if breadItem != None:
            self.breadDict['bType'] = breadItem._type()
            self.breadDict['datetime'] = str(
                datetime.now().strftime("%m-%d om %H:%M"))
            # ensures the dict item is actually overwrtitten because its unique
            self.breadDict['guid'] = uuid.uuid4()
            self.breadDict['machineNr'] = machine
            self.storage.append(self.breadDict)

    def __str__(self):
        dictArr = []
        for d in self.storage:
            for value in d.values():
                dictArr.append(value)
            defaultString = type(self).__name__ + ':' + \
                str(self.count) + \
                '----------------------------------------' + '\n\t'
            btype = str(dictArr[0])
            date = str(dictArr[1])
            machine = str(dictArr[2])
            guid = str(dictArr[3])
            breadString = defaultString+'Bread: '+btype+'\n\t'+'purchase date: ' + \
                date+'\n\t'+'machine Nr: '+machine+'\n\t'+'ID:'+guid+'\n'
        dictArr = []
        return breadString
