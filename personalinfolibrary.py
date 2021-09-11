#Imports
import os
import re
import fnmatch
import importlib

#Personal class.
class PersonDetails(object):

    #Constructor.
    def __init__(self, filePath=None):
        self._filePath   = filePath
        self._personList = []
        self._serializer = None

    # Get Person List
    def personList(self):

        return self._personList

    #Set person list.
    def setPersonList(self, personList):
        self._personList = personList[:]
        if not self._serializer:
            self._serializer = self.getSerializer(self._filePath)()

        self._serializer.setPersonList(self._personList)

    #Add new person.
    def add(self, name, phoneNumber, address, allowDuplicate=False):
        newPerson = PersonDetails.personlibrary.Person(name, phoneNumber, address)
        if not allowDuplicate:
            self.hasPerson(newPerson, raiseException=True)

        self._personList.append(newPerson)

        return True

    #Add new person
    def addByObject(self, personInstance, allowDuplicate=False):
        if not allowDuplicate:
            self.hasPerson(personInstance, raiseException=True)

        self._personList.append(personInstance)

        return True

    #Check whether given person already exists.
    def hasPerson(self, personInstance, raiseException=False):
        if not self._personList:
            return False
        if [x for x in self._personList if personInstance == x]:
            if raiseException:
                raise PersonDetails.exceptionlibrary.PersonAlreadyExistsError('Person with the following data already exists, name: "{}", phone number: "{}", address: "{}"'.format(personInstance.name(),
                                                                                                                                                                                personInstance.phoneNumber(),
                                                                                                                                                                                personInstance.address()))
            return True

        return False

    # Serialize person list into the file based on the format
    def serialize(self, overwrite=False):
        self._serializer = self.getSerializer(self._filePath)(self._personList)
        self._serializer.serialize(self._filePath, overwrite)

        return True

    #Deserialize object from the file
    def deserialize(self):
        self._serializer = self.getSerializer(self._filePath)()
        self._personList = self._serializer.deserialize(self._filePath)

        return self._personList

    #Display personal data.
    def display(self):
        if not self._serializer:
            print ('You must call serialize or deserialize method in order to display data.')
            return
        try:
            self._serializer.display()
        except NotImplementedError as error:
            if not self._personList:
                print ('\nNo person data to display.\n')
                return

            for person in self._personList:
                print (person)
    
    #Convert the personal data into the format by provided by a file.
    def convert(self, toFile, overwrite=False, display=False):
        toFormat = os.path.splitext(toFile)[1][1:].upper()
        formatList = PersonDetails.getFormats()
        if not toFormat in formatList:
            raise PersonDetails.exceptionlibrary.UnsupportedFormatError('This format is not supported: {}'.format(toFormat))

        self.deserialize()

        serializer = PersonDetails.getSerializer(toFormat)(self._personList)
        serializer.serialize(toFile, overwrite)
        if display:
            serializer.display()

        return serializer

    #Filter personal data by using wildcards.
    def filter(self, name=None, phoneNumber=None, address=None):
        if not self._serializer:
            raise PersonDetails.exceptionlibrary.ConfigurationError('You must call serialize or deserialize method in order to display data.')
        if not self._serializer.personList():
            return []

        filteredPersonList = []

        if name:
            filteredPersonList.extend([p for p in self._serializer.personList() if name and fnmatch.fnmatch(p.name(), name)])
        if phoneNumber:
            filteredPersonList.extend([p for p in self._serializer.personList() if phoneNumber and fnmatch.fnmatch(p.phoneNumber(), phoneNumber)])
        if address:
            filteredPersonList.extend([p for p in self._serializer.personList() if address and fnmatch.fnmatch(p.address(), address)])

        return filteredPersonList

    #Get valid formats which can be operated with.
    @staticmethod
    def getFormats():
        pythonModuleList = os.listdir(os.path.dirname(__file__))
        if not pythonModuleList:
            return None

        formatList = []

        for moduleName in pythonModuleList:
            formatName = re.search(r'personalDetailsSerializer([A-Z]{2,})Lib.py$', moduleName)
            if formatName:
                formatList.append(formatName.groups()[0])

        return formatList
    
    # Get serializer for given format.
    @staticmethod
    def getSerializer(formatName):
        formatList = PersonDetails.getFormats()
        if not formatName in formatList:
            formatName = os.path.splitext(formatName)[1][1:].upper()
            if not formatName:
                raise PersonDetails.exceptionlibrary.UnsupportedFormatError('No valid format found, valid formats are: {}'.format(', '.join(PersonDetails.getFormats())))
        if not formatName in formatList:
            raise PersonDetails.exceptionlibrary.UnsupportedFormatError('This format is not supported: {}'.format(formatName))

        serializerModuleName = 'personalDataSerializer{}Lib'.format(formatName)
        module = None

        try:
            module = importlib.import_module('PersonDetails.{}'.format(serializerModuleName))
        except ImportError as error:
            raise PersonDetails.exceptionlibrary.UnsupportedFormatError('This format is not supported: {}\nError: {}'.format(formatName, error))

        #reload (module)

        if not hasattr(module, 'Serializer'):
            raise PersonDetails.exceptionlibrary.ConfigurationError('Module does not have a class named "Serializer" {}'.format(str(module)))

        return getattr(module, 'Serializer')