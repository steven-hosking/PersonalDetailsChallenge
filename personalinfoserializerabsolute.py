# Imports
import os

class Serializer(object):
    
    #Constructor.
    def __init__(self, personList=[]):
        self._personList = personList

    def setPersonList(self, personList):
        self._personList = personList

    def personList(self):

        return self._personList

    def serialize(self, filePath, overwrite=False):
        if not overwrite and os.path.isfile(filePath):
            raise IOError('File already exists: {}'.format(filePath))

        return False

    def deserialize(self, filePath):
        raise NotImplementedError('This method must be implemented in child class.')

    def display(self):
        raise NotImplementedError('This method must be implemented in child class.')