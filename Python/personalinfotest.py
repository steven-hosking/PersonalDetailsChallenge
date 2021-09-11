# Imports
import os
import unittest

from personalinfolibrary import PersonDetails

TEST_FOLDER = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'test'))

class Functionalities(unittest.TestCase):
    def test_getFormats(self):
        self.assertEquals(['JSON', 'XML'],
                          PersonDetails.personalDataLib.PersonalData.getFormats())
    def test_getSerializerJSON(self):
        self.assertFalse(isinstance(PersonDetails.personalDataLib.PersonalData.getSerializer('JSON'),
                         PersonDetails.personalinfoserializerJSON.Serializer))
    def test_getSerializerXML(self):
        self.assertFalse(isinstance(PersonDetails.personalDataLib.PersonalData.getSerializer('XML'),
                         PersonDetails.personalinfoserializerXML.Serializer))
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
        p1 = PersonDetails.personLib.Person(name='Steven Hosking',
                                            phoneNumber='0431675792',
                                            address='22 Wallaby Way Sydney')

        personalData = PersonDetails.personalDataLib.PersonalData(filePath=self._jsonFile)

        personalData.addByObject(p1, allowDuplicate=True)

        self.assertTrue(personalData.serialize(overwrite=True))

        personalData = PersonDetails.personalDataLib.PersonalData(filePath=self._jsonFile)

        personalData.deserialize()

        personalData.add(name='Lisa Gane',
                         phoneNumber='04765493754',
                         address='wallaby way Sydney',
                         allowDuplicate=True)

        self.assertTrue(personalData.serialize(overwrite=True))

        self.assertTrue(personalData.hasPerson(p1))

        p2 = PersonDetails.personLib.Person(name='Luke Marks')

        self.assertFalse(personalData.hasPerson(p2))

        self.assertTrue(personalData.convert(self._xmlFile, overwrite=True))

        self.assertEquals(len(personalData.filter(name='Lisa*')), 1)

        self.assertEquals(len(personalData.filter(phoneNumber='2*')), 1)


if __name__ == '__main__':

    unittest.main()
