#Imports
import os
import argparse
import Lib


#Display personal data.
def display():
    parser = argparse.ArgumentParser(description='Display personal data')
    parser.add_argument('file', type=str, help='File to be read')
    _args   = parser.parse_args()
    filePath = _args.file
    personaldetails = Lib(filePath)
    personaldetails.deserialize()
    personaldetails.display()

#Convert personal data formats.
def convert():
    parser = argparse.ArgumentParser(description='Convert personal data one format to another')
    parser.add_argument('fromFile', type=str, help='From file')
    parser.add_argument('toFile', type=str, help='To file')
    parser.add_argument('-o', '--overwrite', action='store_true', help='Overwrite existing file')
    parser.add_argument('-d', '--display', action='store_true', help='Display personal data after conversion')

    _args   = parser.parse_args()
    fromFilePath = _args.fromFile
    toFilePath   = _args.toFile
    overwrite    = _args.overwrite
    display      = _args.display
    personaldetails = Lib(fromFilePath)
    personaldetails.convert(toFilePath, overwrite, display)

#Add new record to personal data.
def add():
    parser = argparse.ArgumentParser(description='Add personal data')
    parser.add_argument('file', type=str, help='File')
    parser.add_argument('-d', '--display', action='store_true', help='Display personal details')

    _args   = parser.parse_args()
    filePath = _args.file
    display  = _args.display
    name = None
    phoneNumber = None
    address = None
    while not name:
        name = input('Name: ')
    while not phoneNumber:
        phoneNumber = input('Phone Number: ')
    while not address:
        address = input('Address: ')
    personaldetails = Lib(filePath)
    if os.path.isfile(filePath):
        personaldetails.deserialize()
    personaldetails.add(name=name, phoneNumber=phoneNumber, address=address)
    personaldetails.serialize(overwrite=True)
    if display:
        personaldetails.display()

#Display filtered personal data.

def filter():
    parser = argparse.ArgumentParser(description='Filter personal data')
    parser.add_argument('file', type=str, help='File')

    _args   = parser.parse_args()
    filePath = _args.file

    name = input('Name Filter: ')
    phoneNumber = input('Phone Number Filter: ')
    address = input('Address Filter: ')

    personaldetails = Lib(filePath)
    if os.path.isfile(filePath):
        personaldetails.deserialize()
    filter = personaldetails.filter(name=name, phoneNumber=phoneNumber, address=address)
    if not filter:
        print ("No personal details found.")
        return
    personaldetails.setPersonList(filter)
    personaldetails.display()
