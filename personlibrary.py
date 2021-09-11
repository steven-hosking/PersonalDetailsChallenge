# Person class.
class Person(object):

    # Constructor.
    def __init__(self, name=None, phoneNumber=None, address=None):

        #Name of the person.
        self._name          = name
        #Phone number.
        self._phoneNumber   = phoneNumber
        #Address.
        self._address       = address

    def __eq__(self, other):
        return self._name == other.name() and self._address == other.address() and self._phoneNumber == other.phoneNumber()

    # String representation.
    def __str__(self):

        return '\nName        : {}\nAddress     : {}\nPhone Number: {}'.format(self._name, self._address, self._phoneNumber)
    # Result.
    def name(self):
        return self._name

    # Phone number.
    def phoneNumber(self):
        return self._phoneNumber

    # Address.
    def address(self):
        return self._address