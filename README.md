# Table of Contents


1. Requirements for the Task
2. Overview
3. API Reference
4. Setup
5. Creating and Adding Personal Data
6. Displaying Personal Data
7. Converting Personal Data
8. Filtering Personal Data
9. Adding a New Format
10. personalDetails-add
11. personalDetails-convert
12. personalDetails-display
13. personalDetails-filter


# Requirements for the Task


The brief for this challenge is as follows:

In Python or C++ write a module or small library which shows how you would take a set of personal data, where each record contains:

. name
. address
. phone number

And:

build a simple API allowing you to add new records, filter users (e.g "name=Joe*") based on some simple search syntax like Glob

support serialisation in 2 or more formats (e.g JSON, Yaml, XML, CSV etc)

display the data in 2 or more different output formats (no need to use a GUI Framework, use e.g text output/HTML or any other human readable format)

add a command line interface to add records, and display/convert/filter the whole data set

Write it in such a way that it would be easy for a developer to extend the system e.g.

to add support for additional storage formats

to query a list of currently supported formats

This should ideally show Object-Oriented Design and Design Patterns Knowledge, we’re not looking for use of advanced Language constructs.

Please provide reasonable Unit Test coverage and basic API documentation.

The task is designed to allow you some flexibility in how you design and implement it, and you should submit something that demonstrates your abilities and/or values as a Software Engineer.


# Overview


The set of scripts assists and contains tools and an API, which can be used to operate with personal information. The Personal information is collected and stored in the supported formats. The API helps in determining the format to be used based on the extension type, therefore you do not need to manually format.


# API Reference


API reference (Sphinx) of the package is available in PersonalDetails/doc/html folder.


# Setup


Import the modules.

##### import PersonalDetails.personlibrary
##### import PersonalDetails.personalinfolibrary

Set the up the files for serialization.

##### TEST_FOLDER = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'test'))
##### JSON_FILE   = os.path.join(TEST_FOLDER, 'personalData.json')
##### XML_FILE    = os.path.join(TEST_FOLDER, 'personalData.xml')


# Creating and Adding Personal Data


Create an instance.

###### p1 = PersonalDetails.personlibrary.Person(
######                                    name='Steven Hosking',
######                                    phoneNumber='02 9383 4865',
######                                    address='22 Wallaby Way, Sydney')

Create a class by providing the filetype desired to be worked on. If it doesn't exist, it will be created.

###### personalData = PersonalDetails.personalinfolibrary.PersonalData(filePath=JSON_FILE)

Add the person and allow dupicates.

###### personalData.addByObject(p1, allowDuplicate=True)

Serialize the data, also set the overwrite to true to allow the file to be overwritten if it already exists.

###### personalData.serialize(overwrite=True)


# Displaying Personal Data


To display personal data

###### personalData = PersonalDetails.personalinfolibrary.PersonalData(filePath=JSON_FILE)
###### personalData.deserialize()
###### personalData.display()


# Converting Personal Data


You can convert one format to another by using PersonalDetails.personalDataLib.PersonalData.convert method. Please note, this operation applies to supported formats only. Supported formats can be obtained by using PersonalDetails.personalDataLib.PersonalData.getFormats method, like so;

###### print PersonalDetails.personalinfolibrary.PersonalData.getFormats()
###### ['JSON', 'XML']

To convert between the two formats:

###### personalData = PersonalDetails.personalinfolibrary.PersonalData(filePath=JSON_FILE)
###### personalData.deserialize()
###### personalData.convert(toFile=XML_FILE, overwrite=True, display=True)

The convert method can accept three argument methods:

tofile
overwrite
display


# Filtering Personal Data


Filtering can accept three arguments where wildcard filtering can be used. 

Those arguments are:

name
phoneNumber
address

Filtering example below.

###### personalData = PersonalDetails.personalinfolibrary.PersonalData(filePath=JSON_FILE)
###### personalData.deserialize()
###### print personalData.filter(name='Steven*)
###### personalData.filter(name='Steven*', phoneNumber='2*', address='wal*')


# Adding a New Format


Adding a new format is simple.

Create a new python module named personalinfoserializer<FORMAT>Lib.py, since in this example format is yaml, the name of the module must be personalinfoserializerYAMLlibrary.py

The API will use the naming convention and will extract the format name dynamically in order to work on it.
You will need to create a class in this module that inherits PersonalDetails.personalinfoserializerabs.Serializer abstract class.

Overwrite serialize method serialize the data and do the same to deserialize.

The entire class documentation can be found at PersonalDetails.personalinfoserializerabs.Serializer


# PersonalDetails-add


Prompts will request the name, phone number and address. Once the information has been entered, personal information will be saved into the file.

Flags

file File you are working on.
-d --display Display data.
######PersonalDetails-add personalData.json -d


# PersonalDetails-convert


You can convert formats. Formats are determined automatically based on the file extension of the file.

Flags

fromFile From the file.
toFIle To the file.
-o --overwrite Overwrite the existing toFile
-d --display Display the converted data.
PersonalDetails-convert the personalData.json personalData.xml -o -d


# PersonalDetails-display


This command displays the data.

Flags

file File you are working on.
PersonalDetails-displays the personalData.json


# PersonalDetails-filter


This is to filter personal data from the file worked on. Prompts will request the name, phone number and address, none of these questions are mandatory to answer and wildcards can be used to filter.

Flags

file File you are working on.
personaldata-filter personalData.json
Name Filter: S*
Phone Number Filter: 2*
Address Filter:

##### Name        : P Sherman
##### Address     : 22 Wallaby Way, Sydney
##### Phone Number: 02 9383 4865

##### Name        : Steve
##### Address     : 23 Wallaby Way, Sydney
##### Phone Number: 02 9383 4800
