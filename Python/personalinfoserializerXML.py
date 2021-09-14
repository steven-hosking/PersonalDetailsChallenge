# Imports
import xml.etree.ElementTree as ET

from personalinfolibrary import PersonDetails
from personalinfoserializerabsolute import Serializer


# Serializer
class SerializingXML(Serializer):
    def __init__(self, personList=[]):
        Serializer.__init__(self, personList)

    #Serialize person list
    def serialize(self, filePath, overwrite=False):
        Serializer.__dict__['serialize'](self, filePath, overwrite)
        root = ET.Element('personList')
        for person in self._personList:
            personElement = ET.SubElement(root, 'person')
            personElement.set('name', person.name())
            personElement.set('phoneNumber', person.phoneNumber())
            personElement.set('address', person.address())
        tree = ET.ElementTree(root)
        tree.write(filePath, method='xml')

        return True

    #Deserialize
    def deserialize(self, filePath):
        root = ET.parse(filePath).getroot()
        self._personList[:] = []
        for elem in root:
            self._personList.append(PersonDetails.personlibrary.Person(name=elem.attrib['name'],
                                                                   address=elem.attrib['address'],
                                                                   phoneNumber=elem.attrib['phoneNumber']))

        return self._personList

    #Display person list.
    def display(self):
        if not self._personList:
            print ('\nNo person data to display.\n')
            return
        for person in self._personList:
            print ('<b>Name:</b><span>{}</span><br>').format(person.name())
            print ('<b>Phone Number:</b><span>{}</span><br>').format(person.phoneNumber())
            print ('<b>Address:</b><span>{}</span><br><br>\n').format(person.address())
