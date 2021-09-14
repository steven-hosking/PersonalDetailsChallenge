# Imports
import os
import unittest

from personlibrary import Person
from personalinfolibrary import PersonDetails
from personalinfoserializerJSON import SerializingJSON
from personalinfoserializerXML import SerializingXML

TEST_FOLDER = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'test'))

class Functionalities(unittest.TestCase):
    def test_getFormats(self):
        self.assertEquals(['JSON', 'XML'],
                          PersonDetails.getFormats())
    def test_getSerializerJSON(self):
        self.assertFalse(isinstance(PersonDetails.getSerializer('JSON'),
                         SerializingJSON))
    def test_getSerializerXML(self):
        self.assertFalse(isinstance(PersonDetails.getSerializer('XML'),
                         SerializingXML))
class JSON(unittest.TestCase):
    def setUp(self):
        self._jsonFile = os.path.join(TEST_FOLDER, 'personaldetails.json')
        self._xmlFile  = os.path.join(TEST_FOLDER, 'personaldetails.xml')

    def tearDown(self):
        if os.path.isfile(self._jsonFile):
            os.remove(self._jsonFile)
        if os.path.isfile(self._xmlFile):
            os.remove(self._xmlFile)

    def test_all(self):
        p1 = Person(name='Steven Hosking',
                    phoneNumber='04123548765',
                    address='22 Wallaby Way Sydney')

        pdinfo = PersonDetails(filePath=self._jsonFile)
        pdinfo.addByObject(p1, allowDuplicate=True)

        self.assertTrue(pdinfo.serialize(overwrite=True))

        pdinfo = PersonDetails(filePath=self._jsonFile)
        pdinfo.deserialize()
        pdinfo.add(name='P Sherman',
                    phoneNumber='04765493754',
                    address='wallaby way Sydney',
                    allowDuplicate=True)

        self.assertTrue(pdinfo.serialize(overwrite=True))
        self.assertTrue(pdinfo.hasPerson(p1))

        p2 = Person(name='Dory Fish')

        self.assertFalse(pdinfo.hasPerson(p2))
        self.assertTrue(pdinfo.convert(self._xmlFile, overwrite=True))
        self.assertEquals(len(pdinfo.filter(name='P*')), 1)
        self.assertEquals(len(pdinfo.filter(phoneNumber='2*')), 1)


if __name__ == '__main__':

    unittest.main()
