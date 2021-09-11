# Imports
import json
from   pprint import pprint

from personlibrary import Person
from personalinfoserializerabsolute import Serializer



# Serializer
class Serializing(Serializer):
    def __init__(self, personList=[]):
        Serializer.__dict__['__init__'](self, personList)

    #Serialize person list and write it out into the given file.
    def serialize(self, filePath, overwrite=False):
        Serializer.__dict__['serialize'](self, filePath, overwrite)
        personList = [{'name':x.name(), 'phoneNumber':x.phoneNumber(), 'address':x.address()} for x in self._personList]
        with open(filePath, 'w') as outFile:
            json.dump(personList, outFile, sort_keys=True, indent=4)

        return True

    # Deserialize
    def deserialize(self, filePath):
        personList = None
        with open(filePath) as inFile:
            personList = json.load(inFile)
        if not personList:
            return None
        self._personList[:] = []
        self._personList = [Person(name=x['name'],
                                                           phoneNumber=x['phoneNumber'],
                                                           address=x['address']) for x in personList]

        return self._personList

    # Display person list.
    def display(self):
        if not self._personList:
            print ('\nNo person data to display.\n')
            return
        for person in self._personList:
            # Remove _ at the beginning of the attributes and display
            pprint([(v[1:], k) for v, k in person.__dict__.iteritems()])
